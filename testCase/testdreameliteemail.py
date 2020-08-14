#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import warnings
import unittest
import allure
import pytest
from config.http_req import Http_Req
from config import readConfig

read_conf = readConfig.ReadConfig()


@allure.feature("DreameLite 测试环境  Email登录场景测试")
class TestDreameLiteEmail(unittest.TestCase):

    @allure.story("初始化设置 全局变量")
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.s = requests.session()
        print("----开始执行测试用例  start ----")
        global timezone
        timezone = "Asia%2FShanghai"
        global host_lite
        host_lite = read_conf.get_http_url('host_lite')
        global timestamp
        timestamp = read_conf.get_login_dreame_lite('timestamp')
        global interfaceCode
        interfaceCode = read_conf.get_login_dreame_lite('interfaceCode')
        global debug
        debug = read_conf.get_login_dreame_lite('debug')
        global bookId
        bookId = read_conf.get_login_dreame_lite('bookId') + "%3D%3D"
        global keywords
        keywords = read_conf.get_login_dreame_lite('keywords')
        global user
        user = read_conf.get_login_dreame_lite('user')
        global content
        content = read_conf.get_login_dreame_lite('content')
        global bid_email
        bid_email = read_conf.get_login_dreame_lite('bid_email') + "%3D%3D"
        global id_email
        id_email = read_conf.get_login_dreame_lite('id_email') + "%3D%3D"
        global bookId_email
        bookId_email = read_conf.get_login_dreame_lite('bookId_email') + "%3D%3D"
        global chapterId
        chapterId = read_conf.get_login_dreame_lite('chapterId') + "%3D%3D"
        global password
        password = "Yl9E12hQCct758QkTWIYn7LhvbVxkmXYsMlhHTCFGosaOUawl75H3URHpR%2Bl1S1gol8aG49gNfO%2BPGc%2" \
                   "FX%2FaKPeGG8XbJh4jxKlBK4ioQPAxW3D%2BHmydO%2Fb47nxfKM0VGmpVIuoO0TVHrFh66bblCtLPfA5OwG" \
                   "EnbJyR%2FTmr5Cas%3D"
        url = host_lite + f'/api/login?password={password}&user={user}&debug={debug}'
        result = self.s.get(url)
        res = result.json()
        print("登录返回值 ：", res)
        res_sel = res['dataJson']
        # 过滤 u 跟 s
        global u
        u = res_sel['u']
        global s
        s = res_sel['s']

    @pytest.mark.skip()
    @allure.story(" ----Email登录----")
    def test_000_email_login(self):
        url = f"/api/login?password={password}&user={user}&debug={debug}"
        Http_Req().http_lite_req(url)

    @allure.story("----在书城页面，选择任意一本书籍 ----")
    def test_001_case(self):
        url = f"/api/getChapList?s={s}&u={u}&id={id_email}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)
        """---------------------------------------------------------------"""
        url1 = f"/api/readV1?chapterId={chapterId}&bookId={bookId_email}&s={s}&u={u}" \
               f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url1)

    @allure.story("在书架页面，点击右上角的“礼包”，测试能正常跳转到任务管理界面的功能")
    def test_002_case(self):
        url = f"/api/getUserTask?s={s}&u={u}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_activity_req(url)
        """---------------------------------------------------------------"""
        url1 = f"/api/getAll?u={u}&s={s}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url1)

    @allure.story("在书架页面，点击右上角的“时刻钟”按钮，测试其能正常跳转到解锁书籍界面的功能")
    def test_003_case(self):
        url = f"/calendar/getNewCalendarContent?timezone={timezone}&debug={debug}&u={u}&s={s}" \
              f"&interfaceCode={interfaceCode}"
        Http_Req().http_lite_req(url)
        """---------------------------------------------------------------"""
        url1 = f"/api/novelRecommend?id={id_email}&s={s}&u={u}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url1)
        """---------------------------------------------------------------"""
        url2 = f"/api/readV1?chapterId={chapterId}&bookId={bookId_email}&s={s}&u={u}" \
               f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url2)

    @allure.story("在书架页面，根据书名模糊搜索一本书且能正常阅读的功能")
    def test_004_case(self):
        url = f"/api/search?keywords={keywords}&u={u}&s={s}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)

    @allure.story("在书架页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能")
    def test_005_case(self):
        url = f"/api/search?keywords={keywords}&u={u}&s={s}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)

    @allure.story("在书架页面，点击右上角的“会话”按钮，测试其能正常进入到站内信界面的功能")
    def test_006_case(self):
        url = f"/Message/getSepUnreadMessage?timestamp={timestamp}&u={u}&s={s}" \
              f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)
        """---------------------------------------------------------------"""
        url1 = f"/Message/getNewMessage?u={u}&s={s}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url1)

    @allure.story("在书架页面，测试取消一本收藏书籍的功能")
    def test_007_case(self):
        url = f"/apiBookshelf/batchUnfollow?s={s}&u={u}&bid={bid_email}" \
              f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)

    @allure.story("在书架页面，测试收藏 一本收藏书籍的功能")
    def test_008_case(self):
        url = f"/apiBookshelf/follow?s={s}&u={u}&bid={bid_email}" \
              f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)

    @allure.story("在“我的”界面，测试点击 Earn Rewards 能正常进入任务管理页面的功能")
    def test_009_case(self):
        url1 = f"/api/getAll?u={u}&s={s}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url1)
        """---------------------------------------------------------------"""
        url = f"/api/getUserTask?s={s}&u={u}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_activity_req(url)

    @allure.story("在“我的”界面，测试点击 inbox 能正常进入到短信及站内信界面的功能")
    def test_010_case(self):
        url = f"/Message/getSepUnreadMessage?timestamp={timestamp}&u={u}&s={s}" \
              f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)
        """---------------------------------------------------------------"""
        url1 = f"/Message/getNewMessage?u={u}&s={s}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url1)
        """---------------------------------------------------------------"""
        url2 = f"/Calendar/bookRecommend?s={s}&u={u}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url2)

    @allure.story("在“我的”界面，测试点击 feedback 查看反馈功能")
    def test_011_case(self):
        url = f"/api/submitFeedback?u={u}&s={s}&content={content}&contact={user}&debug={debug}"
        Http_Req().http_lite_req(url)

    @allure.story("在书城页面，选择任意一本书籍，测试能正常阅读的功能")
    def test_012_case(self):
        bookId = "vEUXlA%2FLB6knX1Zb3d923g%3D%3D"
        chapterId = "PSmx%2BjMHCx%2BHtS52AzvScQ%3D%3D"
        url = f"/api/readV1?chapterId={chapterId}&bookId={bookId}&s={s}&u={u}" \
              f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)

    @allure.story("在书城页面，选择任意一本书籍，测试能正常进行收藏操作的功能")
    def test_013_case(self):
        bid = "vEUXlA%2FLB6knX1Zb3d923g%3D%3D"
        url = f"/apiBookshelf/follow?s={s}&u={u}&bid={bid}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)

    @allure.story("在书城界面，选择任意一本已收藏的书籍，测试其能取消收藏的功能")
    def test_014_case(self):
        bid = "vEUXlA%2FLB6knX1Zb3d923g%3D%3D"
        url = f"/apiBookshelf/unfollow?s={s}&u={u}&bid={bid}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)

    @allure.story("在书城侧页面，点击右上角的会话按钮，测试其能正常进入到站内信界面的功能")
    def test_015_case(self):
        url = f"/Message/getSepUnreadMessage?timestamp={timestamp}&u={u}&s={s}" \
              f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)
        """---------------------------------------------------------------"""
        url1 = f"/Message/getNewMessage?u={u}&s={s}&interfaceCode={s}&debug={debug}"
        Http_Req().http_lite_req(url1)

    @allure.story("在书城页面，根据书名模糊搜索一本书且能正常阅读的功能")
    def test_016_case(self):
        url = f"/api/search?keywords={keywords}&u={u}&s={s}&debug={debug}"
        Http_Req().http_lite_req(url)
        chapterId = "pDnjBuMVTYOpKvc%2Bdnd9fg%3D%3D"
        bookId = "w9v9FBDnzU0JWqLN3uqfYQ%3D%3D"
        url1 = f"/api/readV1?chapterId={chapterId}&bookId={bookId}&s={s}&u={u}" \
               f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url1)

    @allure.story("在书城页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能")
    def test_017_case(self):
        url = f"/api/search?keywords={keywords}&u={u}&s={s}&debug={debug}"
        Http_Req().http_lite_req(url)
        """---------------------------------------------------------------"""
        chapterId = "pDnjBuMVTYOpKvc%2Bdnd9fg%3D%3D"
        bookId = "w9v9FBDnzU0JWqLN3uqfYQ%3D%3D"
        url1 = f"/api/readV1?chapterId={chapterId}&bookId={bookId}&s={s}&u={u}" \
               f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url1)

    @allure.story()
    def test_018_case(self):
        url = f"/calendar/getNewCalendarContent?timezone={timezone}&u={u}&s={s}" \
              f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_lite_req(url)
