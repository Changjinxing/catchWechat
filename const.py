# !/usr/bin/python2.7
# coding=utf-8
__author__ = 'jinxing.zjx'

class Const:

    # downloader conf
    DEFAULT_TIMEOUT = 30
    DEFAULT_CACHE = 'no-cache'
    DEFAULT_UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
    
    JS_CRAWL_URL_PREFIX = 'http://10.50.66.84:16002/?src='
    JS_RENDER_URL_PREFIX = 'http://10.40.109.145:10381/render/'
    RETRY_COUNT = 3
    
    DATA_SAVING_PATH = './data/data.txt'
    BASEITEM_SAMPLE_PATH = './baseitem_sample'
    
    ENV_IN_ONLINE = "in_online"
    ENV_IN_TEST = "in_test"
    ENV_ID_ONLINE = "id_online"
    ENV_ID_TEST = "id_test"
    
    ENV_ID_LOCAL = "id_local"
    ENV_IN_LOCAL = "in_local"

    # 印尼正式环境
    # CUR_ENV = ENV_ID_ONLINE
    # 印度正式环境
    # CUR_ENV = ENV_IN_ONLINE
    # 印度测试环境
    CUR_ENV = ENV_ID_TEST

    if CUR_ENV == ENV_IN_ONLINE:
        BASEITEM_HOST = "iflow-in.napi.ucweb.com"
        BASEITEM_NAPI_KEY = ""
        BASEITEM_APP_ID = "3b6d17ac31be490e8ea5d08d048538d5"
        BASEITEM_NAPI_CLASS_ID = "baseitem"
    elif CUR_ENV == ENV_IN_TEST:
        BASEITEM_HOST = "napi.ucweb.com"
        BASEITEM_NAPI_KEY = ""
        BASEITEM_APP_ID = "6ec85e7c8b3a4e9f854487ceee4ae7a0"
        BASEITEM_NAPI_CLASS_ID = "baseitem"
    elif CUR_ENV == ENV_ID_ONLINE:
        BASEITEM_HOST = "napi.ucweb.com"
        BASEITEM_NAPI_KEY = ""
        BASEITEM_APP_ID = "bfc72d8c900e443aa7cbb9ecf785e346"
        BASEITEM_NAPI_CLASS_ID = "baseitem"
    elif CUR_ENV == ENV_ID_TEST:
        BASEITEM_HOST = "napi.ucweb.com"
        BASEITEM_NAPI_KEY = ""
        BASEITEM_APP_ID = "6ec85e7c8b3a4e9f854487ceee4ae7a0"
        BASEITEM_NAPI_CLASS_ID = "baseitem"

    mons_map = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Mei': '05',
        'Jun': '06',
        'Jul': '07',
        'Agt': '08',
        'Aug': '08',
        'Sep': '09',
        'Sept': '09',
        'Okt': '10',
        'Oct': '10',
        'Nov': '11',
        'Des': '12',
        'Dec': '12',
        'январь': '01',
        '\u044f\u043d\u0432\u0430\u0440\u044c': '01',
        '%d0%98%d1%8e%d0%bd%d1%8c': '01',
        'февраль': '02',
        '\u0444\u0435\u0432\u0440\u0430\u043b\u044c': '02',
        '%d1%84%d0%b5%d0%b2%d1%80%d0%b0%d0%bb%d1%8c': '02',
        'март': '03',
        '\u043c\u0430\u0440\u0442': '03',
        '%d0%bc%d0%b0%d1%80%d1%82': '03',
        'апрель': '04',
        '\u0430\u043f\u0440\u0435\u043b\u044c': '04',
        '%d0%b0%d0%bf%d1%80%d0%b5%d0%bb%d1%8c': '04',
        'май': '05',
        '\u043c\u0430\u0439': '05',
        '%d0%bc%d0%b0%d0%b9': '05',
        'Июнь': '06',
        '\u0418\u044e\u043d\u044c': '06',
        '%d0%98%d1%8e%d0%bd%d1%8c': '06',
        'июль': '07',
        '\u0438\u044e\u043b\u044c': '07',
        '%d0%b8%d1%8e%d0%bb%d1%8c': '07',
        'август': '08',
        '\u0430\u0432\u0433\u0443\u0441\u0442': '08',
        '%d0%b0%d0%b2%d0%b3%d1%83%d1%81%d1%82': '08',
        'сентябрь': '09',
        '\u0441\u0435\u043d\u0442\u044f\u0431\u0440\u044c': '09',
        '%d1%81%d0%b5%d0%bd%d1%82%d1%8f%d0%b1%d1%80%d1%8c': '09',
        'октябрь': '10',
        '\u043e\u043a\u0442\u044f\u0431\u0440\u044c': '10',
        '%d0%be%d0%ba%d1%82%d1%8f%d0%b1%d1%80%d1%8c': '10',
        'ноябрь': '11',
        '\u043d\u043e\u044f\u0431\u0440\u044c': '11',
        '%d0%bd%d0%be%d1%8f%d0%b1%d1%80%d1%8c': '11',
        'декабрь': '12',
        '\u0434\u0435\u043a\u0430\u0431\u0440\u044c': '12',
        '%d0%b4%d0%b5%d0%ba%d0%b0%d0%b1%d1%80%d1%8c': '12',
    }
    
    days_map = {
        '1': '01',
        '2': '02',
        '3': '03',
        '4': '04',
        '5': '05',
        '6': '06',
        '7': '07',
        '8': '08',
        '9': '09',
    }
    
    mons = [
        '01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12',
    ]
    day_31 = [1, 3, 5, 7, 8, 10, 12]

    

    GOAL_IMG_PREFIX = 'https://secure.cache.images.core.optasports.com/soccer/teams'
    GOAL_IMG_WIDTH = 75
    GOAL_IMG_HEIGHT = 75