from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from api.gui.analyzing.AnalyzingDialogStub import AnalyzingDialogStub
from api.gui.cleaning.CleaningDialogStub import CleaningDialogStub
from api.gui.main.SciToolGui import Ui_MainWindow


class SciToolsGuiStub(Ui_MainWindow):

    def __init__(self):
        self.mainWindow = QMainWindow()
        self.setupUi(self.mainWindow)
        # 设置标题+版本
        self.mainWindow.setWindowTitle('科研助手 V1.0')

        # 居中显示
        self.size_position()
        # 实例化子窗口
        self.cleanDialog = CleaningDialogStub()
        self.analyzeDialog = AnalyzingDialogStub()
        # 加载配置参数
        self.set_default()

        # 按钮绑定事件处理
        self.cleaning_pushButton.clicked.connect(self.cleaning_pushButton_clicked)
        self.analyzing_pushButton.clicked.connect(self.analyzing_pushButton_clicked)

    def cleaning_pushButton_clicked(self):
        self.cleanDialog.mainWindow.show()

    def analyzing_pushButton_clicked(self):
        self.analyzeDialog.mainWindow.show()

    def size_position(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 设置窗口大小，屏幕的80%
        self.mainWindow.resize(int(screen.width() * 0.8), int(screen.height() * 0.8))

        # 获取窗口坐标系
        size = self.mainWindow.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.mainWindow.move(int(newLeft), int(newTop))

    def set_default(self):
        # todo 加载配置文件，读取默认参数，自定义配置
        pass

    def show(self):
        self.mainWindow.show()
