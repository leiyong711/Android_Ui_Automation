# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午6:34
# Email: leiyong711@163.com

import datetime
import os
import time
import xlwt
from config import readConfig
from Handle.createFolder import createFolder
import platform

start = 0


# noinspection PyGlobalUndefined
def start(name):
    global start
    start = name
    print '计时开始时间：%s' % start


def Excel(caseResult):
    # 获取信息配置表
    arr = ["手机品牌", "手机型号", "系统版本", "CPU核心数", "运行内存大小", "手机分辨率", "测试期间耗电"]
    # 品牌、型号、系统版本、CPU核心数、运行内存、手机分辨率
    arr2 = [readConfig.getConfig("phoneConf", "brand"), readConfig.getConfig("phoneConf", "model"),
            readConfig.getConfig("phoneConf", "systemVersion"), readConfig.getConfig("phoneConf", "cpu"),
            readConfig.getConfig("phoneConf", "men"), readConfig.getConfig("phoneConf", "appPix")]
    startBc = int(readConfig.getConfig("phoneConf", "startPower"))

    def batteryCapacity():
        get_cmd = os.popen("adb shell dumpsys battery").readlines()
        for i in range(0, len(get_cmd)):
            a = str(get_cmd[i])
            b = 'level'
            p = a.find(b)
            try:
                if p != -1:
                    s = get_cmd[i].split('level')
                    Battery = "".join(s).strip('\n').strip("'").strip('  : ')
                    return int(Battery)
            except:
                return '获取电量失败'

    # 获取配置信息
    applicationName = readConfig.getConfig("baseconf", "applicationName")  # 获取应用名
    applicationVersion = readConfig.getConfig("baseconf", "applicationVersion")  # 获取应用版本信息
    fileSize = readConfig.getConfig("baseconf", "fileSize")  # 获取app文件大小

    # excel样式
    def set_style(name, height, bold):
        u'字体，高度，背景色，加粗，字体色'
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font

        alignment = xlwt.Alignment()  # Create Alignment
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
        alignment.vert = xlwt.Alignment.VERT_CENTER
        style.alignment = alignment
        return style

    def s_style(name, height, lei, bold, s):
        u'字体，高度，背景色'
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.colour_index = s  # 设置其字体颜色
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        alignment = xlwt.Alignment()  # Create Alignment
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
        alignment.vert = xlwt.Alignment.VERT_CENTER
        style.alignment = alignment
        pattern = xlwt.Pattern()  # Create the Pattern
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern.pattern_fore_colour = lei
        style.pattern = pattern  # Add Pattern to Style创建模式
        return style

    w = xlwt.Workbook()  # 创建一个工作簿
    ws = w.add_sheet('Hey, Hades')  # 创建一个工作表

    # 合并单元格
    ws.write_merge(0, 0, 0, 4, u'测试报告总概况', set_style(u'宋体', 360, True))  # 合并行单元格
    ws.write_merge(1, 1, 0, 4, u'测试概况', s_style(u'宋体', 270, 4, False, 0x01))  # 合并行单元格
    ws.write_merge(8, 8, 0, 6, u'测试手机详情', s_style(u'宋体', 270, 4, False, 0x01))  # 合并行单元格

    alignment = xlwt.Alignment()  # Create Alignment
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER  # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    style = xlwt.XFStyle()  # Create Style
    style.alignment = alignment  # Add Alignment to Style

    end = datetime.datetime.now()
    print '计时结束时间：%s' % end
    timeConsuming = str(end - start)[:-7]  # 用测试结束时间-开始时间得到测试耗时，再把时间转成字符串并去掉小数部分
    print '测试耗时：%s' % timeConsuming

    endBc = batteryCapacity()
    bC = str(startBc - endBc) + '%'
    arr2.append(bC)
    dk = u'%s + Appium:%s + Python:%s' % (platform.platform(),
                                          os.popen('appium -v').readlines()[0].split('\n')[0],
                                          platform.python_version())

    app1 = ["APP名称", applicationName, "用例总数", caseResult[0], "测试环境"]
    app2 = ["APP大小", fileSize, "通过总数", caseResult[1]]
    app3 = ["APP版本", applicationVersion, "失败总数", str(int(caseResult[2]) + int(caseResult[3]))]
    app4 = ["测试日期", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), "测试耗时", timeConsuming + "秒"]
    ws.write_merge(3, 5, 4, 4, dk, set_style(u'宋体', 270, False))  # 合并行单元格
    for i in range(0, len(app1)):
        # print app1[i]
        ws.write(2, i, app1[i].decode('utf-8'), set_style(u'宋体', 270, False))
    for i in range(0, len(app2)):
        ws.write(3, i, app2[i].decode('utf-8'), set_style(u'宋体', 270, False))
    for i in range(0, len(app3)):
        ws.write(4, i, app3[i].decode('utf-8'), set_style(u'宋体', 270, False))
    for i in range(0, len(app4)):
        ws.write(5, i, app4[i].decode('utf-8'), set_style(u'宋体', 270, False))

    for i in range(0, len(arr)):  # 写入第一行arr的内容
        ws.write(9, i, arr[i].decode('utf-8'), set_style(u'宋体', 270, False))
    for i in range(0, len(arr2)):  # 写入第二行arr2的内容
        ws.write(10, i, arr2[i].decode('utf-8'), set_style(u'宋体', 270, False))

    createFolder('../Report/', '/log')  # 判断文件夹是否存在，不存在则创建
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    path = '../Report/%s/%s/log/%s_%s.xls' \
           % (timestr[:10], timestr[11:], arr2[0].strip("\r"), arr2[1].strip("\r").replace(' ', '_'))
    w.save(path.decode('utf-8'))  # 以“品牌_机型”命名保存

    print '导出结束'
