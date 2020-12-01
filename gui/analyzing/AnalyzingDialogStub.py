from PyQt5.QtWidgets import QMainWindow

from gui.analyzing import Ui_AnalyzingDialog


class AnalyzingDialogStub(Ui_AnalyzingDialog):
    def __init__(self):
        self.mainWindow = QMainWindow()
        super().setupUi(self.mainWindow)
