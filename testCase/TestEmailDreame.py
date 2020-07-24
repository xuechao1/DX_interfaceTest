# -*- coding:utf-8 -*-

import time
import requests
import unittest
import warnings
from pprint import pprint

host = 'http://3.85.16.233:32100'
host_comment = 'http://social.dreame.com'
host_www = 'http://activity.dreame.com'


class TestEmailDreame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.s = requests.session()
        print("----开始执行测试用例  start ----")
        print("----Email 邮箱登录 ----")
        url = host + '/api/login?timezone=Asia%2FShanghai&userKeyWithoutImei=' \
                     '&channel=dreameapp-23&advertising_id=cda1c8db-8cca-4d2f-a1d2-70776fba9b84' \
                     '&sign=eddd33db8cc0fe3bc757b7fae1ae238f&mcc=0&versionName=1.7.4' \
                     '&deviceId=aade10b1adfa8268&uuid=e277e108-b959-4b30-b0a7-d5342b0c016b' \
                     '&userKey=&versionCode=125&password=h8cl3q8WRUfTga5faCIp8OABjBm%2BmmRUk2jP0QKD' \
                     'ElkKo%2FKodrumlOjS1%2BxiL3VYi%2BMyZUbWOGbLk%2F%2FzCvK1hNPWsNCE5eJo5p' \
                     '20Pd%2BCzob74HPZQjjb517JATj78VgW4FtErRRJ4JBU3BRmNuaJyl4aOdaDvVfHCW2lTdQB6KE%3D' \
                     '&s=eyJrIjoiY2I1NTdiNmE1Yzg4Y2E2ZGI3ZTFkOTZmMzk5OWQ3YzMiLCJTIjoiamluZ3l1Iiw' \
                     'idiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNzYwMzU4LCJyIjowLCJzIjoiY2Y4NTViM' \
                     'TVlMGFiZTc3MWQyNWQ0MzFkZTQzNTYzMWIifQ%3D%3D' \
                     '&u=eyJxIjo0Mjk2MDAwMzY3LCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzY3IiwiaSI6IiIsInMi' \
                     'OiIwIiwibSI6MTU5MTcwMjg4MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9' \
                     '&distinct_id=aade10b1adfa8268&osType=0&appKey=201020412&interfaceCode=122' \
                     '&user=xuechao%40stary.ltd&apiLevel=29&androidId=aade10b1adfa8268'
        result = cls.s.get(url)
        t = result.json()
        u_1 = t['dataJson']
        # 过滤 u 跟 s
        global u
        u = u_1['u']
        global s
        s = u_1['s']

    def test_000_case(self):
        """
        ---测试邮件用户能正常登录APP的功能----
        :return:
        """
        print("----Email 邮箱登录 ----")
        url = host + '/api/login?timezone=Asia%2FShanghai&userKeyWithoutImei=' \
                     '&channel=dreameapp-23&advertising_id=cda1c8db-8cca-4d2f-a1d2-70776fba9b84' \
                     '&sign=eddd33db8cc0fe3bc757b7fae1ae238f&mcc=0&versionName=1.7.4' \
                     '&deviceId=aade10b1adfa8268&uuid=e277e108-b959-4b30-b0a7-d5342b0c016b' \
                     '&userKey=&versionCode=125&password=h8cl3q8WRUfTga5faCIp8OABjBm%2BmmRUk2jP0QKD' \
                     'ElkKo%2FKodrumlOjS1%2BxiL3VYi%2BMyZUbWOGbLk%2F%2FzCvK1hNPWsNCE5eJo5p' \
                     '20Pd%2BCzob74HPZQjjb517JATj78VgW4FtErRRJ4JBU3BRmNuaJyl4aOdaDvVfHCW2lTdQB6KE%3D' \
                     '&s=eyJrIjoiY2I1NTdiNmE1Yzg4Y2E2ZGI3ZTFkOTZmMzk5OWQ3YzMiLCJTIjoiamluZ3l1Iiw' \
                     'idiI6IjEuMCIsImEiOjEsIkwiOjEwLCJsIjoxNTkxNzYwMzU4LCJyIjowLCJzIjoiY2Y4NTViM' \
                     'TVlMGFiZTc3MWQyNWQ0MzFkZTQzNTYzMWIifQ%3D%3D' \
                     '&u=eyJxIjo0Mjk2MDAwMzY3LCJNIjoiIiwibiI6IkhGUkU0Mjk2MDAwMzY3IiwiaSI6IiIsInMi' \
                     'OiIwIiwibSI6MTU5MTcwMjg4MSwiYyI6MCwiYiI6IiIsImUiOiIiLCJpc0F1dGhvciI6ZmFsc2V9' \
                     '&distinct_id=aade10b1adfa8268&osType=0&appKey=201020412&interfaceCode=122' \
                     '&user=xuechao%40stary.ltd&apiLevel=29&androidId=aade10b1adfa8268'
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_001_case(self):
        print("----在书城页面，选择任意一本书籍，测试能正常阅读的功能----")
        url_1 = host + '/Discover/channel'
        try:
            result_1 = self.s.get(url_1)
            t = result_1.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url_1_1 = host + '/Discover/channel?subChannel=53&appKey=201020412&u={}&s={}&userKey=' \
                         '&userKeyWithoutImei=&interfaceCode=122&mcc=0&channel=dreameapp-23&versionCode=125&versionName=1.7.4&osType=0' \
                         '&distinct_id=aade10b1adfa8268&advertising_id=cda1c8db-8cca-4d2f-a1d2-70776fba9b84&timezone=Asia%2FShanghai' \
                         '&deviceId=aade10b1adfa8268&uuid=e277e108-b959-4b30-b0a7-d5342b0c016b&androidId=aade10b1adfa8268&apiLevel=29' \
                         '&sign=3dc33b4110eca678042538d2e95a1a4f&debug=panjian'.format(u, s)
        try:
            result_1_1 = self.s.get(url_1_1)
            tt = result_1_1.json()
            print(tt)
            self.assertEqual(0, tt["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url_1_2 = host + '/api/bookInfo?bookshelf=vhRlO%2Fp2LPt13fjpOFoo0Q%3D%3D%2CG3yobNQftTHHIdbYESsqCA%3D%3D%2CxLA%2FF' \
                         'piCfzOV09eVC8QEHg%3D%3D%2CRvdq9VhPzTLkgyHofVE8Pw%3D%3D%2C%2BiEFxZxn8dAqSMaLz' \
                         'Mv%2Fjw%3D%3D&timezone=Asia%2FShanghai' \
                         '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                         '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                         '&sign=7d1bf3728227fad3abfddcaaa328b832&mcc=460&versionName=1.7.4' \
                         '&$referrer=com.dreame.reader.common.MainActivity' \
                         '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                         '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125&s={}&u={}' \
                         '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093' \
                         '&appKey=201020412&id=Gzv0Bf5b9nfvE%2F8zzs2IGA%3D%3D&interfaceCode=122' \
                         '&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result_1_2 = self.s.get(url_1_2)
            ttt = result_1_2.json()
            print(ttt)
            self.assertEqual(0, ttt["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url_1_3 = host + '/api/readV1?timezone=Asia%2FShanghai&sex=1' \
                         '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b' \
                         '&channel=dreameoppo-46&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                         '&sign=d226df1bb6fd1ef9320c450bb08b885b&mcc=460&versionName=1.7.4' \
                         '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                         '&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                         '&bookId=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D&s={}&u={}' \
                         '&chapterId=uGAb83UcWy96VHpg5JsHKQ%3D%3D&distinct_id=b1364ddb106b056c' \
                         '&osType=0&imei=866716038443093&appKey=201020412&interfaceCode=122' \
                         '&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result_1_3 = self.s.get(url_1_3)
            tttt = result_1_3.json()
            print(tttt)
            self.assertEqual(0, tttt["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_002_case(self):
        print("----在书城页面，选择任意一本书籍，测试能正常进行收藏操作的功能----")
        url = host + '/apiBookshelf/follow?timezone=Asia%2FShanghai&sex=1' \
                     '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                     '&sign=7c0f870ae478779adf1cd2a1052b4abb&mcc=460&versionName=1.7.4' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                     '&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4&s={}&u={}' \
                     '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                     '&bid=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D&interfaceCode=122&apiLevel=28' \
                     '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_003_case(self):
        print("----在书城界面，选择任意一本已收藏的书籍，测试其能取消收藏的功能----")
        url = host + '/apiBookshelf/unfollow?timezone=Asia%2FShanghai&sex=1' \
                     '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                     '&sign=7c0f870ae478779adf1cd2a1052b4abb&mcc=460&versionName=1.7.4' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                     '&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4&s={}&u={}' \
                     '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                     '&bid=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D&interfaceCode=122&apiLevel=28' \
                     '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_004_case(self):
        print("----在阅读书籍时，测试能正常点击分享链接按钮进行分享的功能----")
        url1 = host_comment + '/api/commentList?timezone=Asia%2FShanghai&userKeyWithoutImei=4e701c7505c' \
                              'e494c7b28be2da07b6f3b&channel=dreameoppo-46&advertising_id=4cd19094-1fd' \
                              'd-436a-8f65-d7f3c27f536f&sign=ad62f0a1d3f0f9a409dc62f1544a2d98&mcc=460' \
                              '&versionName=1.7.4&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b' \
                              '9739a85c813&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125' \
                              '&bookId=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D&s={}&size=10&u={}' \
                              '&chapterId=1EHEpSD%2FKYPjA%2B%2BNQHscAg%3D%3D&distinct_id=b1364ddb106b056c' \
                              '&osType=0&imei=866716038443093&appKey=201020412&page=1&interfaceCode=122' \
                              '&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            tt = result1.json()
            print(tt)
            self.assertEqual(0, tt["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url = host_comment + '/api/doComment?timezone=Asia%2FShanghai&userKeyWithoutImei=4e701c7505ce494' \
                             'c7b28be2da07b6f3b&channel=dreameoppo-46&advertising_id=4cd19094-1fdd-43' \
                             '6a-8f65-d7f3c27f536f&sign=82e8a912b5d9f9365adf59827e956e5f&mcc=460' \
                             '&versionName=1.7.4&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9' \
                             '739a85c813&content=test+community+service+and+the+rest+are+going+through+so' \
                             'me+reason+why+you+should+have+never+seen+with+my+friends.' \
                             '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125' \
                             '&bookId=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D&s={}&u={}' \
                             '&chapterId=1EHEpSD%2FKYPjA%2B%2BNQHscAg%3D%3D&distinct_id=b1364ddb106b056c' \
                             '&osType=0&imei=866716038443093&appKey=201020412&interfaceCode=122&apiLevel=28' \
                             '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_005_case(self):
        print("----在书城侧页面，点击右上角的会话按钮，测试其能正常进入到站内信界面的功能----")
        url = host + '/Message/getSepUnreadMessage?timezone=Asia%2FShanghai&userKeyWithout' \
                     'Imei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f&sign=20a83e4edfd4f2' \
                     '39f77dca68478bd902&mcc=460&versionName=1.7.4&deviceId=b1364ddb106b056c' \
                     '&uuid=9f223804-130d-4069-8f94-b9739a85c813&userKey=b1232786105b6a3c82c0' \
                     'fa447d3946f4&versionCode=125&s={}&u={}&distinct_id=b1364ddb106b056c' \
                     '&osType=0&imei=866716038443093&appKey=201020412&interfaceCode=122&apiLevel=28' \
                     '&androidId=b1364ddb106b056c&timestamp=0&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url1 = host + '/Message/getNewMessage?timezone=Asia%2FShanghai&userKeyWithoutImei=4e701c' \
                      '7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46&advertising_id=4cd19094-1f' \
                      'dd-436a-8f65-d7f3c27f536f&sign=511f14f7ab48ce6c2628c8adbefe8c70&type=0' \
                      '&mcc=460&versionName=1.7.4&deviceId=b1364ddb106b056c&uuid=9f223804-130d-40' \
                      '69-8f94-b9739a85c813&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125' \
                      '&s={}&size=10&u={}&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093' \
                      '&appKey=201020412&page=1&interfaceCode=122&apiLevel=28' \
                      '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            t1 = result1.json()
            pprint(t1)
            self.assertEqual(0, t1["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_006_case(self):
        print("----在书城页面，选择任意一本多章节书，测试用户可以自主选择章节内容的功能----")
        url = host + '/api/readV1?timezone=Asia%2FShanghai&sex=1&userKeyWithoutImei=4e701c7' \
                     '505ce494c7b28be2da07b6f3b&channel=dreameoppo-46&advertising_id=4cd19094-1f' \
                     'dd-436a-8f65-d7f3c27f536f&sign=a2fdc4392ee461454d1927c68efc24b9&mcc=460' \
                     '&versionName=1.7.4&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9' \
                     '739a85c813&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                     '&bookId=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D&s={}&u={}&chapterId=2Moxbu54RxEAefts' \
                     'eDNIZQ%3D%3D&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093' \
                     '&appKey=201020412&interfaceCode=122&apiLevel=28' \
                     '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_007_case(self):
        print("----在书城页面，根据书名模糊搜索一本书且能正常阅读的功能----")
        url = host + '/api/search?keywords=change&timezone=Asia%2FShanghai&userKeyWithoutImei=4e70' \
                     '1c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46&sign=74c4c065f812808b5b' \
                     '8ed52abf0b536d&source=3&mcc=460&versionName=1.7.4&kwType=0&deviceId=b1364ddb' \
                     '106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813&osType=0&appKey=201020412' \
                     '&apiLevel=28&androidId=b1364ddb106b056c&sex=1&count=10&start=1' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f&versionCode=125' \
                     '&userKey=b1232786105b6a3c82c0fa447d3946f4&s={}&u={}&distinct_id=b1364ddb1' \
                     '06b056c&imei=866716038443093&interfaceCode=122&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_008_case(self):
        print("----在书城页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能----")
        url = host + '/api/search?keywords=AnggiePuteri&timezone=Asia%2FShanghai&userKeyWithoutI' \
                     'mei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46&sign=48efc267a' \
                     'ee3f0e03c0321b79a7126e6&source=3&mcc=460&versionName=1.7.4&kwType=2' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813&osType=0' \
                     '&appKey=201020412&apiLevel=28&androidId=b1364ddb106b056c&sex=1&count=10' \
                     '&start=1&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f&versionCode=125' \
                     '&userKey=b1232786105b6a3c82c0fa447d3946f4&s={}&u={}&distinct_id=b1364ddb10' \
                     '6b056c&imei=866716038443093&interfaceCode=122&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url1 = host + '/api/bookInfo?bookshelf=vhRlO%2Fp2LPt13fjpOFoo0Q%3D%3D%2CG3yobNQftTHHIdbY' \
                      'ESsqCA%3D%3D%2CxLA%2FFpiCfzOV09eVC8QEHg%3D%3D%2CRvdq9VhPzTLkgyHofVE' \
                      '8Pw%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D&timezone=Asia%2FShanghai' \
                      '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                      '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f&sign=0df28fa4265c6880a' \
                      'e84341c603c436b&mcc=460&versionName=1.7.4&$referrer=com.dreame.reader.disc' \
                      'over.search.activity.SearchActivity&deviceId=b1364ddb106b056c' \
                      '&uuid=9f223804-130d-4069-8f94-b9739a85c813&userKey=b1232786105b6a3c82c0fa4' \
                      '47d3946f4&versionCode=125&s={}&u={}&distinct_id=b1364ddb106b056c&osType=0' \
                      '&imei=866716038443093&appKey=201020412&id=6xTr0O97dFasD4%2BpXz8Vtw%3D%3D' \
                      '&interfaceCode=122&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            t1 = result1.json()
            print(t1)
            self.assertEqual(0, t1["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_009_case(self):
        print("----在书城页面，点击右上角的“时刻表”，测试其能正常跳转到可解锁书籍查看界面的功能----")
        url = host + '/calendar/getNewCalendarContent?timezone=Asia%2FShanghai&userKeyWithoutI' \
                     'mei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46&advertisi' \
                     'ng_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f&sign=2d19e9c35083383302b1c8ed48e' \
                     'b79d9&mcc=460&versionName=1.7.4&deviceId=b1364ddb106b056c&uuid=9f223804-13' \
                     '0d-4069-8f94-b9739a85c813&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                     '&versionCode=125&s={}&u={}&distinct_id=b1364ddb106b056c&osType=0' \
                     '&imei=866716038443093&appKey=201020412&interfaceCode=122&apiLevel=28' \
                     '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url1 = host + '/Calendar/bookRecommend?bookshelf=vhRlO%2Fp2LPt13fjpOFoo0Q%3D%3D%2CG3yobNQftT' \
                      'HHIdbYESsqCA%3D%3D%2CxLA%2FFpiCfzOV09eVC8QEHg%3D%3D%2CRvdq9VhPzTLkgyHofVE8' \
                      'Pw%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D&timezone=Asia%2FShanghai' \
                      '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                      '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f&sign=f7290cb36cb364a9bbd' \
                      'e77a730c97cf0&mcc=460&versionName=1.7.4&deviceId=b1364ddb106b056c' \
                      '&uuid=9f223804-130d-4069-8f94-b9739a85c813&userKey=b1232786105b6a3c82c0fa447d' \
                      '3946f4&versionCode=125&number=20&s={}&u={}&distinct_id=b1364ddb106b056c' \
                      '&osType=0&imei=866716038443093&appKey=201020412&interfaceCode=122' \
                      '&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            t1 = result1.json()
            print(t1)
            self.assertEqual(0, t1["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_010_case(self):
        print("----对于存在多章节的书籍在该章节阅读完成时，测试其能正常阅读下一章节的功能----")
        url = host + '/api/readV1?timezone=Asia%2FShanghai&sex=1&userKeyWithoutImei=4e701c7505ce494' \
                     'c7b28be2da07b6f3b&channel=dreameoppo-46&advertising_id=4cd19094-1fdd-436a-8' \
                     'f65-d7f3c27f536f&sign=dce126011659e5005c7dd7702e4dbd79&mcc=460' \
                     '&versionName=1.7.4&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9' \
                     '739a85c813&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                     '&bookId=6u9rGU%2F0FVMUPiItbX9ALQ%3D%3D&s={}&u={}&chapterId=ZOpGDCclv%2B7wjkQ' \
                     'KfBDqAQ%3D%3D&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093' \
                     '&appKey=201020412&interfaceCode=122&apiLevel=28' \
                     '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_011_case(self):
        print("----在书架页面，根据书名模糊搜索一本书且能正常阅读的功能----")
        url = host + '/api/search?keywords=patch&timezone=Asia%2FShanghai&userKeyWithoutImei=4e701c7505c' \
                     'e494c7b28be2da07b6f3b&channel=dreameoppo-46&sign=22a643b793dfac47ae5cf0ecbd1b6409' \
                     '&source=3&mcc=460&versionName=1.7.4&kwType=0&deviceId=b1364ddb106b056c' \
                     '&uuid=9f223804-130d-4069-8f94-b9739a85c813&osType=0&appKey=201020412&apiLevel=28' \
                     '&androidId=b1364ddb106b056c&sex=1&count=10&start=1&advertising_id=4cd19094-1fdd-4' \
                     '36a-8f65-d7f3c27f536f&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                     '&s={}&u={}&distinct_id=b1364ddb106b056c&imei=866716038443093' \
                     '&interfaceCode=122&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url1 = host + '/api/bookInfo?bookshelf=vhRlO%2Fp2LPt13fjpOFoo0Q%3D%3D%2CG3yobNQftTHHIdbYESsq' \
                      'CA%3D%3D%2CxLA%2FFpiCfzOV09eVC8QEHg%3D%3D%2CRvdq9VhPzTLkgyHofVE8Pw%3D%3D%2C%2B' \
                      'iEFxZxn8dAqSMaLzMv%2Fjw%3D%3D&timezone=Asia%2FShanghai&userKeyWithoutImei=4e7' \
                      '01c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46&advertising_id=4cd190' \
                      '94-1fdd-436a-8f65-d7f3c27f536f&sign=d42db2457365df5d3e81daa1f6a25dc4&mcc=460' \
                      '&versionName=1.7.4&$referrer=com.dreame.reader.discover.search.activity.Sear' \
                      'chActivity&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                      '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125&s={}&u={}' \
                      '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                      '&id=%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D&interfaceCode=122&apiLevel=28' \
                      '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            t1 = result1.json()
            print(t1)
            self.assertEqual(0, t1["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url2 = host + '/api/readV1?timezone=Asia%2FShanghai&sex=1&userKeyWithoutImei=4e701c7505ce4' \
                      '94c7b28be2da07b6f3b&channel=dreameoppo-46&advertising_id=4cd19094-1fdd-43' \
                      '6a-8f65-d7f3c27f536f&sign=a9234305a20fc94f8373a679996e2941&mcc=460' \
                      '&versionName=1.7.4&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9' \
                      '739a85c813&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                      '&bookId=%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D&s={}&u={}&chapterId=d95odBJm9bJxo5q' \
                      'tm7trwQ%3D%3D&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093' \
                      '&appKey=201020412&interfaceCode=122&apiLevel=28' \
                      '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result2 = self.s.get(url2)
            t2 = result2.json()
            print(t2)
            self.assertEqual(0, t2["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_012_case(self):
        print("----在书架页面，根据作者名模糊搜索其书籍且能查看正常阅读这些书籍的功能----")
        url = host + '/api/search?keywords=Nikii_s&timezone=Asia%2FShanghai&userKeyWithoutImei=4e7' \
                     '01c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46&sign=15770b33ea32a56e78e' \
                     '9b81f483a1b1d&source=3&mcc=460&versionName=1.7.4&kwType=2' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813&osType=0' \
                     '&appKey=201020412&apiLevel=28&androidId=b1364ddb106b056c&sex=1&count=10' \
                     '&start=1&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f&versionCode=125' \
                     '&userKey=b1232786105b6a3c82c0fa447d3946f4&s={}&u={}&distinct_id=b1364ddb106' \
                     'b056c&imei=866716038443093&interfaceCode=122&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url1 = host + '/api/bookInfo?bookshelf=vhRlO%2Fp2LPt13fjpOFoo0Q%3D%3D%2CG3yobNQftTHHIdbYE' \
                      'SsqCA%3D%3D%2CxLA%2FFpiCfzOV09eVC8QEHg%3D%3D%2CRvdq9VhPzTLkgyHofVE8' \
                      'Pw%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D&timezone=Asia%2FShanghai' \
                      '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                      '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                      '&sign=52579f8e4484519f8fbf3df6b47f2b88&mcc=460&versionName=1.7.4' \
                      '&$referrer=com.dreame.reader.discover.search.activity.SearchActivity' \
                      '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                      '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125&s={}&u={}' \
                      '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                      '&id=YLtzLO7fjAV0PuZC3QAogw%3D%3D&interfaceCode=122&apiLevel=28' \
                      '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            t1 = result1.json()
            print(t1)
            self.assertEqual(0, t1["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url2 = host + '/api/readV1?timezone=Asia%2FShanghai&sex=1&userKeyWithoutImei=4e701c7505ce4' \
                      '94c7b28be2da07b6f3b&channel=dreameoppo-46&advertising_id=4cd19094-1fdd-436' \
                      'a-8f65-d7f3c27f536f&sign=6fc3b6971212ea68d233acbf11e13343&mcc=460' \
                      '&versionName=1.7.4&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9' \
                      '739a85c813&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                      '&bookId=YLtzLO7fjAV0PuZC3QAogw%3D%3D&s={}&u={}' \
                      '&chapterId=x0KEwf4SFY8iQTBlLwi%2FKQ%3D%3D&distinct_id=b1364ddb106b056c' \
                      '&osType=0&imei=866716038443093&appKey=201020412&interfaceCode=122' \
                      '&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result2 = self.s.get(url2)
            t2 = result2.json()
            print(t2)
            self.assertEqual(0, t2["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_013_case(self):
        print("----在书架页面，测试直接点击收藏的书会进入到阅读界面的功能----")
        url = host + '/api/readV1?timezone=Asia%2FShanghai&sex=1&userKeyWithoutImei=4e701c7505ce4' \
                     '94c7b28be2da07b6f3b&channel=dreameoppo-46&advertising_id=4cd19094-1fdd-43' \
                     '6a-8f65-d7f3c27f536f&sign=0461690eae250e875fcbec99b7d06ca2&mcc=460' \
                     '&versionName=1.7.4&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b97' \
                     '39a85c813&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                     '&bookId=kCk4XaChah0P1AZHlfhydQ%3D%3D&s={}&u={}' \
                     '&chapterId=TaFpCfviiqibAhIhu3EdVw%3D%3D&distinct_id=b1364ddb106b056c' \
                     '&osType=0&imei=866716038443093&appKey=201020412&interfaceCode=122' \
                     '&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_014_case(self):
        print("----在书架页面，点击右上角的“礼包”，测试能正常跳转到任务管理界面的功能----")
        url = host_www + '/api/getUserTask?u={}&s={}&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                         '&deviceId=b1364ddb106b056c&newUserIndex=0&mcc=460&timezone=Asia%2FShanghai' \
                         '&channel=dreameoppo-46&versionCode=125&versionName=1.7.4&bookshelfCount=1' \
                         '&loginType=16&isAuthor=0&appLanguage=&osType=0&tag=task&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        time.sleep(1)
        url1 = host_www + '/api/getTodayTaskInfo?u={}&s={}&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                          '&deviceId=b1364ddb106b056c&newUserIndex=0&mcc=460&timezone=Asia%2FShanghai' \
                          '&channel=dreameoppo-46&versionCode=125&versionName=1.7.4&bookshelfCount=1' \
                          '&loginType=16&isAuthor=0&appLanguage=&osType=0&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            t1 = result1.json()
            print(t1)
            self.assertEqual(0, t1["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_015_case(self):
        print("----在书架页面，点击右上角的“时刻表”，测试其能正常跳转到可解锁书籍查看界面的功能----")
        url = host + '/calendar/getNewCalendarContent?timezone=Asia%2FShanghai' \
                     '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                     '&sign=2d19e9c35083383302b1c8ed48eb79d9&mcc=460&versionName=1.7.4' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                     '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125&s={}&u={}' \
                     '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                     '&interfaceCode=122&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_016_case(self):
        print("----在书架页面，点击右上角的“会话”按钮，测试其能正常进入到站内信界面的功能----")
        url = host + '/Message/getNewMessage?timezone=Asia%2FShanghai' \
                     '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                     '&sign=511f14f7ab48ce6c2628c8adbefe8c70&type=0&mcc=460&versionName=1.7.4' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                     '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125&s={}&size=10' \
                     '&u={}&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093' \
                     '&appKey=201020412&page=1&interfaceCode=122&apiLevel=28' \
                     '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url1 = host + '/Message/getSepUnreadMessage?timezone=Asia%2FShanghai' \
                      '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                      '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                      '&sign=20a83e4edfd4f239f77dca68478bd902&mcc=460&versionName=1.7.4' \
                      '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                      '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125&s={}&u={}' \
                      '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093' \
                      '&appKey=201020412&interfaceCode=122&apiLevel=28&androidId=b1364ddb106b056c' \
                      '&timestamp=0&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            t1 = result1.json()
            print(t1)
            self.assertEqual(0, t1["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_017_case(self):
        print("----在书架页面，测试取消一本收藏书籍的功能运行正确----")
        url = host + '/apiBookshelf/unfollow?timezone=Asia%2FShanghai&sex=1' \
                     '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                     '&sign=fbd5a247a38419dcc65f9cb6733564ce&mcc=460&versionName=1.7.4' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                     '&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4&s={}&u={}' \
                     '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                     '&bid=kCk4XaChah0P1AZHlfhydQ%3D%3D&interfaceCode=122&apiLevel=28' \
                     '&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_018_case(self):
        print("----在书架页面，测试批量取消多本收藏书籍的功能运行正确----")
        url = host + '/apiBookshelf/batchUnfollow?timezone=Asia%2FShanghai&sex=1' \
                     '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                     '&sign=cbec680f13a57eb945bc6699fee61396&mcc=460&versionName=1.7.4' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                     '&versionCode=125&userKey=b1232786105b6a3c82c0fa447d3946f4&s={}&u={}' \
                     '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                     '&bid=kCk4XaChah0P1AZHlfhydQ%3D%3D%2C%2BiEFxZxn8dAqSMaLzMv%2Fjw%3D%3D' \
                     '&interfaceCode=122&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_019_case(self):
        print("----在“我的”界面，测试点击 Earn Rewards 能正常进入任务管理页面的功能----")
        url = host_www + '/api/getUserTask?u={}&s={}&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                         '&deviceId=b1364ddb106b056c&newUserIndex=0&mcc=460&timezone=Asia%2FShanghai' \
                         '&channel=dreameoppo-46&versionCode=125&versionName=1.7.4&bookshelfCount=1' \
                         '&loginType=16&isAuthor=0&appLanguage=&osType=0&tag=task&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url1 = host_www + '/api/getTodayTaskInfo?u={}&s={}&userKey=b1232786105b6a3c82c0fa447d3946f4' \
                          '&deviceId=b1364ddb106b056c&newUserIndex=0&mcc=460&timezone=Asia%2FShanghai' \
                          '&channel=dreameoppo-46&versionCode=125&versionName=1.7.4&bookshelfCount=1' \
                          '&loginType=16&isAuthor=0&appLanguage=&osType=0&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            t1 = result1.json()
            print(t1)
            self.assertEqual(0, t1["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_020_case(self):
        print("----在“我的”界面，测试点击 inbox 能正常进入到短信及站内信界面的功能----")
        url = host + '/Message/getSepUnreadMessage?timezone=Asia%2FShanghai' \
                     '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                     '&sign=20a83e4edfd4f239f77dca68478bd902&mcc=460&versionName=1.7.4' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                     '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125&s={}&u={}' \
                     '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                     '&interfaceCode=122&apiLevel=28&androidId=b1364ddb106b056c&timestamp=0&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
        print("-----------------------------------------")
        url1 = host + '/Message/getNewMessage?timezone=Asia%2FShanghai' \
                      '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                      '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                      '&sign=51166f17d6e1f881cf2a1bc199c96f20&type=1&mcc=460&versionName=1.7.4' \
                      '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                      '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125&s={}&size=10&u={}' \
                      '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                      '&page=1&interfaceCode=122&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result1 = self.s.get(url1)
            t1 = result1.json()
            pprint(t1)
            self.assertEqual(0, t1["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_021_case(self):
        print("----在“我的”界面，测试点击”Following能正常查看浏览书籍记录的功能----")
        url = host + '/User/getMyFollow?timezone=Asia%2FShanghai' \
                     '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
                     '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
                     '&sign=2d19e9c35083383302b1c8ed48eb79d9&mcc=460&versionName=1.7.4' \
                     '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
                     '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125&s={}&u={}' \
                     '&distinct_id=b1364ddb106b056c&osType=0&imei=866716038443093&appKey=201020412' \
                     '&interfaceCode=122&apiLevel=28&androidId=b1364ddb106b056c&debug=panjian'.format(s, u)
        try:
            result = self.s.get(url)
            t = result.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e


if __name__ == '__main__':
    unittest.main()
