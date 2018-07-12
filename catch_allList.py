#!/usr/bin/python
#-*- coding:utf8 -*-
#这三行代码是防止在python2上面编码错误的，在python3上面不要要这样设置
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



import time
import os
import random

import requests
import urllib
from urllib import quote
from lxml import etree
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver

import MySQLdb as mdb

#add by zjx
import json

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import urllib2

from util import Util
global_util = Util()

import random

'''
def getHtml(url,proxies):
    random_proxy = random.choice(proxies)
    proxy_support = urllib2.ProxyHandler({"http":random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    html=urllib2.urlopen(url)
    return html
'''

proxy_list = ['180.118.86.44:9000',
'183.33.128.127:808',
'61.158.187.157:8080',
'14.20.235.72:9797',
'115.229.112.48:9000',
'163.125.17.174:8888',
'221.214.214.144:53281',
'222.217.68.148:8089',
'101.81.110.17:9000',
'119.57.108.89:53281',
'115.239.79.92:9000',
'222.217.68.148:8089',
'124.207.82.166:8008',
'115.229.112.229:9000',
'27.191.234.69:9999',
'115.229.114.214:9000',
'163.125.17.160:8888',
'222.222.169.60:53281',
'115.229.116.125:9000',
'119.250.23.6:9000',
'163.125.17.167:8888',
'115.229.117.64:9000',
'163.125.68.82:9999',
'163.125.68.100:9999',
'163.125.68.89:9999',
'124.205.155.153:9090',
'163.125.68.105:9999',
'163.125.254.255:9797',
'59.39.63.142:8181',
'125.77.25.116:80',
'58.247.127.145:53281',
'163.125.68.71:9999'
]

