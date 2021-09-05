# coding: utf-8

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from numba import jit
from tqdm import tqdm

DT = 0.0001
GRAVITY = 9.80665
MASS = 12
INERTIA = 2000
TIRE = 13
TREAD = 18.5

CORNERING_FORCE = 0.83

MOT_KT = 0.594
MOT_KE = 0.062
MOT_RESIST = 4.7
GEAR_RATIO = 37/9
V_BAT = 3.7

EDGE_PRE_DISTANCE = 6
EDGE_END_DISTANCE = 8

@jit
def mynapier(_ms):
    if _ms <= 0.0 or 1.0 <= _ms:
        result = 0.0
    else:
        AMPLITUDE = 2.71828182845905
        result = AMPLITUDE * np.exp(1 / (np.power(2 * _ms - 1, 4) - 1))
    return result

@jit
def calcSlalom(_turn_angle, _turn_v, _radius, _init_x, _init_y, _init_dir):
    NAPEIR_INTGRAL = 0.76321461819897
    amplitude = _turn_v / _radius
    cycle = amplitude * NAPEIR_INTGRAL / _turn_angle
    
    time = np.arange(0, 1 / cycle, DT)
    alpha = np.array([amplitude * (mynapier(cycle * t) - mynapier(cycle * (t - DT))) / DT for t in time])
    omega = np.zeros(len(time))
    beta_dot = np.zeros(len(time))
    beta = np.zeros(len(time))
    pos_ideal = {'x':np.zeros(len(time)), 'y':np.zeros(len(time)), 'dir':np.zeros(len(time))}
    pos_ideal['x'][0] = _init_x
    pos_ideal['y'][0] = _init_y
    pos_ideal['dir'][0] = _init_dir

    pos_slip  = {'x':np.zeros(len(time)), 'y':np.zeros(len(time)), 'dir':np.zeros(len(time))}
    pos_slip['x'][0] = _init_x
    pos_slip['y'][0] = _init_y
    pos_slip['dir'][0] = _init_dir

    for num, t in enumerate(time[1::]):
        omega[num+1] = omega[num] + alpha[num+1] * DT
        pos_ideal['dir'][num+1] = pos_ideal['dir'][num] - omega[num+1] * DT
        pos_ideal['x'][num+1]   = pos_ideal['x'][num] + _turn_v * np.cos(pos_ideal['dir'][num+1]) * DT
        pos_ideal['y'][num+1]   = pos_ideal['y'][num] + _turn_v * np.sin(pos_ideal['dir'][num+1]) * DT

        beta_dot[num+1] = -4*CORNERING_FORCE / (MASS/1000) * (_turn_v/1000) * beta[num] / (np.power((_turn_v/1000), 2) - np.power((TREAD/1000) * omega[num+1], 2)) + omega[num+1]
        beta[num+1] = beta[num] + beta_dot[num+1] * DT
        #beta[num+1] = (beta[num] - omega[num+1] * DT) / (1 + CORNERING_FORCE / _turn_v * DT)
        pos_slip['dir'][num+1] = pos_ideal['dir'][num+1] + beta[num+1]
        pos_slip['x'][num+1]   = pos_slip['x'][num] + _turn_v * np.cos(pos_slip['dir'][num+1]) * DT
        pos_slip['y'][num+1]   = pos_slip['y'][num] + _turn_v * np.sin(pos_slip['dir'][num+1]) * DT
    return time, alpha, omega, pos_ideal, pos_slip

@jit
def calcVehicleDynamics(_time, _turn_v, _alpha, _omega):
    torque_l =  TIRE/2 * (INERTIA * _alpha / TREAD) / 2 / GEAR_RATIO / 1000
    torque_r = -TIRE/2 * (INERTIA * _alpha / TREAD) / 2 / GEAR_RATIO / 1000
    motor_rpm_l = (_turn_v - _omega * TREAD) / TIRE * 60/np.pi * GEAR_RATIO
    motor_rpm_r = (_turn_v + _omega * TREAD) / TIRE * 60/np.pi * GEAR_RATIO
    current_l = torque_l / MOT_KT / 1000
    current_r = torque_r / MOT_KT / 1000
    duty_l = (MOT_RESIST * torque_l / MOT_KT + MOT_KE * motor_rpm_l) / V_BAT / 1000
    duty_r = (MOT_RESIST * torque_r / MOT_KT + MOT_KE * motor_rpm_r) / V_BAT / 1000
    return [duty_l, duty_r], [current_l, current_r]

