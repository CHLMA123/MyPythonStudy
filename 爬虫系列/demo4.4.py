#!/usr/bin/python
# -*- coding: UTF-8 -*-

'文档注释:a test module'
__author__ = 'chlma'

import urllib2
import re
import threading
import time


class Tool:
	def pTitle(self):
		return re.compile('<title.*?>(.*?)</', re.S)

	def pContent(self):
		return re.compile(
			'<div class="author.*?>.*?<a.*?<img.*?/>(.*?)</a>.*?</div>.*?<div.*?class="content.*?>(.*?)</div>.*?class="number.*?>(.*?)</.*?',
			re.S)


class CSBK(threading.Thread):
	def __init__(self, max_page):
		threading.Thread.__init__(self, name='christian_thread')
		self.baseUrl = "http://www.qiushibaike.com/hot/page/"
		self.maxPage = int(max_page) + 1
		self.tool = Tool()

	def getPageContent(self, pageNum):
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = {'User-Agent': user_agent}
		url = self.baseUrl + str(pageNum)
		try:
			request = urllib2.Request(url, headers=headers)
			response = urllib2.urlopen(request)
			content = response.read().decode('utf-8', 'ignore')
			content = content.encode('gbk', 'ignore')
			return content
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print u"error: ", e.reason
				return None

	def getPageDetail(self, c):
		items = re.findall(self.tool.pContent(), c)
		result = []
		for item in items:
			p = {}
			p['发布人'] = item[0].strip()
			p['id'] = item[2].strip()
			p['内容'] = item[1].strip()
			result.append(p)
		return result

	def getTitle(self, c):
		result = re.findall(self.tool.pTitle(), c)
		return result[0].strip()

	def run(self):
		print "---- " + time.ctime() + " ----\n"
		for page in range(1, self.maxPage):
			c = self.getPageContent(page)
			if c == None:
				print "URL已失效，请重试"
				return

			print "---- 正在抓取第" + str(page) + "页 ---- "
			title = self.getTitle(c)
			f = open(title + ' - Page_' + str(page) + '.txt', 'w')
			result = self.getPageDetail(c)
			cutLine = u'-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.\n'
			for item in result:
				f.write(cutLine)
				for K, V in item.items():
					f.write(str(K) + ' : ' + str(V) + '\n')
			print "---- 第" + str(page) + "页抓取完毕 ----\n"

			f.close()
			del result
			del f
			del cutLine
			del c
		print "---- " + time.ctime() + " ----"


maxPage = raw_input("输入想抓取的糗事百科的最大页数: \n")
csbk = CSBK(maxPage)
csbk.start()
