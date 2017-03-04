#!/usr/bin/python
# -*- coding: UTF-8 -*-
# __author__ = 'chlma'

'''题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。'''

import math
for i in range(0, 10000):
	# 转化为整型值
	x = int(math.sqrt(i + 100))
	y = int(math.sqrt(i + 268))
	if (x * x == i + 100) and (y * y == i + 268):
		print i


