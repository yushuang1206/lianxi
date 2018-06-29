#!/usr/bin/env python3
# encoding: utf-8

import os
from tkinter import *
import tkinter
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('CheckFile')


def checkFile(file_name):
	with open(file_name, 'rb') as file:
		# print(file,type(file))
		for file_line in file:
			if '<<<<<<<' in str(file_line):
				return '请检查文件:' + file_name

def file_dir(path):
	if os.path.isdir(path):
		filelist = []
		for root, dirs,files in os.walk(path):
			for file_dir in files:
				if '.pyc' not in file_dir:
					file_name = (root+'/'+file_dir)
					error_name = checkFile(file_name)
					if error_name:
						filelist.append(error_name)
						return filelist
			else:
				filelist = ['OK']
				return filelist
	filelist = []
	return filelist

def logInfo(list):
	return " ".join(list)



def printentry():
	lable = tkinter.Label(top, text='-----分隔符-----').pack()
	dir = var.get()
	result = file_dir(dir)
	if result:
		if result[0] == 'OK':
			tkinter.Label(top, text='OK').pack()
		else:
			for lable in result:
				tkinter.Label(top, text=lable).pack()
				logger.error(logInfo(result))
	else:
		tkinter.Label(top, text='路径无效').pack()
		logger.warning('路径无效')

def initLog():
	format = '%(asctime)s - %(levelname)s - %(message)s'
	rHandler = RotatingFileHandler("log", maxBytes=1024 * 1024, backupCount=1)
	#log文件最大1M
	# rHandler.setLevel(logging.DEBUG)

	rHandler.setFormatter(logging.Formatter(format))
	console = logging.StreamHandler()
	# console.setLevel(logging.DEBUG)

	console.setFormatter(logging.Formatter(format))
	logger.addHandler(rHandler)
	logger.addHandler(console)
	logger.info('loading')

if __name__ == '__main__':
	initLog()
	file_dir('.')
	top = tkinter.Tk()
	top.title('checkfile')
	var = StringVar()
	lable = tkinter.Label(top, text='请输入绝对路径').pack()
	enter = tkinter.Entry(top, textvariable=var).pack()
	button = tkinter.Button(top, text='enter', command=printentry).pack()
	top.mainloop()