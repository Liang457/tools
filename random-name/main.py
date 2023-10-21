# -*- coding: utf-8 -*-

import sys
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
import random_extract


class Ui_MainWindow(object):
    def __init__(self, max_num=54, VERSION="") -> None:
        self.max_num = max_num
        self.VERSION = VERSION
        self.lastlist = []

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
        self.output_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_display.setGeometry(QtCore.QRect(220, 10, 381, 621))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.output_display.setFont(font)
        self.output_display.setDocumentTitle("")
        self.output_display.setMarkdown("")
        self.output_display.setObjectName("output_display")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 519, 191, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.number_input = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.number_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.number_input.setMinimum(1)
        self.number_input.setMaximum(self.max_num)
        self.number_input.setObjectName("number_input")
        self.horizontalLayout.addWidget(self.number_input)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 470, 191, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.total_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.total_count.setAlignment(QtCore.Qt.AlignCenter)
        self.total_count.setObjectName("total_count")
        self.horizontalLayout_2.addWidget(self.total_count)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.exclude_previously_drawn = QtWidgets.QCheckBox(self.centralwidget)
        self.exclude_previously_drawn.setGeometry(QtCore.QRect(20, 420, 191, 51))
        self.exclude_previously_drawn.setObjectName("exclude_previously_drawn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.number_input.stepUp)  # type: ignore
        self.pushButton_3.clicked.connect(self.number_input.stepDown)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 抽取主按钮
        self.chouquanniu.clicked.connect(self.chouqu)
        # 重置上次
        self.exclude_previously_drawn.clicked.connect(self.reset_last)

    # 定义抽取
    def chouqu(self, MainWindow):
        num_people = self.number_input.value()
        random_list = self.get_random_result(num_people)
        random_str = "结果为：\n" + "\n".join(random_list)
        self.update_text(random_str)

    def get_random_result(self, num_people):
        if self.exclude_previously_drawn.isChecked():
            random_list = random_extract.get_random_result_rmlast(
                num_people, self.lastlist
            )
            self.lastlist.extend(random_list)
            self.total_count.setText(
                str(self.max_num - len(self.lastlist)) + "/" + str(self.max_num)
            )
        else:
            random_list = random_extract.get_random_result(num_people)
        return random_list

    def update_text(self, text):
        self.output_display.setPlainText(text)

    def reset_last(self, MainWindow):
        self.lastlist = []
        self.total_count.setText(str(self.max_num))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "点人 - " + VERSION))
        self.chouquanniu.setText(_translate("MainWindow", "抽取"))
        self.label.setText(_translate("MainWindow", "人数"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.label_2.setText(_translate("MainWindow", "一共有"))
        self.total_count.setText(_translate("MainWindow", str(self.max_num)))
        self.label_4.setText(_translate("MainWindow", "人"))
        self.exclude_previously_drawn.setText(_translate("MainWindow", "排除已经抽过的人"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    VERSION = "23Y42WA"

    # 判断抽取列表是否存在
    if not os.path.exists("抽取列表.txt"):
        QtWidgets.QMessageBox.critical(None, "错误", "找不到 抽取列表.txt 文件，无法进行抽取")
        raise FileNotFoundError("找不到 抽取列表.txt 文件")

    # 获取行数
    with open("抽取列表.txt", "r", encoding="utf-8") as file:
        lines = len(file.readlines())

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(lines, VERSION)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
