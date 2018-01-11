# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Android_Ui_Automation
# author: "Lei Yong" 
# creation time: 2018/1/10 下午6:32
# Email: leiyong711@163.com

import HTMLTestRunnertest
from TestCase.testCase_001_login import *

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(Dtt('test_phoneLogin'))
    # suite.addTest(certification('certificationPage_01'))
    suite = unittest.defaultTestLoader.discover('../TestCase/', pattern='testCase_*.py',
                                                top_level_dir=None)
    # suite = unittest.defaultTestLoader.discover('..\\testcase\\', pattern='testCase_*.py',
    #                                             top_level_dir=None)
    # timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    # createFolder('..\\report\\', '\\Case_report')  # 判断文件夹是否存在，不存在则创建
    # filename = '\\report\\%s\\%s\\Case_report\\Case_reportweigai.html' % (timestr[:10], timestr[11:])
    fp = open('../Report/Case_reportweigai.html', 'wb')
    runner = HTMLTestRunnertest.HTMLTestRunner(
        stream=fp,
        title='Appium自动化测试结果(Android)',
        description='Android 自动化测试报告',
        tester='最棒QA'
    )
    runner.run(suite)
    ass = HTMLTestRunnertest.leiyong123  # 获取HTMLTestRunner.leiyong123返回的用例执行数量与结果
    fp.close()                       # 测试报告关闭
    # Excel(ass)                       # 调用生成测试信息Excel
    # time.sleep(5)                    # 延时5秒
    # mk()                             # 调用发送邮件releaseDemand
    # / Users / leiyong / PycharmProjects / huibao

