#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
import unittest
import pytest
from pprint import pprint
from config import readConfig

read_conf = readConfig.ReadConfig()

host = read_conf.get_http_url('host')
host_www = read_conf.get_http_url('host_www')
host_comment = read_conf.get_http_url('host_comment')
host_lite = read_conf.get_http_url('host_lite')
host_lite_activity = read_conf.get_http_url('host_lite_activity')


class Http_Req(unittest.TestCase):

    @pytest.mark.skip
    def http_old_req(self, url):
        self.s = requests.session()
        url_0 = host + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def http_req(self, url):
        self.s = requests.session()
        url_0 = host + url
        try:
            result_0 = str(self.s.get(url_0))
            data = re.findall(r"\d+", result_0)  # 使用正则过滤  接口返回码
            code = data[0]
            if code != 500:
                result_1 = self.s.get(url_0)
                t = result_1.json()
                self.assertEqual(0, t["status"], msg="Fail Detail")
            else:
                print("!!!Warning!!! HTTP请求失败 : 500 错误")
                print(result_0)
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def http_req_www(self, url):
        self.s = requests.session()
        url_0 = host_www + url
        try:
            result_0 = self.s.get(url_0)
            t = result_0.json()
            print(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def http_email_req(self, url):
        self.s = requests.session()
        url1 = host + url
        try:
            result = self.s.get(url1)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def http_email_comment_req(self, url):
        self.s = requests.session()
        url1 = host_comment + url
        try:
            result = self.s.get(url1)
            t = result.json()
            pprint(t)
            self.assertEqual(0, t["status"], msg="Fail Detail")
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def http_lite_req(self, url):
        self.s = requests.session()
        url_0 = host_lite + url
        try:
            result_0 = str(self.s.get(url_0))
            data = re.findall(r"\d+", result_0)  # 使用正则过滤  接口返回码
            code = data[0]
            if code != 500:
                result_1 = self.s.get(url_0)
                t = result_1.json()
                print("t:", t)
                self.assertEqual(0, t["status"], msg="Fail Detail")
            else:
                print("!!!Warning!!! HTTP请求失败 : 500 错误")
                print(result_0)
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e

    def http_lite_activity_req(self, url):
        self.s = requests.session()
        url_0 = host_lite_activity + url
        try:
            result_0 = str(self.s.get(url_0))
            data = re.findall(r"\d+", result_0)  # 使用正则过滤  接口返回码
            code = data[0]
            if code != 500:
                result_1 = self.s.get(url_0)
                t = result_1.json()
                print("t:", t)
                self.assertEqual(0, t["status"], msg="Fail Detail")
            else:
                print("!!!Warning!!! HTTP请求失败 : 500 错误")
                print(result_0)
        except Exception as e:
            print("!!!Warning!!! HTTP请求失败 :%s" % e)
            raise e
