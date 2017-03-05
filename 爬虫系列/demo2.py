#!/usr/bin/python
# -*- coding: UTF-8 -*-

'文档注释:a test module'
__author__ = 'chlma'

import urllib
import urllib2

# values = {"username":"877544586@qq.com", "password":"XXXXX"}
values = {}
values['username'] = "877544586@qq.com"
values['password'] = "XXXXX"
data = urllib.urlencode(values)

# POST方式
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)

# GET方式
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print "\n\n\n"
print geturl

print response.read()

'''模拟登陆CSDN，当然上述代码可能登陆不进去，因为CSDN还有个流水号的字段，没有设置全，比较复杂在这里就不写上去了，在此只是说明登录的原理。一般的登录网站一般是这种写法。'''