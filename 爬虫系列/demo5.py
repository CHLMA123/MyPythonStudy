#!/usr/bin/python
# -*- coding: UTF-8 -*-

'文档注释:a test module'
__author__ = 'chlma'

# 1.URL格式的确定
'''观察一下百度贴吧的任意一个帖子。

比如：
	http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1

		http://  代表资源传输使用http协议
 		tieba.baidu.com 是百度的二级域名，指向百度贴吧的服务器。
 		/p/3138733512 是服务器某个资源，即这个帖子的地址定位符
 		see_lz和pn是该URL的两个参数，分别代表了只看楼主和帖子页码，等于1表示该条件为真

	可以把URL分为两部分，一部分为基础部分，一部分为参数部分。

	例如，上面的URL我们划分基础部分是 http://tieba.baidu.com/p/3138733512，参数部分是 ?see_lz=1&pn=1
'''

# 2.页面的抓取

import urllib
import urllib2
import re


# 百度贴吧爬虫类
class BDTB:
	# 初始化，传入基地址，是否只看楼主的参数
	def __init__(self, baseUrl, seeLZ):
		self.baseURL = baseUrl
		self.seeLZ = '?see_lz=' + str(seeLZ)

	# 传入页码，获取该页帖子的代码
	def getPage(self, pageNum):
		try:
			url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			print response.read()
			return response
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print u"连接百度贴吧失败,错误原因", e.reason
				return None

# 3.提取相关信息

	#获取帖子标题
	def getTitle(self):
		page = self.getPage(1)
		pattern = re.compile('<h3 class="core_title_txt.*?>(>*?)</h3>')
		result = re.search(pattern,page)
		if result:
			#print result.group(1) #测试输出
			print result.group(1).strip()
		else:
			return None




baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
bdtb.getPage(1)

