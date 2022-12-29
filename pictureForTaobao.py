# -*- coding:utf-8 -*-
# @Time : 2022/11/7 下午2:42
# @Author : niki
# @File : pictureForTaobao.py
# @Software: PyCharm

import json,re,os
import pprint
import requests
import csv
import time,random


with open('taobao.csv','w',encoding="UTF-8") as filename:
    csvwriter = csv.DictWriter(filename,fieldnames=['商品标题','商品价格','店铺名称','购买人数','地点','商品图片链接','商品详情链接','店铺链接'])
    csvwriter.writeheader()
    for page in range(1,6):
        print(f'====================================正在爬取第{page}页====================================')
        if page == 1:
            url = 'https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99%E5%A5%B3&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20221113&ie=utf8'
        elif page == 2:
            url = 'https://s.taobao.com/search?data-key=s&data-value=44&ajax="true"&_ksTS=1668323970782_786&callback=jsonp787&q=%E8%BF%9E%E8%A1%A3%E8%A3%99%E5%A5%B3&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20221113&ie=utf8&bcoffset=1&ntoffset=7&p4ppushleft=2%2C48'
        else:
            url = f"https://s.taobao.com/search?data-key=s&data-value=88&ajax="true"&_ksTS=1668324110096_1014&callback=jsonp1015&q=%E8%BF%9E%E8%A1%A3%E8%A3%99%E5%A5%B3&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20221113&ie=utf8&bcoffset=-2&ntoffset=4&p4ppushleft=2%2C48&s={(page-3)*44 + 44}"
        time.sleep(random.randint(1,4))
        headers = {
            'cookie':'_samesite_flag_="true"; cookie2=1b2d9328bd0dc0baa59386c333ea6a21; t=b66fdff5ee25cecf5987f5f1fd0c9038; _tb_token_=e51b38b573bb9; cna=+staG23UL3gCATr45ZghXgOg; xlly_s=1; _m_h5_tk=2bbae03e71f83692bb55172899c2b46a_1667830439262; _m_h5_tk_enc=18fc40f3198f07874daa6984c3cb4122; sgcookie=E100K5MRFUPXP0dVWZjDV216lJ61wHGLKE2VSAwXDCtE0Bymcow3%2FoQ6Ne%2FL7Getgz4FXMRMukOYmcvrdJKBZyR2VpmjJjMzA4NS2pQOWuwDcH4%3D; unb=1059650859; uc1=pas=0&cookie14=UoeyCUk%2F2Nf1Lw%3D%3D&existShop="false"&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie21=WqG3DMC9Edo1SB5NB6Qtng%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D; uc3=vt3=F8dCvjXj5%2FSLCyH3AdA%3D&nk2=2B7PiJGu0RrPgQ%3D%3D&id2=UoH60wQj7bGq7w%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; csg=a3a7011e; lgc=%5Cu9EC4%5Cu79CB%5Cu60212012; cancelledSubSites=empty; cookie17=UoH60wQj7bGq7w%3D%3D; dnk=%5Cu9EC4%5Cu79CB%5Cu60212012; skt=9fb5d3b4b968a632; existShop=MTY2NzgyOTU2NQ%3D%3D; uc4=id4=0%40UOnlbPck5f0MpOLWwvMX6tg7nuTk&nk4=0%402iv60lVBklDSkYO1aLt8RomvErOP; tracknick=%5Cu9EC4%5Cu79CB%5Cu60212012; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=290; _nk_=%5Cu9EC4%5Cu79CB%5Cu60212012; cookie1=VAjEiiImoo1gisbdOpx8dxPjYPRh54vF60ee5owj7HY%3D; enc=Po4w07TpaEXvkYKzs3xtKNF9%2B0pBy4sYlEyaW1QBC1SSxmLFqtgd%2B6DozbpT%2FwXM52IpZ2h0lVDynbwuQWHJgA%3D%3D; JSESSIONID=26409AB525CE650E7C6DE1FE84F3CECB; isg=BFVVjaQ5mv1MXL6A7SKk_g_0ZFcPUglkuHwGc9f6rEwbLncgjKNvNCWo-TKYLiEc; tfstk=c8MRBb1RHnI-BC8338d0YS0TFkwdZCX48BaGpAFqgWFMTVBdiykiBr4RAlaaynC..; l=eBIODl6RTFjb66NUKO5Zourza77OwIRbzsPzaNbMiInca6x1aFamJNCUfurkudtxgtCbNHxrUkhpvdh6-iUNwmyD-J-rCyConxvO.',
            'referer':'https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E8%83%8C&imgfile=&js=1&style=grid&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20221107&ie=utf8',
            'sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':"macOS",
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'same-origin',
            'sec-fetch-user':'?1',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

        # 发起请求
        response = requests.get(url, headers=headers)
        # print(response.text)
        # 匹配网页源代码的内容，拿到想要的数据内容【商品数据】
        html_data = re.findall('g_page_config = (.*);',response.text)[0]
        json_data = json.loads((html_data))
        pprint.pprint(json_data)
        data = json_data['mods']['itemlist']['data']['auctions']
        for index in data:
            dict = {'商品标题':index['raw_title'],
                    '商品价格':index['view_price'],
                    '店铺名称': index['nick'],
                    '购买人数': index['view_sales'],
                    '地点': index['item_loc'],
                    '商品图片链接': index['pic_url'],
                    '商品详情链接': index['detail_url'],
                    '店铺链接': index['shopLink'],
                    }
            csvwriter.writerow(dict)
            print(dict)
            # with open('taobao2.csv',mode='a',encoding='utf-8',newline='') as f:
            #     csv_writer = csv.writer(f)
            #     csv_writer.writerow(['商品标题','商品价格','店铺名称','购买人数','地点','商品图片链接','商品详情链接','店铺链接'])







