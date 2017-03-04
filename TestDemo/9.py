#!/usr/bin/python
# -*- coding: UTF-8 -*-
# __author__ = 'chlma'

'''题目：暂停一秒输出。

程序分析：无。'''

import time

myDic = {1:'a', 2:'b'}

for key, value in dict.items(myDic):
	print key, value
	time.sleep(2)
