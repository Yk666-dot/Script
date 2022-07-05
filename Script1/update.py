import time
import re
import requests
import datetime
import smtplib
import time
from selenium import webdriver
import session


def qingqiu():
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
    #                 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}     #设置headers信息，模拟成浏览器取访问网站
    # req = requests.post('https://bugly.qq.com/v2/crash-reporting/crashes/120d741edd?pid=2', headers=headers)   #向网站发起请求，并获取响应对象
    # content = req.text   #获取网站源码
    # pattern = re.compile('.html(.*?)</a>').findall(content)  #正则化匹配字符，根据网站源码设置
    # return pattern  #运行qingqiu()函数，会返回pattern的值
    # profile_directory = r'--user-data-dir=C:\Users\msi\AppData\Local\Google\Chrome\User Data'
    # # 加载配置数据
    # option = webdriver.ChromeOptions()
    # option.add_argument(profile_directory)

    driver = webdriver.Chrome()
    url = "https://bugly.qq.com/v2/crash-reporting/crashes/1103109381?pid=1"
    session.get(url=url,headers=headers)
    driver.maximize_window()
    driver.implicitly_wait(30)
    lastest_time = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text
    # return lastest_time
    old_pattern = lastest_time
    print('通知系统启动中')
    while True:
         # 记录原始内容列表
        driver.implicitly_wait(30)
        print(driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text)
        new_pattern = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text  # 记录新内容列表
        error_title = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/a/div').text
        error = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[5]/div[1]').text
        if (new_pattern != old_pattern):  # 判断内容列表是否更新
            # old_pattern=new_pattern    #原始内容列表改变
            # 发送邮件
            HOST = 'smtp.exmail.qq.com'  # 腾讯邮箱smtp
            PORT = '465'
            fajianren = 'yuk@21cp.com'  # 发送人邮箱
            shoujianren = 'liqy@21cp.com'  # 收件人邮箱
            title = '信息内容'  # 邮件标题
            new_pattern = '有新的错误信息，请注意\n' + error_title + '\n' + error   # 提取网页内容列表
            context = new_pattern  # 邮件内容
            smtp = smtplib.SMTP_SSL(HOST, 465)  # 启用SSL发信, 端口一般是465
            res = smtp.login(user=fajianren, password='Qq84616553')  # 登录验证，password是邮箱授权码而非密码，需要去网易邮箱手动开启
            print('发送结果：', res)
            msg = '\n'.join(
                ['From: {}'.format(fajianren), 'To: {}'.format(shoujianren), 'Subject: {}'.format(title), '', context])
            smtp.sendmail(from_addr=fajianren, to_addrs=shoujianren, msg=msg.encode('utf-8'))  # 发送邮件
            print(context)

        else:
            now = datetime.datetime.now()
            print(now, "尚无更新")
        old_pattern = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[4]/p').text
        time.sleep(300)  # 五分钟检测一次
        driver.refresh()



# def update():
#     driver = webdriver.Chrome()
#     print('通知系统启动中')
#     old_pattern = qingqiu()  #记录原始内容列表
#     while True:
#         new_pattern = qingqiu()  #记录新内容列表
#         if (new_pattern!= old_pattern):  #判断内容列表是否更新
#             #old_pattern=new_pattern    #原始内容列表改变
#             send_email()   #发送邮件
#         else:
#             now=datetime.datetime.now()
#             print(now,"尚无更新")
#         old_pattern = new_pattern
#         time.sleep(300) # 五分钟检测一次
#         driver.refresh()

# def send_email():
#     HOST = 'smtp.qq.com'   # 腾讯邮箱smtp
#     PORT = '465'
#     fajianren = '84616553@qq.com'   #发送人邮箱
#     shoujianren = 'yuk@21cp.com'   #收件人邮箱
#     title = '信息内容'     # 邮件标题
#     new_pattern = '有新的错误信息，请注意\n' + qingqiu() #提取网页内容列表
#     context = new_pattern  # 邮件内容
#     smtp = smtplib.SMTP_SSL(HOST, 465)  # 启用SSL发信, 端口一般是465
#     res = smtp.login(user=fajianren, password='vmjldqtmcgvgbggh') # 登录验证，password是邮箱授权码而非密码，需要去网易邮箱手动开启
#     print('发送结果：', res)
#     msg = '\n'.join(
#         ['From: {}'.format(fajianren), 'To: {}'.format(shoujianren), 'Subject: {}'.format(title), '', context])
#     smtp.sendmail(from_addr=fajianren, to_addrs=shoujianren, msg=msg.encode('utf-8')) # 发送邮件
#     print(context)

if __name__ == '__main__':
    qingqiu()
