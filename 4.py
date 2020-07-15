# 首先需要导入webbrowser模块
import webbrowser
from tkinter import *

# 建立窗口window
window = Tk()

# 给窗口的可视化起名字
window.title('label超链接')

# 设置窗口的居中显示
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
width = 700
height = 150
size = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
# 设定窗口的大小(长 * 宽)
window.geometry(size)

# 设置label标签
link = Label(window, text='点击购买高级版本:  www.baidu.com', font=('Arial', 10))
link.place(x=20, y=130)


# 此处必须注意，绑定的事件函数中必须要包含event参数
s="http://www.baidu.com"
def open_url(event):
    webbrowser.open(s, new=0)


# 绑定label单击时间
link.bind("<Button-1>", open_url)
mainloop()