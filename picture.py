# -*- coding:utf-8 -*-
# @Time : 2022/11/7 下午12:16
# @Author : niki
# @File : Image.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests
import os

# 用户代理，作为用户的角色访问网站
gHeards = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

# 图片保存路径
path = os.getcwd()
path = os.path.join(path, "Image")

# 整个for循环用户控制图片展示页面（第几页）
for i in range(2,5):
    url = "https://wallhaven.cc/hot?page=%s" % (i)
    # url = "https://wallhaven.cc/search?q=FOG&categories=110&purity=100&sorting=date_added&order=desc&page=%s" % (i)
    print(url)
    html = requests.get(url,headers=gHeards)   # 请求页面
    html = html.content    # 获取源码
    soup = BeautifulSoup(html,"lxml")
    href_all = soup.find_all("a",{"class":"preview"})   # 找到对应的a标签，且其class=preview
    for href in href_all:  # 打开高清图片的新标签页
        href_url = href["href"]   # 找到对应的href属性值
        html4 = requests.get(href_url,headers = gHeards).content
        soup4 = BeautifulSoup(html4,"lxml")
        img4 = soup4.find("img",{"id":"wallpaper"})   # 找到image标签，且id=wallpaper
        urlimg = img4["src"]    # 获取属性值

        # 将图片下载到本地
        '''r是response响应对象，stream="true"是以字节流的方式读取数据，同时用于确保数据不会直接全部下载到内存中，
        便于下一步使用itre_content实现边下载边存储（因为数据太大可能会超时）
        '''
        r = requests.get(urlimg,stream="true")
        img_name = urlimg.split("/")[-1]    # 获取图片名称
        with open(path+"/%s" % img_name, "wb") as f:    # image文件必须存在，with as便于实现文件的打开和关闭，且容易处理异常
            '''利用for循环，将响应对象response中的数据信息通过iter_content方法，依次读取大小为128字节的数据块
            先下载到内存中，满128字节后存储在硬盘中，实现边下载并存储，知道数据读取完为止
            '''
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print("Save %s" % img_name)
    print("End...................")







