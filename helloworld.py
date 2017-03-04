#!/usr/bin/python
# -*- coding: utf-8 -*-
#hello world

# import os

# print 'hello world'

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork();
# if pid==0:
# 	print('I am child process (%s) and my parent is %s' %(os.getpid(), os.getppid()))
# else:
# 	print('I (%s)just create a child process (%s) .' %(os.getppid(), pid))

'''由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：'''

from multiprocessing import Process
import os

#子进程要执行的代码块
def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test'),)
	print('Child process will start')
	p.start()
	p.join()
	print('Child process end.')