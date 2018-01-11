# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午6:35
# Email: leiyong711@163.com

import re
import os
import platform

appLocation = ''


class getApp:

    fileNames = os.listdir('../apps')
    for i in range(len(fileNames)):
        num = re.search(r'\.apk$', fileNames[i])
        if num:
            global appLocation
            appLocation = num.string

    def ApkInfo(search):
        if platform.system() == "Windows":
            t = os.popen('cd').read()
            key = '%s: &cd %s &aapt dump badging %s/apps/%s' % (t[0], t[2:].strip(), t[:-5].strip(), appLocation)

        elif platform.system() == "Darwin":
            key = 'cd %s/run/ &aapt dump badging %s/apps/%s' % (os.popen('pwd').read()[:-5], os.popen('pwd').read()[:-5], appLocation)

        aapt = list(os.popen(key).readlines())

        for i in range(0, len(aapt)):           # 遍历列表
            a = str(aapt[i])                    # 列表转字符串
            sStr2 = search                      # 要查询的字符串
            p = a.find(sStr2)                   # 判断字符串是否存在，不存在赋值-1
            if p != -1:
                result = aapt[i].split(search)[1:]           # 获取查询参数在列表中的索引截取参数值
                if search == 'launchable-activity: name=':   # 判断是否查询包名
                    result = result[0].split("label=")[:1]   # 如果是查询启动类就截取“label”前的值
                elif search == 'package: name=':               # 判断是否查询包名
                    result = result[0].split("versionCode=")[:1]            # 如果是查询包名就截取“versionCode=”前的值
                elif search == 'versionName=':
                    # print(re.search(r'\-*\d+(?:\.\d+)?', result))
                    result = re.findall(r'[0-9]\d*\.\d*|\.\d*[0-9]|[0-9]\d*', result[0])

                App_Information = "".join(result).strip('\n').strip("'")    # 去掉字符串中的换行与'号
                return App_Information.strip().lstrip().rstrip("'")         # 去空格及特殊符号并返回查询结果

    '''
    获取应用名、版本信息、包名、启动类
    '''
    applicationName = ApkInfo('application-label:')
    applicationVersion = ApkInfo('versionName=')
    appPackage = ApkInfo('package: name=')
    appActivity = ApkInfo('launchable-activity: name=')

    size = os.path.getsize('../apps/%s' % appLocation)  # 获取应用程序大小
    fileSize = round(size / 1024 / 1024.0, 2)  # 转大小单位
    fileSize = str(fileSize) + 'MB'

    x = ["applicationName = %s\nfileSize = %s\napplicationVersion = %s\nappPackage = %s\nappActivity = %s\n"
         % (applicationName, fileSize, applicationVersion, appPackage, appActivity)]

    with open("../config/app.conf", "w+") as f:  # 写出应用配置信息
        f.write("[baseconf]\n")
        for i in x:
            f.write(i)
            # 获取启动类

if __name__ == '__main__':
    getApp()
