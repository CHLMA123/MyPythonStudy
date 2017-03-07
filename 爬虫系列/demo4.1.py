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
	# 获取了发布人，发布内容
	pattern = re.compile('<a class="contentHerf.*?>.*?<div class="content">.*?<span>(.*?)</span>', re.S)

	items = re.findall(pattern, content)
	for item in items:
		replaceBR = re.compile('<br/>')
		text = re.sub(replaceBR, "\n", item[0])
		print u"第%d页\t发布内容:\n%s" % (page, item[0])
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason




