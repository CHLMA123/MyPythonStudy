#!/usr/bin/python
# -*- coding: UTF-8 -*-

'文档注释:a test module'
__author__ = 'chlma'

import urllib
import urllib2
import cookielib
import re

#山东大学绩点运算
class SDU():

	def __init__(self):
		self.loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
		self.cookies = cookielib.CookieJar()
		self.postdata = urllib.urlencode({
			'stuid':'201200131012',
			'pwd':'23342321'
		})
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

	def getPage(self):
		request = urllib2.Request(
			url=self.loginUrl,
			data=self.postdata
		)
		result = self.opener.open(request)
		#打印登录内容
		print  result.read().decode('gbk')


sdu = SDU()
sdu.getPage()

