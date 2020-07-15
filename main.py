# -*- coding: utf-8 -*-
import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from functools import partial


import fist
from PyQt5.QtCore import QTimer, QThread, pyqtSignal


def click_success():
    print("啊哈哈哈我终于成功了！")
def convert(ui):
    partial
def times(data):
    ui.label.setText('{} s'.format(time.time()))

    # def add(self):
    # btncont = ui.layout.count()
    # widget = QPushButton("1",ui)
    # ui.layout.addWidget(widget)

    ui.tableWidget.setItem(1, 1, QTableWidgetItem(str(data)))  # 设置j
    ui.tableWidget.setItem(1, 2, QTableWidgetItem(str(data)))  # 设置j
    ui.tableWidget.setItem(2, 2, QTableWidgetItem(str(data)))  # 设置j

    for row in range(4):
        for column in range(4):
            # item = QTableWidgetItem(str(data))
            ui.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))  # 设置j

class Threads(QThread):
    update_date = pyqtSignal(str) # pyqt5 支持python3的str，没有Qstring
    def  __init__(self):
        super(Threads,self).__init__()

    def run(self):
        #线程相关的代码
        a = 1
        while(1):
            a=a+1
            self.update_date.emit(str(a))  # 发射信号
            # times()
            # print(a)
            a=a+1
            self.sleep(1)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = fist.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # ui.pushButton.clicked.connect(click_success)
    ui.pushButton.clicked.connect(partial(convert, ui))
    # timer = QTimer()  # 初始化定时器
    # timer.timeout.connect(times)
    # timer.start(2 * 1000)
    threadss = Threads()
    threadss.update_date.connect(times)  # 链接信号

    threadss.start()


    sys.exit(app.exec_())
