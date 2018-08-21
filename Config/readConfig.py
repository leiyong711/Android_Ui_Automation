# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong"
# creation time: 2018/1/25 0025 14:46
# Email: leiyong711@163.com


import ConfigParser
import os


# 获取config配置文件
def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/app.conf'
    config.read(path)
    return config.get(section, key)


if __name__ == '__main__':
    print getConfig("baseconf", "applicationName")
    print getConfig("baseconf", "fileSize")
    print getConfig("baseconf", "applicationVersion")
    print getConfig("baseconf", "appPackage")
    print getConfig("baseconf", "appActivity")
    print '-'*100
    print getConfig("phoneConf", "brand")
    print getConfig("phoneConf", "model")
    print getConfig("phoneConf", "systemVersion")
    print getConfig("phoneConf", "deviceId")
    print getConfig("phoneConf", "men")
    print getConfig("phoneConf", "cpu")
    print getConfig("phoneConf", "appPix")