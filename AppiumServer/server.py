# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午6:33
# Email: leiyong711@163.com

import ConfigParser
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from Handle.getAppInfo import getApp
from Handle.getDevicesInfo import getDevices

# 自动获取App与测试设备信息
getApp()
getDevices()



# 获取config配置文件
def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    path = '../Config/app.conf'
    config.read(path)
    return config.get(section, key)


# 启动appium服务
class server:

    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = getConfig("phoneConf", "platformName")
        desired_caps['platformVersion'] = getConfig("phoneConf", "systemVersion")
        desired_caps['deviceName'] = getConfig("phoneConf", "deviceId")
        desired_caps['appPackage'] = getConfig("baseconf", "appPackage")
        desired_caps['appActivity'] = getConfig("baseconf", "appActivity")
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def get_driver(self):
        return self.driver


if __name__ == '__main__':
    print getConfig("baseconf", "applicationName")
    print getConfig("baseconf", "fileSize")
    print getConfig("baseconf", "applicationVersion")
    print getConfig("baseconf", "appPackage")
    print getConfig("baseconf", "appActivity")

    print '-'*100
    print getConfig("phoneConf", "brand")
    print getConfig("phoneConf", "model")
    print getConfig("phoneConf", "deviceId")
    print getConfig("phoneConf", "systemVersion")
    print getConfig("phoneConf", "men")
    print getConfig("phoneConf", "cpu")
    print getConfig("phoneConf", "appPix")
    print getConfig("phoneConf", "startPower")