@jit
def calcStraightSection(_turn_angle, _end_x, _end_y, _end_dir, _init_angle, _goal_x, _goal_y):
    pos_goal_rot = [
        _goal_x * np.cos(np.pi/2 - _init_angle) - _goal_y * np.sin(np.pi/2 - _init_angle),
        _goal_x * np.sin(np.pi/2 - _init_angle) + _goal_y * np.cos(np.pi/2 - _init_angle),
    ]
    pos_end_rot = [
        _end_x * np.cos(np.pi/2 - _init_angle) - _end_y * np.sin(np.pi/2 - _init_angle),
        _end_x * np.sin(np.pi/2 - _init_angle) + _end_y * np.cos(np.pi/2 - _init_angle),
    ]
    end_section = (pos_goal_rot[0] - pos_end_rot[0]) / np.cos(np.pi/2 - _init_angle + _end_dir)
    pre_section = pos_goal_rot[1] - pos_end_rot[1] - end_section * np.sin(np.pi/2 - _init_angle + _end_dir)
    return pre_section, end_section

@jit
def calcTrajectorySlalom(_pos_x, _pos_y, _pos_dir, _init_x, _init_y, _init_angle, _pre_section, _end_section):
    trajectory_c = {
        'x':_pos_x + _pre_section * np.cos(_init_angle),
        'y':_pos_y + _pre_section * np.sin(_init_angle),
        'dir':_pos_dir
    }
    trajectory_c['x'] = np.append(_init_x, trajectory_c['x'])
    trajectory_c['y'] = np.append(_init_y, trajectory_c['y'])
    trajectory_c['dir'] = np.append(_init_angle, trajectory_c['dir'])
    trajectory_c['x'] = np.append(trajectory_c['x'], trajectory_c['x'][-1] + _end_section * np.cos(_pos_dir[-1]))
    trajectory_c['y'] = np.append(trajectory_c['y'], trajectory_c['y'][-1] + _end_section * np.sin(_pos_dir[-1]))
    trajectory_c['dir'] = np.append(trajectory_c['dir'], _pos_dir[-1])

    trajectory_l = {
        'x':trajectory_c['x'] + TREAD * np.cos(trajectory_c['dir'] + np.pi/2),
        'y':trajectory_c['y'] + TREAD * np.sin(trajectory_c['dir'] + np.pi/2),
    }
    trajectory_r = {
        'x':trajectory_c['x'] - TREAD * np.cos(trajectory_c['dir'] + np.pi/2),
        'y':trajectory_c['y'] - TREAD * np.sin(trajectory_c['dir'] + np.pi/2),
    }
    return trajectory_l, trajectory_c, trajectory_r

