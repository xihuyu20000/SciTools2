import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from api.gui.main.SciToolsGuiStub import SciToolsGuiStub

'''
使用 PyQt5 创建客户端程序
'''


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = SciToolsGuiStub()
    window.show()

    sys.exit(app.exec_())