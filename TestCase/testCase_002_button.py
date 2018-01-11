# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午7:41
# Email: leiyong711@163.com
import unittest
from time import sleep
import xlrd
from Handle.positioning import Element
from wheel.signatures import assertTrue

el = Element()


class button(unittest.TestCase):
    """（新用户状态）【页面按钮】--【认证页】"""
    driver = el.driver

    def helperQuit(self):
        """找帮手退出"""
        sleep(2)
        el.LocalizeDesc('与TA聊聊').click()
        sleep(2)
        el.localizeId('android:id/button1').click()
        el.stime(2)
        assertTrue(el.toCompareDesc(u'个人认证'))
        el.stime(2)
        el.LocalizeDesc('worker-back').click()
        el.stime(2)
        el.LocalizeDesc('worker-back').click()
        el.stime(2)
        el.localizeXpath('//android.view.View[@content-desc=\"\"]').click()
        el.stime(2)
        assertTrue(el.toCompareDesc('首页'))
        # el.toCompareDesc(u'首页22')

    def testCase_001(self):
        """【找帮手】--【公司】--【与TA聊聊】--【认证页】"""

        # el.LocalizeDesc('首页').click()

        sleep(8)
        el.LocalizeDesc('找帮手').click()
        sleep(3)
        el.tap([(453, 132)], 100)
        sleep(2)
        el.LocalizeDesc('worker-eyes').click()
        self.helperQuit()

    def testCase_002(self):
        """【找帮手】--【个人】--【与TA聊聊】--【认证页】"""
        # el.LocalizeDesc('首页').click()
        sleep(2)
        el.LocalizeDesc('找帮手').click()
        sleep(2)
        el.tap([(650, 132)], 100)
        el.stime(8)
        sleep(2)
        # el.findLocal('马晓勇')
        el.LocalizeDesc('worker-eyes').click()
        self.helperQuit()

    def testCase_003(self):
        """【找任务】--【发布任务】--【认证页】"""
        sleep(2)
        el.LocalizeDesc(u'找任务').click()
        sleep(2)
        el.tap([(950, 133)], 200)
        sleep(2)
        el.localizeId('android:id/button1').click()
        sleep(2)
        assertTrue(el.toCompareDesc('个人认证'))
        sleep(2)
        el.LocalizeDesc('worker-back').click()
        sleep(2)
        el.tap([(70, 150)], 200)
        sleep(2)
        assertTrue(el.toCompareDesc('首页'))

    def addPublic(self):
        sleep(2)
        assertTrue(el.toCompareDesc('个人认证'))
        sleep(2)
        el.LocalizeDesc('worker-back').click()
        sleep(2)
        el.LocalizeDesc('foot-add').click()
        sleep(2)
        assertTrue(el.toCompareDesc('首页'))

    def testCase_004(self):
        """【+】--【去认证】--【认证页】"""
        sleep(2)
        # el.LocalizeDesc('tab-menu').click()
        el.tap([(567, 1820)], 200)
        sleep(2)
        el.LocalizeDesc('home-team2').click()
        self.addPublic()

    def testCase_005(self):
        """【+】--【发布任务】--【认证页】"""
        sleep(2)
        el.tap([(567, 1820)], 200)
        sleep(2)
        el.LocalizeDesc('home-task2').click()
        sleep(2)
        el.localizeId('android:id/button1').click()
        self.addPublic()

    def testCase_006(self):
        """【我的】--【编辑】--【认证页】"""
        sleep(1)
        el.LocalizeDesc('我的').click()
        sleep(2)
        el.LocalizeDesc('建筑美好未来').click()
        sleep(2)
        assertTrue(el.toCompareDesc('个人认证'))
        sleep(2)
        el.LocalizeDesc('worker-back').click()
        sleep(2)
        assertTrue(el.toCompareDesc('首页'))

    def testCase_007(self):
        """【我的】--【>】--【认证页】"""
        sleep(1)
        el.LocalizeDesc('我的').click()
        sleep(2)
        el.LocalizeDesc('my-row').click()
        sleep(2)
        assertTrue(el.toCompareDesc('个人认证'))
        sleep(2)
        el.LocalizeDesc('worker-back').click()
        sleep(2)
        assertTrue(el.toCompareDesc('首页'))

