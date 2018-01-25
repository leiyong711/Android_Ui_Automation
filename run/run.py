# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午6:32
# Email: leiyong711@163.com

import HTMLTestRunnertest
from Business.email import mail
from Handle.createFolder import createFolder
from Business.testSummary import Excel
from TestCase.testCase_001_login import *

if __name__ == '__main__':
    # 单条用例执行
    # suite = unittest.TestSuite()
    # suite.addTest(Dtt('test_phoneLogin'))
    # suite.addTest(certification('certificationPage_01'))
    # 所有用例执行
    suite = unittest.defaultTestLoader.discover('../TestCase/', pattern='testCase_*.py',
                                                top_level_dir=None)

    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    createFolder('..\\Report\\', '\\Case_report')  # 判断文件夹是否存在，不存在则创建
    filename = '\\Report\\%s\\%s\\Case_report\\Case_reportweigai.html' % (timestr[:10], timestr[11:])
    fp = open(filename, 'wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(
        stream=fp,
        title='Appium自动化测试结果(Android)',
        description='Android 自动化测试报告',
        tester='最棒QA'  # 可修改为自己名字
    )
    runner.run(suite)
    ass = HTMLTestRunnertest.leiyong123  # 获取HTMLTestRunner.leiyong123返回的用例执行数量与结果
    fp.close()                       # 测试报告关闭
    Excel(ass)                       # 调用生成测试信息Excel
    time.sleep(5)                    # 延时5秒
    mail()                           # 调用发送邮件releaseDemand
