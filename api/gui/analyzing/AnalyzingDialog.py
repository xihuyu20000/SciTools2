# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnalyzingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnalyzingDialog(object):
    def setupUi(self, AnalyzingDialog):
        AnalyzingDialog.setObjectName("AnalyzingDialog")
        AnalyzingDialog.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AnalyzingDialog)
        self.centralwidget.setObjectName("centralwidget")
        AnalyzingDialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnalyzingDialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        AnalyzingDialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnalyzingDialog)
        self.statusbar.setObjectName("statusbar")
        AnalyzingDialog.setStatusBar(self.statusbar)

        self.retranslateUi(AnalyzingDialog)
        QtCore.QMetaObject.connectSlotsByName(AnalyzingDialog)

    def retranslateUi(self, AnalyzingDialog):
        _translate = QtCore.QCoreApplication.translate
        AnalyzingDialog.setWindowTitle(_translate("AnalyzingDialog", "分析数据"))
