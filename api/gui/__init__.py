import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

'''
使用 PyQt5 创建客户端程序
'''


class SciToolsGui(QMainWindow):
    def __init__(self, parent=None):
        super(SciToolsGui, self).__init__(parent)
        # 设置标题+版本
        self.setWindowTitle('科研助手 V1.0')
        # 设置窗口大小
        self.resize(800, 600)
        # 居中
        self.center()

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(int(newLeft), int(newTop))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = SciToolsGui()
    window.show()

    sys.exit(app.exec_())
