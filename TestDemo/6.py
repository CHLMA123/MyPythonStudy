#!/usr/bin/python
# -*- coding: UTF-8 -*-
# __author__ = 'chlma'

'''题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：

F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)'''

# 使用递归

# def fib(n):
# 	if (n == 0):
# 		return 0
# 	if (n==1) or (n == 2):
# 		return 1
# 	return fib(n-1) + fib(n-2)
#
#
# print fib(int(raw_input('键盘输入你要输出的第几个斐波那契数列，结果为：')))

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print fib(int(raw_input('键盘输入你要输出前几个斐波那契数列，结果为：')))
