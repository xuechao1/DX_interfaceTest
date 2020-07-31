# -*- coding:utf-8 -*-

import re
import sys
import requests
import warnings
import unittest
import pytest
from pprint import pprint
from config.http_req import Http_Req
from config import readConfig

read_conf = readConfig.ReadConfig()
sys.path.append("D:\\PycharmProjects\\DX_interfaceTest")
host = 'http://3.85.16.233:32100'
host_www = 'http://activity.dreame.com/'


class TestDreame(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.s = requests.session()
        print("----开始执行测试用例  start ----")
        global userKeyWithoutImei
        userKeyWithoutImei = read_conf.get_login_dreame('userKeyWithoutImei')
        global channel
        channel = read_conf.get_login_dreame('channel')
        global sign
        sign = read_conf.get_login_dreame('sign')
        global mcc
        mcc = read_conf.get_login_dreame('mcc')
        global versionName
        versionName = read_conf.get_login_dreame('versionName')
        global deviceId
        deviceId = read_conf.get_login_dreame('deviceId')
        global versionCode
        versionCode = read_conf.get_login_dreame('versionCode')
        global osType
        osType = read_conf.get_login_dreame('osType')
        global imei
        imei = read_conf.get_login_dreame('imei')
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
        global userKey
        userKey = read_conf.get_login_dreame('userKey')
        global appTag
        appTag = read_conf.get_login_dreame('appTag')
        global originProduct
        originProduct = read_conf.get_login_dreame('originProduct')
        global uuid
        uuid = read_conf.get_login_dreame('uuid')
        global appLanguage
        appLanguage = "en"
        global code
        code = read_conf.get_login_dreame('code')

    def test_000_0_visitor_login(self):
        channel = "ringdomapp-78"
        sign = "3bc0d79ef6498669da353b248c2afd0c"
        """
        ---测试游客用户能正常登录APP的功能----
        :return:
        """
        pprint("----测试游客用户能正常登录APP的功能----")
        url = "/api/visitorLogin?deviceId={}&appKey={}&versionCode={}&uuid={}&" \
              "appLanguage={}&interfaceCode={}&code={}&androidId={}&originProduct={}&imei={}&" \
              "distinct_id={}&appTag={}&mcc={}&channel={}&apiLevel={}&userKey={}&" \
              "advertising_id={}&sign={}&userKeyWithoutImei={}&" \
              "timezone={}&versionName={}&oid={}&osType={}&login_type={}" \
            .format(deviceId, appKey, versionCode, uuid, appLanguage, interfaceCode,
                    code, androidId, originProduct, imei, distinct_id,
                    appTag, mcc, channel, apiLevel, userKey, advertising_id,
                    sign, userKeyWithoutImei, timezone, versionName, oid,
                    osType, login_type)
        Http_Req().http_req(url)

    # @pytest.fixture()
    def pytest_http_req(self, url):
        self.s = requests.session()
        url_0 = host + url
        try:
            result_0 = str(self.s.get(url_0))
            data = re.findall(r"\d+", result_0) # 使用正则过滤  接口返回码
            code = data[0]
            if code != 500:
                result_1 = self.s.get(url_0)
                t = result_1.json()
                print(t)
                self.assertEqual(0, t["status"], msg="Fail Detail")
            else:
                print("!!!Warning!!! HTTP请求失败 : 500 错误")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def test_001_visitor_login(self):
        channel = "ringdomapp-78"
        sign = "3bc0d79ef6498669da353b248c2afd0c"
        """
        ---测试游客用户能正常登录APP的功能----
        :return:
        """
        pprint("----测试游客用户能正常登录APP的功能----")
        url = "/api/visitorLogin?deviceId={}&appKey={}&versionCode={}&uuid={}&" \
              "appLanguage={}&interfaceCode={}&code={}&androidId={}&originProduct={}&imei={}&" \
              "distinct_id={}&appTag={}&mcc={}&channel={}&apiLevel={}&userKey={}&" \
              "advertising_id={}&sign={}&userKeyWithoutImei={}&" \
              "timezone={}&versionName={}&oid={}&osType={}&login_type={}" \
            .format(deviceId, appKey, versionCode, uuid, appLanguage, interfaceCode,
                    code, androidId, originProduct, imei, distinct_id,
                    appTag, mcc, channel, apiLevel, userKey, advertising_id,
                    sign, userKeyWithoutImei, timezone, versionName, oid,
                    osType, login_type)
        self.pytest_http_req(url)


if __name__ == '__main__':
    unittest.main()