class Slalom:
    def __init__(self, _turn_angle, _pos_init, _init_angle, _goal_pos):
        self.turn_angle = np.deg2rad(_turn_angle)
        self.pos_init = _pos_init
        self.init_angle = np.deg2rad(_init_angle)
        self.pos_goal = _goal_pos

    def plotTest(self, _turn_v, _radius):
        self.time, self.alpha, self.omega, self.pos_ideal, self.pos_slip = calcSlalom(
            self.turn_angle, _turn_v, _radius, self.pos_init[0], self.pos_init[1], self.init_angle)
        #self.duty_l, self.duty_r = calcVehicleDynamics(self.time, _turn_v, self.alpha, self.omega)
        duty, current = calcVehicleDynamics(self.time, _turn_v, self.alpha, self.omega)
        self.duty_l = duty[0]
        self.duty_r = duty[1]
        self.current_l = current[0]
        self.current_r = current[1]
        #self.pre_section, self.end_section = calcStraightSection(self.turn_angle,
        #    self.pos_slip['x'][-1], self.pos_slip['y'][-1], self.pos_slip['dir'][-1], self.init_angle, self.pos_goal[0], self.pos_goal[1])
        self.pre_section = self.end_section = 0
        _ ,self.locus_ideal_c, _ = calcTrajectorySlalom(self.pos_ideal['x'], self.pos_ideal['y'], self.pos_ideal['dir'], 
                self.pos_init[0], self.pos_init[1], self.init_angle, self.pre_section, self.end_section)
        self.locus_slip_l ,self.locus_slip_c, self.locus_slip_r = calcTrajectorySlalom(self.pos_slip['x'], self.pos_slip['y'], self.pos_slip['dir'], 
                self.pos_init[0], self.pos_init[1], self.init_angle, self.pre_section, self.end_section)
        self.plotGenerateResult()

    def generateSlalom(self, _gravity):
        if np.rad2deg(self.turn_angle) == 180:
            max_v = np.sqrt(43.5 * _gravity * (GRAVITY*1000))
            min_v = np.sqrt(43.0 * _gravity * (GRAVITY*1000))
            velocity_list = np.arange(max_v, min_v, -0.001)
        else:
            velocity_list = np.arange(2000, 400, -10)
        for turn_v in velocity_list:
            radius = np.power(turn_v, 2) / _gravity / (GRAVITY*1000)
            time, alpha, omega, pos_ideal, pos_slip = calcSlalom(
                self.turn_angle, turn_v, radius, self.pos_init[0], self.pos_init[1], self.init_angle)
            duty, current = calcVehicleDynamics(time, turn_v, alpha, omega)
            #if np.max(duty[0]) > 0.8 or np.max(duty[1]) > 0.8:
            #    continue
            pre_section, end_section = calcStraightSection(self.turn_angle,
                pos_slip['x'][-1], pos_slip['y'][-1], pos_slip['dir'][-1], self.init_angle, self.pos_goal[0], self.pos_goal[1])
            if pre_section < EDGE_PRE_DISTANCE or end_section < EDGE_END_DISTANCE:
                continue
            _ ,locus_c, locus_r = calcTrajectorySlalom(pos_slip['x'], pos_slip['y'], pos_slip['dir'], 
                self.pos_init[0], self.pos_init[1], self.init_angle, pre_section, end_section)
            if np.min(np.sqrt(np.power(45 - locus_r['x'], 2) + np.power(45 - locus_r['y'], 2))) < 8:
                continue
            if np.max(locus_c['y']) > 135 - TREAD - 8:
                continue
            break

        self.turn_v = turn_v
        self.radius = radius
        self.time = time
        self.omega = omega
        self.pos_ideal = pos_ideal
        self.pos_slip = pos_slip
        self.pre_section = pre_section
        self.end_section = end_section
        self.duty_l = duty[0]
        self.duty_r = duty[1]
        self.current_l = current[0]
        self.current_r = current[1]

        _ ,self.locus_ideal_c, _ = calcTrajectorySlalom(self.pos_ideal['x'], self.pos_ideal['y'], self.pos_ideal['dir'], 
                self.pos_init[0], self.pos_init[1], self.init_angle, self.pre_section, self.end_section)
        self.locus_slip_l ,self.locus_slip_c, self.locus_slip_r = calcTrajectorySlalom(self.pos_slip['x'], self.pos_slip['y'], self.pos_slip['dir'], 
                self.pos_init[0], self.pos_init[1], self.init_angle, self.pre_section, self.end_section)

        #print('turn_v = {:>4.0f}, radius = {:>5.1f}, pre_section = {:>4.1f}, end_section = {:>4.1f}, beta = {:>4.2f}'
        #        .format(turn_v, radius, pre_section, end_section, np.rad2deg(pos_slip['dir'][-1] - self.init_angle + self.turn_angle)))
        return [turn_v, self.turn_angle, time[-1] + (pre_section + end_section) / turn_v, radius, pre_section, end_section]

    def plotMaze(self, _maze_size, _ax):
        SECTION_SIZE = 90       # 区画サイズ
        WALL_SIZE = 6           # 壁の厚さ
        MAZE_SIZE = _maze_size  # 表示する区画数
        PILLAR_MARGIN = 5       # 柱からの安全距離
        # 区画線
        for n in np.arange(MAZE_SIZE*2+1):
            _ax.plot([-SECTION_SIZE/2, (MAZE_SIZE-0.5)*SECTION_SIZE], [(n-1)*SECTION_SIZE/2, (n-1)*SECTION_SIZE/2], '--k', alpha=0.2, linewidth=0.8)
            _ax.plot([(n-1)*SECTION_SIZE/2, (n-1)*SECTION_SIZE/2], [-SECTION_SIZE/2, (MAZE_SIZE-0.5)*SECTION_SIZE], '--k', alpha=0.2, linewidth=0.8)
        # 斜め区画線
        for n in np.arange(MAZE_SIZE):
            _ax.plot([-SECTION_SIZE/2, n*SECTION_SIZE], [(MAZE_SIZE-1-n)*SECTION_SIZE, (MAZE_SIZE-0.5)*SECTION_SIZE], '--k', alpha=0.2, linewidth=0.8)
            _ax.plot([(MAZE_SIZE-1-n)*SECTION_SIZE, (MAZE_SIZE-0.5)*SECTION_SIZE], [-SECTION_SIZE/2, n*SECTION_SIZE], '--k', alpha=0.2, linewidth=0.8)
            _ax.plot([n*SECTION_SIZE, -SECTION_SIZE/2], [-SECTION_SIZE/2, n*SECTION_SIZE], '--k', alpha=0.2, linewidth=0.8)
            _ax.plot([n*SECTION_SIZE, (MAZE_SIZE-0.5)*SECTION_SIZE], [(MAZE_SIZE-0.5)*SECTION_SIZE, n*SECTION_SIZE], '--k', alpha=0.2, linewidth=0.8)
        # 柱
        pos_pillar = [(n-0.5)*SECTION_SIZE-WALL_SIZE/2 for n in np.arange(MAZE_SIZE+1)]
        for y in pos_pillar:
            for x in pos_pillar:
                _ax.add_patch(patches.Rectangle(xy=(x, y), width=6, height=6, fc='r', ec='k'))
        _ax.add_patch(patches.Circle(xy=(SECTION_SIZE/2, SECTION_SIZE/2), radius=PILLAR_MARGIN+WALL_SIZE/2, fc='k', linestyle='--', fill=False))
        # 壁
        for n in np.arange(MAZE_SIZE):
            _ax.add_patch(patches.Rectangle(xy=(pos_pillar[0], pos_pillar[n]+WALL_SIZE), width=WALL_SIZE, height=SECTION_SIZE-WALL_SIZE, fc='r', ec='k'))
            _ax.add_patch(patches.Rectangle(xy=(pos_pillar[n]+WALL_SIZE, pos_pillar[0]), width=SECTION_SIZE-WALL_SIZE, height=WALL_SIZE, fc='r', ec='k'))
        _ax.add_patch(patches.Rectangle(xy=(pos_pillar[1], pos_pillar[0]+WALL_SIZE), width=WALL_SIZE, height=SECTION_SIZE-WALL_SIZE, fc='r', ec='k'))

    def plotSlalomLocus(self, _maze_size, _ax):
        self.plotMaze(_maze_size, _ax)
        _ax.plot(self.locus_ideal_c['x'], self.locus_ideal_c['y'], '-.k')
        _ax.plot(self.locus_slip_c['x'][0:2], self.locus_slip_c['y'][0:2], '-.b')
        _ax.plot(self.locus_slip_c['x'][1:-1], self.locus_slip_c['y'][1:-1], '-.g')
        _ax.plot(self.locus_slip_c['x'][-2:], self.locus_slip_c['y'][-2:], '-.r')
        _ax.plot(self.locus_slip_r['x'], self.locus_slip_r['y'], '-g')
        _ax.plot(self.locus_slip_l['x'], self.locus_slip_l['y'], '-g')

        _ax.axes.xaxis.set_ticks([])
        _ax.axes.yaxis.set_ticks([])
        _ax.set_aspect('equal', 'datalim')
        _ax.axis('scaled')

    def plotGenerateResult(self):
        plt.figure()

        ax0 = plt.subplot2grid((3, 4), (0, 0), rowspan=3, colspan=2)
        self.plotSlalomLocus(2, ax0)

        ax1 = plt.subplot2grid((3, 4), (0, 2), rowspan=1, colspan=2)
        ax1.plot(self.time, np.rad2deg(self.pos_ideal['dir'] - self.pos_slip['dir']))
        ax1.grid(which='major', color='black', linestyle='--', alpha=0.2)
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Side Slip Angle')

        ax2 = plt.subplot2grid((3, 4), (1, 2), rowspan=1, colspan=2)
        ax2.plot(self.time, self.duty_l, self.time, self.duty_r)
        ax2.grid(which='major', color='black', linestyle='--', alpha=0.2)
        ax2.set_ylim([-1, 1])
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Duty')
        ax2.legend(['Left', 'Right'])

        ax3 = plt.subplot2grid((3, 4), (2, 2), rowspan=1, colspan=2)
        ax3.plot(self.time, self.current_l, self.time, self.current_r)
        ax3.grid(which='major', color='black', linestyle='--', alpha=0.2)
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Current')
        ax3.legend(['Left', 'Right'])
        

