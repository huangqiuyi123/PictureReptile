# -*- coding:utf-8 -*-
# @Time : 2022/11/13 下午4:17
# @Author : niki
# @File : goods.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import openpyxl
import time
import re
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

key_world = '包包'
# f = open(f'Dior商品数据.csv', mode='a', encoding='utf-8', newline='')
# csv_writer = csv.DictWriter(f,fieldnames=[
#     '商品主标题',
#     '商品副标题',
#     '商品价格',
#     '商品主图',
#     '商品详情链接',
# ])
# csv_writer.writeheader()

# selenium模拟人的行为，获取数据内容
# selenium 操控谷歌驱动，然后操控浏览器
driver = webdriver.Chrome()
print("正在打开网页......")
# 打开网址
driver.get('https://www.dior.cn/zh_cn/fashion')   # https://www.dior.cn/zh_cn/fashion/womens-fashion/cruise-2023-collection
time.sleep(1)
driver.maximize_window()   # 浏览器窗口最大化
time.sleep(1)
# 找到搜索按钮
search_button = driver.find_element(By.CSS_SELECTOR,'#prc-3-1 > div > header > div.desktop-header__top > nav.desktop-header__nav.open > ul > li:nth-child(1) > div > div > div')
# 鼠标悬浮
ActionChains(driver).move_to_element(search_button).perform()
# 找到输入框
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,'#header_input_search_id').send_keys(key_world)
# 输入关键字后点击查询按钮
driver.find_element(By.XPATH,'//*[@id="prc-3-1"]/div/header/div[1]/nav[2]/ul/li[1]/div/div/button').click()
print("正在搜索数据......")
time.sleep(1)



def drop_down():
    """执行页面滚动的操作"""  # js
    for x in range(1,12,4):
        time.sleep(1)
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)  # 执行我们JS代码
    target = driver.find_element(By.CLASS_NAME,"search-results-load-more")
    driver.execute_script("arguments[0].scrollIntoView();", target)

    # # 确定拖拽目标的起点
    # source = driver.find_element(By.ID,"main")
    # # 确定拖拽目标的终点
    # target = driver.find_element(By.CLASS_NAME,"search-results-load-more")
    # # 形成动作链接
    # actions = ActionChains(driver)
    # actions.drag_and_drop(source,target)
    # # 执行
    # actions.perform()


def get_shop_info():
    with open(f'Dior商品数据.csv', mode='a', encoding='utf-8', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=[
                                       '商品主标题',
                                       '商品副标题',
                                       '商品价格',
                                       '商品主图',
                                       '商品详情链接',
                                   ])
        csv_writer.writeheader()
        # 第一步：获取所有的li标签内容
        print("正在获取数据......")
        driver.implicitly_wait(10)
        # 获取多个li标签
        ul = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/ul')
        lis = ul.find_elements(By.TAG_NAME,'li')

        for li in lis:
            print("正在定位数据......")
            driver.implicitly_wait(5)
            # print("价格：",li.find_element(By.CLASS_NAME, 'price-line').text)
            # print("图片链接：",li.find_element(By.CLASS_NAME,'image').find_element(By.TAG_NAME,'img').get_attribute('src'))
            # print("店铺详情：",li.find_element(By.CLASS_NAME,'product-wrapper').get_attribute('href'))
            # print("标题：",li.find_element(By.CLASS_NAME,'multiline-text multiline-text--is-china').text)
            li_data = []
            for i in li.text.split('\n'):
                print(i)
                li_data.append(i)
            # print("li_data结果：",li_data)
            main_title = li_data[0]
            sub_title = li_data[1]
            price = li_data[2]
            # main_title = li.find_element(By.CLASS_NAME,'multiline-text multiline-text--is-china').text # 主标题
            # sub_title = li.find_element(By.CLASS_NAME, 'multiline-text product-subtitle multiline-text--is-china').text  # 副标题
            # price = li.find_element(By.CLASS_NAME, 'price-line').text   # 价格
            driver.implicitly_wait(5)
            img = li.find_element(By.CLASS_NAME,'image').find_element(By.TAG_NAME,'img').get_attribute('src')
            href = li.find_element(By.CLASS_NAME,'product-wrapper').get_attribute('href')
            dict= {
                '商品主标题': main_title,
                '商品副标题': sub_title,
                '商品价格': price,
                '商品主图': img,
                '商品详情链接': href,
            }
            csv_writer.writerow(dict)
            print(main_title,sub_title,price,img,href,sep=' | ')


for page in range(1,2):
    print(f'正在爬取第{page}页的数据')
    drop_down()
    driver.implicitly_wait(5)
    try:
        get_shop_info()
        # 点击查看更多结果按钮（翻页）
        driver.find_element(By.CLASS_NAME,'button-link search-results-load-more-button css-lv160i').click()
    except Exception as e:
        print(e)

print("关闭网页")
# 关闭浏览器
driver.quit()


