proxy_list = ['http://sjiang:2mb9JpFL@149.255.104.146:29842',
'http://sjiang:2mb9JpFL@149.255.104.182:29842',
'http://sjiang:2mb9JpFL@149.255.104.189:29842',
'http://sjiang:2mb9JpFL@149.255.104.224:29842',
'http://sjiang:2mb9JpFL@149.255.104.249:29842',
'http://sjiang:2mb9JpFL@149.255.105.106:29842',
'http://sjiang:2mb9JpFL@149.255.105.126:29842',
'http://sjiang:2mb9JpFL@149.255.105.25:29842',
'http://sjiang:2mb9JpFL@149.255.105.42:29842',
'http://sjiang:2mb9JpFL@149.255.105.85:29842',
'http://sjiang:2mb9JpFL@149.255.105.94:29842',
'http://sjiang:2mb9JpFL@172.241.142.108:29842',
'http://sjiang:2mb9JpFL@172.241.142.198:29842',
'http://sjiang:2mb9JpFL@172.241.142.20:29842',
'http://sjiang:2mb9JpFL@172.241.142.207:29842',
'http://sjiang:2mb9JpFL@172.241.142.4:29842',
'http://sjiang:2mb9JpFL@172.241.142.7:29842',
'http://sjiang:2mb9JpFL@172.241.143.149:29842',
'http://sjiang:2mb9JpFL@172.241.143.157:29842',
'http://sjiang:2mb9JpFL@172.241.143.158:29842',
'http://sjiang:2mb9JpFL@172.241.143.229:29842',
'http://sjiang:2mb9JpFL@172.241.143.32:29842',
'http://sjiang:2mb9JpFL@172.241.143.39:29842',
'http://sjiang:2mb9JpFL@23.105.143.102:29842',
'http://sjiang:2mb9JpFL@23.105.143.105:29842',
'http://sjiang:2mb9JpFL@23.105.143.110:29842',
'http://sjiang:2mb9JpFL@23.105.143.115:29842',
'http://sjiang:2mb9JpFL@23.105.143.116:29842',
'http://sjiang:2mb9JpFL@23.105.143.134:29842',
'http://sjiang:2mb9JpFL@23.105.143.135:29842',
'http://sjiang:2mb9JpFL@23.105.143.203:29842',
'http://sjiang:2mb9JpFL@23.105.143.223:29842',
'http://sjiang:2mb9JpFL@23.105.146.100:29842',
'http://sjiang:2mb9JpFL@23.105.146.127:29842',
'http://sjiang:2mb9JpFL@23.105.146.150:29842',
'http://sjiang:2mb9JpFL@23.105.146.158:29842',
'http://sjiang:2mb9JpFL@23.105.146.178:29842',
'http://sjiang:2mb9JpFL@23.105.146.200:29842',
'http://sjiang:2mb9JpFL@23.105.146.217:29842',
'http://sjiang:2mb9JpFL@23.105.146.242:29842',
'http://sjiang:2mb9JpFL@23.105.146.247:29842',
'http://sjiang:2mb9JpFL@23.105.165.111:29842',
'http://sjiang:2mb9JpFL@23.105.165.171:29842',
'http://sjiang:2mb9JpFL@23.105.165.17:29842',
'http://sjiang:2mb9JpFL@23.105.165.234:29842',
'http://sjiang:2mb9JpFL@23.105.165.92:29842',
'http://sjiang:2mb9JpFL@23.105.167.135:29842',
'http://sjiang:2mb9JpFL@23.105.167.169:29842',
'http://sjiang:2mb9JpFL@23.105.167.29:29842',
'http://sjiang:2mb9JpFL@23.105.167.46:29842',
'http://sjiang:2mb9JpFL@23.105.167.73:29842',
'http://sjiang:2mb9JpFL@23.105.167.96:29842',
'http://sjiang:2mb9JpFL@172.241.153.153:29842',
'http://sjiang:2mb9JpFL@172.241.153.209:29842',
'http://sjiang:2mb9JpFL@172.241.153.223:29842',
'http://sjiang:2mb9JpFL@172.241.153.82:29842',
'http://sjiang:2mb9JpFL@172.241.153.86:29842',
'http://sjiang:2mb9JpFL@172.241.94.154:29842',
'http://sjiang:2mb9JpFL@172.241.94.162:29842',
'http://sjiang:2mb9JpFL@172.241.94.173:29842',
'http://sjiang:2mb9JpFL@172.241.94.183:29842',
'http://sjiang:2mb9JpFL@172.241.94.228:29842',
'http://sjiang:2mb9JpFL@172.241.94.245:29842',
'http://sjiang:2mb9JpFL@172.241.94.34:29842',
'http://sjiang:2mb9JpFL@172.241.94.38:29842',
'http://sjiang:2mb9JpFL@172.241.94.78:29842',
'http://sjiang:2mb9JpFL@172.241.95.121:29842',
'http://sjiang:2mb9JpFL@172.241.95.122:29842',
'http://sjiang:2mb9JpFL@172.241.95.139:29842',
'http://sjiang:2mb9JpFL@172.241.95.142:29842',
'http://sjiang:2mb9JpFL@172.241.95.169:29842',
'http://sjiang:2mb9JpFL@172.241.95.218:29842',
'http://sjiang:2mb9JpFL@172.241.95.222:29842',
'http://sjiang:2mb9JpFL@172.241.95.254:29842',
'http://sjiang:2mb9JpFL@172.241.95.69:29842',
'http://sjiang:2mb9JpFL@23.106.22.121:29842',
'http://sjiang:2mb9JpFL@23.106.22.213:29842',
'http://sjiang:2mb9JpFL@23.106.22.49:29842',
'http://sjiang:2mb9JpFL@23.106.22.58:29842',
'http://sjiang:2mb9JpFL@23.106.22.82:29842',
'http://sjiang:2mb9JpFL@23.106.24.129:29842',
'http://sjiang:2mb9JpFL@23.106.24.144:29842',
'http://sjiang:2mb9JpFL@23.106.24.157:29842',
'http://sjiang:2mb9JpFL@23.106.24.164:29842',
'http://sjiang:2mb9JpFL@23.106.24.179:29842',
'http://sjiang:2mb9JpFL@23.106.24.80:29842',
'http://sjiang:2mb9JpFL@172.241.152.11:29842',
'http://sjiang:2mb9JpFL@172.241.152.126:29842',
'http://sjiang:2mb9JpFL@172.241.152.215:29842',
'http://sjiang:2mb9JpFL@172.241.152.42:29842',
'http://sjiang:2mb9JpFL@172.241.152.64:29842',
'http://sjiang:2mb9JpFL@172.241.152.70:29842',
'http://sjiang:2mb9JpFL@23.80.138.111:29842',
'http://sjiang:2mb9JpFL@23.80.138.132:29842',
'http://sjiang:2mb9JpFL@23.80.138.159:29842',
'http://sjiang:2mb9JpFL@23.80.138.35:29842',
'http://sjiang:2mb9JpFL@23.80.138.48:29842',
'http://sjiang:2mb9JpFL@23.80.140.119:29842',
'http://sjiang:2mb9JpFL@23.80.140.149:29842',
'http://sjiang:2mb9JpFL@23.80.140.210:29842',
'http://sjiang:2mb9JpFL@23.80.140.254:29842',
'http://sjiang:2mb9JpFL@23.80.140.95:29842',
'http://sjiang:2mb9JpFL@23.80.156.107:29842',
'http://sjiang:2mb9JpFL@23.80.156.191:29842',
'http://sjiang:2mb9JpFL@23.80.156.214:29842',
'http://sjiang:2mb9JpFL@23.80.156.217:29842',
'http://sjiang:2mb9JpFL@23.80.156.218:29842',
'http://sjiang:2mb9JpFL@23.80.156.36:29842',
'http://sjiang:2mb9JpFL@23.80.156.41:29842',
'http://sjiang:2mb9JpFL@23.80.156.58:29842',
'http://sjiang:2mb9JpFL@23.80.156.91:29842',
'http://sjiang:2mb9JpFL@23.80.157.120:29842',
'http://sjiang:2mb9JpFL@23.80.157.124:29842',
'http://sjiang:2mb9JpFL@23.80.157.133:29842',
'http://sjiang:2mb9JpFL@23.80.157.15:29842',
'http://sjiang:2mb9JpFL@23.80.157.194:29842',
'http://sjiang:2mb9JpFL@23.80.157.41:29842',
'http://sjiang:2mb9JpFL@23.80.157.59:29842',
'http://sjiang:2mb9JpFL@23.80.157.87:29842',
'http://sjiang:2mb9JpFL@23.80.157.91:29842',
'http://sjiang:2mb9JpFL@23.80.157.96:29842',
'http://sjiang:2mb9JpFL@23.81.57.117:29842',
'http://sjiang:2mb9JpFL@23.81.57.125:29842',
'http://sjiang:2mb9JpFL@23.81.57.152:29842',
'http://sjiang:2mb9JpFL@23.81.57.15:29842',
'http://sjiang:2mb9JpFL@23.81.57.228:29842',
'http://sjiang:2mb9JpFL@23.81.57.243:29842',
'http://sjiang:2mb9JpFL@23.81.58.145:29842',
'http://sjiang:2mb9JpFL@23.81.58.191:29842',
'http://sjiang:2mb9JpFL@23.81.58.4:29842',
'http://sjiang:2mb9JpFL@23.81.58.74:29842',
'http://sjiang:2mb9JpFL@23.81.58.77:29842',
'http://sjiang:2mb9JpFL@23.81.63.113:29842',
'http://sjiang:2mb9JpFL@23.81.63.121:29842',
'http://sjiang:2mb9JpFL@23.81.63.131:29842',
'http://sjiang:2mb9JpFL@23.81.63.192:29842',
'http://sjiang:2mb9JpFL@23.81.63.233:29842',
'http://sjiang:2mb9JpFL@23.81.63.236:29842',
'http://sjiang:2mb9JpFL@23.81.63.43:29842',
'http://sjiang:2mb9JpFL@23.81.63.5:29842',
'http://sjiang:2mb9JpFL@23.81.63.84:29842',
'http://sjiang:2mb9JpFL@23.81.80.106:29842',
'http://sjiang:2mb9JpFL@23.81.80.128:29842',
'http://sjiang:2mb9JpFL@23.81.80.149:29842',
'http://sjiang:2mb9JpFL@23.81.80.151:29842',
'http://sjiang:2mb9JpFL@23.81.80.163:29842',
'http://sjiang:2mb9JpFL@23.81.80.21:29842',
'http://sjiang:2mb9JpFL@23.81.80.40:29842',
'http://sjiang:2mb9JpFL@23.81.80.4:29842',
'http://sjiang:2mb9JpFL@23.81.80.80:29842',
'http://sjiang:2mb9JpFL@23.81.80.94:29842',
'http://sjiang:2mb9JpFL@23.83.81.172:29842',
'http://sjiang:2mb9JpFL@23.83.92.10:29842',
'http://sjiang:2mb9JpFL@23.83.92.125:29842',
'http://sjiang:2mb9JpFL@23.83.92.136:29842',
'http://sjiang:2mb9JpFL@23.83.92.144:29842',
'http://sjiang:2mb9JpFL@23.83.92.165:29842',
'http://sjiang:2mb9JpFL@23.83.92.189:29842',
'http://sjiang:2mb9JpFL@23.83.92.200:29842',
'http://sjiang:2mb9JpFL@23.83.92.57:29842',
'http://sjiang:2mb9JpFL@23.83.92.62:29842',
'http://sjiang:2mb9JpFL@23.83.93.161:29842',
'http://sjiang:2mb9JpFL@23.83.93.163:29842',
'http://sjiang:2mb9JpFL@23.83.93.184:29842',
'http://sjiang:2mb9JpFL@23.83.93.210:29842',
'http://sjiang:2mb9JpFL@23.83.93.21:29842',
'http://sjiang:2mb9JpFL@23.83.93.26:29842',
'http://sjiang:2mb9JpFL@23.83.93.66:29842',
'http://sjiang:2mb9JpFL@23.83.93.70:29842',
'http://sjiang:2mb9JpFL@23.83.93.85:29842',
'http://sjiang:2mb9JpFL@8.18.120.149:29842',
'http://sjiang:2mb9JpFL@8.18.120.154:29842',
'http://sjiang:2mb9JpFL@8.18.120.23:29842',
'http://sjiang:2mb9JpFL@8.18.120.240:29842',
'http://sjiang:2mb9JpFL@8.18.120.242:29842',
'http://sjiang:2mb9JpFL@8.18.120.27:29842',
'http://sjiang:2mb9JpFL@8.18.120.37:29842',
'http://sjiang:2mb9JpFL@8.18.120.70:29842',
'http://sjiang:2mb9JpFL@8.18.120.95:29842',
'http://sjiang:2mb9JpFL@8.18.121.11:29842',
'http://sjiang:2mb9JpFL@8.18.121.162:29842',
'http://sjiang:2mb9JpFL@8.18.121.171:29842',
'http://sjiang:2mb9JpFL@8.18.121.174:29842',
'http://sjiang:2mb9JpFL@8.18.121.183:29842',
'http://sjiang:2mb9JpFL@8.18.121.213:29842',
'http://sjiang:2mb9JpFL@8.18.121.218:29842',
'http://sjiang:2mb9JpFL@8.18.121.247:29842',
'http://sjiang:2mb9JpFL@8.18.121.249:29842',
'http://sjiang:2mb9JpFL@84.201.17.112:29842',
'http://sjiang:2mb9JpFL@84.201.17.199:29842',
'http://sjiang:2mb9JpFL@84.201.17.209:29842',
'http://sjiang:2mb9JpFL@84.201.17.239:29842',
'http://sjiang:2mb9JpFL@84.201.17.37:29842',
'http://sjiang:2mb9JpFL@84.201.17.63:29842',
'http://sjiang:2mb9JpFL@84.201.18.122:29842',
'http://sjiang:2mb9JpFL@84.201.18.208:29842',
'http://sjiang:2mb9JpFL@84.201.18.236:29842',
'http://sjiang:2mb9JpFL@84.201.18.238:29842',
'http://sjiang:2mb9JpFL@84.201.18.243:29842',
'http://sjiang:2mb9JpFL@84.201.18.41:29842',
'http://sjiang:2mb9JpFL@91.108.64.186:29842',
'http://sjiang:2mb9JpFL@91.108.64.132:29842',
'http://sjiang:2mb9JpFL@91.108.64.139:29842',
'http://sjiang:2mb9JpFL@91.108.64.145:29842',
'http://sjiang:2mb9JpFL@91.108.64.156:29842',
'http://sjiang:2mb9JpFL@91.108.65.134:29842',
'http://sjiang:2mb9JpFL@91.108.65.138:29842',
'http://sjiang:2mb9JpFL@91.108.65.142:29842',
'http://sjiang:2mb9JpFL@91.108.65.161:29842',
'http://sjiang:2mb9JpFL@91.108.65.169:29842',
'http://sjiang:2mb9JpFL@91.108.66.139:29842',
'http://sjiang:2mb9JpFL@91.108.66.152:29842',
'http://sjiang:2mb9JpFL@91.108.66.157:29842',
'http://sjiang:2mb9JpFL@91.108.66.174:29842',
'http://sjiang:2mb9JpFL@91.108.66.182:29842',
'http://sjiang:2mb9JpFL@91.108.66.185:29842',
'http://sjiang:2mb9JpFL@91.108.67.130:29842',
'http://sjiang:2mb9JpFL@91.108.67.141:29842',
'http://sjiang:2mb9JpFL@91.108.67.145:29842',
'http://sjiang:2mb9JpFL@91.108.67.154:29842',
'http://sjiang:2mb9JpFL@91.108.67.162:29842',
'http://41717sean:gspr77@38.145.168.251:80',
'http://41717sean:gspr77@149.115.178.38:80',
'http://41717sean:gspr77@149.115.176.107:80',
'http://41717sean:gspr77@149.115.191.47:80',
'http://41717sean:gspr77@38.145.171.1:80',
'http://41717sean:gspr77@149.115.164.202:80',
'http://41717sean:gspr77@38.145.186.196:80',
'http://41717sean:gspr77@38.145.165.126:80',
'http://41717sean:gspr77@38.145.186.133:80',
'http://41717sean:gspr77@38.145.187.22:80',
'http://41717sean:gspr77@38.145.166.216:80',
'http://41717sean:gspr77@38.145.180.246:80',
'http://41717sean:gspr77@149.115.184.6:80',
'http://41717sean:gspr77@38.145.161.238:80',
'http://41717sean:gspr77@38.145.165.225:80',
'http://41717sean:gspr77@149.115.178.122:80',
'http://41717sean:gspr77@38.145.173.194:80',
'http://41717sean:gspr77@38.145.176.126:80',
'http://41717sean:gspr77@38.145.181.94:80',
'http://41717sean:gspr77@38.145.171.176:80',
'http://41717sean:gspr77@38.145.162.202:80',
'http://41717sean:gspr77@38.145.178.108:80',
'http://41717sean:gspr77@38.145.183.213:80',
'http://41717sean:gspr77@38.145.179.160:80',
'http://41717sean:gspr77@149.115.191.10:80',
'http://41717sean:gspr77@38.145.187.218:80',
'http://41717sean:gspr77@38.145.170.131:80',
'http://41717sean:gspr77@38.145.175.253:80',
'http://41717sean:gspr77@38.145.169.61:80',
'http://41717sean:gspr77@38.145.173.11:80',
'http://41717sean:gspr77@38.145.168.170:80',
'http://41717sean:gspr77@38.145.169.181:80',
'http://41717sean:gspr77@38.145.172.106:80',
'http://41717sean:gspr77@38.145.188.182:80',
'http://41717sean:gspr77@38.145.168.240:80',
'http://41717sean:gspr77@149.115.191.23:80',
'http://41717sean:gspr77@149.115.187.237:80',
'http://41717sean:gspr77@38.145.171.101:80',
'http://41717sean:gspr77@149.115.181.232:80',
'http://41717sean:gspr77@38.145.177.129:80',
'http://41717sean:gspr77@38.145.188.181:80',
'http://41717sean:gspr77@38.145.167.191:80',
'http://41717sean:gspr77@38.145.181.194:80',
'http://41717sean:gspr77@38.145.170.164:80',
'http://41717sean:gspr77@149.115.183.8:80',
'http://41717sean:gspr77@149.115.183.82:80',
'http://41717sean:gspr77@38.145.168.60:80',
'http://41717sean:gspr77@38.145.162.184:80',
'http://41717sean:gspr77@38.145.176.137:80',
'http://41717sean:gspr77@149.115.185.194:80',
'http://41717sean:gspr77@38.145.183.73:80',
'http://41717sean:gspr77@149.115.177.21:80',
'http://41717sean:gspr77@149.115.189.197:80',
'http://41717sean:gspr77@149.115.191.32:80',
'http://41717sean:gspr77@38.145.184.140:80',
'http://41717sean:gspr77@149.115.179.204:80',
'http://41717sean:gspr77@38.145.182.143:80',
'http://41717sean:gspr77@149.115.182.146:80',
'http://41717sean:gspr77@149.115.177.205:80',
'http://41717sean:gspr77@149.115.168.9:80',
'http://41717sean:gspr77@38.145.183.52:80',
'http://41717sean:gspr77@38.86.50.15:80',
'http://41717sean:gspr77@149.115.191.8:80',
'http://41717sean:gspr77@149.115.191.11:80',
'http://41717sean:gspr77@38.145.187.164:80',
'http://41717sean:gspr77@149.115.191.104:80',
'http://41717sean:gspr77@149.115.191.44:80',
'http://41717sean:gspr77@149.115.177.132:80',
'http://41717sean:gspr77@149.115.191.14:80',
'http://41717sean:gspr77@149.115.179.237:80',
'http://41717sean:gspr77@149.115.183.197:80',
'http://41717sean:gspr77@38.145.178.48:80',
'http://41717sean:gspr77@38.145.186.166:80',
'http://41717sean:gspr77@38.145.174.95:80',
'http://41717sean:gspr77@38.145.182.231:80',
'http://41717sean:gspr77@149.115.191.24:80',
'http://41717sean:gspr77@149.115.184.125:80',
'http://41717sean:gspr77@38.145.162.117:80',
'http://41717sean:gspr77@149.115.182.184:80',
'http://41717sean:gspr77@38.145.185.20:80',
'http://41717sean:gspr77@38.145.166.89:80',
'http://41717sean:gspr77@149.115.191.26:80',
'http://41717sean:gspr77@38.145.180.75:80',
'http://41717sean:gspr77@38.145.180.231:80',
'http://41717sean:gspr77@149.115.178.105:80',
'http://41717sean:gspr77@38.145.170.84:80',
'http://41717sean:gspr77@38.145.181.78:80',
'http://41717sean:gspr77@38.145.188.179:80',
'http://41717sean:gspr77@38.145.178.152:80',
'http://41717sean:gspr77@149.115.167.146:80',
'http://41717sean:gspr77@38.145.182.240:80',
'http://41717sean:gspr77@38.145.178.12:80',
'http://41717sean:gspr77@38.145.182.105:80',
'http://41717sean:gspr77@149.115.177.42:80',
'http://41717sean:gspr77@149.115.183.51:80',
'http://41717sean:gspr77@149.115.182.214:80',
'http://41717sean:gspr77@149.115.176.184:80',
'http://41717sean:gspr77@38.145.187.181:80',
'http://41717sean:gspr77@38.145.172.188:80',
'http://41717sean:gspr77@149.115.181.35:80',
'http://user1:opcrawl@192.227.242.134:3128',
'http://user2:opcrawl@192.227.242.139:3128',
'http://user3:opcrawl@192.227.242.142:3128',
'http://user4:opcrawl@192.227.242.143:3128',
'http://user1:opcrawl@172.245.128.245:3128',
'http://user2:opcrawl@205.234.153.38:3128',
'http://user3:opcrawl@205.234.153.39:3128',
'http://user4:opcrawl@205.234.153.40:3128',
'http://user1:opcrawl@172.245.128.243:3128',
'http://user2:opcrawl@172.245.128.246:3128',
'http://user3:opcrawl@172.245.128.247:3128',
'http://user4:opcrawl@172.245.128.248:3128',
'http://user1:opcrawl@172.245.32.34:3128',
'http://user2:opcrawl@172.245.32.53:3128',
'http://user3:opcrawl@192.210.236.230:3128',
'http://user4:opcrawl@66.225.232.13:3128',
'http://user1:opcrawl@192.227.242.135:3128',
'http://user2:opcrawl@192.227.242.144:3128',
'http://user3:opcrawl@192.227.242.145:3128',
'http://user4:opcrawl@192.227.242.146:3128',
'http://user1:opcrawl@192.227.242.138:3128',
'http://user2:opcrawl@192.227.242.167:3128',
'http://user3:opcrawl@192.227.242.168:3128',
'http://user4:opcrawl@192.227.242.169:3128',
'http://user1:opcrawl@192.227.242.136:3128',
'http://user2:opcrawl@192.227.242.147:3128',
'http://user3:opcrawl@192.227.242.148:3128',
'http://user4:opcrawl@192.227.242.163:3128',
'http://user1:opcrawl@192.227.242.137:3128',
'http://user2:opcrawl@192.227.242.164:3128',
'http://user3:opcrawl@192.227.242.165:3128',
'http://user4:opcrawl@192.227.242.166:3128',
'62.210.169.105:2631',
'62.210.169.105:2632',
'62.210.169.105:2633',
'62.210.169.105:2634',
'62.210.169.105:2635',
'62.210.169.105:2636',
'62.210.169.105:2637',
'62.210.169.105:2638',
'62.210.169.105:2639',
'62.210.169.105:2640',
'62.210.169.105:2641',
'62.210.169.105:2642',
'62.210.169.105:2643',
'62.210.169.105:2644',
'62.210.169.105:2645',
'62.210.169.105:2646',
'62.210.169.105:2647',
'62.210.169.105:2648',
'62.210.169.105:2649',
'62.210.169.105:2650',
'62.210.169.105:2651',
'62.210.169.105:2652',
'62.210.169.105:2653',
'62.210.169.105:2654',
'62.210.169.105:2655']

