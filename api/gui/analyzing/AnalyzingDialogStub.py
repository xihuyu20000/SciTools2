import os
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow


from api.biz import biz_cleaningfiles
from api.gui.analyzing.AnalyzingDialog import Ui_AnalyzingDialog


class AnalyzingDialogStub(Ui_AnalyzingDialog):
    def __init__(self):
        self.mainWindow = QMainWindow()
        super().setupUi(self.mainWindow)
