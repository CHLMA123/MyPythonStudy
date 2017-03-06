#!/usr/bin/python
# -*- coding: UTF-8 -*-

'文档注释:a test module'
__author__ = 'chlma'

# 2.提取某一页的所有段子

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}
try:
	request = urllib2.Request(url, headers=headers)
	reponse = urllib2.urlopen(request)
	content = reponse.read().decode('utf-8')
	# pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
     #                     'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)

	# 获取了发布人，发布内容
	pattern = re.compile('<div.*?clearfix">.*?<a.*?<a>*?<h2>(.*?)</h2>>*?<div.*?"content">.*?<span>(.*?)</span>', re.S)

	items = re.findall(pattern, content)
	for item in items:
		# haveImg = re.search("img", item[3])
		# if not haveImg:
		# 	print item[0], item[1], item[2], item[4]
		print item[0], item[1]
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason




