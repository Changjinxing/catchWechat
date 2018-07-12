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

