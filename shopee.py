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
domain_sg = "shopee.sg"
domain_ph = "shopee.ph"
domain_vn = "shopee.vn"


# 采集的商品地址，必须是recommend接口，爬取数据的限制修改URL中的limit值
id_url = "https://shopee.co.id/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11044364&limit=200&offset=0"
th_url = "https://shopee.co.th/api/v4/recommend/recommend?bundle=daily_discover_main&item_card=3&limit=200&offset=0&view_session_id=568693e2-b6d9-4f95-9bc5-40d3f3f0b565"
tw_url = "https://shopee.tw/api/v4/recommend/recommend?bundle=daily_discover_main&item_card=3&limit=60&offset=0&view_session_id=db749f4d-9a1a-4686-bd46-7b31261389c2"
sg_url = "https://shopee.sg/api/v4/recommend/recommend?bundle=daily_discover_main&item_card=3&limit=100&offset=0&view_session_id=8caa27ce-30f6-4ca3-b4d1-26a2bddebbb5"
ph_url = "https://shopee.ph/api/v4/recommend/recommend?bundle=daily_discover_main&item_card=3&limit=100&offset=0&view_session_id=180bf3de-af89-405e-bdfa-eb1b7e4181fa"
vn_url = "https://shopee.vn/api/v4/recommend/recommend?bundle=daily_discover_main&item_card=3&limit=100&offset=0&view_session_id=86ac0010-42f8-4743-9f32-6ee6c377eba8"

# 每次切换-修改这个值
domain = domain_vn
good_url = vn_url



