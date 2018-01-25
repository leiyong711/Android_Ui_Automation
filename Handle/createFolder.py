# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/25 0025 14:46
# Email: leiyong711@163.com
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong"
# creation time: 2018/1/25 0025 14:15
# Email: leiyong711@163.com
import os
import time


def createFolder(folderPath0, folderPath1):
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    a = os.path.exists(folderPath0 + timestr[:10] + '\\' + timestr[11:] + folderPath1)
    if not a:
        os.makedirs(folderPath0 + timestr[:10] + '\\' + timestr[11:] + folderPath1)

