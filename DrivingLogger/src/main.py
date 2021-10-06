# coding: utf-8

import os
import sys
import serial
import serial.tools.list_ports
import datetime
import csv
import mplcursors
from PySide2 import QtWidgets
from PySide2 import QtCore
from matplotlib.figure import Figure
from matplotlib.backends import backend_qt5agg

from designer import Ui_MainWindow

class MatplotlibWidget(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Micro Mouse Logger ver.β")
        self.ui.statusbar.showMessage("No Data")
        toolbar = backend_qt5agg.NavigationToolbar2QT(self.ui.widget.canvas, self)
        self.ui.verticalLayoutToolbar.addWidget(toolbar)
        self.ui.pushButtonConnect.clicked.connect(self.communicateMouse)
        self.ui.pushButtonClear.clicked.connect(self.clearGraph)
        self.ui.toolButtonDirectory.clicked.connect(self.selectDirectory)
        self.ui.pushButtonSave.clicked.connect(self.saveLogData)
        self.ui.pushButtonLoad.clicked.connect(self.loadLogData)

        comport_list = self.search_com_port()
        self.ui.comboBoxPort.addItems(comport_list)

        self.rootPath = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.fileModel = QtWidgets.QFileSystemModel()
        self.fileModel.setRootPath(self.rootPath)
        self.fileModel.setNameFilters(['*.csv', '*.CSV'])
        self.fileModel.setNameFilterDisables(False)

        self.ui.treeViewDataList.setHeaderHidden(True)
        self.ui.treeViewDataList.setModel(self.fileModel)
        self.ui.treeViewDataList.setRootIndex(self.fileModel.index(self.rootPath))
        self.ui.treeViewDataList.setSortingEnabled(True)
        self.ui.treeViewDataList.sortByColumn(3, QtCore.Qt.SortOrder.AscendingOrder)
        self.ui.treeViewDataList.hideColumn(1)
        self.ui.treeViewDataList.hideColumn(2)
        self.ui.treeViewDataList.hideColumn(3)
        self.ui.treeViewDataList.show()
        self.ui.treeViewDataList.doubleClicked.connect(self.crickLogData)

        self.log_data = {}

    # 接続されているCOMポートの検索
    def search_com_port(self):
        coms = serial.tools.list_ports.comports()
        comlist = []
        for com in coms:
            comlist.append(com.device)
        return comlist

    # マイクロマウスとの接続
    def communicateMouse(self):
        self.clearGraph()
        self.ui.statusbar.showMessage("Now Loading...")
        baudrate = int(self.ui.comboBoxBaudRate.currentText())
        usb_port = self.ui.comboBoxPort.currentText()
        comport = serial.Serial(usb_port, baudrate=baudrate, parity=serial.PARITY_NONE)
        comport.reset_input_buffer()
        
        # ログの通信開始コマンド
        while comport.in_waiting == 0:
            comport.write(b'log\r\n')

        # ログの受信
        log_line = []
        _ = comport.readline()
        header_list = comport.readline().decode().strip().replace(" ", "").split(",")
        while 1:
            recv_data = comport.readline()
            if recv_data == b'\x1b\r\n':
                break
            log_line.append(recv_data.decode().strip().replace(" ", "").split(","))
        comport.close()
        log_line = [list(val) for val in zip(*log_line)]

        # ログデータの分類
        for num, header in enumerate(header_list):
            self.log_data.setdefault(header, [float(val) for val in log_line[num]])
        del(log_line)

        # ログデータの表示    
        self.displayLogData(self.log_data)
        self.ui.statusbar.showMessage("Display Log Data")

    # ログデータの表示
    def displayLogData(self, _data):
        graph_list = ['Control_Mode', 'Battery_Voltage', 'Interrupt_Load', 'Motor_Duty', 'Velocity', 'Angular_Velocity', 'Distance', 'Angle', 
                      'IR_Sensor', 'Wall_Edge', 'Velocity_Control', 'Angular_Control', 'Gap']
        if hasattr(self, 'ax') == False:
            for num, graph in enumerate(graph_list):
                if num == 0:
                    self.ax = {graph : self.ui.widget.canvas.figure.add_subplot(len(graph_list), 1, num+1)}
                else:
                    self.ax[graph] = self.ui.widget.canvas.figure.add_subplot(len(graph_list), 1, num+1, sharex=self.ax[graph_list[0]])

        plots = []
        vline = []
        markers = []
        texts = []
        for _, graph in enumerate(self.ax.keys()):
            if graph == 'Control_Mode':
                plots.append(self.ax[graph].plot(_data['Time'], _data['Mode'])[0])
                mode_list = ['ERROR', 'NONE', 'SEARCH', 'FASTEST', 'TURN', 'ROTATE', 'DIAGONAL', 'FWALL', 'ADJUST']
                self.ax[graph].set_yticks(range(-1, len(mode_list)-1))
                self.ax[graph].set_yticklabels(mode_list)
            elif graph == 'Battery_Voltage':
                if 'Boost' in _data:
                    plots.append(self.ax[graph].plot(_data['Time'], [data/100 for data in _data['Battery']],
                                                     _data['Time'], [data/100 for data in _data['Boost']])[0])
                    self.ax[graph].legend(['Battery', 'Boost'], loc='best')
                else:
                    plots.append(self.ax[graph].plot(_data['Time'], [data/100 for data in _data['Battery']])[0])
                self.ax[graph].set_yticks([i / 10 for i in range(0, 51, 5)])
            elif graph == 'Interrupt_Load':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Load']])[0])
                self.ax[graph].set_yticks([i / 10 for i in range(0, 1001, 100)])
            elif graph == 'Motor_Duty':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Duty_L']], 
                                                 _data['Time'], [data/10 for data in _data['Duty_R']])[0])
                #self.ax[graph].plot()
                self.ax[graph].set_yticks([i / 10 for i in range(-1000, 1001, 100)])
                self.ax[graph].legend(['Left', 'Right'], loc='best')
            elif graph == 'Current':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Current_L']],
                                                 _data['Time'], [data/10 for data in _data['Current_R']])[0])
                #self.ax[graph].set_yticks([i / 10 for i in range(-1000, 1001, 100)])
                self.ax[graph].legend(['Left', 'Right'], loc='best')
            elif graph == 'Force':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Force_L']],
                                                 _data['Time'], [data/10 for data in _data['Force_R']])[0])
                self.ax[graph].set_yticks([i / 10 for i in range(0, 3001, 500)])
                self.ax[graph].legend(['Left', 'Right'], loc='best')
            elif graph == 'Velocity':
                plots.append(self.ax[graph].plot(_data['Time'], _data['Target_V'], 'k',
                                                 _data['Time'], _data['Measure_V'])[0])
                self.ax[graph].legend(['Target', 'Measure'], loc='best')
            elif graph == 'Angular_Velocity':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Target_Omega']], 'k',
                                                 _data['Time'], [data/10 for data in _data['Measure_Omega']])[0])
                self.ax[graph].legend(['Target', 'Measure'], loc='best')
            elif graph == 'Distance':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Target_D']], 'k',
                                                 _data['Time'], [data/10 for data in _data['Measure_D']])[0])
                self.ax[graph].legend(['Target', 'Measure'], loc='best')
            elif graph == 'Angle':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Target_Theta']], 'k',
                                                 _data['Time'], [data/10 for data in _data['Measure_Theta']])[0])
                self.ax[graph].legend(['Target', 'Measure'], loc='best')
            elif graph == 'IR_Sensor':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Sensor_SL']],
                                                 _data['Time'], [data/10 for data in _data['Sensor_FL']],
                                                 _data['Time'], [data/10 for data in _data['Sensor_FR']],
                                                 _data['Time'], [data/10 for data in _data['Sensor_SR']])[0])
                self.ax[graph].set_ylim(0, 200)
                self.ax[graph].legend(['SL', 'FL', 'FR', 'SR'], loc='best')
            elif graph == 'Sensor_Delta':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['SensorDelta_SL']],
                                                 _data['Time'], [data/10 for data in _data['SensorDelta_SR']])[0])
                self.ax[graph].set_ylim(-50, 50)
                self.ax[graph].legend(['SL', 'SR'], loc='best')
            elif graph == 'Wall_Edge':
                plots.append(self.ax[graph].plot(_data['Time'], _data['Edge_SL'],
                                                 _data['Time'], _data['Edge_SR'])[0])
                self.ax[graph].legend(['SL', 'SR'], loc='best')
            elif graph == 'Velocity_Control':
                plots.append(self.ax[graph].plot(_data['Time'], _data['Control_Encoder'])[0])
                self.ax[graph].set_ylim(-8000, 8000)
            elif graph == 'Angular_Control':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Control_Gyro']],
                                                 _data['Time'], [data/10 for data in _data['Control_Angle']],
                                                 _data['Time'], [data/10 for data in _data['Control_Sensor']])[0])
                self.ax[graph].set_ylim(-800, 800)
                self.ax[graph].legend(['Gyro', 'Angle', 'Sensor'], loc='best')
            elif graph == 'Gap':
                plots.append(self.ax[graph].plot(_data['Time'], [data/10 for data in _data['Gap']])[0])

            self.ax[graph].grid(which='major', color='black', linestyle='--', alpha=0.2)
            #self.ax[graph].set_xlabel('Time')
            self.ax[graph].set_ylabel(graph)
            vline.append(self.ax[graph].axvline(0, color='k', ls=':', alpha=0.5, visible=True))
            markers.append(self.ax[graph].plot([0], [0], marker='.', color='k', alpha=0.5))
            texts.append(self.ax[graph].text(0.02, 0.95, "", horizontalalignment='left', verticalalignment='top', transform=self.ax[graph].transAxes))

        def crosshair(sel):
            x = sel.target[0]
            #sel.annotation.set_text(f'x: {x:.2f}\ny: {y:.2f}')
            sel.annotation.set_visible(False)
            #print(x, max(_data['Time']), len(_data['Time']))
            for num, graph in enumerate(graph_list):
                vline[num].set_xdata([x])
                markers[num][0].set_data([x], [plots[num].get_ydata()[int(x*len(_data['Time'])/max(_data['Time']))]])
                if(self.ax[graph].get_legend() == None):
                    texts[num].set_text('Time=%1.3f\nValue=%f'%(x, plots[num].get_ydata()[int(x*len(_data['Time'])/max(_data['Time']))]))
                else:
                    text = 'Time=%1.3f' %x
                    for i in range(len(self.ax[graph].get_legend().get_texts())):
                        text += '\n%s=%f' %(self.ax[graph].get_legend().get_texts()[i].get_text(), 
                                            self.ax[graph].get_lines()[i].get_data()[1][int(x*len(_data['Time'])/max(_data['Time']))])
                    texts[num].set_text(text)
        
        cursor = mplcursors.cursor(plots, hover=True)
        cursor.connect('add', crosshair)
        self.ui.widget.canvas.draw()

    # データとグラフの削除
    def clearGraph(self):
        self.log_data = {}
        if hasattr(self, 'ax') == True:
            del(self.ax)
        self.ui.widget.canvas.figure.clf()
        self.ui.widget.canvas.draw()

    # ファイルを開く動作設定
    def selectDirectory(self):
        self.ui.treeViewDataList.clearSelection()
        tempPath = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Log File Directory", self.rootPath)
        if len(tempPath) != 0:
            self.rootPath = tempPath
            self.fileModel.setRootPath(self.rootPath)
            self.ui.treeViewDataList.setRootIndex(self.fileModel.index(self.rootPath))

    # ログデータを保存する
    def saveLogData(self):
        if len(self.log_data) != 0:
            now = datetime.datetime.now().strftime("%y%m%d_%H%M")[0:]
            file_name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Log File', os.path.join(self.rootPath, now + '.csv'), '*.csv')
            if len(file_name[0]) != 0:
                header = [str(key) for key in self.log_data.keys()]
                data = [list(val) for val in zip(*self.log_data.values())]
                with open(file_name[0], 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(data)
            self.rootPath = os.path.dirname(file_name[0])
            self.fileModel.setRootPath(self.rootPath)
            self.ui.treeViewDataList.setRootIndex(self.fileModel.index(self.rootPath))
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'No Log Data!')

    def loadCSV(self, _file):
        data_line = []
        with open(_file, 'r') as f:
            reader = csv.reader(f)
            for row in list(reader):
                data_line.append(row)
            header_list = data_line[0]
            data_line = [list(val) for val in zip(*data_line[1:])]
        data = {}
        for num, header in enumerate(header_list):
            data.setdefault(header, [float(val) for val in data_line[num]])
        return data

    # 保存されたログデータを読み込む
    def loadLogData(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Load Log Data', self.rootPath, '*.csv')
        if len(file_name[0]) != 0:
            compare_data = self.loadCSV(file_name[0])
            self.displayLogData(compare_data)

            self.rootPath = os.path.dirname(file_name[0])
            self.fileModel.setRootPath(self.rootPath)
            self.ui.treeViewDataList.setRootIndex(self.fileModel.index(self.rootPath))

    def crickLogData(self, index):
        indexItem = self.fileModel.index(index.row(), 0, index.parent())
        file_name = self.fileModel.fileName(indexItem)
        if len(file_name[0]) != 0:
            compare_data = self.loadCSV(os.path.join(self.rootPath, file_name))
            self.displayLogData(compare_data)        

class mpl_widget(QtWidgets.QWidget):
    
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = backend_qt5agg.FigureCanvas(Figure())
        self.canvas.figure.subplots_adjust(left=0.08,right=0.99,bottom=0.01,top=0.99,hspace=0.2,wspace=0.0)

        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)

if __name__ in ('__main__', 'micromouselogger__main__', 'MicroMouseLogger__main__'):
    app = QtWidgets.QApplication(sys.argv)
    window = MatplotlibWidget()
    window.show()
    sys.exit(app.exec_())