def getRes():
    # 写入商品数据到csv
    with open(f'%s商品数据.xlsx' % (domain), mode='a', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=[
                                       '商品标题',
                                       '商品最低价格',
                                       '商品最高价格',
                                       '商品图片链接',
                                       '商品详情链接',
                                       '商品类目id',
                                       '商品店铺id',

                                   ])
        csv_writer.writeheader()
        url = good_url
        headers = {
            "authority": domain,
            "accept": "*/*",
            "sec-ch-ua": 'Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108',
            "referer": "https://%s/" % domain,
            "cookie": "SPC_F=hgQkdQfLV04bEcbmW0e63bRCBOWuNlcW; REC_T_ID=32cdfb2c-2cf3-11ed-91f9-2cea7fa51b88; SPC_R_T_ID=W7ZIeowX4MhVZstvJyfGiwUTX55asfp1R/sYDV5Og2H9anEmq2rnkCcv6usphsqGeKrvfRAq8LLYXmypFt0kmCVB9sZUO0NnZOHfwSKUM4706xMhvV+itsj/OdSxzLULUt+ZPHxYMed1XmPS5P8AGdr/cq2sZVFqhecmpagtvpU=; SPC_R_T_IV=cjQ2TGtLSUN0TGl4cDFxSw==; SPC_T_ID=W7ZIeowX4MhVZstvJyfGiwUTX55asfp1R/sYDV5Og2H9anEmq2rnkCcv6usphsqGeKrvfRAq8LLYXmypFt0kmCVB9sZUO0NnZOHfwSKUM4706xMhvV+itsj/OdSxzLULUt+ZPHxYMed1XmPS5P8AGdr/cq2sZVFqhecmpagtvpU=; SPC_T_IV=cjQ2TGtLSUN0TGl4cDFxSw==; _fbp=fb.1.1662365856278.1281250952; _tt_enable_cookie=1; _ttp=7f0ec687-1356-4fac-9e4e-1e525c0fe582; __LOCALE__null=SG; csrftoken=i4K6FyNghGLvoXO5TEKD3yFYxURx5S18; _QPWSDCXHZQA=bc98f36b-d176-4962-b9a3-678a662617c0; _med=refer; language=zhHans; G_ENABLED_IDPS=google; _gcl_au=1.1.1632386507.1670310099; SPC_SI=P6iHYwAAAABHdjVPcG9scvP59AMAAAAAblp1SEQzTnc=; _gid=GA1.2.1100490365.1670555858; _ga=GA1.1.127516175.1662365857; shopee_webUnique_ccd=CuqIYUUiy0u%2B%2BvTRpEyYLg%3D%3D%7C2BZqIHXQLwrmvUMrIr0xKsXZFxE9OP42Jj9lYekh3GAp2UfUDozg0ujxejTaQkBY4HYuz0uuJmt19z0XZK8JQCPW0Bm%2FyTgn8ZU%3D%7CgDx4io5drpX%2Fjokw%7C06%7C3; ds=c09c598eefea4bfcbfe101947d4de22f; AMP_TOKEN=%24RETRIEVING; _ga_4572B3WZ33=GS1.1.1670566262.11.1.1670566479.57.0.0; cto_bundle=8BVMKF9tTlByeiUyRmkza0xsVXpEOGNnS0NXUUVtcEhnZnd2ajVFcjNJdzdLUWZ6THBUZlFyVVV6Sk9CdVkxT1Y3dUNQMFA1MGF2S0FFclJ5RXFRa2xvS2dScUVXa3ltWDhJSDJQNEpEWXglMkJNdmxoS09MdmtSTlVrTG5RT294RTFiMWZ1OSUyRlloZVBqQnQ4NFJ3YXUzJTJCZktJS1lsVldOOEZYRlNHQjFtNiUyQlE4S3BTZjZGR3BuVTNubk5wS3FNb3BXSG1yT3M5",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
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
            itemid = data['itemid']
            shopid = data['shopid']
            imagelist = []
            for image in data['images']:
                imagelist.append(f'https://cf.%s/file/{image}' % (domain))   # 拼接商品图片链接
            pic = "\n".join(imagelist)
            try:
                url = f"https://%s/{data['name']}-i.{data['shopid']}.{data['itemid']}" % (domain)    # 拼接商品详情链接
            except Exception as e:
                print(e)
            dict = {
                '商品标题': title,
                '商品最低价格': price_min,
                '商品最高价格': price_max,
                '商品图片链接': pic,
                '商品详情链接': url,
                '商品类目id': itemid,
                '商品店铺id': shopid,
            }
            csv_writer.writerow(dict)
            print(dict)

# getRes()


def get_good_detail():
    with open(f'%s商品详情页数据.xlsx' % (domain), mode='a', encoding='utf-8-sig', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=[
            '商品主标题',
            '商品描述',
            '销售价',
            '原价',
            '规格1',
            '规格1属性',
            '规格图片',
            '规格2',
            '规格2属性',
            '商品主图',
            '商品图片',
        ])
        csv_writer.writeheader()
        # url = "https://shopee.tw/api/v4/item/get?itemid=18030259778&shopid=77747852"
        url = "https://shopee.tw/api/v4/item/get?itemid=16681526061&shopid=4077408"
        headers = {
                "authority": domain,
                "x-csrftoken": "CDQqJchs234sygru0BuSA5YKPrtCKgeo",
                "accept-language": "zh-CN,zh;q=0.9",
                "sz-token": "eeROx2NtES1MJ3R7YrP7WA==|yrm5Lkwa7dr3PXlV+BPl7ikMSorogBCAn5eyQbByXYbY2LnyxPeGpWZMTHDN0Tl1M7bLGGCwJsgXK+GoFKphaqIsncWHiIBeIrE=|9nSSti7N1sPuVrdw|06|3",
                "referer": "https://shopee.tw/%E5%A4%A7%E5%B0%BA%E5%AF%B8-36-41-%E7%B6%B2%E7%BE%8E%E6%8B%96%E9%9E%8B-%E5%8E%9A%E5%BA%95%E6%AF%9B%E6%AF%9B%E6%8B%96%E9%9E%8B-%E4%BF%9D%E6%9A%96%E6%8B%96%E9%9E%8B-%E9%9B%99%E5%B8%B6-%E5%AF%AC%E7%89%88-%E6%AF%9B%E6%AF%9B%E6%8B%96-%E5%B1%85%E5%AE%B6%E6%8B%96%E9%9E%8B-%E5%A4%96%E7%A9%BF%E6%8B%96%E9%9E%8B-%E8%88%92%E9%81%A9%E5%8F%AF%E6%84%9B-%E5%8E%9A%E5%BA%95%E6%8B%96%E9%9E%8B-i.4077408.16681526061?sp_atk=45fddbcd-c216-4d5e-838f-c967f9556667&xptdk=45fddbcd-c216-4d5e-838f-c967f9556667",
                "af-ac-enc-dat": "AAcyLjUuMC0yAAABhOKDRFoAAAo3AiAAAAAAAAAAAuvlR3weVVU60ykHUkkzSmQs+0sol/82EyfDx/bVRcPaaRvYmwJ9KYdif1XAOmD+GJEhgTRYGnQXniWTABYptobIXzBCiRQx8xZNwvh+lDfsdTeW7pf/NhMnw8f21UXD2mkb2Js4fgyhyOmWOwejDo7KtGV7rF2PwVkc1NjsoSgUjSXuwTuM3tpSiyZxjiOEw+R2Y7KFxoPStJ1W9NgfFnwzRj0xC1KTeTWGYwbbIDAE9kj5owf9BJ5rmlzPMgc1VDQc2z6XJKS1jUoRjUU1R+bYuYwBLre/9piK99KkCAWY2dsxilRiZeaLJCVJU0SfG5dRLyWdTBzDyqY+p5N5+gnZgWZI9qn7E4LLSp/oVx5gI1zUlEatt8la5FiUWn4nS1xSTq/p6TjLE9sHSxPyhKowBwikRw3ZqhCq5H8W//tsiqUNaUIBakjvio5MdNiZZvHBTV5PFwjBDmBAu/hT5yBBMqK1GAt58mjadOCSqdJGJMljclRiZeaLJCVJU0SfG5dRLyVh0ilDfBWvKEoqh5t7DCKi8d6UNu1kvBhvzRSm+h+lNta/q6j7FU1rKTCbsJlGI8xc70tTuOulbDIsPHW96Bo8kEkzXzlUminZqx7uiyz8f7Y3jKui8iGHJXFI6XXJzuiqdZO9Vdn2yh5kYcJmodJy0RySdhyhKzToeXrsCr/7VhN1fC6+VLg/YeH41Xd4gXEmS6bo/9QcGruu2yuB+9UK",
                "content-type": "application/json",
                "sec-ch-ua": 'Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24',
                "cookie": '_gcl_au=1.1.2127580314.1663814606; _fbp=fb.1.1663814606437.1893299170; SPC_IA=-1; SPC_EC=-; REC_T_ID=55884cfa-3a20-11ed-a174-06672f7401d8; SPC_U=-; SPC_F=SwQXzn6nj0aHAzICCwN9fT7Rt0KR9f8v; REC_T_ID=55868540-3a20-11ed-a846-d094665a025a; SPC_T_IV="aFBQOTV3Rmk1NTk3SHZaTA=="; SPC_T_ID="noIRLm4bclIG404GoI83AxidbsOsxInnUXQK2hTKPV8cNb1ojIuZWqyteD/RmZVs2VoyB7O5qKhaCYXzFdqlV/71HXaRswedcQjEPHLolsVDOFYO9pQqL1/uX6JgYQAesiSQn8MK9t0tnGa2d0APMFCNxGpTqLKZYc88XKrl36Y="; _med=refer; SPC_R_T_ID=rQ5/NzjkWkcyEf/TAJvIuPDM1EjSZ95e+Fz6/fDz6q3lfgzVsg4YmSmxQ9PH4F6Uo8onoDvew0XPSoaf9Y7uqMYa3P2mGpwUgVSjNTExnfU3Iq4jvGRiuoVYA4WUHFK0II5WlK1EPDzZ8DFhxAyU1TGWan9+cgjbGcCisB3BJ94=; SPC_R_T_IV=WmFXWTBORmIzRmpIY3pMQQ==; SPC_T_ID=rQ5/NzjkWkcyEf/TAJvIuPDM1EjSZ95e+Fz6/fDz6q3lfgzVsg4YmSmxQ9PH4F6Uo8onoDvew0XPSoaf9Y7uqMYa3P2mGpwUgVSjNTExnfU3Iq4jvGRiuoVYA4WUHFK0II5WlK1EPDzZ8DFhxAyU1TGWan9+cgjbGcCisB3BJ94=; SPC_T_IV=WmFXWTBORmIzRmpIY3pMQQ==; __LOCALE__null=TW; csrftoken=CDQqJchs234sygru0BuSA5YKPrtCKgeo; _QPWSDCXHZQA=5c8cb4b7-6176-475e-aac1-25fc4bdd4614; SPC_SI=Mbh0YwAAAABBSkUzUGJzSrfQtwEAAAAAZUFZdUEwako=; _gid=GA1.2.1864389640.1670213435; AMP_TOKEN=%24NOT_FOUND; cto_bundle=GptpT19rY1F4a1dpUlNseXdsNlNWbmdYSllQazFhMnpNT1JkclRPZ0F3JTJGb2lTWEVPdjZ1V2VpdlRxaGxPTiUyQkRTRTlXRU9wekkzN1NEa2dEd3NGJTJCbGdVVGNyZ0k4aWZFOTA1dDZYdE5hRWFHa1pqbHUlMkYlMkJBdVVpeWJkSnhWbTV5QiUyRlV5THN1NFVyJTJGc1ZOa1olMkZWYjNPQXJOZG1Ec1c0c3ElMkJxQXlZbnY5ZSUyRk52JTJCckZNVlBqNWdqdld2ZFpsWXoxOGZZSGFF; _dc_gtm_UA-61915057-6=1; _ga_RPSBE3TQZZ=GS1.1.1670243718.11.1.1670247564.59.0.0; _ga=GA1.1.1818205630.1667543284; shopee_webUnique_ccd=PFva23n3LgsLylydLq3mGw%3D%3D%7Cyry5Lkwa7dr3PXlV%2BBPl7ikMSorogBCAn5eyQbByXYbY2LnyxPeGpWZMTHDN0Tl1M7bLGGCwJsgXK%2BGoFKpiaaItmcKBiIBeIrE%3D%7C9nSSti7N1sPuVrdw%7C06%7C3; ds=3e7c866be668e176ac14b80510d26051',
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            }
        res = requests.get(url=url,headers=headers).json()
        print(res)
        title = res['data']['name']
        description = res['data']['description']
        spec = res['data']['tier_variations']
        spec0_name = spec[0]['name']        # 规格1
        option0_list = []
        for i in spec[0]['options']:
            option0_list.append(i)
        spec0_options = "\n".join(option0_list)  # 规格1属性

        spec0_imgs = spec[0]['images']     # 规格图片合集
        spec_img_list = []
        for i in spec0_imgs:
            spec_img_list.append(f'https://cf.%s/file/{i}' % (domain))  # 拼接商品图片链接
        spec_img = "\n".join(spec_img_list)    # 规格图片

        spec1_name = spec[1]['name']     # 规格2
        option1_list = []
        for i in spec[1]['options']:
            option0_list.append(i)
        spec1_options = "\n".join(option1_list)  # 规格2属性

        imgs = res['data']['images']
        selling_price = res['data']['price']
        original_price = res['data']['price_before_discount']
        imagelist = []
        for image in imgs:
            imagelist.append(f'https://cf.%s/file/{image}' % (domain))  # 拼接商品图片链接
        img = "\n".join(imagelist)
        main_img = img.split('\n')[0]

        dict = {
            '商品主标题': title,
            '商品描述': description,
            '销售价': selling_price,
            '原价': original_price,
            '规格1': spec0_name,
            '规格1属性': spec0_options,
            '规格图片': spec_img,
            '规格2': spec1_name,
            '规格2属性': spec1_options,
            '商品主图': main_img,
            '商品图片': img,

        }
        csv_writer.writerow(dict)
        print(dict)




if __name__ == '__main__':
    # get_good_detail()
    getRes()



















