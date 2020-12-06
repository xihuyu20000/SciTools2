import os

import msgpack
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox


from . import biz_cleaningfiles
from .CleaningDialog import Ui_CleaningDialog


class CleaningDialogStub(Ui_CleaningDialog):
    def __init__(self):
        self.mainWindow = QMainWindow()
        super().setupUi(self.mainWindow)

        # '加载'页按钮
        self.rawDataPath_pushButton.clicked.connect(self.rawDataPath_pushButton_clicked)
        self.startCleaning_pushButton.clicked.connect(self.startCleaning_pushButton_clicked)
        self.openbrowser_pushButton.clicked.connect(self.openbrowser_pushButton_clicked)

    def rawDataPath_pushButton_clicked(self):
        self.rawDataPath_lineEdit.setText('')
        files, filetypes = QFileDialog.getOpenFileNames(caption="选择数据文件", directory=os.getcwd())
        if files:
            self.rawDataPath_lineEdit.setText(' , '.join(files))

    def startCleaning_pushButton_clicked(self):
        datafiles = self.rawDataPath_lineEdit.text()
        datatype = self.rawDataType_comboBox.currentText()
        dataencoding = self.rawDataEncoding_comboBox.currentText()
        datalang = self.rawDataLang_comboBox.currentText()

        files = [x.strip() for x in datafiles.split(',') if x.strip()] # 加载的数据文件用,分割
        if not files:
            QMessageBox.information(self.mainWindow, '提示', '请选择文件!', QMessageBox.Ok)
            return

        datas = biz_cleaningfiles.parsefiles(datatype, files)

        # 最后保存
        filenames = QFileDialog.getSaveFileName(self.mainWindow, '保存文件', os.getcwd(), '.st')
        with open(filenames[0]+'.st', 'wb') as f1:
            # 数据格式，序列化
            datas = [x.to_dict() for x in datas]
            bdata = msgpack.packb(datas, use_bin_type=True)
            f1.write(bdata)
        QMessageBox.information(self.mainWindow, '提示', '清洗结束，请上传到网站', QMessageBox.Ok)

    def openbrowser_pushButton_clicked(self):
        QDesktopServices.openUrl(QUrl("http://localhost:22222/"))