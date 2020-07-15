# -*- coding:utf8 -*-
import time
import tkinter
from tkinter import *

numb = 0


def run_num(root):
    def counting():

        ticks = time.time()
        # tkinter.Label(root, text=str(ticks), bg="pink", width=20).grid(row=1, column=1)
        # tkinter.Label(root, text=str(ticks), bg="pink", width=20).grid(row=1, column=2)
        # tkinter.Label(root, text=str(ticks), bg="pink", width=20).grid(row=1, column=3)
        # tkinter.Label(root, text=str(ticks), bg="pink", width=20).grid(row=1, column=4)
        for i in [1,2,3,4,5]:
            a=r'tkinter.Label(root, text={}, bg="pink", width=20).grid(row=1, column={})'.format(str(ticks),i)
            b=r'tkinter.Label(root, text={}, bg="pink", width=20).grid(row=2, column={})'.format(str(ticks),i)

            exec(a)
            exec(b)


        root.after(3000, counting)   # 间隔1000毫秒再次执行counting函数
    counting()


root = Tk()
root.title("Label Demo")
root.geometry("600x400")
# label = Label(root, bg="lightyellow", height=2, width=20)
# label.pack()

run_num(root)

root.mainloop()