def generateSlalomHeader(_slalom_dict, _gravity_list):

    pbar = tqdm(total=len(_slalom_dict.keys()) * len(_gravity_list))
    with open(os.path.join(os.getcwd(), 'slalom.h'), mode='w') as f:
        f.write('#ifndef SLALOM_H_\n#define SLALOM_H_\n\n')
        f.write('const t_init_slalom init_slalom[{0}][{1}]'.format(len(_slalom_dict)+1, len(_gravity_list)) + '= {\n\n')
        f.write('\t// slalom_90\n')
        f.write('\t// velocity, angle, time, radius, pre_section, end_section\n')
        f.write('\t{ { 350.f,  90.0f, 0.3064f, 28.0f,  7.0f, 10.0f }, },\n\n')
        for slalom_name, slalom_type in _slalom_dict.items():
            pbar.set_description('%s' % slalom_name)
            f.write('\t// ' + slalom_name + '\n')
            f.write('\t// velocity, angle, time, radius, pre_section, end_section\n')
            for num, gravity in enumerate(_gravity_list):
                pbar.update(1)
                result = slalom_type.generateSlalom(gravity)
                if num == 0:
                    f.write('\t{ ')
                else:
                    f.write('\t  ')
                f.write('{' + '{:>4.0f}.f, {:>5.1f}f, {:>5.4f}f, {:>3.1f}f, {:>4.1f}f, {:>4.1f}f'
                    .format(result[0], np.rad2deg(result[1]), result[2], result[3], result[4], result[5]) + ' },')
                if num == len(_gravity_list)-1:
                    f.write(' },')
                else:
                    f.write('  ')
                f.write('\t// {}\n'.format(num))
            f.write('\n')
        f.write('};\n')
        f.write('#endif /* SLALOM_H_ */')
    pbar.set_description('Generate Finish!')
    pbar.close()

