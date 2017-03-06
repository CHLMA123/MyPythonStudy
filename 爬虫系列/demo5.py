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

#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()


# 百度贴吧爬虫类
class BDTB:
	# 初始化，传入基地址，是否只看楼主的参数
	def __init__(self, baseUrl, seeLZ):
		self.baseURL = baseUrl
		self.seeLZ = '?see_lz=' + str(seeLZ)
		self.tool = Tool()
	# 传入页码，获取该页帖子的代码
	def getPage(self, pageNum):
		try:
			url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			#print response.read()
			return response.read().decode('utf-8')
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print u"连接百度贴吧失败,错误原因", e.reason
				return None

# 3.提取相关信息

	#获取帖子标题
	def getTitle(self):
		page = self.getPage(1)
		pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
		result = re.search(pattern,page)
		if result:
			#print result.group(1) #测试输出
			print result.group(1).strip()
		else:
			return None

	#提取帖子页数,获取帖子一共有多少页
	def getPageNum(self):
		page = self.getPage(1)
		pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
		result = re.search(pattern,page)
		if result:
			return result.group(1).strip()
		else:
			return None

	#提取正文内容,获取每一层楼的内容,传入页面内容
	def getContent(self,page):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
		items = re.findall(pattern,page)
		# for item in items:
		# 	print item
		print self.tool.replace(items[1])


baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
bdtb.getContent(bdtb.getPage(1))

