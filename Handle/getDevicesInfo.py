# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午6:35
# Email: leiyong711@163.com

import os
import re


def getDevices():

    # 获取手机信息
    def Info():

        # 手机信息正则限制
        def modified(name):
            try:
                reu = list(os.popen(name).readlines())
                return re.findall('.*', reu[0])[0]  # ([^\s\\\]+)
            except:
                return 'Get error'
        brand = modified('adb shell getprop ro.product.brand')                       # 读取手机品牌
        phone_models = modified('adb shell getprop ro.semc.product.name')            # 读取设备型号
        deviceVersion = modified('adb shell getprop ro.build.version.release')       # 读取设备系统版本号
        readDeviceId = list(os.popen('adb devices').readlines())                     # 读取设备 id
        devices = str(readDeviceId[1])[:-8]                                          # 正则表达式匹配出 id 信息
        # devices = re.findall(r'^\w*\b', readDeviceId[1])[0]                         # 正则表达式匹配出 id 信息
        # if phone_models == '':
        #     phone_models = u'获取失败'
        if not devices:
            devices = 'Get error'
        return brand, phone_models, deviceVersion, devices      # 返回品牌、型号、系统版本、设备id

    # 得到运行内存
    def men(devices):
        cmd = "adb -s "+devices+ " shell cat /proc/meminfo"
        get_cmd = os.popen(cmd).readlines()
        men_total = 0
        men_total_str = "MemTotal"
        for line in get_cmd:
            if line.find(men_total_str) >= 0:
                men_total = line[len(men_total_str) +1:].replace("kB", "").strip()
                break
        ram = int(men_total) / 1024
        return str(ram) + "MB"

    # 得到CPU核心数
    def cpu(devices):
        cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
        get_cmd = os.popen(cmd).readlines()
        find_str = "processor"
        int_cpu = 0
        for line in get_cmd:
            if line.find(find_str) >= 0:
                int_cpu += 1
        return str(int_cpu) + "核"

    # 得到手机分辨率
    def appPix(devices):
        try:
            result = os.popen("adb -s %s shell wm size" % devices, "r")
            return result.readline().split("Physical size:")[1]
        except:
            return 'Get error'

    # 获取电量
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
                return u'获取电量失败'
        return 'Get error'

    startPower = batteryCapacity()
    brand, model, systemVersion, deviceId = Info()  # 返回品牌、型号、系统版本、设备id
    men = men(deviceId)
    cpu = cpu(deviceId)
    appPix = appPix(deviceId)
    x = ["brand = %s\nmodel = %s\nplatformName = Android\nsystemVersion = %s\ndeviceId = %s\nmen = %s\ncpu = %s\nappPix = %s\nstartPower = %s\n"
         % (brand, model, systemVersion, deviceId, men, cpu, appPix, startPower)]
    with open("../config/app.conf", "a") as f:  # 写出应用配置信息
        f.write("\n[phoneConf]\n")
        for i in x:
            f.write(i)
            # 获取启动类


if __name__ == '__main__':
    getDevices()
