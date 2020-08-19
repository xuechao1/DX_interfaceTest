#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import allure
import requests
import unittest
import warnings
from config import readConfig
from config.http_req import Http_Req

read_conf = readConfig.ReadConfig()


@allure.feature("测试 Email登录app进行相关操作")
class TestEmailDreame(unittest.TestCase):

    @allure.story("初始化设置 全局变量")
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.s = requests.session()
        global debug
        debug = read_conf.get_login_dreame('debug')
        global host
        host = read_conf.get_http_url('host')
        global host_www
        host_www = read_conf.get_http_url('host_www')
        global host_comment
        host_comment = read_conf.get_http_url('host_comment')
        global versionCode
        versionCode = read_conf.get_login_dreame('versionCode')
        global content
        content = read_conf.get_login_dreame('content')
        global timezone
        timezone1 = read_conf.get_login_dreame('timezone1')
        timezone2 = read_conf.get_login_dreame('timezone2')
        timezone = timezone1 + "%" + timezone2
        global user
        user = read_conf.get_login_dreame('user')
        global page
        page = read_conf.get_login_dreame('page')
        global bid
        bid = read_conf.get_login_dreame('bid')
        global size
        size = read_conf.get_login_dreame('size')
        global timestamp
        timestamp = read_conf.get_login_dreame('timestamp')
        global channel
        channel = read_conf.get_login_dreame('channel')
        global advertising_id
        advertising_id = read_conf.get_login_dreame('advertising_id')
        global keywords
        keywords = read_conf.get_login_dreame('keywords')
        global password
        password1 = read_conf.get_login_dreame('password1') + "%"
        password2 = read_conf.get_login_dreame('password2') + "%"
        password3 = read_conf.get_login_dreame('password3') + "%"
        password4 = read_conf.get_login_dreame('password4') + "%3D"
        password = password1 + password2 + password3 + password4
        global chapterId
        chapterId = read_conf.get_login_dreame('chapterId') + "%3D%3D"
        global id
        id = read_conf.get_login_dreame('id') + "%3D%3D"
        global bookId
        bookId = read_conf.get_login_dreame('bookId') + "%3D%3D"
        global interfaceCode
        interfaceCode = read_conf.get_login_dreame('interfaceCode')
        url = host + f'/api/login?password={password}&user={user}&debug={debug}'
        result = self.s.get(url)
        t = result.json()
        u_1 = t['dataJson']
        # 过滤 u 跟 s
        global u
        u = u_1['u']
        global s
        s = u_1['s']

    @allure.story("----Email 邮箱登录 ----")
    def test_000_case(self):
        """
        ---测试邮件用户能正常登录APP的功能----
        :return:
        """
        url = f'/api/login?password={password}&user={user}&debug={debug}'
        Http_Req().http_email_req(url)

    @allure.story("----在书城页面，选择任意一本书籍 ----")
    def test_001_case(self):
        url_1_1 = f'/Discover/channel?u={u}&s={s}&debug={debug}'
        Http_Req().http_email_req(url_1_1)
        print("-----------------------------------------")
        url_1_2 = f'/api/bookInfo?s={s}&u={u}&id={id}&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url_1_2)

    @allure.story("----在书城页面，阅读一本书----")
    def test_001_1_case(self):
        url = f'/api/readV1?bookId={bookId}&s={s}&u={u}&chapterId={chapterId}' \
              f'&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url)

    @allure.story("----在书城页面，选择任意一本书籍，测试能正常进行收藏操作的功能----")
    def test_002_case(self):
        url = f"/apiBookshelf/follow?s={s}&u={u}&bid={bid}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_email_req(url)

    @allure.story("----在书城页面，选择任意一本书籍，测试能正常进行取消收藏的功能----")
    def test_003_case(self):
        url = f"/apiBookshelf/unfollow?s={s}&u={u}&bid={bid}&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_email_req(url)

    @allure.story("----在阅读书籍时，测试能正常点击分享链接按钮进行分享的功能----")
    def test_004_case(self):
        print("----在阅读书籍时，测试能正常点击分享链接按钮进行分享的功能----")
        url1 = f'/api/commentList?bookId={bookId}&s={s}&u={u}&debug={debug}'
        Http_Req().http_email_comment_req(url1)
        print("-----------------------------------------")
        url = f'/api/doComment?content={content}&bookId={bookId}&s={s}&u={u}' \
              f'&chapterId={chapterId}&debug={debug}'
        Http_Req().http_email_comment_req(url)

    @allure.story("----在书城侧页面，点击右上角的会话按钮，测试其能正常进入到站内信界面的功能----")
    def test_005_case(self):
        url = f'/Message/getSepUnreadMessage?&s={s}&u={u}&timestamp={timestamp}&debug={debug}'
        Http_Req().http_email_req(url)
        print("-----------------------------------------")
        url1 = f'/Message/getNewMessage?s={s}&u={u}&debug={debug}'
        Http_Req().http_email_req(url1)

    @allure.story("----在书城页面，选择任意一本多章节书，测试用户可以自主选择章节内容的功能----")
    def test_006_case(self):
        url = f'/api/readV1?bookId={bookId}&s={s}&u={u}&chapterId={chapterId}' \
              f'&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url)

    @allure.story("----在书城页面，根据书名模糊搜索一本书且能正常阅读的功能----")
    def test_007_case(self):
        url = f'/api/search?keywords={keywords}&s={s}&u={u}&debug={debug}'
        Http_Req().http_email_req(url)

    @allure.story("----在书城页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能----")
    def test_008_case(self):
        url = f'/api/search?keywords={keywords}&s={s}&u={u}&debug={debug}'
        Http_Req().http_email_req(url)
        print("-----------------------------------------")
        url1 = f'/api/bookInfo?s={s}&u={u}&id={id}&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url1)

    @allure.story("在书城页面，点击右上角的“时刻表”，测试其能正常跳转到可解锁书籍查看界面")
    def test_009_case(self):
        url = f'/calendar/getNewCalendarContent?timezone={timezone}' \
              f'&s={s}&u={u}&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url)
        print("-----------------------------------------")
        url1 = f'/Calendar/bookRecommend?&s={s}&u={u}&debug={debug}'
        Http_Req().http_email_req(url1)

    @allure.story("对于存在多章节的书籍在该章节阅读完成时，测试其能正常阅读下一章节的功能")
    def test_010_case(self):
        url = f'/api/readV1?bookId={bookId}&s={s}&u={u}&chapterId={chapterId}' \
              f'&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url)

    @allure.story("----在书架页面，根据书名模糊搜索一本书且能正常阅读的功能----")
    def test_011_case(self):
        url = f'/api/search?keywords={keywords}&s={s}&u={u}&debug={debug}'
        Http_Req().http_email_req(url)
        print("-----------------------------------------")
        url1 = f'/api/bookInfo?s={s}&u={u}&id={id}&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url1)
        print("-----------------------------------------")
        url2 = f'/api/readV1?bookId={bookId}&s={s}&u={u}&chapterId={chapterId}' \
               f'&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url2)

    @allure.story("----在书架页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能----")
    def test_012_case(self):
        url = f'/api/search?keywords={keywords}&s={s}&u={u}' \
              f'&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url)
        print("-----------------------------------------")
        url1 = f'/api/bookInfo?s={s}&u={u}&id={id}&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url1)
        print("-----------------------------------------")
        url2 = f'/api/readV1?bookId={bookId}&s={s}&u={u}&chapterId={chapterId}' \
               f'&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url2)

    @allure.story("----在书架页面，测试直接点击收藏的书会进入到阅读界面的功能----")
    def test_013_case(self):
        url = f'/api/readV1?bookId={bookId}&s={s}&u={u}&chapterId={chapterId}' \
              f'&interfaceCode={interfaceCode}&debug={debug}'
        Http_Req().http_email_req(url)

    @allure.story("----在书架页面，点击右上角的“礼包”，测试能正常跳转到任务管理界面的功能----")
    def test_014_case(self):
        url = f'/api/getUserTask?u={u}&s={s}&debug={debug}'
        Http_Req().http_req_www(url)
        print("-----------------------------------------")
        time.sleep(1)
        url1 = f'/api/getTodayTaskInfo?u={u}&s={s}&debug={debug}'
        Http_Req().http_req_www(url1)

    @allure.story("----在书架页面，点击右上角的“时刻表”，测试其能正常跳转到可解锁书籍查看界面的功能----")
    def test_015_case(self):
        url = f'/calendar/getNewCalendarContent?timezone={timezone}&s={s}&u={u}&debug={debug}'
        Http_Req().http_email_req(url)

    @allure.story("----在书架页面，点击右上角的“会话”按钮，测试其能正常进入到站内信界面的功能----")
    def test_016_case(self):
        url = f'/Message/getNewMessage?s={s}&u={u}&debug={debug}'
        Http_Req().http_email_req(url)
        print("-----------------------------------------")
        url1 = f'/Message/getSepUnreadMessage?s={s}&u={u}&timestamp={timestamp}&debug={debug}'
        Http_Req().http_email_req(url1)

    @allure.story("----在书架页面，测试取消一本收藏书籍的功能运行正确----")
    def test_017_case(self):
        url = f"/apiBookshelf/unfollow?s={s}&u={u}&bid={bid}" \
              f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_email_req(url)

    @allure.story("----在书架页面，测试批量取消多本收藏书籍的功能运行正确----")
    def test_018_case(self):
        url = f"/apiBookshelf/batchUnfollow?s={s}&u={u}&bid={bid}" \
              f"&interfaceCode={interfaceCode}&debug={debug}"
        Http_Req().http_email_req(url)

    @allure.story("----在“我的”界面，测试点击 Earn Rewards 能正常进入任务管理页面的功能----")
    def test_019_case(self):
        url = f'/api/getUserTask?u={u}&s={s}&debug={debug}'
        Http_Req().http_req_www(url)
        print("-----------------------------------------")
        url1 = f'/api/getTodayTaskInfo?u={u}&s={s}&debug={debug}'
        Http_Req().http_req_www(url1)

    @allure.story("----在“我的”界面，测试点击 inbox 能正常进入到短信及站内信界面的功能----")
    def test_020_case(self):
        url = f'/Message/getSepUnreadMessage?s={s}&u={u}&timestamp={timestamp}&debug={debug}'
        Http_Req().http_email_req(url)
        print("-----------------------------------------")
        url1 = f'/Message/getNewMessage?s={s}&size={size}&u={u}&debug={debug}'
        Http_Req().http_email_req(url1)

    @allure.story("----在“我的”界面，测试点击”Following能正常查看浏览书籍记录的功能----")
    def test_021_case(self):
        url = f'/User/getMyFollow?&s={s}&u={u}&debug={debug}'
        Http_Req().http_email_req(url)


if __name__ == '__main__':
    unittest.main()
