# -*- coding:utf-8 -*-
# @Time : 2022/11/13 下午4:17
# @Author : niki
# @File : goods.py
# @Software: PyCharm

import requests
import csv


# 采集的国家域名
domain_id = "shopee.co.id"
domain_th = "shopee.co.th"
domain_tw = "shopee.tw"

# 每次切换-修改这个值
domain = "shopee.tw"

# 采集的商品地址，必须是recommend接口，爬取数据的限制修改URL中的limit值
id_url = "https://shopee.co.id/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11044364&limit=200&offset=0"
th_url = "https://shopee.co.th/api/v4/recommend/recommend?bundle=daily_discover_main&item_card=3&limit=200&offset=0&view_session_id=568693e2-b6d9-4f95-9bc5-40d3f3f0b565"
tw_url = "https://shopee.tw/api/v4/recommend/recommend?bundle=daily_discover_main&item_card=3&limit=60&offset=0&view_session_id=db749f4d-9a1a-4686-bd46-7b31261389c2"

# 每次切换-修改这个值
good_url = "https://shopee.tw/api/v4/recommend/recommend?bundle=daily_discover_main&item_card=3&limit=60&offset=0&view_session_id=db749f4d-9a1a-4686-bd46-7b31261389c2"



def getRes():
    # 写入商品数据到csv
    with open(f'%s商品数据.xlsx' % (domain), mode='a', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=[
                                       '商品标题',
                                       '商品最低价格',
                                       '商品最高价格',
                                       '商品图片链接',
                                       '商品详情链接',
                                   ])
        csv_writer.writeheader()
        url = good_url
        headers = {
            "authority": domain,
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        }
        # 发起请求
        res = requests.get(url, headers=headers)
        # 获取商品数据
        datas = res.json()['data']['sections'][0]['data']['item']
        # 提取商品数据
        for data in datas:
            title = data['name']
            price_min = data['price_min']*0.00001
            price_max = data['price_max']*0.00001
            imagelist = []
            for image in data['images']:
                imagelist.append(f'https://cf.%s/file/{image}' % (domain))   # 拼接商品图片链接
            pic = "\n".join(imagelist)
            url = f"https://%s/{data['name']}-i.{data['shopid']}.{data['itemid']}" % (domain)    # 拼接商品详情链接
            dict = {
                '商品标题': title,
                '商品最低价格': price_min,
                '商品最高价格': price_max,
                '商品图片链接': pic,
                '商品详情链接': url,
            }
            csv_writer.writerow(dict)
            print(dict)

getRes()






