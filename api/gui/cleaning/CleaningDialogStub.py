import os

import msgpack
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow

from api.gui.cleaning.CleaningDialog import Ui_CleaningDialog
from api.biz import biz_cleaningfiles


class CleaningDialogStub(Ui_CleaningDialog):
    def __init__(self):
        self.mainWindow = QMainWindow()
        super().setupUi(self.mainWindow)
        # 帮助类
        self.helper = CleaningHelper()
        # 初始化开始日期、结束日期
        self.startDate_lineEdit.setText('1900-01-01')
        self.endDate_lineEdit.setText('2020-01-01')
        # '加载'页按钮
        self.rawDataPath_pushButton.clicked.connect(self.rawDataPath_pushButton_clicked)
        self.startCleaning_pushButton.clicked.connect(self.startCleaning_pushButton_clicked)
        self.showCleaningInfo_pushButton.clicked.connect(self.showCleaningInfo_pushButton_clicked)
        # ’字典‘页按钮
        self.dict_stopWords_pushButton.clicked.connect(self.dict_stopWords_pushButton_clicked)
        self.dict_userdict_pushButton.clicked.connect(self.dict_userdict_pushButton_clicked)
        self.dict_tongyi_pushButton.clicked.connect(self.dict_tongyi_pushButton_clicked)

    def rawDataPath_pushButton_clicked(self):
        self.rawDataPath_lineEdit.setText('')
        files, filetypes = QFileDialog.getOpenFileNames(caption="选择数据文件", directory=os.getcwd())
        if files:
            self.rawDataPath_lineEdit.setText(' , '.join(files))

    def startCleaning_pushButton_clicked(self):
        cleanConfig = CleaningConfig()
        cleanConfig.datafiles = self.rawDataPath_lineEdit.text()
        cleanConfig.datatype = self.rawDataType_comboBox.currentText()
        cleanConfig.dataencoding = self.rawDataEncoding_comboBox.currentText()
        cleanConfig.datalang = self.rawDataLang_comboBox.currentText()
        cleanConfig.data_startdate = self.startDate_lineEdit.text()
        cleanConfig.data_enddate = self.endDate_lineEdit.text()
        cleanConfig.data_dateperiod = self.rawDatePeriod_comboBox.currentText()
        cleanConfig.dict_stopwords_path = self.dict_stopWords_lineEdit.text()
        cleanConfig.dict_userdict_path = self.dict_userdict_lineEdit.text()
        cleanConfig.dict_tongyi_path = self.dict_tongyi_lineEdit.text()

        # 1 检查数据完整性
        flag, msg = self.helper.check_integrity(cleanConfig)
        self.status_label.setText(msg)
        if not flag:
            return
        # 2 解析格式
        files = [x.strip() for x in cleanConfig.datafiles.split(',') if x.strip()]
        datas = biz_cleaningfiles.parsefiles(cleanConfig.datatype, files)
        self.status_label.setText('解析数据文件')
        # 3 加载停用词词典、自定义词典
        datas = biz_cleaningfiles.cut_words(datas, stopwords_dict_path=cleanConfig.dict_stopwords_path, splitwords_dict_path=cleanConfig.dict_userdict_path)
        # 4 加载同义词词典
        # 5 加载学科分类词典、国家词典、省份词典等等
        # 最后保存
        filename=QFileDialog.getSaveFileName(self.mainWindow,'save file',os.getcwd())
        with open(filename[0], 'wb') as f1:
            # 数据格式，序列化
            datas = [x.to_dict() for x in datas]
            bdata = msgpack.packb(datas, use_bin_type=True)
            f1.write(bdata)
        self.status_label.setText('解析完数据文件')



    def showCleaningInfo_pushButton_clicked(self):
        print('查看结果')

    def dict_stopWords_pushButton_clicked(self):
        file, filetype = QFileDialog.getOpenFileName(caption="选择停用词词典", directory=os.getcwd())
        if file:
            self.dict_stopWords_lineEdit.setText(file)

    def dict_userdict_pushButton_clicked(self):
        file, filetype = QFileDialog.getOpenFileName(caption="选择自定义词典", directory=os.getcwd())
        if file:
            self.dict_userdict_lineEdit.setText(file)

    def dict_tongyi_pushButton_clicked(self):
        file, filetype = QFileDialog.getOpenFileName(caption="选择同义词词典", directory=os.getcwd())
        if file:
            self.dict_tongyi_lineEdit.setText(file)


class CleaningConfig:
    def __init__(self):
        self.datafiles: str = ''
        self.datatype: str = ''
        self.dataencoding: str = ''
        self.datalang: str = ''
        self.data_startdate: str = ''
        self.data_enddate: str = ''
        self.data_dateperiod: str = ''
        self.dict_stopwords_path: str = ''
        self.dict_userdict_path: str = ''
        self.dict_tongyi_path: str = ''


class CleaningHelper:

    def check_integrity(self, config: CleaningConfig):
        if not config.datafiles:
            return False, '必须选择数据文件'
        return True, '完整性检查结束，全部正确'
