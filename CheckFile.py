import os
from tkinter import *
import tkinter

def checkFile(file_name):
    with open(file_name, 'r') as file:
        for file_line in file:
            if '<<<<<<<' in file_line:
                return '请检查文件:' + file_name

def file_dir(path):
    if os.path.isdir(path):
        filelist = []
        for root, dirs,files in os.walk(path):
            for file_dir in files:
                if '.py' in file_dir and '.pyc' not in file_dir:
                    file_name = (root+'/'+file_dir)
                    error_name = checkFile(file_name)
                    if error_name:
                        filelist.append(error_name)
                else:
                    pass
        if filelist:
            return filelist
    return False

def printentry():
    lable = tkinter.Label(top, text='-----分隔符-----').pack()
    dir = var.get()
    result = file_dir(dir)
    if result:
        for lable in result:
            tkinter.Label(top, text=lable).pack()
    else:
        tkinter.Label(top, text='路径无效').pack()

if __name__ == '__main__':
    file_dir('.')
    top = tkinter.Tk()
    top.title('checkfile')
    var = StringVar()
    lable = tkinter.Label(top, text='请输入绝对路径').pack()
    enter = tkinter.Entry(top, textvariable=var).pack()
    button = tkinter.Button(top, text='enter', command=printentry).pack()
    top.mainloop()