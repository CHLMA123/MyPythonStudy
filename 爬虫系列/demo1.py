#!/usr/bin/python
# -*- coding: UTF-8 -*-

'文档注释:a test module'
__author__ = 'chlma'

import urllib2
''' 第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，
    第三个timeout是设置超时时间。
    第二三个参数是可以不传送的，data默认为空None，
    timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT'''
# response = urllib2.urlopen('http://www.baidu.com')
# # esponse对象有一个read方法，可以返回获取到的网页内容。
# print response.read()

request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
print response.read()



