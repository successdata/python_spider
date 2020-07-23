# -*- coding: utf-8 -*-
import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QAbstractItemView, QDialog, \
    QMessageBox, QWidget
from functools import partial


import second
import third
import Warning
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, Qt

from PyQt5.QtGui import QBrush, QColor

from bokeh.models import TableWidget
from qtpy import QtCore


def click_success():
    print("啊哈哈哈我终于成功了！")
def showTaskDialog():
    dialog=QDialog
    # btn=QPushButton("ok",dialog)
    # btn.move(50,50)
    dialog.setWindowModality(Qt.ApplicationModal)
    dialog.exec_()
def times(data):
    ui.label_8.setText('{} s'.format(time.strftime("%Y-%m-%d %H:%M:%S")))

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
def show_dialog(data):
    child.show()
    _translate = QtCore.QCoreApplication.translate
    child.child.label.setText(_translate("Dialog", str(data)))

class Threads(QThread):
    update_date = pyqtSignal(str) # pyqt5 支持python3的str，没有Qstring
    warning_dialog=pyqtSignal(str)
    task_warning_dialog=pyqtSignal(str)
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
            if a>=100:
                self.warning_dialog.emit(str(a))
            elif a>=4:
                self.task_warning_dialog.emit(str(a))

            self.sleep(1)
def set_UI(ui):
    ui.tableWidget.setColumnCount(10)
    ui.tableWidget.setRowCount(8)
    ui.tableWidget.setColumnWidth(1,100)
    ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    ui.tableWidget.setHorizontalHeaderLabels(['姓名      ','姓名','姓名','姓名','姓名','姓名','姓名','姓名','姓名','性别','体重（kg）'])
    ui.tableWidget.resizeColumnsToContents()  #自适应列宽
class childWindow(QDialog):
  def __init__(self):
    QDialog.__init__(self)
    self.child=Warning.Ui_Dialog()
    self.child.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = second.Ui_MainWindow()
    ui.setupUi(MainWindow)
    set_UI(ui)
    child: childWindow = childWindow()
    #通过toolButton将两个窗体关联
    # btn = ui.pushButton
    # btn.clicked.connect(child.show)

    MainWindow.show()
    threadss = Threads()
    threadss.update_date.connect(times)
    threadss.warning_dialog.connect(show_dialog)# 链接信号
    threadss.task_warning_dialog.connect(show_dialog)# 链接信号

    threadss.start()
    sys.exit(app.exec_())
