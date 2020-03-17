#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import schedule
import datetime
# from apscheduler.schedulers.background import BackgroundScheduler
import getUser  # getUser()：读数据库 (('学号', '密码', '邮箱'), ())
import smtpEmail  # smtpEmail(receivers, content): 发content给receivers


def work(user, pwd, email):
    res = '\n学号：' + user;
    print(res)

    try:
        # 打开浏览器，进入健康打卡
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        browser = webdriver.Firefox(options=option)
        res += "(webdriver.Firefox)\n"
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ": webdriver.Firefox")
        browser.get('http://login.cuit.edu.cn/Login/xLogin/Login.asp')
        # 用户名密码id txtId/txtMM
        time.sleep(5)
        userInput = browser.find_element_by_id('txtId')
        userInput.clear()
        userInput.send_keys(user)
        pwdInput = browser.find_element_by_id('txtMM')
        pwdInput.clear()
        pwdInput.send_keys(pwd + Keys.ENTER)
        time.sleep(5)

        # 当天的打卡链接
        date = time.strftime('%m%d', time.localtime())
        res += 'date:' + date + '\n'
        print('date:', date)
        browser.find_element_by_link_text(date + "疫情防控——师生健康状态采集").click()

        # 信息填写 sF21650_5~9
        time.sleep(5)
        msgSelect5 = browser.find_element_by_name('sF21650_5')
        Select(msgSelect5).select_by_visible_text("一般地区")
        res += '一般地区\n'
        print("一般地区")
        time.sleep(1)
        msgSelect6 = browser.find_element_by_name('sF21650_6')
        Select(msgSelect6).select_by_visible_text("在家")
        res += '在家\n'
        print("在家")
        time.sleep(1)
        msgSelect7 = browser.find_element_by_name('sF21650_7')
        Select(msgSelect7).select_by_visible_text("正常")
        res += '正常\n'
        print("正常")
        time.sleep(1)
        msgSelect8 = browser.find_element_by_name('sF21650_8')
        Select(msgSelect8).select_by_visible_text("正常")
        res += '正常\n'
        print("正常")
        time.sleep(1)
        msgSelect9 = browser.find_element_by_name('sF21650_9')
        Select(msgSelect9).select_by_visible_text("全部正常")
        res += '全部正常\n'
        print("全部正常")

        # 点击提交
        browser.find_element_by_name('B1').click()

        # 退出浏览器
        time.sleep(5)
        browser.quit()
        res += time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ": Clock Success!\n"
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ": Clock Success!")

    except:
        res += time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ": Clock Filed!\n"
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ": Clock Filed!")
        time.sleep(5)
        browser.quit()

    smtpEmail.smtpEmail(email, res)


def doAllWork():
    userMsg = getUser.getUser()
    print(userMsg)
    for msg in userMsg:
        try:
            work(msg[0], msg[1], msg[2])
        except:
            work(msg[0], msg[1], msg[2])


if __name__ == '__main__':
    c_time = '09:33'

    schedule.every().day.at(c_time).do(doAllWork)
    while True:
        schedule.run_pending()
