#!/usr/bin/python
# -*- coding: utf-8 -*-
#hello world

'''第一行是告诉操作系统用哪个Python解释器执行代码，本例中的写法是告诉系统使用系统环境配置里的python解释器，你也可以写入一个完整python解释器路径，例如 #!/usr/bin/python                       第二行 # -*- coding:utf-8 -*-  是告诉解释器，这个脚本里的文本编码是utf-8，如果没有这行代码，Python解释器会默认使用ASCII作为脚本的编码，当脚本中出现中文、西欧字符、日文、韩文的时候就会产生异常。'''

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

'''if __name__=="__main__" 用于判断这个脚本是独立运行，还是被作为模块导入到别的脚本的
    
    如果该脚本是独立运行的， __name__=="__main__" 返回True
    
    raw_input 是Python标准库里自带的函数，用于等待并捕获用户输入。
    
    print 也是Python标准库里自带的函数，用于打印到控制台'''
