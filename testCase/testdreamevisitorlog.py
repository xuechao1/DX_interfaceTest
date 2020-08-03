# -*- coding:utf-8 -*-

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
sys.path.append("D:\\PycharmProjects\\DX_interfaceTest")
host = 'http://3.85.16.233:32100'
host_www = 'http://activity.dreame.com/'


@allure.feature("Dreame 测试环境  游客登录场景测试")
class TestDreameVisitorLogin(unittest.TestCase):

    @allure.story("初始化设置 全局变量")
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.s = requests.session()
        print("----开始执行测试用例  start ----")
        global bookshelf
        bookshelf = "qvKshA91NtuSl6pT32r2zQ%3D%3D%2CafpUCUXTG5LOtYLQgyOFdw%3D%3D%2CtKIiqGQH9ujzsIerqicrkg%3D%3D"
        global bookshelf1
        bookshelf1 = "afpUCUXTG5LOtYLQgyOFdw%3D%3D%2CtKIiqGQH9ujzsIerqicrkg%3D%3D%2CtchOexxodN%2FybrimwnB5gw%3D%3D"
        global channel
        channel = read_conf.get_login_dreame('channel')
        global sign
        sign = read_conf.get_login_dreame('sign')
        global mcc
        mcc = read_conf.get_login_dreame('mcc')
        global number
        number = read_conf.get_login_dreame('number')
        global bid
        bid = read_conf.get_login_dreame('bid') + "%3D%3D"
        global bid_batch_unfollow
        bid_batch_unfollow = read_conf.get_login_dreame('bid_batch_unfollow') + "%3D%3D"
        global bid_unfollow
        bid_unfollow = read_conf.get_login_dreame('bid_unfollow') + "%3D%3D"
        global versionName
        versionName = read_conf.get_login_dreame('versionName')
        global deviceId
        deviceId = read_conf.get_login_dreame('deviceId')
        global versionCode
        versionCode = read_conf.get_login_dreame('versionCode')
        global osType
        osType = read_conf.get_login_dreame('osType')
        global referrer
        referrer = read_conf.get_login_dreame('referrer')
        global appKey
        appKey = read_conf.get_login_dreame('appKey')
        global interfaceCode
        interfaceCode = read_conf.get_login_dreame('interfaceCode')
        global apiLevel
        apiLevel = read_conf.get_login_dreame('apiLevel')
        global androidId
        androidId = read_conf.get_login_dreame('androidId')
        global distinct_id
        distinct_id = read_conf.get_login_dreame('distinct_id')
        global timezone
        timezone = "Asia%2FShanghai"
        global login_type
        login_type = read_conf.get_login_dreame('login_type')
        global advertising_id
        advertising_id = read_conf.get_login_dreame('advertising_id')
        global oid
        oid = read_conf.get_login_dreame('oid')
        global keywords
        keywords = read_conf.get_login_dreame('keywords')
        global page
        page = read_conf.get_login_dreame('page')
        global size
        size = read_conf.get_login_dreame('size')
        global type
        type = read_conf.get_login_dreame('type')
        global count
        count = read_conf.get_login_dreame('count')
        global start
        start = read_conf.get_login_dreame('start')
        global s
        s = read_conf.get_login_dreame('s') + "%3D%3D"
        global u
        u = read_conf.get_login_dreame('u') + "%3D%3D"
        global s1
        s1 = read_conf.get_login_dreame('s1') + "%3D%3D"
        global u1
        u1 = read_conf.get_login_dreame('u1') + "%3D%3D"
        global id
        id = read_conf.get_login_dreame('id') + "%3D%3D"
        global uuid
        uuid = read_conf.get_login_dreame('uuid')
        global source
        source = read_conf.get_login_dreame('source')
        global appLanguage
        appLanguage = read_conf.get_login_dreame('appLanguage')
        global code
        code = read_conf.get_login_dreame('code')
        global sex
        sex = read_conf.get_login_dreame('sex')
        global kwType
        kwType = read_conf.get_login_dreame('kwType')
        global bookId
        bookId = read_conf.get_login_dreame('bookId') + "%3D%3D"
        global chapterId
        chapterId = "%2FyfyxhU3d%2B9CW4a8jlzK4Q%3D%3D"
        global timestamp
        timestamp = read_conf.get_login_dreame('timestamp')

    @allure.story("测试游客用户能正常登录APP的功能")
    def test_001_visitor_login(self):
        """
        ---测试游客用户能正常登录APP的功能----
        :return:
        """
        url = f"/api/visitorLogin?code={code}&login_type={login_type}&timezone={timezone}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&oid={oid}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&distinct_id={distinct_id}" \
              f"&osType={osType}&appKey={appKey}&interfaceCode={interfaceCode}&apiLevel={apiLevel}" \
              f"&androidId={androidId}"
        Http_Req().http_req(url)

    @allure.story("在书城页面，选择任意一本书籍，测试能正常阅读")
    def test_002_discover_read(self):
        """
        在书城页面，选择任意一本书籍，测试能正常阅读的功
        :return:
        """
        sign = 'fe952927888c1e3dd526186f564a7476'
        url = f"/api/bookInfo?bookshelf={bookshelf}&timezone={timezone}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&$referrer={referrer}&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s}" \
              f"&u={u}&distinct_id={distinct_id}&osType={osType}&appKey={appKey}&id={id}" \
              f"&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url)
        """
        阅读一本书
        """
        sign1 = "b14126ea25f880b62e2e2d1d10411262"
        url1 = f"/api/readV1?timezone={timezone}&sex={sex}&channel={channel}&" \
               f"advertising_id={advertising_id}&sign={sign1}&mcc={mcc}&versionName={versionName}" \
               f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&bookId={bookId}&s={s}&u={u}" \
               f"&chapterId={chapterId}&distinct_id={distinct_id}&osType={osType}&appKey={appKey}" \
               f"&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url1)

    @allure.story("在书城页面，选择任意一本书籍，测试能正常进行收藏操作")
    def test_004_book_follow(self):
        """
        书籍收藏
        :return:
        """
        sign = "bc6d0c30c31e8b91f67b8eb277c1522c"
        url = f"/apiBookshelf/follow?timezone={timezone}&sex={sex}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s}&u={u}" \
              f"&distinct_id={distinct_id}&osType={osType}&appKey={appKey}&bid={bid}" \
              f"&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url)

    @allure.story("在书城界面，选择任意一本已收藏的书籍，测试其能取消收藏的功能")
    def test_005_book_un_follow(self):
        """
        取消书籍收藏
        :return:
        """
        sign = "bc6d0c30c31e8b91f67b8eb277c1522c"
        url = f"/apiBookshelf/unfollow?timezone={timezone}&sex={sex}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s}&u={u}" \
              f"&distinct_id={distinct_id}&osType={osType}&appKey={appKey}&bid={bid}" \
              f"&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url)

    @allure.story("在书城侧页面，点击右上角的会话按钮，测试其能正常进入到站内信界面的功能")
    def test_006_inbox(self):
        """
        站内信
        :return:
        """
        sign = "4e920059bb22e6c57e636978bd242f79"
        url = f"/Message/getSepUnreadMessage?timezone={timezone}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s}&u={u}&" \
              f"distinct_id={distinct_id}&osType={osType}&appKey={appKey}&interfaceCode={interfaceCode}" \
              f"&apiLevel={apiLevel}&androidId={androidId}&timestamp={timestamp}"
        Http_Req().http_req(url)
        sign1 = "9b34672cdd116c7a7686be45e89e87e1"
        url1 = f"/Message/getNewMessage?timezone={timezone}&channel={channel}" \
               f"&advertising_id={advertising_id}&sign={sign1}&type={type}&mcc={mcc}" \
               f"&versionName={versionName}&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}" \
               f"&s={s}&size={size}&u={u}&distinct_id={distinct_id}&osType={osType}&appKey={appKey}" \
               f"&page={page}&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url1)

    @allure.story("在书城页面，选择任意一本多章节书，测试用户可以自主选择章节内容的功能")
    def test_007_sel_page(self):
        """
        选择一个章节阅读
        :return:
        """
        sign1 = "b14126ea25f880b62e2e2d1d10411262"
        url1 = f"/api/readV1?timezone={timezone}&sex={sex}&channel={channel}&" \
               f"advertising_id={advertising_id}&sign={sign1}&mcc={mcc}&versionName={versionName}" \
               f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&bookId={bookId}&s={s}&u={u}" \
               f"&chapterId={chapterId}&distinct_id={distinct_id}&osType={osType}&appKey={appKey}" \
               f"&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url1)

    @allure.story("在书城页面，点击右上角的“时刻表”")
    def test_008_time_list(self):
        """
        在书城页面，点击右上角的“时刻表”
        :return:
        """
        sign = "3fdaac918e980387acd80f9d48aeaf0c"
        url = f"/calendar/getNewCalendarContent?timezone={timezone}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s1}&u={u1}" \
              f"&distinct_id={distinct_id}&osType={osType}&appKey={appKey}&interfaceCode={interfaceCode}" \
              f"&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url)

    @allure.story("在书城页面，根据书名模糊搜索一本书/根据作者名模糊搜索一本书--同一个接口")
    def test_009_cook_name_search(self):
        """
        在书城页面，根据书名模糊搜索一本书
        :return:
        """
        sign = "a2603875921db937cbbb982dc988ab3f"
        url = f"/api/search?keywords={keywords}&timezone={timezone}&channel={channel}&sign={sign}" \
              f"&source={source}&mcc={mcc}&versionName={versionName}&kwType={kwType}&deviceId={deviceId}" \
              f"&uuid={uuid}&osType={osType}&appKey={appKey}&apiLevel={apiLevel}&androidId={androidId}" \
              f"&sex={sex}&count={count}&start={start}&advertising_id={advertising_id}" \
              f"&versionCode={versionCode}&s={s1}&u={u1}&distinct_id={distinct_id}" \
              f"&interfaceCode={interfaceCode}"
        Http_Req().http_req(url)

    @allure.story("阅读一本在 书架上收藏的书")
    def test_010_bookshelf_read(self):
        """
        阅读一本在 书架上收藏的书
        """
        sign = "b14126ea25f880b62e2e2d1d10411262"
        url = f"/api/readV1?timezone={timezone}&sex={sex}&channel={channel}&" \
              f"advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&bookId={bookId}&s={s}&u={u}" \
              f"&chapterId={chapterId}&distinct_id={distinct_id}&osType={osType}&appKey={appKey}" \
              f"&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url)

    @allure.story("在书架页面，根据书名模糊搜索一本书")
    def test_011_bookshelf_name_search(self):
        """
        在书架页面，根据书名模糊搜索一本书
        :return:
        """
        sign = "a2603875921db937cbbb982dc988ab3f"
        url = f"/api/search?keywords={keywords}&timezone={timezone}&channel={channel}&sign={sign}" \
              f"&source={source}&mcc={mcc}&versionName={versionName}&kwType={kwType}&deviceId={deviceId}" \
              f"&uuid={uuid}&osType={osType}&appKey={appKey}&apiLevel={apiLevel}&androidId={androidId}" \
              f"&sex={sex}&count={count}&start={start}&advertising_id={advertising_id}" \
              f"&versionCode={versionCode}&s={s1}&u={u1}&distinct_id={distinct_id}" \
              f"&interfaceCode={interfaceCode}"
        Http_Req().http_req(url)

    @allure.story("在书架页面，点击右上角的“会话”按钮，测试其能正常进入到站内信")
    def test_012_bookshelf_inbox(self):
        """
        在书架页面，点击右上角的“会话”按钮，测试其能正常进入到站内信
        :return:
        """
        sign = "326e4236264baa2ab5f8ddea5d1b50e8"
        url = f"/Message/getSepUnreadMessage?timezone={timezone}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s1}&u={u1}" \
              f"&distinct_id={distinct_id}&osType={osType}&appKey={appKey}&interfaceCode={interfaceCode}" \
              f"&apiLevel={apiLevel}&androidId={androidId}&timestamp={timestamp}"
        Http_Req().http_req(url)

    @allure.story("在书架页面，测试取消一本收藏的书籍---接口不稳，一会行，一会不行")
    def test_014_bookshelf_un_follow(self):
        """
        在书架页面，测试取消一本收藏的书籍
        :return:
        """
        sign = "3d6a4cdf7cb6a90b18d44717371a4d2d"
        url = f"/apiBookshelf/unfollow?timezone={timezone}&sex={sex}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s1}&u={u1}" \
              f"&distinct_id={distinct_id}&osType={osType}&appKey={appKey}&bid={bid_unfollow}" \
              f"&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url)

    @allure.story("在书架页面，测试收藏一本书籍")
    def test_013_bookshelf_follow(self):
        """
        在书架页面，测试收藏一本书籍
        :return:
        """
        sign = "3d6a4cdf7cb6a90b18d44717371a4d2d"
        url = f"/apiBookshelf/follow?timezone={timezone}&sex={sex}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s1}&u={u1}" \
              f"&distinct_id={distinct_id}&osType={osType}&appKey={appKey}&bid={bid_unfollow}" \
              f"&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url)

    @allure.story("在书架页面，测试批量取消多本收藏书籍")
    def test_015_batch_un_follow(self):
        """
        在书架页面，测试批量取消多本收藏书籍
        :return:
        """
        sign = "8084ab616a14044c1a460a1844a33333"
        url = f"/apiBookshelf/batchUnfollow?timezone={timezone}&sex={sex}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&s={s1}&u={u1}" \
              f"&distinct_id={distinct_id}&osType={osType}&appKey={appKey}&bid={bid_batch_unfollow}" \
              f"&interfaceCode={interfaceCode}&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url)

    @allure.story("在“我的”界面，测试点击“inbox”能正常进入到短信及站内信界面的功能")
    def test_016_my_inbox(self):
        """
        在“我的”界面，测试点击“inbox”能正常进入到短信及站内信界面的功能
        :return:
        """
        sign = "f8a532ab9648e59582041d38eeb40d58"
        url = f"/Calendar/bookRecommend?bookshelf={bookshelf1}&timezone={timezone}&channel={channel}" \
              f"&advertising_id={advertising_id}&sign={sign}&mcc={mcc}&versionName={versionName}" \
              f"&deviceId={deviceId}&uuid={uuid}&versionCode={versionCode}&number={number}&s={s1}&u={u1}" \
              f"&distinct_id={distinct_id}&osType={osType}&appKey={appKey}&interfaceCode={interfaceCode}" \
              f"&apiLevel={apiLevel}&androidId={androidId}"
        Http_Req().http_req(url)


if __name__ == '__main__':
    unittest.main()
