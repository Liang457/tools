# -*- coding: utf-8 -*-

import sys
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
import random_extract


class Ui_MainWindow(object):
    def __init__(self, max_num=54) -> None:
        self.max_num = max_num

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(620, 640)
        MainWindow.setMinimumSize(QtCore.QSize(620, 640))
        MainWindow.setMaximumSize(QtCore.QSize(620, 640))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chouquanniu = QtWidgets.QPushButton(self.centralwidget)
        self.chouquanniu.setGeometry(QtCore.QRect(150, 580, 61, 41))
        self.chouquanniu.setObjectName("chouquanniu")
        self.shuchuwenbenkuang = QtWidgets.QTextBrowser(self.centralwidget)
        self.shuchuwenbenkuang.setGeometry(QtCore.QRect(220, 10, 381, 621))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.shuchuwenbenkuang.setFont(font)
        self.shuchuwenbenkuang.setDocumentTitle("")
        self.shuchuwenbenkuang.setMarkdown("")
        self.shuchuwenbenkuang.setObjectName("shuchuwenbenkuang")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 450, 191, 120))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numberhumer = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.numberhumer.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.numberhumer.setMinimum(1)
        self.numberhumer.setMaximum(self.max_num)
        self.numberhumer.setObjectName("numberhumer")
        self.horizontalLayout.addWidget(self.numberhumer)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        # self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        # self.checkBox.setChecked(True)
        # self.checkBox.setObjectName("checkBox")
        # self.verticalLayout.addWidget(self.checkBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.numberhumer.stepUp)  # type: ignore
        self.pushButton_3.clicked.connect(self.numberhumer.stepDown)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 抽取主按钮
        self.chouquanniu.clicked.connect(self.chouqu)

    # 定义抽取
    def chouqu(self, MainWindow):
        num_people = self.numberhumer.value()

        random_list = random_extract.get_random_result(num_people, self.max_num)
        random_str = "结果为：\n" + "\n".join(random_list)

        self.shuchuwenbenkuang.setPlainText(random_str)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "抽取"))
        self.chouquanniu.setText(_translate("MainWindow", "抽取"))
        self.label.setText(_translate("MainWindow", "人数"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        # self.checkBox.setText(_translate("MainWindow", "使用真随机数"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # 判断抽取列表是否存在
    if not os.path.exists("抽取列表.txt"):
        QtWidgets.QMessageBox.critical(None, "错误", "找不到 抽取列表.txt 文件，无法进行抽取")
        exit(-1)

    # 获取行数
    with open("抽取列表.txt", "r", encoding="utf-8") as file:
        lines = len(file.readlines())

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(lines)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
