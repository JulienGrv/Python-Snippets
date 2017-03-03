# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GRA8HI\Documents\Projects\Test_Environment_Client\qt_designer\MainWindow.ui'
#
# Created: Mon Feb 13 13:40:41 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSettings = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/interface"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon)
        self.actionSettings.setObjectName("actionSettings")
        self.actionStart = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/start"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart.setIcon(icon1)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/stop"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon2)
        self.actionStop.setObjectName("actionStop")
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addAction(self.actionStop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setToolTip(QtGui.QApplication.translate("MainWindow", "Test environment settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setToolTip(QtGui.QApplication.translate("MainWindow", "Start test environment", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setToolTip(QtGui.QApplication.translate("MainWindow", "Stop test environment", None, QtGui.QApplication.UnicodeUTF8))

# import resources_rc
