#-*- coding:utf-8 -*-
__author__ = 'pf'

import urllib
import urllib2
import socket
import types
import time
import re
import os
import subprocess
import requests

class Login:

    #初始化
    def __init__(self):
        #检测间隔时间，单位为秒
        self.every = 10

    #模拟登录
    def login(self):
        print self.getCurrentTime(), u"拼命连网中..."
 #消息头
        url="http://222.24.19.190:8080/portal/pws?t=li"

        headers={
        'Host':"222.24.19.190:8080",
        'User-Agent':"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        'Accept':"application/json, text/javascript, */*; q=0.01",
        'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding':"gzip, deflate",
        'Referer':"http://222.24.19.190:8080/portal/index_default.jsp",
        'Content-Type':"application/x-www-form-urlencoded",
        'X-Requested-With':"XMLHttpRequest",
        'Content-Length':"291",
        'Connection':"close"
        }
        #消息头
        payload={
        'userName':'1403810041',
        'userPwd':'MTk4NDEy',
        'userurl':'http%3A%2F%2Fwww.msn.com%3Focid%3Dwispr&userip=222.24.52.200',
        'portalProxyIP':'222.24.19.190',
        'portalProxyPort':'50200',
        'dcPwdNeedEncrypt':'1',
        'assignIpType':'0',
        'appRootUrl':'=http%3A%2F%2F222.24.19.190%3A8080%2Fportal%2F',
        'manualUrlEncryptKey':'rTCZGLy2wJkfobFEj0JF8A%3D%3D'
        }

        r=requests.post(url,headers=headers,data=payload)
        print self.getCurrentTime(),u'连上了，没毛病...现在开始看连接正常着不'

    #判断当前是否可以连网
    def canConnect(self):
        fnull = open(os.devnull, 'w')
        result = subprocess.call('ping www.baidu.com', shell = True, stdout = fnull, stderr = fnull)
        fnull.close()
        if result:
            return False
        else:
            return True

    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #主函数
    def main(self):
        print self.getCurrentTime(), u"老铁您好，欢迎使用自动登陆系统"
        while True:
            self.login()
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print self.getCurrentTime(),u"断网了，呵呵哒"
                    self.login()
                else:
                    print self.getCurrentTime(), u"嗯，一切正常"
                time.sleep(self.every)
            time.sleep(self.every)

login = Login()
login.main()