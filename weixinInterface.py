# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json,urllib
from lxml import etree
class WeixinInterface:
def __init__(self):
self.app_root = os.path.dirname(__file__)
self.templates_root = os.path.join(self.app_root, 'templates')
self.render = web.template.render(self.templates_root)
def GET(self):
#��ȡ�������
data = web.input()
signature = data.signature
timestamp = data.timestamp
nonce = data.nonce
echostr = data.echostr
#�Լ���token
Token = "luluyun33"
#�ֵ�������
list = [token,timestamp,nonce]
list.sort()
sha1 = hashlib.sha1()
map(sha1.update,list)
hashcode = sha1.hexdigest()
#sha1 �����㷨
#���������΢�ŵ�������ظ�echostr
if hashcode == signature:
return echostr
def POST(self):
str_xml = web.data() #���post ��������
xml = etree.fromstring(str_xml)#����XML ����
content = xml.find("Content").text#����û������������
msgType = xml.find("MsgType").text
fromUser = xml.find("FromUserName").text
toUser = xml.find("ToUserName").text
return self.render.reply_text(fromUser, toUser, int(time.time()),
u"�����ڻ��ڿ����У���û��ʲô���ܣ����ղ�˵���ǣ�\n" + content)