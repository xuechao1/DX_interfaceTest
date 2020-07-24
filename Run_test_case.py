# -*- coding:utf-8 -*-
#！/bin/bash

import time
import unittest
from common.configEmail import *
from HTMLTestRunner import HTMLTestRunner  # 把html的py文件导入到lib文件夹下
from testCase import TestInnovel
from testCase import TestDreame
from testCase import TestEmailDreame


class Run_case(object):

    def run(self):
        now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前系统的时间，生成字符串
        path = "python_api_report_" + now + ".html"
        suite = unittest.TestSuite()  # 创建用例搜集容器
        ts = unittest.TestLoader()  # 创建用例加载器
        # 从模块中加载，加载test开头的用例
        suite.addTests(ts.loadTestsFromModule(TestDreame))  # 传入模块名--APP游客登录测试脚本名
        suite.addTests(ts.loadTestsFromModule(TestEmailDreame))  # APP邮件登录测试脚本名
        suite.addTests(ts.loadTestsFromModule(TestInnovel))
        """
        执行用例，
        生成用例执行器
        """
        # 生成测试报告，文件类型为HTML，写入的方式是wb+，以流的方式写入
        with open(path, "wb+") as f:
            # # verbosity = 2，只有1和2的值，2    展示的信息更全面一点，如果代码出错，也有错误信息
            runner = HTMLTestRunner(stream=f, verbosity=2, title="html_api_测试报告")
            runner.run(suite)  # 传参，集合suite
        time.sleep(1)
        # 生成文件到指定路径
        os.popen("move D:\\PycharmProjects\\DX_interfaceTest\\*.html D:\\PycharmProjects\\DX_interfaceTest\\result")
        # 执行邮件脚本
        os.system("python D:\\PycharmProjects\\DX_interfaceTest\\common\\configEmail.py")


if __name__ == '__main__':
    Run_case().run()
