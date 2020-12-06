import sys
from PyQt5.QtWidgets import QApplication

from gui.cleaning.CleaningDialogStub import CleaningDialogStub

'''
使用 PyQt5 创建客户端程序
'''


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = CleaningDialogStub()
    window.mainWindow.show()

    sys.exit(app.exec_())