def get_proxy(proxy_list):
    random_proxy = random.choice(proxy_list)
    #random_proxy = 'http://%s' % random_proxy
    print random_proxy
    proxies = { "http": random_proxy }
    return proxies
#proxies = { "http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080", } 
#requests.get("http://example.org", proxies=proxies)

class weixin_spider:
    def __init__(self, ):
        self.check = True
        
    def run(self):
        self.sublist = self.getSubList()
        #add by zjx
        #print json.dumps(self.sublist)
        #exit()
        cur_page = 1
        while cur_page < 100:
            for self.ename, self.name in self.sublist:
                
                crawl_names = ['sangongzi0906', 'ceb-licai']
                crawl_names = ['sangongzi0906']
                crawl_names = ['ceb-licai']
                
                if self.name not in crawl_names:
                    self.log('公众号: [' + self.ename + '] is not target account, skip')
                    continue
                
                print self.name
                
                self.search_url = ("http://weixin.sogou.com/weixin?usip=&query=%s&ft=&tsn=1&et=&interation=&type=2&wxid=&page=%d&ie=utf8") %(self.ename, cur_page)
                #add by zjx
                print self.search_url
                self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0","Referer": self.search_url}
                self.log('开始抓取公众号[' + self.name + ']' + time.strftime('%Y-%m-%d') + '的文章'   +':')
                maincontent = self.get_list(self.search_url)
                time.sleep(10)
            cur_page += 1
        self.log('crawled 100 page done')
        
    def get_list(self, search_url):
        global proxy_list
        random_proxies = get_proxy(proxy_list)
        html = requests.get(search_url, headers=self.headers, verify=False, proxies=random_proxies).content
        selector = etree.HTML(html)
        # 提取文本
        content = selector.xpath('//div[@class="news-box"]/ul/li/div[@class="txt-box"]/h3/a/@href')
        #add by zjx
        #print content
        #exit()
        if not content:
            print 'get empty list for %s' % search_url
            
        for list in content:
            maincontent = self.get_content(list)

    # 获得公众号文章列表详情内容
    def get_content(self, each):
        data = {}
        article = requests.get(each, headers=self.headers, verify=False).content
        soup = BeautifulSoup(article, 'html.parser')
        selector = etree.HTML(article)
        
        print soup
        
        select_user = selector.xpath('//*[@id="js_name"]/text()')
        if(select_user):
            #data['user'] = selector.xpath('//*[@id="post-user"]/text()')[0]
            data['user'] = select_user[0].strip()
        else:
            data['user'] = ''
        
        content_user = selector.xpath('//*[@id="js_content"]//span/span[4]/text()')
        #print self.ename, self.ename in content_user
        if self.ename in content_user:
            data['user'] = self.name
        #print json.dumps(content_user), data['user']
        #exit()
        
        # 使用webdriver.PhantomJS
        driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs',
                                     service_args=['--ignore-ssl-errors=true', '--ssl-protocol=tlsv1'])
        driver.get(each)
        page_source =  driver.page_source
        page_source_selector = etree.HTML(page_source)
        
        
         # 1 标题
        if (page_source_selector.xpath('//*[@id="activity-name"]/text()')):
            data['title'] = page_source_selector.xpath('//*[@id="activity-name"]/text()')
        else:
            data['title'] = ''

        for ix in data['title']:
            data['title'] = ix.strip()
        
        data['description'] = data['title']

        print 'title is '+ data['title']
        print 'description is '+ data['description']
        print 'user is ' + data['user']

        checkrelate = self.checkRelate(data['user'])
        print 'user:' + data['user'] + 'name:' + self.name
        # checkrelate = (False,True)[data['user'] == self.name]
        isexist = self.checkExist(data['title'])
        
        print checkrelate, isexist
        #exit()

        if(checkrelate and isexist):#判断是否是目标公众号
            #exit()
            #print soup
            #exit()

            #data['createtime'] = selector.xpath('//*[@id="post-date"]/text()')[0]
            publish_time_result = selector.xpath('//*[@id="publish_time"]/text()')
            #print json.dumps(publish_time_result)
            #exit();
            data['createtime'] = 'now'
            if publish_time_result:
                data['createtime'] = publish_time_result[0]

            #作者昵称
            # data['nickname'] = selector.xpath('//*[@id="img-content"]/div[1]/em[2]/text()')[0]
            
            data['url'] = each

            # 图片
            imglist = soup.find_all('img')
            #print (imglist)
            #exit()
            length = len(imglist)
            newlist = []
            for i in range(0, length):
                if (imglist[i].get('data-src') != None):
                    newlist.insert(1, imglist[i].get('data-src'))
                if (imglist[i].get('src') != None):
                    newlist.insert(1, imglist[i].get('src'))
            #print newlist
            #exit()
            body = soup.find_all('div', class_='rich_media_content ')[0]
            body = str(body).replace('data-src', 'src')
            img = ''
            local_imgs = list()
            for i in range(len(newlist)):
                print i
                if (newlist[i].encode("UTF-8") != ''):
                    #save to img cloud or save to local storage
                    imgurl = newlist[i].encode("UTF-8")
                    print imgurl
                    if imgurl.startswith('http') or imgurl.startswith('https'):
                        #check end
                        #if imgurl.endwith('.png') or imgurl.endwith('.jpg'):
                        img_id = global_util.gen_image_id(imgurl)
                        print imgurl, img_id
                        #local_img_path = '/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/imgs/%s.jpg' % img_id
                        #urllib.urlretrieve(imgurl, local_img_path)
                        
                        imgpath = str(time.time()) + str(int(random.uniform(10, 20))) + str(img_id)
                        if not os.path.exists('/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/laravel/public/img/weixin/' + data['user']):
                            os.makedirs('/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/laravel/public/img/weixin/' + data['user'], mode=0755)
                        newImgPath = '/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/laravel/public/img/weixin/' + data['user'] + '/' + imgpath + '.jpg'
                        urllib.urlretrieve(newlist[i], newImgPath)
                        
                        local_imgs.append(newImgPath)
                        #exit()
                        #else:
                        #    print "error: image[%s] type not png or jpg" % imgurl
                        #    #self.log('error: image type not png or jpg')
                    '''
                    tempBody = newlist[i]
                    newlist[i] = newlist[i].replace('https:','')
                    newlist[i] = newlist[i].replace('http:','')
                    newlist[i] = newlist[i].replace('//','http://')
                    
                    imgpath = str(time.time()) + str(int(random.uniform(10, 20)))
                    if not os.path.exists('/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/laravel/public/img/weixin/' + data['user']):
                        os.makedirs('/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/laravel/public/img/weixin/' + data['user'], mode=0755)
                    newImgPath = '/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/laravel/public/img/weixin/' + data['user'] + '/' + imgpath + '.jpg'
                    urllib.urlretrieve(newlist[i], newImgPath)
                    
                    saveimgpath = newImgPath.replace('/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/laravel/public', '')
                    body = body.replace(tempBody, 'https://www.zjx.com' + saveimgpath)
                    
                    img += 'https://www.zjx.com' + newImgPath
                    '''
            data['imgurl'] = ';'.join(local_imgs)
            
            # 文章主体部分
            file_path = data['title']
            file = file_path.replace('/', '-')
            file = '%s.%s.html' % (file, str(time.time()))
            if not os.path.exists('/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/url/weixin/' + data['user']):
                os.makedirs('/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/url/weixin/' + data['user'], mode=0755)
            with open('/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/url/weixin/' + data['user'] + '/' + file, 'w') as f:
                f.write(body)
            data['body'] = '/Users/zhangjinxing/git/catchWechat/catchWechat/wwwroot/url/weixin/' + data['user'] + '/' + file

            # 信息处理状态： 0 未处理  1 图片已经转储到本地 2 已经发布到线上待处理数据库
            data['status'] = 0
            data['userEname'] = self.getuserEname(data['user'])
            self.log('suceess : 抓取文章：'+data['title'] +'成功！' )
            ##存储
            #add by zjx
            print json.dumps(data)
            #exit()
            self.save(data)
        else:
            print 'user[%s] is not [%s]' % (data['user'], self.name)
            self.log('waring : have checked unlink-subscription，catch forwards!')


