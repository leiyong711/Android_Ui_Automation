# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午6:35
# Email: leiyong711@163.com

import time
import sys
import os
from time import sleep
from AppiumServer.server import server
A = server()

reload(sys)
sys.setdefaultencoding('utf8')
co = 1  # 截图序号初始化


# 元素定位&操作
class Element:

    def __init__(self):
        self.driver = A.get_driver()

    # 相对坐标路径元素定位点击（兼容不同分辨率机型）
    def tap(self, coordinate, t):
        li = []
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        test_x = 1080
        test_y = 1920
        li.append((int((float(coordinate[0][0]) / test_x) * x), int((float(coordinate[0][1]) /test_y) * y)))
        self.driver.tap(li, t)

    # content-desc定位元素
    def LocalizeDesc(self, id):
        return self.driver.find_element_by_accessibility_id(id)

    # id定位元素
    def localizeId(self, id):
        return self.driver.find_element_by_id(id)

    # name定位元素
    def localizeName(self, name):
        return self.driver.find_element_by_name(name)

    # xpath定位元素
    def localizeXpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # 获取元素的文本值
    def gainText(self, text):
        return self.driver.find_element_by_id(text).text

    # 获取屏幕宽和高
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 从右向左滑动
    def swipeLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 从左向右滑动
    def swipeRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 从下向上滑动
    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 从上向下滑动
    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    # # 查找元素，没找到就滑动
    # def findLocal(self, name):
    #     x = 1
    #     while x == 1:
    #         if self.fact(name) ==1:
    #             self.swipeUp(10)
    #             time.sleep(2)
    #             self.fact(name)
    #         else:
    #             print '找到了'
    #             x = 2

    # 查找元素，没找到就滑动
    # def findLocal(self, name):
    #     x = 1
    #     num = 1
    #     while x == 1:
    #         try:
    #             global num
    #             num = self.driver.find_element_by_accessibility_id(name)
    #             break
    #         except:
    #             num = 1
    #         if num == 1:
    #             self.swipeUp(1000)
            # else:
            #     print '找到了'
            #     x = 2

    def findLocal(self, name):
        # x = 1
        # while x == 1:
        #     try:
        #         global num
        #         num = self.driver.find_element_by_accessibility_id(name)
        #     except:
        #         num = 1
        #     if num == 1:
        #         self.swipeUp(1000)
        #     time.sleep(1)
        flag = True
        while flag:

            elelist = self.driver.find_elements_by_accessibility_id(name)
            if len(elelist) == 0:
                print "当前屏幕没有这个元素"
                self.swipeUp()
            elif len(elelist) == 1:
                elelist[0].click()
                flag = False
                break
            else:
                for i in range(0, len(elelist)):
                    if elelist[i].text == name:
                        elelist[i].click()
                        flag = False
                        break
                    else:
                        print "整个屏幕都没有找到这个元素"

    # 判断输入结果与实际结果
    def Compare_the_text(self, id, expected):
        actual = self.driver.find_element_by_xpath(id).text  # "获取实际输入验证码"
        if expected == actual:
            return True
        else:
            return False

    # 比较元素
    def to_compareName(self, name):
        try:
            element = self.driver.find_element_by_name(name)
            return element.is_enabled()
        except:
            return False

    # content - desc比较元素
    def toCompareDesc(self, name):
        try:
            return self.driver.find_element_by_accessibility_id(name).is_displayed()
        except:
            return False

    # 报错并截图
    def Error_screenshot(self):
        global co
        cou = str(co)
        ti = time.strftime('%Y%m%d', time.localtime(time.time()))
        timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))

        createFolder('../report/','/er_img')
        path = ('../report/%s/%s/er_img/%s_%s.jpg') % (str(timestr[:10]), str(timestr[11:]), str(ti), str(cou))

        #Create_folder('..\\The_report\\', '\\er_img')   # 判断文件夹是否存在，不存在则创建
        self.driver.get_screenshot_as_file(path)
        co += 1
        print u'截图完毕'
        # print '失败请到..\\jpg\\%s\\%s\\er_img\\目录下查看“%s”错误截图' % (timestr[:10], timestr[11:], ti)

    # 关闭程序
    def quit(self):
        self.driver.quit()

    # 方法运行时间
    def timeMe(self, fn):
        def _wrapper(*args, **kwargs):
            start = time.clock()
            fn(*args, **kwargs)
            print "%s cost %s second" % (fn.__name__, time.clock() - start)
        return _wrapper

    # 隐示等待
    def stime(self, ti):
        self.driver.implicitly_wait(ti)

    # 切换'appium'输入法      查询输入法（ime list -s）
    def baidu(self):
        os.popen('adb shell "ime set com.baidu.input/.ImeService"')

    # 切换'xperia'国际输入法
    def sony(self):
        # 索尼国际输入法
        os.popen('adb shell "ime set com.sonyericsson.textinput.uxp/.glue.InputMethodServiceGlue"')
        # 夜神模拟器
        # os.'popen'('adb shell "ime set com.example.android.softkeyboard/.SoftKeyboard"')
        # 逍遥模拟器
        # os.popen('adb shell "ime set com.microvirt.memuime /.MemuIME"')

    # 隐示等待
    def wait(self, t):
        self.driver.implicitly_wait(t)

    def touch(self, e=None, x=None, y=None):
        """
        触摸事件
        usage: touch(e), touch(x=0.5,y=0.5)
        """
        width, high = self.get_screen_resolution()
        if (e is not None):
            x = e[0]
            y = e[1]
        if (0 < x < 1):
            x = x * width
        if (0 < y < 1):
            y = y * high

        self.shell("input tap %s %s" % (str(x), str(y)))
        sleep(0.5)

    def kk(self,name):
        self.assertTrue(self.driver.find_element_by_name(name))


if __name__ == '__main__':
    Element.touch()
