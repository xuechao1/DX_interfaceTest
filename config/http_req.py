#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import unittest

host = 'http://3.85.16.233:32100'
host_www = 'http://activity.dreame.com/'
sys.path.append("D:\\PycharmProjects\\DX_interfaceTest")


class Http_Req(unittest.TestCase):

    def http_req(self, url):
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
