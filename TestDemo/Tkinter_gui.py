#!/usr/bin/python
# -*- coding: UTF-8 -*-

'文档注释:a test module'
__author__ = 'chlma'

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ww.sina.com.cn',80))


