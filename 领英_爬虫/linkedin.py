from urllib.parse import quote

from selenium import webdriver

import time
from urllib.parse import quote

import requests

from openpyxl import Workbook

requests.packages.urllib3.disable_warnings()
import re
import json
import redis
from lxml import etree
import os
import time


global page_num
page_num = 0

wb = Workbook()

global sheet

sheet = wb.active



def person_info(url):
    tm = round(time.time()) - 10
    cookies = {
       #写为自己的cookie
    }
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "www.linkedin.com",
        "refer": '',
        'authority': 'www.linkedin.com',
        'method': 'GET',
        'csrf-token': '5069125369962806516',
        'path': '/company/bytedance/jobs/'
    }
    res = requests.get(url=url, headers=headers, cookies=cookies, verify=False)
    html_content = res.content.decode('utf-8')

    html_content = html_content.replace('&quot', '')
    html_content = html_content.replace(':', '')
    html_content = html_content.replace(';', '')

    # print(html_content)

    def get_school_name():
        info = re.findall(r',schoolName(\w*?),fieldOfStudy(\w*?),degreeName(\w*?),', html_content)
        if len(info):
            # k = 1
            # school_dict = {}
            school_info = ''
            for i in info:
                for k in i:
                    name = ''
                    name += k
                    name += ' '
                    school_info += name
                school_info += '|'

                # print('--------------')
                # school_dict['大学-{}'.format(k)] = i[0]
                # k += 1
            # print(school_dict)
            return school_info

        else:
            info = re.findall(r',schoolName(\w*?)大学', html_content)
            school_info = ''
            for i in info:
                school_info = i + '大学'

            if not school_info:
                info = re.findall(r',schoolName(\w*?),fieldOfStudy(\w*?),',html_content)
                for i in info:
                    for k in i:
                        name = ''
                        name += k
                        name += ' '
                        school_info += name
                    school_info += '|'
                if not school_info:
                    info = re.findall(r'fsd_school(\d+),name(\w*?),logo{',html_content)
                    if len(info):
                        school_info = info[-1][-1]
                    return school_info
                return school_info
            return school_info

    def get_person_name():
        info = re.findall(r'firstName(\w*?),lastName(\w*?),', html_content)

        name = info[-1][-1] + info[-1][0]
        name = name.replace(' ', '')
        return name

    global sheet
    sheet.append([get_person_name(), get_school_name()])


def get_per_url(url_list):
    url_list = list(set(url_list))
    # per_url_list = []
    for url in url_list:
        if '//www.baidu.com/link?url' in url:

            # print(url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
            }
            for i in range(5):
                try:
                    res = requests.get(url,headers = headers)
                    url = res.url
                    if '/in/' in url:
                        global page_num
                        page_num += 1
                        # per_url_list.append(url)
                        print(url)
                        person_info(url)
                    break


                except Exception as e:
                    print(e)

                    if i < 5:
                        time.sleep(0.5)
            time.sleep(0.2)
    # return per_url_list




def browser_init():
    option = webdriver.ChromeOptions()
    option.binary_location = '/usr/bin/google-chrome-stable'
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    option.add_argument('--no-sandbox')
    option.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    browser = webdriver.Chrome(chrome_options=option)

    return browser


def get_url_list(browser,company_name):


    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=02003390_42_hao_pg&wd=%E9%A2%86%E8%8B%B1' + quote(company_name)

    print(url)
    browser.get(url)
    for i in range(75):
        # time.sleep()
        html_content = browser.page_source
        html = etree.HTML(html_content)
        href = html.xpath("//a/@href")
        get_per_url(href)
        # print(browser.page_source)

        next_button = browser.find_element_by_xpath("//a[contains(text(),'下一页')]")
        next_button.click()
    print('共爬取{}个个人主页'.format(page_num))








def run(company_name):
    browser = browser_init()




    sheet.title = company_name + '员工档案'
    column_title = ['姓名', '学校']
    sheet.append(column_title)
    get_url_list(browser, company_name)


    wb.save(company_name + '.xlsx')
    print('保存完毕')


# person_url = 'https://cn.linkedin.com/in/%E9%9C%81%E7%8E%A5-%E4%B8%A5-79510b109?trk=prof-samename-name'
# browser.get(person_url)
# html_content = browser.page_source
# print(html_content)






# browser.delete_all_cookies()
# browser.add_cookie(cookie2)
# browser.get('https://www.qimai.cn/rank/index/brand/free/country/cn/genre/5000/device/iphone')
# html = browser.execute_script("return document.documentElement.outerHTML")
# print(html)
# res = browser.execute_script(open('hook.js').read())

# time.sleep(2)
# js = "var q=document.documentElement.scrollTop=100000"
# for i in range(10):
#     print('第{}次爬取'.format(i))
#     time.sleep(2)
#     browser.execute_script(js)
if __name__ == '__main__':
    start_time = time.time()
    company_name = input('请输入公司名称：')
    run(company_name)
    print('共耗时{}'.format(time.time() - start_time))


