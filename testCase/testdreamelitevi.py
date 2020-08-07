#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import sys
import requests
import warnings
import unittest
import allure
import pytest
from pprint import pprint
from config.http_req import Http_Req
from config import readConfig

read_conf = readConfig.ReadConfig()


@allure.feature("DreameLite 测试环境  游客登录场景测试")
class TestDreameLiteVi(unittest.TestCase):

    @allure.story("初始化设置 全局变量")
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.s = requests.session()
        print("----开始执行测试用例  start ----")
        global channel
        channel = read_conf.get_login_dreame_lite('channel')
        global sign
        sign = read_conf.get_login_dreame_lite('sign')
        global mcc
        mcc = read_conf.get_login_dreame_lite('mcc')
        global versionName
        versionName = read_conf.get_login_dreame_lite('versionName')
        global deviceId
        deviceId = read_conf.get_login_dreame_lite('deviceId')
        global versionCode
        versionCode = read_conf.get_login_dreame_lite('versionCode')
        global osType
        osType = read_conf.get_login_dreame_lite('osType')
        global appKey
        appKey = read_conf.get_login_dreame_lite('appKey')
        global interfaceCode
        interfaceCode = read_conf.get_login_dreame_lite('interfaceCode')
        global apiLevel
        apiLevel = read_conf.get_login_dreame_lite('apiLevel')
        global androidId
        androidId = read_conf.get_login_dreame_lite('androidId')
        global distinct_id
        distinct_id = read_conf.get_login_dreame_lite('distinct_id')
        global timezone
        timezone1 = read_conf.get_login_dreame_lite('timezone1')
        timezone2 = read_conf.get_login_dreame_lite('timezone2')
        timezone = timezone1 + "%" + timezone2
        global login_type
        login_type = read_conf.get_login_dreame_lite('login_type')
        global debug
        debug = read_conf.get_login_dreame_lite('debug')
        global advertising_id
        advertising_id = read_conf.get_login_dreame_lite('advertising_id')
        global oid
        oid = read_conf.get_login_dreame_lite('oid')
        global uuid
        uuid = read_conf.get_login_dreame_lite('uuid')
        global appLanguage
        appLanguage = read_conf.get_login_dreame_lite('appLanguage')
        global code
        code = read_conf.get_login_dreame_lite('code')
        global imei
        imei = read_conf.get_login_dreame_lite('imei')
        global originProduct
        originProduct = read_conf.get_login_dreame_lite('originProduct')
        global appTag
        appTag = read_conf.get_login_dreame_lite('appTag')
        global id
        id = read_conf.get_login_dreame_lite('id') + "%3D%3D"
        global u
        u = read_conf.get_login_dreame_lite('u')
        global s
        s = read_conf.get_login_dreame_lite('s') + "%3D%3D"
        global chapterId
        chapterId = "YnSos%2FKO5x%2FlNb5h7Z0xOA%3D%3D"
        global bookId
        bookId = read_conf.get_login_dreame_lite('bookId') + "%3D%3D"
        global bid
        bid = read_conf.get_login_dreame_lite('bid') + "%3D%3D"
        global timestamp
        timestamp = read_conf.get_login_dreame_lite('timestamp')
        global type
        type = read_conf.get_login_dreame_lite('type')
        global page
        page = read_conf.get_login_dreame_lite('page')
        global size
        size = read_conf.get_login_dreame_lite('size')
        global keywords
        keywords = read_conf.get_login_dreame_lite('keywords')
        global source
        source = read_conf.get_login_dreame_lite('source')
        global start
        start = read_conf.get_login_dreame_lite('start')
        global kwType
        kwType = read_conf.get_login_dreame_lite('kwType')
        global count
        count = read_conf.get_login_dreame_lite('count')
        global number
        number = read_conf.get_login_dreame_lite('number')
        global bookshelf
        bookshelf = "kcksI4Tiid%2Fxsi88Qok99Q%3D%3D%2CD7qGJ2uk2cfDCQRkErWbww%3D%3D%2CF6uVYSO8WVVC" \
                    "T4%2B9TjLU2A%3D%3D%2CaZvsTa%2FeqhKF5m3JlGh%2FdA%3D%3D%2Cw9v9FBDnzU0JWqLN3uq" \
                    "fYQ%3D%3D%2CfjmJIgjzgRqJrgM206kSqw%3D%3D%2CtNQXQc54vu8MQofqy%2BZy%2Fw%3D%3D%2C" \
                    "IFF5DIMCqUEengfzimH1sQ%3D%3D%2Cu262i4rKMA0iW%2BMHgzBBVA%3D%3D%2CR2LIHLUt1Vuh" \
                    "vM%2BTpVOTqw%3D%3D%2CVFobxyr1WNzaF43uM1I80A%3D%3D%2CMtdHemLBOTrZBf0azOiEX" \
                    "Q%3D%3D%2CkAM%2Be5GVCR1mIVamWo4nbA%3D%3D"

    @allure.story(" ----游客登录----")
    def test_000_visitor_login(self):
        url = f"/api/visitorLogin?code={code}&login_type={login_type}&timezone={timezone}" \
              f"&channel={channel}&sign={sign}&oid={oid}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&osType={osType}&appKey={appKey}&apiLevel={apiLevel}" \
              f"&appTag={appTag}&androidId={androidId}&advertising_id={advertising_id}" \
              f"&versionCode={versionCode}&distinct_id={distinct_id}&originProduct={originProduct}" \
              f"&imei={imei}&interfaceCode={interfaceCode}&appLanguage={appLanguage}"
        Http_Req().http_lite_req(url)

    @allure.story("在书城页面，选择任意一本书籍，测试能正常阅读的功能")
    def test_001_discover_book_read(self):
        sign = 'ed6e87bdc8da69ec1fb56f9ce1995ebc'
        url = f"/api/bookInfo?id={id}&appKey={appKey}&u={u}&s={s}&imei={imei}" \
              f"&interfaceCode={interfaceCode}&mcc={mcc}&channel={channel}&versionCode={versionCode}" \
              f"&versionName={versionName}&osType={osType}&distinct_id={distinct_id}" \
              f"&advertising_id={advertising_id}&timezone={timezone}&deviceId={deviceId}&uuid={uuid}" \
              f"&androidId={androidId}&apiLevel={apiLevel}&appLanguage={appLanguage}&appTag={appTag}" \
              f"&originProduct={originProduct}&sign={sign}"
        Http_Req().http_lite_req(url)
        sign1 = "949349cb0dd7d5ac4a22abdecc568905"
        url1 = f"/api/readV1?timezone={timezone}&channel={channel}&sign={sign1}&mcc={mcc}" \
               f"&versionName={versionName}&deviceId={deviceId}&uuid={uuid}&chapterId={chapterId}" \
               f"&osType={osType}&appKey={appKey}&apiLevel={apiLevel}&appTag={appTag}" \
               f"&androidId={androidId}&advertising_id={advertising_id}&versionCode={versionCode}" \
               f"&bookId={bookId}&s={s}&u={u}&distinct_id={distinct_id}&originProduct={originProduct}" \
               f"&imei={imei}&interfaceCode={interfaceCode}&appLanguage={appLanguage}"
        Http_Req().http_lite_req(url1)

    @allure.story("在书城页面，选择任意一本书籍，测试能正常进行收藏操作的功能")
    def test_002(self):
        sign = "503396a8a4563bb5b40dffff65dfc8d1"
        url = f"/apiBookshelf/follow?timezone={timezone}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s}&u={u}" \
              f"&distinct_id={distinct_id}&originProduct={originProduct}&osType={osType}&imei={imei}" \
              f"&appKey={appKey}&bid={bid}&interfaceCode={interfaceCode}&apiLevel={apiLevel}" \
              f"&appTag={appTag}&androidId={androidId}&appLanguage={appLanguage}"
        Http_Req().http_lite_req(url)

    @allure.story("在书城界面，选择任意一本已收藏的书籍，测试其能取消收藏的功能")
    def test_003(self):
        sign = "503396a8a4563bb5b40dffff65dfc8d1"
        url = f"/apiBookshelf/unfollow?timezone={timezone}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s}&u={u}" \
              f"&distinct_id={distinct_id}&originProduct={originProduct}&osType={osType}&imei={imei}" \
              f"&appKey={appKey}&bid={bid}&interfaceCode={interfaceCode}&apiLevel={apiLevel}" \
              f"&appTag={appTag}&androidId={androidId}&appLanguage={appLanguage}"
        Http_Req().http_lite_req(url)

    @allure.story("在书城侧页面，点击右上角的会话按钮，测试其能正常进入到站内信界面的功能")
    def test_004(self):
        sign = "b9aae16551b8bd242f93645105c306a9"
        url = f"/Message/getSepUnreadMessage?timestamp={timestamp}&appKey={appKey}&u={u}&s={s}" \
              f"&imei={imei}&interfaceCode={interfaceCode}&mcc={mcc}&channel={channel}" \
              f"&versionCode={versionCode}&versionName={versionName}&osType={osType}" \
              f"&distinct_id={distinct_id}&advertising_id={advertising_id}&timezone={timezone}" \
              f"&deviceId={deviceId}&uuid={uuid}&androidId={androidId}&apiLevel={apiLevel}" \
              f"&appLanguage={appLanguage}&appTag={appTag}&originProduct={originProduct}&sign={sign}"
        Http_Req().http_lite_req(url)
        sign1 = "015746a842ede844f45f72eae00adceb"
        url1 = f"/Message/getNewMessage?type={type}&page={page}&size={size}&appKey={appKey}&u={u}" \
               f"&s={s}&imei={imei}&interfaceCode={interfaceCode}&mcc={mcc}&channel={channel}" \
               f"&versionCode={versionCode}&versionName={versionName}&osType={osType}" \
               f"&distinct_id={distinct_id}&advertising_id={advertising_id}&timezone={timezone}" \
               f"&deviceId={deviceId}&uuid={uuid}&androidId={androidId}&apiLevel={apiLevel}" \
               f"&appLanguage={appLanguage}&appTag={appTag}&originProduct={originProduct}&sign={sign1}"
        Http_Req().http_lite_req(url1)

    @allure.story("在书城页面，选择任意一本多章节书，测试用户可以自主选择章节内容的功能")
    def test_005(self):
        sign = "9832835e7dd5618810f431ec4d47c6b1"
        chapterId = "mdbhq3m%2Fpkk3Gp79NOj5Jw%3D%3D"
        bookId = "D7qGJ2uk2cfDCQRkErWbww%3D%3D"
        url = f"/api/readV1?timezone={timezone}&channel={channel}&sign={sign}&mcc={mcc}" \
              f"&versionName={versionName}&deviceId={deviceId}&uuid={uuid}&chapterId={chapterId}" \
              f"&osType={osType}&appKey={appKey}&apiLevel={apiLevel}&appTag={appTag}" \
              f"&androidId={androidId}&advertising_id={advertising_id}&versionCode={versionCode}" \
              f"&bookId={bookId}&s={s}&u={u}&distinct_id={distinct_id}&originProduct={originProduct}" \
              f"&imei={imei}&interfaceCode={interfaceCode}&appLanguage={appLanguage}"
        Http_Req().http_lite_req(url)

    @allure.story("在书城页面，根据书名模糊搜索一本书且能正常阅读的功能完成")
    def test_006(self):
        sign = "dfedd654675f48f08cc2a7269f8b4efb"
        url = f"/api/search?keywords={keywords}&source={source}&start={start}&kwType={kwType}" \
              f"&count={count}&appKey={appKey}&u={u}&s={s}&imei={imei}&interfaceCode={interfaceCode}" \
              f"&mcc={mcc}&channel={channel}&versionCode={versionCode}&versionName={versionName}" \
              f"&osType={osType}&distinct_id={distinct_id}&advertising_id={advertising_id}" \
              f"&timezone={timezone}&deviceId={deviceId}&uuid={uuid}&androidId={androidId}" \
              f"&apiLevel={apiLevel}&appLanguage={appLanguage}&appTag={appTag}" \
              f"&originProduct={originProduct}&sign={sign}"
        Http_Req().http_lite_req(url)
        # ------------------------------间隔符------------------------------
        sign1 = "8a1b96ce3c96229ee0299a3e0ecc2cb2"
        chapterId = "oHWS3s9pl%2BsnThc%2B2A6atg%3D%3D"
        bookId = "w9v9FBDnzU0JWqLN3uqfYQ%3D%3D"
        url1 = f"/api/readV1?timezone={timezone}&channel={channel}&sign={sign1}&mcc={mcc}" \
               f"&versionName={versionName}&deviceId={deviceId}&uuid={uuid}&chapterId={chapterId}" \
               f"&osType={osType}&appKey={appKey}&apiLevel={apiLevel}&appTag={appTag}" \
               f"&androidId={androidId}&advertising_id={advertising_id}&versionCode={versionCode}" \
               f"&bookId={bookId}&s={s}&u={u}&distinct_id={distinct_id}&originProduct={originProduct}" \
               f"&imei={imei}&interfaceCode={interfaceCode}&appLanguage={appLanguage}"
        Http_Req().http_lite_req(url1)

    @allure.story("在书城页面，点击右上角的“时刻表”，测试其能正常跳转到可解锁书籍查看界面的功能")
    def test_007(self):
        sign = "c10a90781a1a80614a5909de9b4b1659"
        url = f"/calendar/getNewCalendarContent?timezone={timezone}&appKey={appKey}&u={u}&s={s}" \
              f"&imei={imei}&interfaceCode={interfaceCode}&mcc={mcc}&channel={channel}" \
              f"&versionCode={versionCode}&versionName={versionName}&osType={osType}" \
              f"&distinct_id={distinct_id}&advertising_id={advertising_id}&deviceId={deviceId}" \
              f"&uuid={uuid}&androidId={androidId}&apiLevel={apiLevel}&appLanguage={appLanguage}" \
              f"&appTag={appTag}&originProduct={originProduct}&sign={sign}"
        Http_Req().http_lite_req(url)
        sign1 = "a73c66c99f57167701bb1eb4b0c71c5d"
        url1 = f"/Calendar/bookRecommend?number={number}&bookshelf={bookshelf}&appKey={appKey}&u={u}" \
               f"&s={s}&imei={imei}&interfaceCode={interfaceCode}&mcc={mcc}&channel={channel}" \
               f"&versionCode={versionCode}&versionName={versionName}&osType={osType}" \
               f"&distinct_id={distinct_id}&advertising_id={advertising_id}&timezone={timezone}" \
               f"&deviceId={deviceId}&uuid={uuid}&androidId={androidId}&apiLevel={apiLevel}" \
               f"&appLanguage={appLanguage}&appTag={appTag}&originProduct={originProduct}&sign={sign1}"
        Http_Req().http_lite_req(url1)

    @allure.story()
    def test_008(self):
        pass

    @allure.story()
    def test_009(self):
        pass

    @allure.story()
    def test_010(self):
        pass

    @allure.story()
    def test_011(self):
        pass

    @allure.story()
    def test_012(self):
        pass

    @allure.story()
    def test_013(self):
        pass

    @allure.story()
    def test_014(self):
        pass

    @allure.story()
    def test_015(self):
        pass

    @allure.story()
    def test_016(self):
        pass
