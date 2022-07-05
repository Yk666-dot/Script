# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import datetime
import smtplib
import time
from selenium import webdriver

###########################################################################
## Class MyFrame3
###########################################################################


class MyFrame3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(497, 177), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"文件地址", wx.DefaultPosition, wx.Size(500, -1),
                                           wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText5.Wrap(-1)

        bSizer2.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(500, -1), 0)
        bSizer2.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.button = wx.Button(self, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.Size(500, -1), 0)
        bSizer2.Add(self.button, 0, wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button.Bind(wx.EVT_BUTTON, self.find_square)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def find_square(self, event):
        address = self.m_textCtrl5.GetValue() # GetValue是为了获取输入的文本
        with open(address, encoding='utf-8') as file:  # 使用输入的文件地址获取邮箱等参数
            content = file.readlines()
            content = ''.join(content).strip('\n').splitlines()  # 删除字符串的\n

        profile_directory = r'--user-data-dir=C:\Users\msi\AppData\Local\Google\Chrome\User Data'
        # 加载配置数据
        option = webdriver.ChromeOptions()
        option.add_argument(profile_directory)

        driver = webdriver.Chrome(chrome_options=option)
        url = content[0]  # GetValue是为了获取输入的文本
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        lastest_time = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text
        # return lastest_time
        old_pattern = lastest_time
        print('通知系统启动中')
        while True:
            # 记录原始内容列表
            driver.implicitly_wait(30)
            print(
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text)
            new_pattern = driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text  # 记录新内容列表
            error_title = driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/a/div').text
            error = driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/div[1]').text
            driver.implicitly_wait(20)
            status = driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/div[3]/span').text
            print(status)
            if (new_pattern != old_pattern) and (len(status) != 0):  # 判断内容列表是否更新,去除更新的是已解决信息
                # old_pattern=new_pattern    #原始内容列表改变
                # 发送邮件
                HOST = 'smtp.exmail.qq.com'  # 腾讯邮箱smtp
                PORT = '465'
                fajianren = content[2]  # 发送人邮箱
                shoujianren = content[1]  # 收件人邮箱
                title = '信息内容'  # 邮件标题
                new_pattern = '有新的错误信息，请注意\n' + error_title + '\n' + error  # 提取网页内容列表
                context = new_pattern  # 邮件内容
                smtp = smtplib.SMTP_SSL(HOST, 465)  # 启用SSL发信, 端口一般是465
                res = smtp.login(user=fajianren,
                                 password=content[3])  # 登录验证，password是邮箱授权码而非密码，需要去网易邮箱手动开启
                print('发送结果：', res)
                msg = '\n'.join(
                    ['From: {}'.format(fajianren), 'To: {}'.format(shoujianren), 'Subject: {}'.format(title), '',
                     context])
                smtp.sendmail(from_addr=fajianren, to_addrs=shoujianren, msg=msg.encode('utf-8'))  # 发送邮件
                print(context)

            else:
                now = datetime.datetime.now()
                print(now, "尚无更新")
            old_pattern = driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text
            time.sleep(300)  # 五分钟检测一次
            driver.refresh()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame3(None)
    frame.Show(True)
    app.MainLoop()

