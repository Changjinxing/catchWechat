#-*- coding: UTF-8 -*-
import sys
import requests
import json
import time
import hashlib

from const import Const

class Util:
    def __init__(self,\
        img_prefix=Const.GOAL_IMG_PREFIX,\
        img_width=Const.GOAL_IMG_WIDTH, img_height=Const.GOAL_IMG_HEIGHT):
        self.img_prefix = img_prefix
        self.img_width = img_width
        self.img_height = img_height

    def format_date_time(self, dateStr, timeStr, mons_map=Const.mons_map, days_map=Const.days_map):
        if dateStr in ['Today', 'Hari Ini', 'Сегодня']:
            return 0

        dates = dateStr.split(' ')
        #print not dates
        #print len(dates)
        #print dates[1]
        #print dates[1] in mons_map
        #print isinstance(int(dates[0]), int)
        if not dates or len(dates) < 3 or dates[1] not in mons_map or not isinstance(int(dates[0]), int):
            print 'return format_date_time'
            return 0
        day = dates[0]
        monStr = dates[1]
        year = dates[2]
        mon = mons_map[monStr]
        print year, mon, day
        if day in days_map:
            day = days_map[day]
        
        time_str = '%s-%s-%sT%s:00' % (year, mon, day, timeStr)
        #logger.debug('format time str:%s', time_str)
        timeStamp = self.timeStr2timeStamp(time_str)
        #logger.debug('dateStr:%s`year:%s`mon:%s`day:%s`time_str:%s', dateStr, year,mon,day,time_str)
        return timeStamp


    def get_date_time(self, date_str, time_str):

        print time_str, date_str
        date_time = int(time.time()) * 1000
        if time_str and date_str:
            cur_date_time = self.format_date_time(date_str, time_str) * 1000
            date_time = cur_date_time
        return date_time

    def generateIconUrl(self, img_id):
        #url_prefix = 'https://secure.cache.images.core.optasports.com/soccer/teams/75x75/uuid_'
        #'https://secure.cache.images.core.optasports.com/soccer/teams/75x75/uuid_%s.png' % id
        icon_url = "{}/{}x{}/uuid_{}.png".format(self.img_prefix, self.img_width, self.img_height, img_id)

        return icon_url

    # load game_ids from game_data/game.txt
    # Const.GAME_DATA_SAVING_PATH
    def loadGameData2List(self, game_file):
        game_ids = list()
        live_urls = list()
        date_times = list()
        
        f = open(game_file, 'r')
        for line in f:
            line = line.strip()
            if not line:
                continue
            line_data = line.split('\t')
            if len(line_data) != 3:
                continue
            game_ids.append(line_data[0])
            live_urls.append(line_data[1])
            date_times.append(int(line_data[2]))
        f.close()
        
        return game_ids, live_urls, date_times
    
    # check game_id already exists by checking game_data/game.txt
    # Const.GAME_DATA_SAVING_PATH
    def checkExistGameId(self, game_id, game_file):
        game_ids, live_urls, date_times = self.loadGameData2List(game_file)
        if game_id in game_ids:
            return True
        else:
            return False

    # output game_id, live_url, game_time
    # Const.GAME_DATA_SAVING_PATH
    def outputSingleGame(self, game_id, live_url, game_time, lang, file_path):
        f = open(file_path, "a")
        line = '%s\t%s\t%s\t%s' % (game_id, live_url, game_time, lang)
        f.write(line.encode('utf-8'))
        f.write('\n')
        f.close()
        return line

    # output game_id, live_url, game_time
    # Const.GAME_DATA_SAVING_PATH
    def outputJsons(self, json_obj, file_path):
        f = open(file_path, "w")
        line = json.dumps(json_obj)
        f.write(line.encode('utf-8'))
        f.write('\n')
        f.close()
        return line

    # quote str using urllib2.quote()
    # return quoteStr
    def strQuote(self, str):
        import urllib2
        return urllib2.quote(str)

    # judge begin of mon or not
    def judgeBegofMon(self, time_stamp_ms):
        time_stamp_s = time_stamp_ms / 1000
        time_arr = time.localtime(time_stamp_s)
        other_style_time_str = time.strftime("%Y%m%d%H%M%s", time_arr)
        #logger.debug('%s to %s', time_stamp_s, other_style_time_str)
        
        #year = other_style_time_str[0:4]
        #mon = other_style_time_str[4:6]
        day = other_style_time_str[6:8]
        
        hour = other_style_time_str[8:10]
        min = other_style_time_str[10:12]
        sec = other_style_time_str[12:14]
        
        print 'time_stamp_s:%d`other_style_time_str:%s`day:%s`hour:%s`min:%s`sec:%s' % (time_stamp_s, other_style_time_str, day, hour, min, sec)
        #if day == '01':
            #exit()
        if day == '01' and hour == '00' and min == '00':
            return True, int(sec)
        elif day == '01' and hour == '00':
            return True, int(min) * 60 + int(sec)
            
        return False, 0

    def get_year_mon(self, date_time):
        time_stamp_s = date_time / 1000
        time_arr = time.localtime(time_stamp_s)
        time_str = time.strftime("%Y%m", time_arr)
        
        year = time_str[0:4]
        mon = time_str[4:6]

        return year, mon

    def int2dateStr(self, idx):
        next_idx = -1
        idx_str = str(idx)
        if len(idx_str) != 8:
            return '', next_idx

        year = idx_str[0:4]
        mon = idx_str[4:6]
        day = idx_str[6:8]

        date_str = '%s-%s-%s' % (year, mon, day)

        if mon not in Const.mons:
            return '', next_idx

        #print year, mon, day
        y = int(year)
        m = int(mon)
        d = int(day)

        divsor = 30
        if m in Const.day_31:
            divsor = 31

        next_d = (d + 1) % divsor
        next_d = divsor if next_d == 0 else next_d
        next_m = (m + d / divsor) % 12
        next_m = 12 if next_m == 0 else next_m
        next_y = y
        if m == 12 and d == divsor:
            next_y += 1

        next_date_str = '%d%02d%02d' % (next_y, next_m, next_d)

        next_idx = int(next_date_str)

        return date_str, next_idx

    def genRand(self, start=0, end=1, step=1):
        import random
        return random.randrange(start, end, step)

    # split by '\t', check conf_cnt
    # return  list of (line.split('\t'))
    def loadConf(self, filepath, conf_cnt=3):
        conf_infos = list()
        f = open(filepath, 'r')
        for line in f:
            line = line.strip()
            if not line:
                continue
            line_data = line.split('\t')
            if len(line_data) != conf_cnt:
                #logger.error('not format data, line: %s', line)
                continue
            conf = list()
            for i in range(conf_cnt):
                conf.append(line_data[i])
            
            conf_infos.append(conf)
        
        f.close()
        
        return conf_infos
    
    def loadDoc(self, filepath):
        f = open(filepath, 'r')
        
        doc = ''
        for line in f:
            line = line.strip()
            if not line:
                continue
            doc  += line
        
        f.close()
        
        return doc
        
    def loadDatas(self, filepath):
        f = open(filepath, 'r')
        
        data = list()
        for line in f:
            line = line.strip()
            if not line:
                continue
            data.append(line)
        
        f.close()
        
        return data
        
    # seed_crawl_infos = ELUTHU_util.loadCrawlInfo(Const.SEED_CRAWL_FILE)
    # file format: seed_name\tis_finished\tlast_crawl_page
    #                    seed_name\tis_finished\tlast_crawl_page
    # return: {'seed_name': {'is_finished': 0/1, 'last_crawl_page': 1/2(int)},
    #              'seed_name': {'is_finished': 0/1, 'last_crawl_page': 1/2(int)},}
    def loadCrawlInfo(self, filepath):
        seed_crawl_infos = dict()
        f = open(filepath, 'r')
        for line in f:
            line = line.strip()
            if not line:
                continue
            line_data = line.split('\t')
            if len(line_data) != 3:
                #logger.error('not format data, line: %s', line)
                continue
            seed_name = line_data[0]
            seed_crawl_info = dict()
            seed_crawl_info['is_finished'] = int(line_data[1])
            seed_crawl_info['last_crawl_page'] = int(line_data[2])
            seed_crawl_infos[seed_name] = seed_crawl_info
        
        f.close()
        
        return seed_crawl_infos
    
    # output str to file
    # outputStr(str, file_path=Const.LEAGUE_TEAM_INFO_PATH)
    def outputStr(self, str, file_path=''):
        try:
            f = open(file_path, "a")
            line = str
            f.write(line.encode('utf-8'))
            f.write('\n')
            f.close()
            return True
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            return False
        except:
            print "Unexpected error:", sys.exc_info()[0]
            return False
        #logger.info('file_path:%s`line:%s', file_path, line)

    #2018-03-16T20:00:00+00:00 to timestamp: sec int(time.time())
    def timeStr2timeStamp(self, timeStr, format='%Y-%m-%dT%H:%M:%S'):
        timeStamp = int(time.mktime(time.strptime(timeStr, format)))
        return timeStamp

    def timeStamp2str(self, time_stamp, format='%Y%m'):
        timeArray = time.localtime(time_stamp)
        otherStyleTime = time.strftime(format, timeArray)
        return otherStyleTime

    def gen_list_id(self, time_stamp, prefix='upcoming_'):
        if not time_stamp:
            return None

        curMon = self.timeStamp2str(time_stamp)
        list_id = prefix + curMon
        return list_id

    # get live title by live_url
    # example: live_url = 'http://www.goal.com/id/pertandingan/be%C5%9Fikta%C5%9F-v-bayern-m%C3%BCnchen/3erv06wriro3dztm17zja79m2'
    def get_live_title(self, live_url, goal_id):
        if not live_url:
            return None

        live_info = live_url.split('/')
        if goal_id not in live_info:
            return None

        game_title = live_info[-2]
        return game_title

    
    def gen_image_id(self, image_url):
        m = hashlib.md5()
        m.update(image_url)
        image_id = m.hexdigest()[0:10]
        return image_id

    # gen teamid using md5, key = teamid crawled
    def genItemId(self, seedUrl, contentUrl):
        idstr = self.url_normalize(seedUrl) + contentUrl
        m = hashlib.md5()
        m.update(idstr)
        key = m.hexdigest()[0:13]
        itemId = int(key, 16)
        return itemId

    # gen id using md5, key = str
    def genItemId(self, idstr, len=13):
        m = hashlib.md5()
        m.update(idstr)
        key = m.hexdigest()[0:len]
        id = int(key, 16)
        return id

    # gen teamid using md5, key = teamid crawled
    #usage: 
    #teamIdStr = '2ez9cvam9lp9jyhng3eh3znb4'
    #teamId = genTeamId(teamIdStr)
    def genTeamId(self, teamIdStr):
        m = hashlib.md5()
        m.update(teamIdStr)
        key = m.hexdigest()[0:13]
        teamId = int(key, 16)
        return teamId
    
    def loadSampleData(self, file_path):
        input_str = open(file_path, 'r')
        content = input_str.read()
        if not content:
            return {}
        #exit()
        sample = json.loads(content)
        input_str.close()
        return sample
    
    # generate resource
    def genResources(self, img_url, img_info, is_cover_pic=True, res_type='image', img_title=''):

        res=dict()
        #print img_url
        #exit()
        res['originalUrl'] = img_url
        res['isCoverPic'] = is_cover_pic
        res['type'] = res_type
        res['title'] = img_title
        
        res_id = self.gen_image_id(img_url)
        res['id'] = res_id
        
        res['oriSize'] = int(img_info['size'])
        res['oriWidth'] = int(img_info['width'])
        res['oriHeight'] = int(img_info['height'])
        res['phash'] = img_info['phash']
        res['originalSaveUrl'] = img_info['org_url']
        res['thumbUrl'] = img_info['org_url'] + ";,,PNG;3,208x"
        res['optimalUrl'] = img_info['org_url'] + ";,,png;3,480x"
        
        res['thumbHeight'] = 160
        res['thumbWidth'] = 208
        res['optimalHeight'] = 240
        res['optimalWidth'] = 312
        
        resources = list()
        resources.append(res)
        
        return res_id, resources
    
    # generate json
    def genBaseItemJson(self, update_info, file_path='./baseitem_sample'):
        
        #content_image_part = '<div style="text-align: center;"><res-image id="%s"></res-image></div>' % res_id
        #final_content = content_image_part + final_content

        sample_dict = self.loadSampleData(file_path)
        
        # need to check special field you need
        sample_dict['data']['title'] = update_info.get('title', '')
        sample_dict['data']['pages'][0]['content'] = update_info.get('content', '')
        sample_dict['data']['pages'][0]['originalUrl'] = update_info.get('url', '')
        sample_dict['data']['originalUrl'] = update_info.get('originalUrl', '')
        
        del sample_dict['data']['resources']
        sample_dict['data']['resources'] = update_info.get('resources', [])
        
        sample_dict['data']['transfer_to_swift'] = 'false'
        sample_dict['data']['status'] = 0
        sample_dict['data']['error_desc'] = ""
        
        del sample_dict['data']['_created_at']
        del sample_dict['data']['_updated_at']
        del sample_dict['data']['status']
        del sample_dict['data']['error_desc']
        del sample_dict['data']['description']
        del sample_dict['data']['id_flag']
        del sample_dict['data']['timestamps']

        sample_dict['data']['itemType'] = update_info.get('itemType', 0)
        sample_dict['data']['styleType'] = update_info.get('styleType', 0)
        sample_dict['data']['country'] = update_info.get('country', 'india')
        sample_dict['data']['daoliuType'] = update_info.get('daoliuType', 0)
        sample_dict['data']['isCp'] = update_info.get('isCp', 0)
        sample_dict['data']['language'] = update_info.get('language', 'english')
        sample_dict['data']['mediaType'] = update_info.get('mediaType', 0)
        sample_dict['data']['comscore_id'] = update_info.get('comscore_id', '')
        sample_dict['data']['channel'] = update_info.get('channel', [])
        sample_dict['data']['contentType'] = update_info.get('contentType', 0)
        sample_dict['data']['seedDeliverStatus'] = update_info.get('seedDeliverStatus', 0)
        sample_dict['data']['classifyMethod'] = update_info.get('classifyMethod', 0)
        
        sample_dict['data']['seedName'] = update_info.get('seedName', '')
        sample_dict['data']['seedIconDesc'] = update_info.get('seedIconDesc', '')
        sample_dict['data']['listArticleFrom'] = update_info.get('listArticleFrom', '')
        sample_dict['data']['seedSite'] = update_info.get('seedSite', '')
        sample_dict['data']['belongSeed'] = update_info.get('belongSeed', '')
        sample_dict['data']['belongSite'] = update_info.get('belongSite', '')
        sample_dict['data']['seedIconUrl'] = update_info.get('seedIconUrl', '')
        sample_dict['data']['seedUrl'] = update_info.get('seedUrl', '')
        sample_dict['data']['unionId'] = update_info.get('unionId', '')
        sample_dict['data']['gaId'] = update_info.get('gaId', '')
        sample_dict['data']['categoryId'] = update_info.get('categoryId', [])
        
        source_pub_time = int(time.time())*1000
        sample_dict['data']['sourcePublishTime'] = update_info.get('source_pub_time', source_pub_time)
        print sample_dict['data']['sourcePublishTime']
        
        sample_dict['data']['skipTitle'] = update_info.get('skipTitle', 1)
        sample_dict['data']['city'] = update_info.get('city', '')
        sample_dict['data']['province'] = update_info.get('province', '')

        itemId = update_info.get('itemId', '')
        print "[debug] itemId: %s" % itemId
        sample_dict['data']['id'] = int(itemId)
        sample_dict['data']['_id'] = itemId
        
        sample_dict['data']['retry_count'] = 0
        
        return sample_dict
    
    # convert dict(key, list[]) to list[dict(key, val)]
    # lxml.etree.path return list, not usable
    def parseResult(self, cnt, ret_dict):
        ret = list()
        for i in range(0, cnt):
            item = dict()
            ret.append(item)
        for key,val in ret_dict.items():
            item = dict()
            #print key, val
            for idx, v in enumerate(val):
                ret[idx][key] = v
        return ret
    
    # dedup by dedup_key in a list[dict()]
    def deleteRepeat(self, l1, dedup_key):
            
        if not l1:
            #logger.warning('input list empty.')
            return l1
        
        l2 = list()
        l2.append(l1[0])
            
        for dict_item in l1:
            k = 0
            for item in l2:
                if dict_item[dedup_key] != item[dedup_key]:
                    k = k+1
                else:
                    break
                if k == len(l2):
                    l2.append(dict_item)
        #logger.debug('dedup_key:%s`ori_list:%s`dedup_list:%s', dedup_key, json.dumps(l1), json.dumps(l2))      
        return l2
    
    """Given two dicts, merge them into a new dict as a shallow copy."""
    def merge_two_dicts(self, x, y):
        z = x.copy()
        z.update(y)
        return z
    
    def get_goal_id(self, live_url):
        if not live_url:
            return None
        live_url = live_url.strip().strip('/')
        goal_id = live_url.split('/')[-1]
        return goal_id
    
    
    def delRelIds(self, host, class_id, app_id, napi_key, item_id, rel_ids):
        import recoitem_common
        #print item_id, item_info, class_id, app_id, napi_key
        #exit()
        recoitem_common.setNapiHost(host)
        
        for id in rel_ids:
             is_exist = recoitem_common.checkRecoItemList(app_id, class_id, id, item_id)
             if is_exist:
                 recoitem_common.delFromNapiLstCurl(app_id, class_id, id, item_id)
                 #logger.info('status:%s`tag:%s`game_id:%s`classsid:%s`appid:%s', status, id, game_id, classId, appId)
    
    def patchToNapi(self, host, class_id, app_id, napi_key, item_id, item_info, user='jinxing.zjx'):
        import recoitem_common
        #print item_id, item_info, class_id, app_id, napi_key
        #exit()
        recoitem_common.setNapiHost(host)
        
        if not user:
            status, url = recoitem_common.patchRecoItem(item_id, item_info, class_id, app_id, napi_key)
        else:
            status, url = recoitem_common.patchRecoItemUser(item_id, item_info, class_id, app_id, napi_key, user)
        
        return status, url
    
    def putToNapi(self, host, class_id, app_id, napi_key, item_id, item_info, user='jinxing.zjx'):
        import recoitem_common
        #print item_id, item_info, class_id, app_id, napi_key
        #exit()
        recoitem_common.setNapiHost(host)
        
        if not user:
            status, url = recoitem_common.postRecoItem(item_id, item_info, class_id, app_id, napi_key)
        else:
            status, url = recoitem_common.postRecoItemUser(item_id, item_info, class_id, app_id, napi_key, user)
        
        return status, url
        
    def deleteFromNapi(self, host, class_id, app_id, napi_key, item_id, user='jinxing.zjx'):
        import recoitem_common
        #print item_id, item_info, class_id, app_id, napi_key
        #exit()
        recoitem_common.setNapiHost(host)
        
        if not user:
            status, url = recoitem_common.delRecoItem(item_id, class_id, app_id, napi_key)
        else:
            status, url = recoitem_common.delRecoItemUser(item_id, class_id, app_id, napi_key, user)
        
        return status, url
        
    def inactiveNapi(self, host, class_id, app_id, napi_key, item_id, user='jinxing.zjx'):
        import recoitem_common
        #print item_id, item_info, class_id, app_id, napi_key
        #exit()
        recoitem_common.setNapiHost(host)
        
        if not user:
            status, url = recoitem_common.inactiveRecoItem(item_id, class_id, app_id, napi_key)
        else:
            status, url = recoitem_common.inactiveRecoItemUser(item_id, class_id, app_id, napi_key, user)
        
        return status, url
        
    def patchToNapiList(self, host, class_id, app_id, napi_key, item_id, item_info, list_id, user='jinxing.zjx'):
        import recoitem_common
        #print item_id, item_info, class_id, app_id, napi_key
        #exit()
        recoitem_common.setNapiHost(host)
        
        if not user:
            status, url = recoitem_common.patchRecoItemList(item_id, item_info, class_id, app_id, napi_key, list_id)
        else:
            status, url = recoitem_common.patchRecoItemListUser(item_id, item_info, class_id, app_id, napi_key, list_id, user)
        
        return status, url
        
    def delFromNapiList(self, host, class_id, app_id, item_id, list_id, user='jinxing.zjx'):
        import recoitem_common
        #print item_id, item_info, class_id, app_id, napi_key
        #exit()
        recoitem_common.setNapiHost(host)
        
        if not user:
            status, url = recoitem_common.delFromNapiList(app_id,class_id,list_id,item_id)
        else:
            status, url = recoitem_common.delFromNapiListUser(app_id,class_id,list_id,item_id, user)
        
        return status, url
        
    def patchToNapiListCategory(self, host, class_id, app_id, napi_key, item_id, item_info, list_id, category_id, user='jinxing.zjx'):
        import recoitem_common
        #print item_id, item_info, class_id, app_id, napi_key
        #exit()
        recoitem_common.setNapiHost(host)
        
        if not user:
            status, url = recoitem_common.patchRecoItemListCategory(item_id, item_info, class_id, app_id, napi_key, list_id, category_id)
        else:
            status, url = recoitem_common.patchRecoItemListCategoryUser(item_id, item_info, class_id, app_id, napi_key, list_id, category_id, user)
        
        return status, url
        
    def delFromNapiListCategory(self, host, class_id, app_id, item_id, list_id, category_id, user='jinxing.zjx'):
        import recoitem_common
        #print item_id, item_info, class_id, app_id, napi_key
        #exit()
        recoitem_common.setNapiHost(host)
        
        if not user:
            status, url = recoitem_common.delFromNapiLstCategory(app_id,class_id,category_id,list_id,item_id)
        else:
            status, url = recoitem_common.delFromNapiLstCategoryUser(app_id,class_id,category_id,list_id,item_id, user)
        
        return status, url
