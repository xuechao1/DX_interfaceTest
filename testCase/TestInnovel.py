# -*- coding:utf-8 -*-

import time, os
import requests
import warnings
import unittest
from pprint import pprint
from config import readConfig

read_conf = readConfig.ReadConfig()


class TestInnovel(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.s = requests.session()
        print("----开始执行测试用例  start ----")
        global code
        code = read_conf.get_login('code')
        global login_type
        login_type = read_conf.get_login('login_type')
        global userKeyWithoutImei
        userKeyWithoutImei = read_conf.get_login('userKeyWithoutImei')
        global channel
        channel = read_conf.get_login('channel')
        global sign
        sign = read_conf.get_login('sign')
        global timestamp
        timestamp = read_conf.get_login('timestamp')
        global oid
        oid = read_conf.get_login('oid')
        global mcc
        mcc = read_conf.get_login('mcc')
        global versionName
        versionName = read_conf.get_login('versionName')
        global deviceId
        deviceId = read_conf.get_login('deviceId')
        global uuid
        uuid = read_conf.get_login('uuid')
        global osType
        osType = read_conf.get_login('osType')
        global appKey
        appKey = read_conf.get_login('appKey')
        global apiLevel
        apiLevel = read_conf.get_login('apiLevel')
        global appTag
        appTag = read_conf.get_login('appTag')
        global androidId
        androidId = read_conf.get_login('androidId')
        global advertising_id
        advertising_id = read_conf.get_login('advertising_id')
        global userKey
        userKey = read_conf.get_login('userKey')
        global versionCode
        versionCode = read_conf.get_login('versionCode')
        global distinct_id
        distinct_id = read_conf.get_login('distinct_id')
        global originProduct
        originProduct = read_conf.get_login('originProduct')
        global imei
        imei = read_conf.get_login('imei')
        global interfaceCode
        interfaceCode = read_conf.get_login('interfaceCode')
        global appLanguage
        appLanguage = read_conf.get_login('appLanguage')
        global u
        u = read_conf.get_login('u')
        global s
        ss = read_conf.get_login('s')
        s = ss + '%3D%3D'
        global timezone
        timezone = 'Asia%2FShanghai'
        global host
        host = 'http://3.85.16.233:32100'
        global host_www
        host_www = 'http://activity.dreame.com/'
        global type
        type = read_conf.get_login('type')
        global page
        page = read_conf.get_login('page')
        global size
        size = read_conf.get_login('size')
        global source
        source = read_conf.get_login('source')
        global start
        start = read_conf.get_login('start')
        global kwType
        kwType = read_conf.get_login('kwType')
        global count
        count = read_conf.get_login('count')
        global device_type
        device_type = read_conf.get_login('device_type')
        global net_type
        net_type = read_conf.get_login('net_type')
        global app_ver
        app_ver = read_conf.get_login('app_ver')
        global bid
        bid = '3TXM0%2FmmzB0r6NeOsPRhmg%3D%3D'

    def test_001_visitor_login(self):
        """
        ---测试游客用户能正常登录APP的功能----
        :return:
        """
        print("----测试游客用户能正常登录APP的功能----")
        url = '/api/visitorLogin?code={}&login_type={}&timezone={}&userKeyWithoutImei={}' \
              '&channel={}&sign={}&oid={}&mcc={}&versionName={}&deviceId={}&uuid={}&osType={}' \
              '&appKey={}&apiLevel={}&appTag={}&androidId={}&advertising_id={}&userKey={}' \
              '&versionCode={}&distinct_id={}&originProduct={}&imei={}&interfaceCode={}' \
              '&appLanguage={}'.format(code, login_type, timezone, userKeyWithoutImei, channel, sign,
                                       oid, mcc, versionName, deviceId, uuid, osType, appKey, apiLevel,
                                       appTag, androidId, advertising_id, userKey, versionCode,
                                       distinct_id, originProduct, imei, interfaceCode, appLanguage)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_002_library_reading(self):
        print("----在书城页面，选择任意一本书籍，测试能正常阅读的功能----")
        sign = '9135c6a69783403e5267a3da6bdccd87'
        url = '/Discover?appKey={}&userKey={}&userKeyWithoutImei={}&imei={}&interfaceCode={}' \
              '&mcc={}&channel={}&versionCode={}&versionName={}&osType={}' \
              '&distinct_id={}&advertising_id={}&timezone={}&deviceId={}&uuid={}&androidId={}' \
              '&apiLevel={}&appLanguage={}&appTag={}&originProduct={}' \
              '&sign={}'.format(appKey, userKey, userKeyWithoutImei, imei, interfaceCode, mcc, channel,
                                versionCode, versionName, osType, distinct_id, advertising_id, timezone,
                                deviceId, uuid, androidId, apiLevel, appLanguage, appTag, originProduct, sign)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("----------------book details -------------------")
        chapterId = 'vP22tN7fHy4nfPWt0a3RAw%3D%3D'
        bookId = '3TXM0%2FmmzB0r6NeOsPRhmg%3D%3D'
        sign = 'b9f4ef215549f8ea7cedb6ac58bb08aa'
        url = '/api/readV1?timezone={}&userKeyWithoutImei={}&channel={}&sign={}&mcc={}' \
              '&versionName={}&deviceId={}&uuid={}&chapterId={}&osType={}&appKey={}&apiLevel={}' \
              '&appTag={}&androidId={}&advertising_id={}&userKey={}&versionCode={}&bookId={}' \
              '&s={}&u={}&distinct_id={}&originProduct={}&imei={}&interfaceCode={}' \
              '&appLanguage={}'.format(timezone, userKeyWithoutImei, channel, sign, mcc, versionName,
                                       deviceId, uuid, chapterId, osType, appKey, apiLevel, appTag,
                                       androidId, advertising_id, userKey, versionCode, bookId, s, u,
                                       distinct_id, originProduct, imei, interfaceCode, appLanguage)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_003_library_book_follow(self):
        print("----在书城页面，选择任意一本书籍，测试能正常进行收藏操作的功能----")
        sign = '5870deddf7e479f0c4d70f3c2b9fad6a'
        url = '/apiBookshelf/follow?timezone={}&userKeyWithoutImei={}&channel={}&advertising_id={}' \
              '&sign={}&mcc={}&versionName={}&deviceId={}&uuid={}&userKey={}&versionCode={}&s={}' \
              '&u={}&distinct_id={}&originProduct={}&osType={}&imei={}&appKey={}&bid={}' \
              '&interfaceCode={}&apiLevel={}&appTag={}&androidId={}' \
              '&appLanguage={}'.format(timezone, userKeyWithoutImei, channel, advertising_id, sign, mcc,
                                       versionName, deviceId, uuid, userKey, versionCode, s, u, distinct_id,
                                       originProduct, osType, imei, appKey, bid, interfaceCode, apiLevel,
                                       appTag, androidId, appLanguage)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_004_library_book_unfollow(self):
        print("----在书城界面，选择任意一本已收藏的书籍，测试其能取消收藏的功能----")
        sign = '5870deddf7e479f0c4d70f3c2b9fad6a'
        url = '/apiBookshelf/unfollow?timezone={}&userKeyWithoutImei={}&channel={}&advertising_id={}' \
              '&sign={}&mcc={}&versionName={}&deviceId={}&uuid={}&userKey={}&versionCode={}&s={}' \
              '&u={}&distinct_id={}&originProduct={}&osType={}&imei={}&appKey={}&bid={}' \
              '&interfaceCode={}&apiLevel={}&appTag={}&androidId={}' \
              '&appLanguage={}'.format(timezone, userKeyWithoutImei, channel, advertising_id, sign,
                                       mcc, versionName, deviceId, uuid, userKey, versionCode, s, u,
                                       distinct_id, originProduct, osType, imei, appKey, bid,
                                       interfaceCode, apiLevel, appTag, androidId, appLanguage)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_005_library_time_list(self):
        print("----在书城侧页面，点击右上角的会话按钮，测试其能正常进入到站内信界面的功能----")
        sign1 = '2ed3ae9c1c080507c0c6eba98b30b781'
        url = '/Message/getSepUnreadMessage?timestamp={}&appKey={}&u={}&s={}&userKey={}' \
              '&userKeyWithoutImei={}&imei={}&interfaceCode={}&mcc={}&channel={}&versionCode={}' \
              '&versionName={}&osType={}&distinct_id={}&advertising_id={}&timezone={}&deviceId={}' \
              '&uuid={}&androidId={}&apiLevel={}&appLanguage={}&appTag={}&originProduct={}' \
              '&sign={}'.format(timestamp, appKey, u, s, userKey, userKeyWithoutImei, imei,
                                interfaceCode, mcc, channel, versionCode, versionName, osType,
                                distinct_id, advertising_id, timezone, deviceId, uuid, androidId,
                                apiLevel, appLanguage, appTag, originProduct, sign1)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        sign2 = 'dea2959e5f7748262ee5bfc6b0575bee'
        url = '/Message/getNewMessage?type={}&page={}&size={}&appKey={}&u={}&s={}&userKey={}' \
              '&userKeyWithoutImei={}&imei={}&interfaceCode={}&mcc={}&channel={}&versionCode={}' \
              '&versionName={}&osType={}&distinct_id={}&advertising_id={}&timezone={}&deviceId={}' \
              '&uuid={}&androidId={}&apiLevel={}&appLanguage={}&appTag={}&originProduct={}' \
              '&sign={}'.format(type, page, size, appKey, u, s, userKey, userKeyWithoutImei, imei,
                                interfaceCode, mcc, channel, versionCode, versionName, osType,
                                distinct_id, advertising_id, timezone, deviceId, uuid, androidId,
                                apiLevel, appLanguage, appTag, originProduct, sign2)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_006_library_get_time_list_content(self):
        print("----在书城页面，点击右上角的“时刻表”，测试其能正常跳转到可解锁书籍查看界面的功能----")
        sign = 'd17dc931fcee87641fc37971232e6812'
        url = '/calendar/getNewCalendarContent?timezone={}&appKey={}&u={}&s={}&userKey={}' \
              '&userKeyWithoutImei={}&imei={}&interfaceCode={}&mcc={}&channel={}&versionCode={}' \
              '&versionName={}&osType={}&distinct_id={}&advertising_id={}&deviceId={}&uuid={}' \
              '&androidId={}&apiLevel={}&appLanguage={}&appTag={}&originProduct={}' \
              '&sign={}'.format(timezone, appKey, u, s, userKey, userKeyWithoutImei, imei, interfaceCode,
                                mcc, channel, versionCode, versionName, osType, distinct_id,
                                advertising_id, deviceId, uuid, androidId, apiLevel, appLanguage,
                                appTag, originProduct, sign)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_007_library_sel_page_reading(self):
        print("----在书城页面，选择任意一本多章节书，测试用户可以自主选择章节内容的功能----")
        chapterId = 'iWWOUOIP8qYSuSjfhPiqHQ%3D%3D'
        bookId = 'CGjoBU1ZajfcBfrRWpDOMQ%3D%3D'
        sign = 'b518b3c941450deb557eeef527b26f00'
        url = '/api/readV1?timezone={}&userKeyWithoutImei={}&channel={}&sign={}&mcc={}' \
              '&versionName={}&deviceId={}&uuid={}&chapterId={}&osType={}&appKey={}&apiLevel={}' \
              '&appTag={}&androidId={}&advertising_id={}&userKey={}&versionCode={}&bookId={}' \
              '&s={}&u={}&distinct_id={}&originProduct={}&imei={}&interfaceCode={}' \
              '&appLanguage={}'.format(timezone, userKeyWithoutImei, channel, sign, mcc, versionName,
                                       deviceId, uuid, chapterId, osType, appKey, apiLevel, appTag,
                                       androidId, advertising_id, userKey, versionCode, bookId, s, u,
                                       distinct_id, originProduct, imei, interfaceCode, appLanguage)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_008_library_read_follow(self):
        print("----在书架页面，测试直接点击收藏的书会进入到阅读界面的功能----")
        sign1 = '8b57cf7e71e999a49b59a2d2ddbd9558'
        bookshelf = '5sWGWgn3N3%2BRmsriaWVXjg%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D%2CjgTrpkm6Vt3gp7f%2BHJvJsQ%3D%3D%2CRvdq9VhPzTLkgyHofVE8Pw%3D%3D%2CGzv0Bf5b9nfvE%2F8zzs2IGA%3D%3D%2CywFOb6nQwlgTfz7puYkRfQ%3D%3D'
        url1 = '/api/novelRecommend?timezone={}&userKeyWithoutImei={}&channel={}&sign={}&mcc={}' \
               '&versionName={}&deviceId={}&uuid={}&osType={}&appKey={}&id={}&apiLevel={}' \
               '&appTag={}&androidId={}&bookshelf={}&advertising_id={}&userKey={}&versionCode={}' \
               '&s={}&u={}&distinct_id={}&originProduct={}&imei={}&interfaceCode={}' \
               '&appLanguage={}'.format(timezone, userKeyWithoutImei, channel, sign1, mcc, versionName,
                                        deviceId, uuid, osType, appKey, id, apiLevel, appTag, androidId,
                                        bookshelf, advertising_id, userKey, versionCode, s, u,
                                        distinct_id, originProduct, imei, interfaceCode, appLanguage)
        url_1 = host + url1
        try:
            result_1 = self.s.get(url_1)
            t = result_1.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

        bookId = 'Gzv0Bf5b9nfvE%2F8zzs2IGA%3D%3D'
        chapterId = 'F40uCGCFZPCXZJXpOdrwoA%3D%3D'
        sign = '826df00c1bdd5a96ef119fc023620b67'
        url_0 = '/api/readV1?timezone={}&userKeyWithoutImei={}&channel={}&sign={}&mcc={}' \
                '&versionName={}&deviceId={}&uuid={}&chapterId={}&osType={}&appKey={}&apiLevel={}' \
                '&appTag={}&androidId={}&advertising_id={}&userKey={}&versionCode={}&bookId={}' \
                '&s={}&u={}&distinct_id={}&originProduct={}&imei={}&interfaceCode={}' \
                '&appLanguage={}'.format(timezone, userKeyWithoutImei, channel, sign, mcc,
                                         versionName, deviceId, uuid, chapterId, osType, appKey,
                                         apiLevel, appTag, androidId, advertising_id, userKey,
                                         versionCode, bookId, s, u, distinct_id, originProduct, imei,
                                         interfaceCode, appLanguage)
        url_0_0 = host + url_0
        try:
            result_0 = self.s.get(url_0_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_009_library_mohu_search_bookname(self):
        print("----在书架页面，根据书名模糊搜索一本书且能正常阅读的功能----")
        sign = '1dff0472e9ebd88f7104c1d591060e9b'
        keywords = 'change+it'
        url = '/api/search?keywords={}&source={}&start={}&kwType={}&count={}&appKey={}&u={}&s={}' \
              '&userKey={}&userKeyWithoutImei={}&imei={}&interfaceCode={}&mcc={}&channel={}' \
              '&versionCode={}&versionName={}&osType={}&distinct_id={}&advertising_id={}' \
              '&timezone={}&deviceId={}&uuid={}&androidId={}&apiLevel={}&appLanguage={}&appTag={}' \
              '&originProduct={}&sign={}'.format(keywords, source, start, kwType, count, appKey, u, s,
                                                 userKey, userKeyWithoutImei, imei, interfaceCode,
                                                 mcc, channel, versionCode, versionName, osType,
                                                 distinct_id, advertising_id, timezone, deviceId,
                                                 uuid, androidId, apiLevel, appLanguage, appTag,
                                                 originProduct, sign)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_010_library_mohu_search_writername(self):
        print("----在书架页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能----")
        keywords = 'junieloo'
        sign = '3e2de35cc631eb79511e66843ff7d527'
        url = '/api/search?keywords={}&source={}&start={}&kwType={}&count={}&appKey={}&u={}&s={}' \
              '&userKey={}&userKeyWithoutImei={}&imei={}&interfaceCode={}&mcc={}&channel={}' \
              '&versionCode={}&versionName={}&osType={}&distinct_id={}&advertising_id={}' \
              '&timezone={}&deviceId={}&uuid={}&androidId={}&apiLevel={}&appLanguage={}&appTag={}' \
              '&originProduct={}&sign={}'.format(keywords, source, start, kwType, count, appKey, u, s,
                                                 userKey, userKeyWithoutImei, imei, interfaceCode,
                                                 mcc, channel, versionCode, versionName, osType,
                                                 distinct_id, advertising_id, timezone, deviceId,
                                                 uuid, androidId, apiLevel, appLanguage, appTag,
                                                 originProduct, sign)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_011_library_get_book_detail(self):
        print("----获取书籍详细信息----")
        id = 'vbJogk9HjI387%2BmGfULrQQ%3D%3D'
        sign = 'cf2c39c61b9802c5d7e9036e03619fcf'
        url = '/api/bookInfo?id={}&appKey={}&u={}&s={}&userKey={}&userKeyWithoutImei={}&imei={}' \
              '&interfaceCode={}&mcc={}&channel={}&versionCode={}&versionName={}&osType={}' \
              '&distinct_id={}&advertising_id={}&timezone={}&deviceId={}&uuid={}&androidId={}' \
              '&apiLevel={}&appLanguage={}&appTag={}&originProduct={}' \
              '&sign={}'.format(id, appKey, u, s, userKey, userKeyWithoutImei, imei, interfaceCode, mcc,
                                channel, versionCode, versionName, osType, distinct_id, advertising_id,
                                timezone, deviceId, uuid, androidId, apiLevel, appLanguage, appTag,
                                originProduct, sign)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_012_bookshelf_site_message(self):
        print("----在书架页面，点击右上角的“会话”按钮，测试其能正常进入到站内信界面的功能----")
        sign = 'dea2959e5f7748262ee5bfc6b0575bee'
        url = '/Message/getNewMessage?type={}&page={}&size={}&appKey={}&u={}&s={}&userKey={}' \
              '&userKeyWithoutImei={}&imei={}&interfaceCode={}&mcc={}&channel={}&versionCode={}' \
              '&versionName={}&osType={}&distinct_id={}&advertising_id={}&timezone={}&deviceId={}' \
              '&uuid={}&androidId={}&apiLevel={}&appLanguage={}&appTag={}&originProduct={}' \
              '&sign={}'.format(type, page, size, appKey, u, s, userKey, userKeyWithoutImei, imei,
                                interfaceCode, mcc, channel, versionCode, versionName, osType,
                                distinct_id, advertising_id, timezone, deviceId, uuid, androidId,
                                apiLevel, appLanguage, appTag, originProduct, sign)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_013_bookshelf_batchUnfollow_one_book(self):
        print("----在书架页面，测试取消一本收藏书籍的功能运行正确----")
        bid = '%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D'
        sign = 'b7a0e8d3f5ba9dbbb0c1326394dc280f'
        url = '/apiBookshelf/batchUnfollow?timezone={}&userKeyWithoutImei={}&channel={}' \
              '&advertising_id={}&sign={}&mcc={}&versionName={}&deviceId={}&uuid={}&userKey={}' \
              '&versionCode={}&s={}&u={}&distinct_id={}&originProduct={}&osType={}&imei={}' \
              '&appKey={}&bid={}&interfaceCode={}&apiLevel={}&appTag={}&androidId={}' \
              '&appLanguage={}'.format(timezone, userKeyWithoutImei, channel, advertising_id, sign,
                                       mcc, versionName, deviceId, uuid, userKey, versionCode, s, u,
                                       distinct_id, originProduct, osType, imei, appKey, bid,
                                       interfaceCode, apiLevel, appTag, androidId, appLanguage)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_014_bookshelf_batchUnfollow_all_book(self):
        print("----在书架页面，测试批量取消多本收藏书籍的功能运行正确----")
        bid = '5sWGWgn3N3%2BRmsriaWVXjg%3D%3D%2CjgTrpkm6Vt3gp7f%2BHJvJsQ%3D%3D'
        sign = '1a302affb013540cf693c8b065ac232b'
        url = '/apiBookshelf/batchUnfollow?timezone={}&userKeyWithoutImei={}&channel={}' \
              '&advertising_id={}&sign={}&mcc={}&versionName={}&deviceId={}&uuid={}&userKey={}' \
              '&versionCode={}&s={}&u={}&distinct_id={}&originProduct={}&osType={}&imei={}' \
              '&appKey={}&bid={}&interfaceCode={}&apiLevel={}&appTag={}&androidId={}' \
              '&appLanguage={}'.format(timezone, userKeyWithoutImei, channel, advertising_id, sign,
                                       mcc, versionName, deviceId, uuid, userKey, versionCode, s, u,
                                       distinct_id, originProduct, osType, imei, appKey, bid,
                                       interfaceCode, apiLevel, appTag, androidId, appLanguage)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_015_me_feedback(self):
        print("----测试游客用户提交反馈意见的功能----")
        os_type = '9'
        content = 'test+the+supreme+'
        contact = '623858143%40qq.com'
        url = '/api/submitFeedback?channel={}&u={}&s={}&device_type={}&os_type={}&net_type={}' \
              '&app_ver={}&content={}&contact={}&originProduct={}' \
            .format(channel, u, s, device_type, os_type, net_type, app_ver, content, contact, originProduct)
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e


if __name__ == '__main__':
    unittest.main()
