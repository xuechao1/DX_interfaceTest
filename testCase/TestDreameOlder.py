# -*- coding:utf-8 -*-

import sys
import requests
import warnings
import unittest
import pytest
import allure
from pprint import pprint
from config.http_req import Http_Req
from config import readConfig


read_conf = readConfig.ReadConfig()
sys.path.append("D:\\PycharmProjects\\DX_interfaceTest")
host = 'http://3.85.16.233:32100'
host_www = 'http://activity.dreame.com/'


class TestDreame(unittest.TestCase):

    @allure.description("""忽略执行的警告信息""")
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.s = requests.session()
        print("----开始执行测试用例  start ----")

    @allure.title("测试用例1--测试游客用户能正常登录APP的功能")
    def test_000_0_visitor_login(self):
        """
        ---测试游客用户能正常登录APP的功能----
        :return:
        """
        print("----测试游客用户能正常登录APP的功能----")
        url = "/api/visitorLogin?deviceId=ce22584ad748d9ec&" \
              "appKey=201020412&versionCode=121&uuid=91a601bf-e555-4beb-9518-f6473284f9ef&" \
              "appLanguage=en&interfaceCode=122&code=5b5b0d6cc931bdaac02d3eb5d79440af&" \
              "androidId=ce22584ad748d9ec&originProduct=4&imei=ce22584ad748d9ec&" \
              "distinct_id=ce22584ad748d9ec&appTag=0&mcc=0&channel=ringdomapp-78&" \
              "apiLevel=23&userKey=001f191d1d25daa402a34f04bc93507d&" \
              "advertising_id=ab0dfc48-4340-4953-a908-d06253e992a4&" \
              "sign=3bc0d79ef6498669da353b248c2afd0c&userKeyWithoutImei=9977c1a4fb842edaf66ff4964018130b&" \
              "timezone=Asia%2FShanghai&versionName=1.7.2&oid=001f191d1d25daa402a34f04bc93507d&" \
              "osType=0&login_type=10"
        Http_Req().http_req(url)

    @pytest.mark.skip
    def test_000_1_book_list(self):
        print("----获取书城的书籍列表----")
        url = '/Discover?timezone=Asia%2FShanghai' \
              '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd' \
              '&channel=dreameapp-23&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
              '&sign=718f33fc1a7b110f9d20399ef8f9a767&mcc=460&versionName=1.7.2' \
              '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
              '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
              '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1Iiwid' \
              'iI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk' \
              '2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
              '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsIn' \
              'MiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9' \
              '&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379&appKey=201020412' \
              '&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url)

    @allure.title("测试用例2--在书城页面，选择任意一本书籍，测试能正常阅读的功能")
    def test_001_library_book_reading(self):
        print("----在书城页面，选择任意一本书籍，测试能正常阅读的功能----")
        print("-----------------------------------------")
        url = '/api/bookInfo?bookshelf=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D%2CvhRlO%2Fp2LPt13f' \
              'jpOFoo0Q%3D%3D%2CRvdq9VhPzTLkgyHofVE8Pw%3D%3D%2CR5NDszuwekbhS0c3i3%2B' \
              'cyg%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D%2C6sB5aEzcmvjSF5yvPFDGOQ%3D%3D' \
              '&timezone=Asia%2FShanghai&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd' \
              '&channel=dreameapp-23&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
              '&sign=0fa75a98c43919ee5e2a691fef49a7e6&mcc=460&versionName=1.7.2' \
              '&$referrer=com.dreame.reader.common.MainActivity&deviceId=6fb3537dbc70aad5' \
              '&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf&userKey=5f210fa758cd2db391305b0e' \
              '2749fadc&versionCode=120&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFm' \
              'MDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LC' \
              'JyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
              '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsIn' \
              'MiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6Zm' \
              'Fsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
              '&appKey=201020412&id=IBHlOVzembrdDbPW%2BlY4ow%3D%3D&interfaceCode=122' \
              '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url)
        print("----阅读一本书----")
        url_1 = '/api/getChapList?timezone=Asia%2FShanghai&userKeyWithoutImei=e694c359a7' \
                '08d6ceda7ae2dd9fe6cacd&channel=dreameapp-23&advertising_id=7a6c42db-28' \
                '52-4db4-9206-47184fa7b8dd&sign=fac1d9f71603713065377f5ee9ea20f7&mcc=460' \
                '&versionName=1.7.2&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84' \
                'd0-6e8d64d3ecdf&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1Ii' \
                'widiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlY' \
                'WY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzL' \
                'CJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4N' \
                'DM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9' \
                '&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                '&appKey=201020412&id=ywFOb6nQwlgTfz7puYkRfQ%3D%3D&interfaceCode=122' \
                '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_1)

    @allure.title("测试用例3--在书城页面，选择任意一本书籍，测试能正常进行收藏操作的功能")
    def test_002_library_book_follow(self):
        print("----在书城页面，选择任意一本书籍，测试能正常进行收藏操作的功能----")
        url = '/apiBookshelf/follow?timezone=Asia%2FShanghai&sex=1' \
              '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
              '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd&sign=61ee37c599147b45' \
              '5ffe6f6291efbefa&mcc=460&versionName=1.7.2&deviceId=6fb3537dbc70aad5' \
              '&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf&versionCode=120' \
              '&userKey=5f210fa758cd2db391305b0e2749fadc&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZj' \
              'AwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLC' \
              'JsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0' \
              'MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiw' \
              'iaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1' \
              'dGhvciI6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
              '&appKey=201020412&bid=ywFOb6nQwlgTfz7puYkRfQ%3D%3D&interfaceCode=122' \
              '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url)

    @allure.title("测试用例4--在书城页面，选择任意一本书籍，测试其能取消收藏的功能")
    def test_003_library_book_un_follow(self):
        print("----在书城界面，选择任意一本已收藏的书籍，测试其能取消收藏的功能----")
        url_3 = '/apiBookshelf/unfollow?timezone=Asia%2FShanghai&sex=1' \
                '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd&sign=61ee37c599147b45' \
                '5ffe6f6291efbefa&mcc=460&versionName=1.7.2&deviceId=6fb3537dbc70aad5' \
                '&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf&versionCode=120' \
                '&userKey=5f210fa758cd2db391305b0e2749fadc&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZj' \
                'AwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwL' \
                'CJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OG' \
                'Y0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzI' \
                'iwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0' \
                'F1dGhvciI6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0' \
                '&imei=357052092096379&appKey=201020412&bid=ywFOb6nQwlgTfz7puYkRfQ%3D%3D' \
                '&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_3)

    @allure.title("测试用例5--在书城侧页面，点击右上角的会话按钮，测试其能正常进入到站内信界面的功能")
    def test_004_library_site_message(self):
        print("----在书城侧页面，点击右上角的会话按钮，测试其能正常进入到站内信界面的功能----")
        url_4 = '/Message/getNewMessage?timezone=Asia%2FShanghai' \
                '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                '&sign=3c10273fcab950d4f2df412bfa47e449&type=0&mcc=460&versionName=1.7.2' \
                '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1Ii' \
                'widiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5' \
                'Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D&size=10&u=eyJxIjo0Mjk2MDAwMz' \
                'YzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4' \
                'NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9' \
                '&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379&appKey=201020412' \
                '&page=1&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_4)
        print("-----------------------------------------")
        url_5 = '/Message/getSepUnreadMessage?timezone=Asia%2FShanghai' \
                '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                '&sign=296d345a8a679e6ba501234c5bd2c098&mcc=460&versionName=1.7.2' \
                '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1' \
                'IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNl' \
                'YWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsInM' \
                'iOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2' \
                'V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                '&appKey=201020412&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5' \
                '&timestamp=0'
        Http_Req().http_req(url_5)

    @allure.title("测试用例6--在书城页面，选择任意一本多章节书，测试用户可以自主选择章节内容的功能")
    def test_005_library_sel_article_page(self):
        print("----在书城页面，选择任意一本多章节书，测试用户可以自主选择章节内容的功能----")
        url_5 = '/api/readV1?timezone=Asia%2FShanghai&sex=1&userKeyWithoutImei=e694c359a708' \
                'd6ceda7ae2dd9fe6cacd&channel=dreameapp-23&advertising_id=7a6c42' \
                'db-2852-4db4-9206-47184fa7b8dd&sign=1fb05a95f7da7755be457d09a1929f22' \
                '&mcc=460&versionName=1.7.2&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22' \
                'e1-490e-84d0-6e8d64d3ecdf&versionCode=120&userKey=5f210fa758cd2db391305' \
                'b0e2749fadc&bookId=I7E5iWEe9YsOXMCEwrXTwg%3D%3D&s=eyJrIjoiMWMyYzg5ZTY' \
                '5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiO' \
                'jEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGV' \
                'jZGM3YWVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhG' \
                'UkU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI' \
                '6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9&chapterId=EujTCbLEkpgWh%2BU' \
                'Y64WoSg%3D%3D&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                '&appKey=201020412&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_5)

    @allure.title("测试用例7--在书城页面，根据书名模糊搜索一本书且能正常阅读的功能")
    def test_006_library_unclear_book_name_search(self):
        print("----在书城页面，根据书名模糊搜索一本书且能正常阅读的功能----")
        url_6 = '/api/search?keywords=the+lone&timezone=Asia%2FShanghai&userKeyWithoutI' \
                'mei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23&sign=44afd3a' \
                '421874975f74c928d6a222976&source=3&mcc=460&versionName=1.7.2&kwType=0' \
                '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                '&osType=0&appKey=201020412&apiLevel=28&androidId=6fb3537dbc70aad5&sex=1' \
                '&count=10&start=1&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                '&versionCode=120&userKey=5f210fa758cd2db391305b0e2749fadc' \
                '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1Ii' \
                'widiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYW' \
                'Y5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJN' \
                'IjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0' \
                'MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9' \
                '&distinct_id=6fb3537dbc70aad5&imei=357052092096379&interfaceCode=122'
        Http_Req().http_req(url_6)
        print("-----------------------------------------")
        url_6_1 = '/api/bookInfo?bookshelf=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D%2CvhRlO%2Fp2LPt1' \
                  '3fjpOFoo0Q%3D%3D%2CRvdq9VhPzTLkgyHofVE8Pw%3D%3D%2CR5NDszuwekbhS0c3i3%2Bc' \
                  'yg%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D%2C6sB5aEzcmvjSF5yvPF' \
                  'DGOQ%3D%3D&timezone=Asia%2FShanghai&userKeyWithoutImei=e694c359a708d6' \
                  'ceda7ae2dd9fe6cacd&channel=dreameapp-23&advertising_id=7a6c42db-285' \
                  '2-4db4-9206-47184fa7b8dd&sign=2cab9dd4e36d60fd7c5b725b89edb596&mcc=460' \
                  '&versionName=1.7.2' \
                  '&$referrer=com.dreame.reader.discover.search.activity.SearchActivity' \
                  '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                  '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                  '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1' \
                  'IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZG' \
                  'NlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                  '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIs' \
                  'InMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI' \
                  '6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                  '&appKey=201020412&id=8rsCWXiM6QUCApeco5HOPw%3D%3D&interfaceCode=122' \
                  '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_6_1)
        print("-----------------------------------------")
        url_6_2 = '/api/readV1?timezone=Asia%2FShanghai&sex=1&userKeyWithoutImei=e694c359a' \
                  '708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23&advertising_id=7a6c42db-28' \
                  '52-4db4-9206-47184fa7b8dd&sign=eafc1c5ee768d485d6b260059febb9c3&mcc=460' \
                  '&versionName=1.7.2&deviceId=6fb3537dbc70aad5' \
                  '&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf&versionCode=120' \
                  '&userKey=5f210fa758cd2db391305b0e2749fadc' \
                  '&bookId=kCk4XaChah0P1AZHlfhydQ%3D%3D&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZj' \
                  'AwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsIkwiO' \
                  'jEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3Y' \
                  'WVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU' \
                  '0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6I' \
                  'iIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9&chapterId=cCrJo30Q6ljmZGN' \
                  'T1intTg%3D%3D&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                  '&appKey=201020412&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_6_2)

    @allure.title("测试用例8--在书城页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能")
    def test_007_library_unclear_writer_name_search(self):
        print("----在书城页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能--")
        url_7 = '/api/search?keywords=Tasha+%28Tashie%29&timezone=Asia%2FShanghai' \
                '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                '&sign=50f9b88bdb8ab815b6a12132925df006&source=3&mcc=460&versionName=1.7.2' \
                '&kwType=2&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                '&osType=0&appKey=201020412&apiLevel=28&androidId=6fb3537dbc70aad5&sex=1' \
                '&count=10&start=1&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                '&versionCode=120&userKey=5f210fa758cd2db391305b0e2749fadc&s=eyJrIjoiMWMyYz' \
                'g5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsIm' \
                'EiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGV' \
                'jZGM3YWVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGU' \
                'kU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6Ii' \
                'IsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9&distinct_id=6fb3537dbc70aad5' \
                '&imei=357052092096379&interfaceCode=122'
        Http_Req().http_req(url_7)
        print("-----------------------------------------")
        url_7_1 = '/api/bookInfo?bookshelf=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D%2CvhRlO%2Fp2LPt' \
                  '13fjpOFoo0Q%3D%3D%2CRvdq9VhPzTLkgyHofVE8Pw%3D%3D%2CR5NDszuwekbhS0c3i3%2B' \
                  'cyg%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D%2C6sB5aEzcmvjSF5yvPFD' \
                  'GOQ%3D%3D&timezone=Asia%2FShanghai&userKeyWithoutImei=e694c359a708d6ce' \
                  'da7ae2dd9fe6cacd&channel=dreameapp-23' \
                  '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd&sign=2cab9dd4e36d' \
                  '60fd7c5b725b89edb596&mcc=460&versionName=1.7.2' \
                  '&$referrer=com.dreame.reader.discover.search.activity.SearchActivity' \
                  '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                  '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                  '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3' \
                  'l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjo' \
                  'iZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                  '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6Ii' \
                  'IsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGh' \
                  'vciI6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                  '&appKey=201020412&id=8rsCWXiM6QUCApeco5HOPw%3D%3D&interfaceCode=122' \
                  '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_7_1)
        print("-----------------------------------------")
        url_7_2 = '/api/readV1?timezone=Asia%2FShanghai&sex=1&userKeyWithoutImei=e694c359a7' \
                  '08d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                  '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                  '&sign=7fb9f86313218b39c73e92a85adceddb&mcc=460&versionName=1.7.2' \
                  '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                  '&versionCode=120&userKey=5f210fa758cd2db391305b0e2749fadc' \
                  '&bookId=8rsCWXiM6QUCApeco5HOPw%3D%3D&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZj' \
                  'AwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOj' \
                  'EwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YW' \
                  'VmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0' \
                  'Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6' \
                  'IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9&chapterId=uyn3O7EZoC%2Frvv' \
                  'DplC2nfw%3D%3D&distinct_id=6fb3537dbc70aad5&osType=0' \
                  '&imei=357052092096379&appKey=201020412&interfaceCode=122&apiLevel=28' \
                  '&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_7_2)

    @allure.title("测试用例9--在书城页面，点击右上角的“时刻表”，测试其能正常跳转到可解锁书籍查看界面的功能")
    def test_008_library_clock_time_list(self):
        print("----在书城页面，点击右上角的“时刻表”，测试其能正常跳转到可解锁书籍查看界面的功能----")
        url_8 = '/calendar/getNewCalendarContent?timezone=Asia%2FShanghai' \
                '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                '&sign=718f33fc1a7b110f9d20399ef8f9a767&mcc=460&versionName=1.7.2' \
                '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1' \
                'IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNl' \
                'YWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzL' \
                'CJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4ND' \
                'M0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9' \
                '&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379&appKey=201020412' \
                '&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_8)
        print("-----------------------------------------")
        url_8_1 = '/Calendar/bookRecommend?bookshelf=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D%2Cvh' \
                  'RlO%2Fp2LPt13fjpOFoo0Q%3D%3D%2CRvdq9VhPzTLkgyHofVE8Pw%3D%3D%2CR5NDszuw' \
                  'ekbhS0c3i3%2Bcyg%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D%2C6sB5aEzcmv' \
                  'jSF5yvPFDGOQ%3D%3D&timezone=Asia%2FShanghai&userKeyWithoutImei=e694c3' \
                  '59a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                  '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd&sign=fa319fda1e8f' \
                  'f3c04273a66ee84f2b73&mcc=460&versionName=1.7.2&deviceId=6fb3537dbc70aad5' \
                  '&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf&userKey=5f210fa758cd2db3' \
                  '91305b0e2749fadc&versionCode=120&number=20&s=eyJrIjoiMWMyYzg5ZTY5Mzhl' \
                  'MDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsI' \
                  'kwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZ' \
                  'GM3YWVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6I' \
                  'khGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6' \
                  'MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9&distinct_id=6fb3537dbc70aad5' \
                  '&osType=0&imei=357052092096379&appKey=201020412&interfaceCode=122' \
                  '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_8_1)

    @allure.title("测试用例10--对于存在多章节的书籍在该章节阅读完成时，测试其能正常阅读下一章节的功能")
    def test_009_library_next_article_reading(self):
        print("----对于存在多章节的书籍在该章节阅读完成时，测试其能正常阅读下一章节的功能----")
        url_9 = '/api/readV1?timezone=Asia%2FShanghai&sex=1' \
                '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                '&sign=b78961756c8b99642765d05e3b2853f4&mcc=460&versionName=1.7.2' \
                '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                '&versionCode=120&userKey=5f210fa758cd2db391305b0e2749fadc' \
                '&bookId=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D' \
                '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamlu' \
                'Z3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjo' \
                'iZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiI' \
                'sInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI' \
                '6ZmFsc2V9&chapterId=4WmrQSbPh8dZb0su5lkjRA%3D%3D&distinct_id=6fb3537dbc70aad5' \
                '&osType=0&imei=357052092096379&appKey=201020412&interfaceCode=122' \
                '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_9)

    @allure.title("测试用例11--当用户余额足够时，测试其能正常购买收费章节书的功能能")
    @pytest.mark.skip
    def test_010_case(self):  # 未完成
        print("----当用户余额足够时，测试其能正常购买收费章节书的功能----")
        print("----查询用户钱包余额----")
        url_wallet = host + '/user/getUserInfo?timezone=Asia%2FShanghai' \
                            '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd' \
                            '&channel=dreameapp-23&advertising_id=7a6c42db-2852-4db4-9206-47184fa' \
                            '7b8dd&sign=718f33fc1a7b110f9d20399ef8f9a767&mcc=460&versionName=1.7.2' \
                            '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                            '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                            '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamlu' \
                            'Z3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjow' \
                            'LCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                            '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI' \
                            '6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc' \
                            '0F1dGhvciI6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0' \
                            '&imei=357052092096379&currency=&appKey=201020412&interfaceCode=122' \
                            '&apiLevel=28&androidId=6fb3537dbc70aad5'
        result_10 = self.s.get(url_wallet)
        pprint(result_10.json())
        res = result_10.json()
        wallet = res['dataJson']
        wallet_1 = wallet['balance']
        wallet_coin = wallet_1['coupon']
        money = int(wallet_coin)
        if money > 30:
            print("----购买章节----")
            url_10 = host + '/api/payBuy?timezone=Asia%2FShanghai&sex=1' \
                            '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd' \
                            '&channel=dreameapp-23&advertising_id=7a6c42db-2852-4db4-9206-47184f' \
                            'a7b8dd&sign=0d22f9213cf880d5cf69103eedfc3471&mcc=460&versionName=1.7.2' \
                            '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                            '&versionCode=120&userKey=5f210fa758cd2db391305b0e2749fadc' \
                            '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiaml' \
                            'uZ3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowL' \
                            'CJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                            '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI' \
                            '6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0' \
                            'F1dGhvciI6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0' \
                            '&imei=357052092096379&appKey=201020412&bid=I7E5iWEe9YsOXMCEwr' \
                            'XTwg%3D%3D&interfaceCode=122&apiLevel=28&auto_pay=0' \
                            '&androidId=6fb3537dbc70aad5&cid=PJ1h5%2F9WBnTxA9WvBRmCWA%3D%3D'
            result_10 = self.s.get(url_10)
            print(result_10.json())
        else:
            print("----余额不足，请充值")

    @allure.title("测试用例12--在书架页面，测试直接点击收藏的书会进入到阅读界面的功能")
    def test_011_bookshelf_save_book_reading(self):
        print("----在书架页面，测试直接点击收藏的书会进入到阅读界面的功能----")
        url_11 = '/api/getChapList?timezone=Asia%2FShanghai' \
                 '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                 '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                 '&sign=1c7e5a5ded0bd26562f15312c2b76356&mcc=460&versionName=1.7.2' \
                 '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                 '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                 '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l' \
                 '1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZ' \
                 'GNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                 '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIs' \
                 'InMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI' \
                 '6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                 '&appKey=201020412&id=6sB5aEzcmvjSF5yvPFDGOQ%3D%3D&interfaceCode=122' \
                 '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_11)

    @allure.title("测试用例13--在书架页面，点击右上角的“礼包”，测试能正常跳转到任务管理界面的功能")
    def test_012_bookshelf_gift_task_list(self):
        print("----在书架页面，点击右上角的“礼包”，测试能正常跳转到任务管理界面的功能----")
        url_12 = '/api/getUserTask?u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2M' \
                 'DAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIs' \
                 'ImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjA' \
                 'wNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOj' \
                 'EwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3Y' \
                 'WVmOTA5OGY0MWEifQ%3D%3D&userKey=5f210fa758cd2db391305b0e2749fadc' \
                 '&deviceId=6fb3537dbc70aad5&newUserIndex=2&mcc=460' \
                 '&timezone=Asia%2FShanghai&channel=dreameapp-23&versionCode=120' \
                 '&versionName=1.7.2&bookshelfCount=1&loginType=10&isAuthor=0&osType=0&tag=task'
        Http_Req().http_req_www(url_12)
        print("-----------------------------------------")
        url_12_1 = '/api/getTodayTaskInfo?u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU' \
                   '0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiY' \
                   'iI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9&s=eyJrIjoiMWMyYzg5ZTY5Mzhl' \
                   'MDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOj' \
                   'EsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ' \
                   '2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                   '&userKey=5f210fa758cd2db391305b0e2749fadc&deviceId=6fb3537dbc70aad5' \
                   '&newUserIndex=2&mcc=460&timezone=Asia%2FShanghai&channel=dreameapp-23' \
                   '&versionCode=120&versionName=1.7.2&bookshelfCount=1&loginType=10' \
                   '&isAuthor=0&osType=0'
        Http_Req().http_req_www(url_12_1)
        print("-----------------------------------------")
        url_12_2 = '/api/getTomorrowTask?u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6Ikh' \
                   'GUkU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYy' \
                   'I6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9&s=eyJrIjoiMWMyYzg5' \
                   'ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuM' \
                   'CIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2' \
                   'OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                   '&userKey=5f210fa758cd2db391305b0e2749fadc&deviceId=6fb3537dbc70aad5' \
                   '&newUserIndex=2&mcc=460&timezone=Asia%2FShanghai&channel=dreameapp-23' \
                   '&versionCode=120&versionName=1.7.2&bookshelfCount=1&loginType=10' \
                   '&isAuthor=0&osType=0'
        Http_Req().http_req_www(url_12_2)

    @allure.title("测试用例14--在任务管理界面，点击“阅读”任务，测试其能正常跳转到书架（可配置）页面的功能")
    def test_013_task_list_reading_task_turn(self):
        print("----在任务管理界面，点击“阅读”任务，测试其能正常跳转到书架（可配置）页面的功能----")
        url_13 = '/api/getAll?timezone=Asia%2FShanghai&userKeyWithoutImei=e694c359a708d' \
                 '6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                 '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                 '&sign=3a7f7d722641893216a93b158260d0ea&type=54&mcc=460&versionName=1.7.2' \
                 '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                 '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                 '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1' \
                 'IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZ' \
                 'GNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                 '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsI' \
                 'nMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvci' \
                 'I6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                 '&isSuggest=1&appKey=201020412&interfaceCode=122&apiLevel=28' \
                 '&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_13)

    @allure.title("测试用例15--在书架页面，点击右上角的“时刻钟”按钮，测试其能正常跳转到解锁书籍界面的功能")
    def test_014_bookshelf_time_clock_unlock_book(self):
        print("----在书架页面，点击右上角的“时刻钟”按钮，测试其能正常跳转到解锁书籍界面的功能----")
        url_14 = '/calendar/getNewCalendarContent?timezone=Asia%2FShanghai' \
                 '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd' \
                 '&channel=dreameapp-23&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                 '&sign=718f33fc1a7b110f9d20399ef8f9a767&mcc=460&versionName=1.7.2' \
                 '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                 '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120&' \
                 's=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1Ii' \
                 'widiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYW' \
                 'Y5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                 '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIs' \
                 'InMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvci' \
                 'I6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                 '&appKey=201020412&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_14)

    @allure.title("测试用例16--在书架页面，根据书名模糊搜索一本书且能正常阅读的功能")
    def test_015_bookshelf_unclear_book_name_api_search(self):
        print("----在书架页面，根据书名模糊搜索一本书且能正常阅读的功能----")
        url_15 = '/api/search?keywords=Wolf&timezone=Asia%2FShanghai' \
                 '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                 '&sign=9535651e879ece1354ac9ed7f113a0ba&source=3&mcc=460&versionName=1.7.2' \
                 '&kwType=2&deviceId=6fb3537dbc70aad5' \
                 '&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf&osType=0&appKey=201020412' \
                 '&apiLevel=28&androidId=6fb3537dbc70aad5&sex=1&count=10&start=1' \
                 '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd&versionCode=120' \
                 '&userKey=5f210fa758cd2db391305b0e2749fadc' \
                 '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l' \
                 '1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZG' \
                 'NlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                 '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIs' \
                 'InMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvci' \
                 'I6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&imei=357052092096379' \
                 '&interfaceCode=122'
        Http_Req().http_req(url_15)
        print("-----------------------------------------")
        url_15_1 = '/api/bookInfo?bookshelf=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D%2CvhRlO%2Fp2LP' \
                   't13fjpOFoo0Q%3D%3D%2CRvdq9VhPzTLkgyHofVE8Pw%3D%3D%2CR5NDszuwekbh' \
                   'S0c3i3%2Bcyg%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D%2C6sB5aEzcmvjS' \
                   'F5yvPFDGOQ%3D%3D&timezone=Asia%2FShanghai' \
                   '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd' \
                   '&channel=dreameapp-23&advertising_id=7a6c42db-2852-4db4-9206-47184fa7' \
                   'b8dd&sign=be6bfce2d7bf32da9b83cbdbfb1b1378&mcc=460&versionName=1.7.2' \
                   '&$referrer=com.dreame.reader.discover.search.activity.SearchActivity' \
                   '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                   '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                   '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3' \
                   'l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIj' \
                   'oiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                   '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIs' \
                   'InMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvci' \
                   'I6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                   '&appKey=201020412&id=%2BIoJltntt7k0ftGy3YzEhg%3D%3D&interfaceCode=122' \
                   '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_15_1)
        print("-----------------------------------------")
        url_15_2 = '/api/readV1?timezone=Asia%2FShanghai&sex=1' \
                   '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd' \
                   '&channel=dreameapp-23&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b' \
                   '8dd&sign=730fd6be12a53c7ddd031bd08c2ec252&mcc=460&versionName=1.7.2' \
                   '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                   '&versionCode=120&userKey=5f210fa758cd2db391305b0e2749fadc' \
                   '&bookId=%2BIoJltntt7k0ftGy3YzEhg%3D%3D' \
                   '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l' \
                   '1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoi' \
                   'ZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                   '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6Ii' \
                   'IsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1d' \
                   'GhvciI6ZmFsc2V9&chapterId=RfDEOUT1stbtlBimIukDNA%3D%3D' \
                   '&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                   '&appKey=201020412&interfaceCode=122&apiLevel=28' \
                   '&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_15_2)

    @allure.title("测试用例17--在书架页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能")
    def test_016_bookshelf_unclear_writer_name_api_search(self):
        print("----在书架页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能----")
        url_16 = '/api/search?keywords=coming&timezone=Asia%2FShanghai' \
                 '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                 '&sign=84be9400a27ed5cf1ff5e774f819e384&source=3&mcc=460&versionName=1.7.2' \
                 '&kwType=0&deviceId=6fb3537dbc70aad5' \
                 '&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf&osType=0&appKey=201020412' \
                 '&apiLevel=28&androidId=6fb3537dbc70aad5&sex=1&count=10&start=1' \
                 '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd&versionCode=120' \
                 '&userKey=5f210fa758cd2db391305b0e2749fadc' \
                 '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3' \
                 'l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjo' \
                 'iZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                 '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsI' \
                 'nMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI' \
                 '6ZmFsc2V9&distinct_id=6fb3537dbc70aad5' \
                 '&imei=357052092096379&interfaceCode=122'
        Http_Req().http_req(url_16)
        print("-----------------------------------------")
        url_16_1 = '/api/bookInfo?bookshelf=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D%2CvhRlO%2Fp2LP' \
                   't13fjpOFoo0Q%3D%3D%2CRvdq9VhPzTLkgyHofVE8Pw%3D%3D%2CR5NDszuwekbhS0c' \
                   '3i3%2Bcyg%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D%2C6sB5aEzcmvjSF5y' \
                   'vPFDGOQ%3D%3D&timezone=Asia%2FShanghai' \
                   '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd' \
                   '&channel=dreameapp-23&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                   '&sign=43b1a177cf80ff87860f9aea56ea53b9&mcc=460&versionName=1.7.2' \
                   '&$referrer=com.dreame.reader.discover.search.activity.SearchActivity' \
                   '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                   '&userKey=5f210fa758cd2db391305b0e2749fadc' \
                   '&versionCode=120&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFm' \
                   'MDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg' \
                   '0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OG' \
                   'Y0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwM' \
                   'zYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUi' \
                   'OiIiLCJpc0F1dGhvciI6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0' \
                   '&imei=357052092096379&appKey=201020412&id=6u9rGU%2F0FVMUPiItb' \
                   'X9ALQ%3D%3D&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_16_1)
        print("-----------------------------------------")
        url_16_2 = '/api/readV1?timezone=Asia%2FShanghai&sex=1' \
                   '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                   '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                   '&sign=353fb8b8627e0c433c1de3b6d51d0e0f&mcc=460&versionName=1.7.2' \
                   '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                   '&versionCode=120&userKey=5f210fa758cd2db391305b0e2749fadc' \
                   '&bookId=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDF' \
                   'mZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsIkw' \
                   'iOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM' \
                   '3YWVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUk' \
                   'U0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI' \
                   '6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9&chapterId=%2BHuH0D4XYnMpZmksh' \
                   'MYvcA%3D%3D&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                   '&appKey=201020412&interfaceCode=122&apiLevel=28' \
                   '&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_16_2)

    @allure.title("测试用例18--在书架页面，点击右上角的“会话”按钮，测试其能正常进入到站内信界面的功能")
    def test_017_bookshelf_site_message(self):
        print("----在书架页面，点击右上角的“会话”按钮，测试其能正常进入到站内信界面的功能----")
        url_17 = '/Message/getSepUnreadMessage?timezone=Asia%2FShanghai' \
                 '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd' \
                 '&channel=dreameapp-23&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                 '&sign=296d345a8a679e6ba501234c5bd2c098&mcc=460&versionName=1.7.2' \
                 '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                 '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                 '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1I' \
                 'iwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlY' \
                 'WY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzL' \
                 'CJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4N' \
                 'DM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9' \
                 '&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                 '&appKey=201020412&interfaceCode=122&apiLevel=28' \
                 '&androidId=6fb3537dbc70aad5&timestamp=0'
        Http_Req().http_req(url_17)
        print("-----------------------------------------")
        url_17_1 = '/Message/getNewMessage?timezone=Asia%2FShanghai' \
                   '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                   '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                   '&sign=3c10273fcab950d4f2df412bfa47e449&type=0&mcc=460&versionName=1.7.2' \
                   '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                   '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                   '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3' \
                   'l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZ' \
                   'GNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D&size=10' \
                   '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiI' \
                   'sInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvci' \
                   'I6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                   '&appKey=201020412&page=1&interfaceCode=122&apiLevel=28' \
                   '&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_17_1)

    @allure.title("测试用例19--在书架页面，测试取消一本收藏书籍的功能")
    def test_018_bookshelf_un_follow_book(self):
        print("----在书架页面，测试取消一本收藏书籍的功能运行正确----")
        url_18 = '/apiBookshelf/batchUnfollow?timezone=Asia%2FShanghai&sex=1' \
                 '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                 '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                 '&sign=6720ac191dc5612e9ff2c2fbf0a5f32a&mcc=460&versionName=1.7.2' \
                 '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                 '&versionCode=120&userKey=5f210fa758cd2db391305b0e2749fadc' \
                 '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1Ii' \
                 'widiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNlYW' \
                 'Y5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                 '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsIn' \
                 'MiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6Z' \
                 'mFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                 '&appKey=201020412&bid=6sB5aEzcmvjSF5yvPFDGOQ%3D%3D&interfaceCode=122' \
                 '&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_18)

    @allure.title("测试用例20--在书架页面，测试批量取消多本收藏书籍的功能")
    def test_019_bookshelf_piliang_cancle_books(self):
        print("----在书架页面，测试批量取消多本收藏书籍的功能运行正确----")
        url_19 = '/apiBookshelf/batchUnfollow?timezone=Asia%2FShanghai&sex=1' \
                 '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                 '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                 '&sign=38db412505f967ce3dbbd83bdb8720d5&mcc=460&versionName=1.7.2' \
                 '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                 '&versionCode=120&userKey=5f210fa758cd2db391305b0e2749fadc' \
                 '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1I' \
                 'iwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZGNl' \
                 'YWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzYzL' \
                 'CJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTU4' \
                 'NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9' \
                 '&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                 '&appKey=201020412&bid=vhRlO%2Fp2LPt13fjpOFoo0Q%3D%3D%2C6u9rGU%2F0FVMUPiI' \
                 'tbX9ALQ%3D%3D&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_19)

    @allure.title("测试用例21--在“我的”界面，测试点击inbox能正常进入到短信及站内信界面的功能")
    def test_020_my_account_inbox_function(self):
        print("----在“我的”界面，测试点击inbox能正常进入到短信及站内信界面的功能----")
        url_20 = '/Message/getSepUnreadMessage?timezone=Asia%2FShanghai' \
                 '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                 '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                 '&sign=296d345a8a679e6ba501234c5bd2c098&mcc=460&versionName=1.7.2' \
                 '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                 '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                 '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamluZ3l1' \
                 'IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJzIjoiZG' \
                 'NlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D' \
                 '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6IiIsIn' \
                 'MiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6Zm' \
                 'Fsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                 '&appKey=201020412&interfaceCode=122&apiLevel=28&androidId=6fb3537dbc70aad5' \
                 '&timestamp=0'
        Http_Req().http_req(url_20)
        print("-----------------------------------------")
        url_20_1 = '/Message/getNewMessage?timezone=Asia%2FShanghai' \
                   '&userKeyWithoutImei=e694c359a708d6ceda7ae2dd9fe6cacd&channel=dreameapp-23' \
                   '&advertising_id=7a6c42db-2852-4db4-9206-47184fa7b8dd' \
                   '&sign=3c10273fcab950d4f2df412bfa47e449&type=0&mcc=460&versionName=1.7.2' \
                   '&deviceId=6fb3537dbc70aad5&uuid=0cd7ed1a-22e1-490e-84d0-6e8d64d3ecdf' \
                   '&userKey=5f210fa758cd2db391305b0e2749fadc&versionCode=120' \
                   '&s=eyJrIjoiMWMyYzg5ZTY5MzhlMDFmZjAwNDQ0ZWI1YjVhMjFmMDYiLCJTIjoiamlu' \
                   'Z3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNTg0MzY2LCJyIjowLCJz' \
                   'IjoiZGNlYWY5Yzk2OGNiOTQ2NGVjZGM3YWVmOTA5OGY0MWEifQ%3D%3D&size=10' \
                   '&u=eyJxIjo0Mjk2MDAwMzYzLCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzYzIiwiaSI6Ii' \
                   'IsInMiOiIwIiwibSI6MTU5MTU4NDM0MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhv' \
                   'ciI6ZmFsc2V9&distinct_id=6fb3537dbc70aad5&osType=0&imei=357052092096379' \
                   '&appKey=201020412&page=1&interfaceCode=122&apiLevel=28' \
                   '&androidId=6fb3537dbc70aad5'
        Http_Req().http_req(url_20_1)


if __name__ == '__main__':
    unittest.main()
