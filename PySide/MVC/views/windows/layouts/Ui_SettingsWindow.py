# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\GRA8HI\Documents\Projects\Test_Environment_Client\qt_designer\SettingsWindow.ui'
#
# Created: Tue Feb 14 15:34:12 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        self.centralwidget = QtGui.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QtGui.QApplication.translate("SettingsWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))

