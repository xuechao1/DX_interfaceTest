#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/7/28 7:53'

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# appium-python-client  客户端脚本
import pytest
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

"""
改造1：pytest
"""


class TestWeChat:

    # def setup(self):
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
        caps['settings[waitForIdleTimeout]'] = 0
        # 与server 建立连接,初始化一个driver 创建session,返回一个sessionid
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    @pytest.mark.skip
    def test_01_daka(self):
        """打卡功能
        """
        # 步骤1：点击工作台
        el1 = self.driver.find_element(MobileBy.XPATH,
                                       "//*[@text='工作台']")
        el1.click()
        # 滚动查找 "打卡" 元素
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("打卡").instance(0));').click()
        # el3 = self.driver.find_element_by_id("com.tencent.wework:id/gcx")
        # 点击"外出打卡"
        el3 = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/h58")
        el3.click()
        # 点击 第N次外出打卡
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        # 验证打卡成功
        result = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/o_").text
        assert '打卡成功' in result

    def test_02_del_man(self):
        """
        删除账号
        """
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'通讯录')]").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hi7").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'云潇潇')]").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e8u").click()  # 删除按钮
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ber").click()  # 确认按钮

    # @pytest.mark.parametrize("name,tel_num", [("云潇", "15915766618"), ("潇潇", "15915766617"), ("潇潇云", "15915766620")])
    # def test_03_add_man(self, name, tel_num):
    #     """
    #     添加成员
    #     """
    #     self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '通讯录')]").click()
    #     time.sleep(0.7)
    #     self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成员')]").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手动输入添加')]").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'必填')]").send_keys(name)
    #     self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机号')]").send_keys(tel_num)
    #     self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'设置部门')]").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hi9").click()  # 保存按钮
    #     time.sleep(1.5)
    #     self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hhr").click()
    #     time.sleep(0.5)
    #     result = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'人未加入')]").text
    #     assert '人未加入' in result

    # def teardown(self):

    def test_03_add_man(self):
        """
        添加成员
        """
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '通讯录')]").click()
        time.sleep(0.7)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成员')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手动输入添加')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'必填')]").send_keys("云潇潇")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机号')]").send_keys("15915766618")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'设置部门')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hi9").click()  # 保存按钮
        time.sleep(1.5)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hhr").click()
        time.sleep(0.5)
        result = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'人未加入')]").text
        assert '人未加入' in result

    def teardown_class(self):
        # 消毁session
        self.driver.quit()