# Model ()
# host,port,user,passwd,db 配置成自己的 Mysql 配置
# 实际使用可以考虑把model层封装成包import使用，这里为了方便环境搭建没有做

    def save(self,data):
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'passwd': '123456',
            'db': 'weixin',
            'charset': 'utf8'
        }
        self.conn = mdb.connect(**self.config)
        cursor = self.conn.cursor()
        try:
            sql = (
            "insert into Article (title, user, userEname,createtime, body, status,url,imgurl) values('%s','%s', '%s', '%s','%s', '%s', '%s', '%s')" %
            (data['title'],data['user'],data['userEname'],data['createtime'],data['body'],data['status'],data['url'],data['imgurl']))
            cursor.execute(sql)
            self.conn.commit()
        except:
            import traceback
            traceback.print_exc()
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()
            
        
    def checkRelate(self,subName):
        self.config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': '123456',
            'db': 'weixin',
            'charset': 'utf8'
        }
        self.conn = mdb.connect(**self.config)

        cursor = self.conn.cursor()
        try:
            sql ="select subName from subscription where status= 1 and subName ='%s'  " %(subName)
            print sql
            cursor.execute(sql)
            self.conn.commit()
            temp = cursor.fetchall()
            print temp
            if (temp):
                return True
            else:
                return False
        except:
            import traceback
            traceback.print_exc()
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()


    def checkExist(self,title):
        #检查查到的文章标题是否存在
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'passwd': '123456',
            'db': 'weixin',
            'charset': 'utf8'
        }
        self.conn = mdb.connect(**self.config)
        cursor = self.conn.cursor()
        try:
            sql ="select id from Article where title ='%s'  " %(title)
            cursor.execute(sql)
            self.conn.commit()
            temp = cursor.fetchall()
            if (temp):
                return False
            else:
                return True
        except:
            import traceback
            traceback.print_exc()
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    def getuserEname(self,user):
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'passwd': '123456',
            'db': 'weixin',
            'charset': 'utf8'
        }
        self.conn = mdb.connect(**self.config)
        cursor = self.conn.cursor()
        try:
            sql ="select id from subscription where subName ='%s'  " %(user)
            cursor.execute(sql)
            self.conn.commit()
            temp = cursor.fetchall()
            return temp
        except:
            import traceback
            traceback.print_exc()
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    def getSubList(self):
        # 查询公众号列表
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'passwd': '123456',
            'db': 'weixin',
            'charset': 'utf8'
        }
        self.conn = mdb.connect(**self.config)
        cursor = self.conn.cursor()
        try:
            sql = "select subEname,subName from Subscription where status= 1 "
            cursor.execute(sql)
            temp = cursor.fetchall()
            return  temp
            self.conn.commit()
        except:
            import traceback
            traceback.print_exc()
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()


    def get_search_result_by_keywords(self):
        self.log('搜索地址为：%s' % self.sogou_search_url)
        return self.s.get(self.sogou_search_url, headers=self.headers, timeout=self.timeout).content


    def log(self,msg):
        # print u'%s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg) 
        print msg


if __name__ == '__main__':
    """
    print ''''' 
              *****************************************  
              **    Welcome to Spider of 公众号爬虫       **  
              **      Created on 2018-07--11          **  
              **      @author: zjx              **  
              ***************************************** 
      '''
      """

    # subscription = raw_input(u'输入要爬取的公众号')
    # if not subscription:
    #     subscription = 'Article'
    weixin_spider().run()

