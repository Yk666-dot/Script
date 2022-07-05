# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import datetime
import smtplib
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

###########################################################################
# Class MyFrame3
###########################################################################


class MyFrame3(wx.Frame):
    # 设置界面ui
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
    # 设置按钮事件
    def find_square(self, event):
        global driver, tiplist
        for i in range(20):
            t1 = time.strftime('%H:%M:%S', time.localtime(time.time()))
            if i == 20:
                print("第20次重启失败网页异常,停止运行")
                break
            tip1 = "第%s次重启失败网页异常" % str(i)
            tiplist = []   # 定个时间列表，到点后把时间写入列表，判断下面的重启浏览器时间
            if t1 >= '17:30:00':
                tiplist.append(tip1)
            print("第%s次重启失败网页异常" % str(i) + '\n')

            try:
                address = self.m_textCtrl5.GetValue()  # GetValue是为了获取输入的文本
                with open(address, encoding='utf-8') as file:  # 使用输入的文件地址获取邮箱等参数
                    self.content = file.readlines()  # 遍历文件内的每行，形成一个list
                    self.content = ''.join(self.content).strip('\n').splitlines()  # 删除字符串的\n

                profile_directory = r'--user-data-dir=C:\Users\msi\AppData\Local\Google\Chrome\User Data'  # 获取本地缓存
                # 加载配置数据，进入网站无需登录
                option = webdriver.ChromeOptions()
                option.add_argument(profile_directory)
                option.add_argument('--no-sandbox')
                option.add_argument('--disable-gpu')  # 防止网页奔溃
                option.add_argument('--ignore-certificate-errors')  # 忽略exe执行时的证书报错
                driver = webdriver.Chrome(chrome_options=option)

                url = self.content[1]  # GetValue是为了获取输入的文本
                driver.get(url)
                driver.maximize_window()
                driver.implicitly_wait(30)
                lastest_time = driver.find_element_by_xpath(
                    '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text
                old_pattern = lastest_time   # 首次进入获取Android页面最新数据的上报时间来进行比对
                time.sleep(10)
                # 进入ios页面
                element = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[1]/div/div')
                ActionChains(driver).move_to_element(element).perform()
                driver.find_element_by_xpath(
                    '//*[@id="root"]/div/div/div[2]/div/div[1]/div[1]/div[2]/ul/li[1]/div').click()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/ul[2]/li').click()
                time.sleep(10)
                # 首次进入获取ios页面最新数据的上报时间来进行比对
                old_pattern_ios = driver.find_element_by_xpath(
                    '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text
                # 返回Android页面
                element = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[1]/div/div')
                ActionChains(driver).move_to_element(element).perform()
                driver.find_element_by_xpath(
                    '//*[@id="root"]/div/div/div[2]/div/div[1]/div[1]/div[2]/ul/li[2]/div').click()
                driver.implicitly_wait(20)
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/ul[2]/li').click()
                time.sleep(100)
                print('通知系统启动中')

                while True:
                    t2 = time.strftime('%H:%M:%S', time.localtime(time.time()))  # 格式输出系统化时间
                    if t2 >= '17:30:00' and len(tiplist) == 0:    # 到5点半重启一下防止浏览器崩溃
                        print(t2 + "重启\n")
                        break

                    # Android
                    time.sleep(10)
                    print("Android最新信息的上报时间：" +
                        driver.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text)
                    new_pattern = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text  # 记录刷新后最新一条数据的上报时间
                    self.error_title = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/a/div').text  # 记录错误编号
                    self.error = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/div[1]').text  # 记录错误信息
                    time.sleep(10)
                    status = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/div[3]/span').text  # 记录状态
                    print("Android" + status)
                    if (new_pattern != old_pattern) and (status == "状态变更"):  # 判断内容列表是否更新,去除更新的是已解决信息
                        self.send_email(rec=self.content[3])
                        print('已发送邮件')
                    else:
                        now = datetime.datetime.now()
                        print(now, "Android尚无更新\n")
                    # 将当前最新消息的上报时间记录，跟刷新后最新消息的上报记录进行对比
                    old_pattern = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text

                    # ios
                    time.sleep(10)
                    element = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[1]/div/div')
                    ActionChains(driver).move_to_element(element).perform()
                    driver.implicitly_wait(20)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[1]/div[2]/ul/li[1]/div').click()
                    driver.implicitly_wait(20)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/ul[2]/li').click()
                    time.sleep(10)
                    print("ios最新信息的上报时间：" +
                        driver.find_element_by_xpath(
                            '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text)
                    new_pattern_ios = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text  # 记录新内容列表
                    self.error_title = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/a/div').text
                    self.error = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/div[1]').text
                    n_version = self.content[11]  # 手动输入的版本号
                    version = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/div[2]/div[1]').text  # 获取版本号
                    nu = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[3]').text  # 获取发生次数
                    status = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/div[3]/span').text
                    print("ios" + status)
                    if (new_pattern_ios != old_pattern_ios) and (status == "状态变更") \
                            and (version.find(n_version) == 0) and (int(nu) >= 10):  # 判断内容列表是否更新,去除更新的是已解决信息
                        self.send_email(rec=self.content[5])
                        print('已发送邮件')

                    elif (new_pattern_ios != old_pattern_ios) and (status == "状态变更"):  # 判断非最新的报错,写入文件
                        file_name = r'C:\Users\msi\Documents\一周bugly崩溃id.txt'
                        with open(file_name, 'a+', encoding='utf-8') as file2:
                            lis = file2.readlines()
                            if self.error_title not in lis:
                                file2.write(self.error_title + '\n')
                                now = datetime.datetime.now()
                                print('ios错误已写入文档：', now)
                    else:                                      # 无新报错
                        now = datetime.datetime.now()
                        print(now, "ios尚无更新\n")
                    old_pattern_ios = driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text
                    time.sleep(220)  # 220s后重新检测一次

                    # 返回安卓页面
                    ActionChains(driver).move_to_element(element).perform()
                    driver.implicitly_wait(20)
                    driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div[2]/div/div[1]/div[1]/div[2]/ul/li[2]/div').click()
                    time.sleep(5)
                    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/ul[2]/li').click()
            except Exception as e:
                print(e)
                driver.quit()

    def send_email(self, rec):
        # 发送邮件
        HOST = 'smtp.exmail.qq.com'  # 腾讯邮箱smtp
        PORT = '465'
        fajianren = self.content[7]  # 发送人邮箱
        shoujianren = rec  # 收件人邮箱
        title = '信息内容'  # 邮件标题
        new_pattern = '有新的错误信息，请注意\n' + self.error_title + '\n' + self.error + '\n'  # 提取网页内容列表
        context = new_pattern  # 邮件内容
        smtp = smtplib.SMTP_SSL(HOST, 465)  # 启用SSL发信, 端口一般是465
        res = smtp.login(user=fajianren,
                         password=self.content[9])  # 登录验证，password是邮箱授权码而非密码
        print('发送结果：', res)
        msg = '\n'.join(
            ['From: {}'.format(fajianren), 'To: {}'.format(shoujianren), 'Subject: {}'.format(title), '',
             context])
        smtp.sendmail(from_addr=fajianren, to_addrs=shoujianren, msg=msg.encode('utf-8'))  # 发送邮件
        print(context)


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame3(None)
    frame.Show(True)
    app.MainLoop()
