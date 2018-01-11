# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午7:40
# Email: leiyong711@163.com
import unittest
from time import sleep

from wheel.signatures import assertTrue
from Business.authCode import msm
from Handle.positioning import Element

el = Element()


class Case(unittest.TestCase):
    """登录"""
    driver = el.driver

    def guidePage(self):
        u"""首次打开app引导页"""
        # el.localizeName('允许').click()
        # el.localizeName('允许').click()
        # el.localizeName('允许').click()
        # el.localizeName('允许').click()
        # el.localizeName('允许').click()
        sleep(5)
        el.swipeLeft(100)
        el.swipeLeft(100)
        el.swipeLeft(100)
        el.touch(x=492, y=1618)

    def testCase_001(self):
        u"""手机号登录用例"""
        # el.sony()
        el.stime(5)
        sleep(4)
        # el.LocalizeDesc('login-1').click()
        el.tap([(550, 765)], 200)
        el.stime(5)
        el.LocalizeDesc('请输入您的手机号').send_keys('18900000000')
        # el.LocalizeDesc('获取验证码').click()
        el.baidu()
        sleep(1)
        # el.LocalizeDesc('验证码').send_keys(msm())
        el.LocalizeDesc('验证码').send_keys(5555)
        el.LocalizeDesc('login-title').click()
        el.LocalizeDesc('登录').click()
        el.stime(10)
        assertTrue(el.toCompareDesc('任务推荐'))

    def testCase_002(self):
        u"""关闭红包"""
        # el.sony()
        el.stime(5)
        el.tap([(548, 1310)], 200)
        sleep(2)
        el.tap([(547, 1323)], 200)


    def exit(self):
        """退出登录"""
        el.LocalizeDesc('我的').click()
        el.LocalizeDesc('my-set').click()
        el.LocalizeDesc('退出登录').click()

    def weixin(self):
        el.LocalizeDesc('login-2')