def main():
    slalom_dict = {
        'SlalomLarge' :Slalom( 90, [0,  0], 90, [ 90, 90]),
        'Slalom180'   :Slalom(180, [0,  0], 90, [ 90,  0]),
        'Slalom45in'  :Slalom( 45, [0,  0], 90, [ 45, 90]),
        'Slalom135in' :Slalom(135, [0,  0], 90, [ 90, 45]),
        'Slalom90v'   :Slalom( 90, [0, 45], 45, [ 90, 45]),
        'Slalom45out' :Slalom( 45, [0, 45], 45, [ 90, 90]),
        'Slalom135out':Slalom(135, [0, 45], 45, [ 90,  0]),
        'SlalomKojima':Slalom( 90, [0, 45], 45, [180, 45]),
    }
    #gravity_list = np.array([0.5, 0.8, 1., 1.2, 1.4, 1.5, 1.8, 2.])
    gravity_list = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1., 1.1])
    generateSlalomHeader(slalom_dict, gravity_list)
    '''
    gravity = 3.
    print('velocity, turn_angle, time, radius, pre_section, end_section')
    for slalom_name, slalom_type in slalom_dict.items():
        result = slalom_type.generateSlalom(gravity)
        print('{:<14s}: {:>4.0f}, {:>4.0f}, {:>5.4f}, {:>3.1f}, {:>4.1f}, {:>4.1f}'
                .format(slalom_name, result[0], np.rad2deg(result[1]), result[2], result[3], result[4], result[5]))
    
    for num, slalom_type in enumerate(slalom_dict.values()):
        slalom_type.plotGenerateResult()

    plt.figure()
    plt.subplots_adjust(hspace=0.1, wspace=0.1)
    for num, slalom_type in enumerate(slalom_dict.values()):
        ax = plt.subplot(2, 4, num+1)
        if num == len(slalom_dict.keys()):
            slalom_type.plotSlalomLocus(3, ax)
        else:
            slalom_type.plotSlalomLocus(2, ax)
    '''
    '''
    SlalomTest = Slalom(45, [0, 0], 90, [45, 90])
    SlalomTest.plotTest(1470, 55.1)
    '''
    plt.show()

if __name__ == '__main__':
    main()