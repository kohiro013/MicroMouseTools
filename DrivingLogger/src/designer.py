# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\user\kohiro\Desktop\MicroMouseTools\DrivingLogger\src\designer.ui',
# licensing of 'G:\user\kohiro\Desktop\MicroMouseTools\DrivingLogger\src\designer.ui' applies.
#
# Created: Thu Jul  9 20:26:00 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1433, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background:rgb(255,255,255);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxSerial = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxSerial.sizePolicy().hasHeightForWidth())
        self.groupBoxSerial.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.groupBoxSerial.setFont(font)
        self.groupBoxSerial.setStyleSheet("QGroupBox {\n"
"    border: 1.2px solid gray;\n"
"    margin-top: 1.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 3 0 3 0;\n"
"}\n"
"")
        self.groupBoxSerial.setObjectName("groupBoxSerial")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxSerial)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBoxSerial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.groupBoxSerial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBoxBaudRate = QtWidgets.QComboBox(self.groupBoxSerial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxBaudRate.sizePolicy().hasHeightForWidth())
        self.comboBoxBaudRate.setSizePolicy(sizePolicy)
        self.comboBoxBaudRate.setMinimumSize(QtCore.QSize(150, 36))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.comboBoxBaudRate.setFont(font)
        self.comboBoxBaudRate.setFrame(True)
        self.comboBoxBaudRate.setObjectName("comboBoxBaudRate")
        self.comboBoxBaudRate.addItem("")
        self.comboBoxBaudRate.addItem("")
        self.comboBoxBaudRate.addItem("")
        self.comboBoxBaudRate.addItem("")
        self.comboBoxBaudRate.addItem("")
        self.comboBoxBaudRate.addItem("")
        self.comboBoxBaudRate.addItem("")
        self.comboBoxBaudRate.addItem("")
        self.comboBoxBaudRate.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxBaudRate)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBoxSerial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.groupBoxSerial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBoxPort = QtWidgets.QComboBox(self.groupBoxSerial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPort.sizePolicy().hasHeightForWidth())
        self.comboBoxPort.setSizePolicy(sizePolicy)
        self.comboBoxPort.setMinimumSize(QtCore.QSize(150, 36))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.comboBoxPort.setFont(font)
        self.comboBoxPort.setStyleSheet("background-color: white;")
        self.comboBoxPort.setObjectName("comboBoxPort")
        self.horizontalLayout_2.addWidget(self.comboBoxPort)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(18)
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButtonConnect = QtWidgets.QPushButton(self.groupBoxSerial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonConnect.sizePolicy().hasHeightForWidth())
        self.pushButtonConnect.setSizePolicy(sizePolicy)
        self.pushButtonConnect.setMinimumSize(QtCore.QSize(136, 0))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.pushButtonConnect.setFont(font)
        self.pushButtonConnect.setStyleSheet("QPushButton {\n"
"    background-color: #00b06B;\n"
"    border: 2px solid #00b06B;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    border: 2px solid #00b06B;\n"
"    border-radius: 5px;\n"
"    color: #00b06B;\n"
"}\n"
"")
        self.pushButtonConnect.setDefault(False)
        self.pushButtonConnect.setFlat(False)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.horizontalLayout_7.addWidget(self.pushButtonConnect)
        self.pushButtonClear = QtWidgets.QPushButton(self.groupBoxSerial)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClear.sizePolicy().hasHeightForWidth())
        self.pushButtonClear.setSizePolicy(sizePolicy)
        self.pushButtonClear.setMinimumSize(QtCore.QSize(136, 0))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setStyleSheet("QPushButton {\n"
"    background-color: #FF0000;\n"
"    border: 2px solid red;\n"
"    border-radius: 5px;\n"
"    color: #FFffFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFffFF;\n"
"    border: 2px solid red;\n"
"    border-radius: 5px;\n"
"    color: #FF0000;\n"
"}")
        self.pushButtonClear.setDefault(False)
        self.pushButtonClear.setFlat(False)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_7.addWidget(self.pushButtonClear)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.groupBoxSerial)
        self.groupBoxDataList = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxDataList.sizePolicy().hasHeightForWidth())
        self.groupBoxDataList.setSizePolicy(sizePolicy)
        self.groupBoxDataList.setMinimumSize(QtCore.QSize(330, 0))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.groupBoxDataList.setFont(font)
        self.groupBoxDataList.setStyleSheet("QGroupBox {\n"
"    border: 1.2px solid gray;\n"
"    margin-top: 1.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 3 0 3 0;\n"
"}\n"
"")
        self.groupBoxDataList.setObjectName("groupBoxDataList")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxDataList)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setContentsMargins(18, 9, 18, 18)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(18)
        self.horizontalLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButtonSave = QtWidgets.QPushButton(self.groupBoxDataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSave.sizePolicy().hasHeightForWidth())
        self.pushButtonSave.setSizePolicy(sizePolicy)
        self.pushButtonSave.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setStyleSheet("QPushButton {\n"
"    background-color: #00b06B;\n"
"    border: 2px solid #00b06B;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    border: 2px solid #00b06B;\n"
"    border-radius: 5px;\n"
"    color: #00b06B;\n"
"}\n"
"")
        self.pushButtonSave.setDefault(False)
        self.pushButtonSave.setFlat(False)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_6.addWidget(self.pushButtonSave)
        self.pushButtonLoad = QtWidgets.QPushButton(self.groupBoxDataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLoad.sizePolicy().hasHeightForWidth())
        self.pushButtonLoad.setSizePolicy(sizePolicy)
        self.pushButtonLoad.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.pushButtonLoad.setFont(font)
        self.pushButtonLoad.setStyleSheet("QPushButton {\n"
"    background-color: #00b06B;\n"
"    border: 2px solid #00b06B;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    border: 2px solid #00b06B;\n"
"    border-radius: 5px;\n"
"    color: #00b06B;\n"
"}\n"
"")
        self.pushButtonLoad.setDefault(False)
        self.pushButtonLoad.setFlat(False)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout_6.addWidget(self.pushButtonLoad)
        self.toolButtonDirectory = QtWidgets.QToolButton(self.groupBoxDataList)
        self.toolButtonDirectory.setMinimumSize(QtCore.QSize(32, 32))
        self.toolButtonDirectory.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButtonDirectory.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButtonDirectory.setAutoRaise(False)
        self.toolButtonDirectory.setArrowType(QtCore.Qt.DownArrow)
        self.toolButtonDirectory.setObjectName("toolButtonDirectory")
        self.horizontalLayout_6.addWidget(self.toolButtonDirectory)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.treeViewDataList = QtWidgets.QTreeView(self.groupBoxDataList)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(16)
        self.treeViewDataList.setFont(font)
        self.treeViewDataList.setObjectName("treeViewDataList")
        self.verticalLayout_3.addWidget(self.treeViewDataList)
        self.verticalLayout.addWidget(self.groupBoxDataList)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayoutMplWidget = QtWidgets.QVBoxLayout()
        self.verticalLayoutMplWidget.setContentsMargins(-1, -1, 9, 9)
        self.verticalLayoutMplWidget.setObjectName("verticalLayoutMplWidget")
        self.verticalLayoutToolbar = QtWidgets.QVBoxLayout()
        self.verticalLayoutToolbar.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayoutToolbar.setObjectName("verticalLayoutToolbar")
        self.verticalLayoutMplWidget.addLayout(self.verticalLayoutToolbar)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1032, 4018))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget = mpl_widget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 4000))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(14)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout_9.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutMplWidget.addWidget(self.scrollArea)
        self.horizontalLayout_4.addLayout(self.verticalLayoutMplWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1433, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setWeight(75)
        font.setBold(True)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBoxSerial.setTitle(QtWidgets.QApplication.translate("MainWindow", "Config UART", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Baud Rate", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", ":", None, -1))
        self.comboBoxBaudRate.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "921600", None, -1))
        self.comboBoxBaudRate.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "460800", None, -1))
        self.comboBoxBaudRate.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "230400", None, -1))
        self.comboBoxBaudRate.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "115200", None, -1))
        self.comboBoxBaudRate.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "57600", None, -1))
        self.comboBoxBaudRate.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "38400", None, -1))
        self.comboBoxBaudRate.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "19200", None, -1))
        self.comboBoxBaudRate.setItemText(7, QtWidgets.QApplication.translate("MainWindow", "14400", None, -1))
        self.comboBoxBaudRate.setItemText(8, QtWidgets.QApplication.translate("MainWindow", "9600", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Port", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", ":", None, -1))
        self.pushButtonConnect.setText(QtWidgets.QApplication.translate("MainWindow", "Connect", None, -1))
        self.pushButtonClear.setText(QtWidgets.QApplication.translate("MainWindow", "Clear", None, -1))
        self.groupBoxDataList.setTitle(QtWidgets.QApplication.translate("MainWindow", "Data List", None, -1))
        self.pushButtonSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.pushButtonLoad.setText(QtWidgets.QApplication.translate("MainWindow", "Load", None, -1))
        self.toolButtonDirectory.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))

from main import mpl_widget
