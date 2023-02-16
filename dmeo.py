# -*- coding:utf-8 -*-
# @Time : 2023/1/18 上午10:33
# @Author : niki
# @File : dmeo.py
# @Software: PyCharm
import pymysql.connections


#
#
# class MysqlConnection():
#     def __init__(self,db=None):
#         self.db = pymysql.connect(
#             host="10.98.32.8",
#             port= 6329,
#             user="sales_test",
#             passwd="JO7c9m9gDTFKO7SxDW7SZ9ze",
#             database="outsee",
#         )
#
#     def selcet(self,sql):
#         try:
#             mycursor = self.db.cursor()
#             mycursor.execute(sql)
#             myresult = mycursor.fetchall()
#             rs_list = []
#             for x in myresult:
#                 rs_list.append(x)
#             print(rs_list)
#             print("SQL数据查询成功！")
#
#         except Exception as e:
#             print("SQL查询失败",e)
#             mycursor.close()
#             self.db.close()
#
#
#     def inser(self,sql):
#         try:
#             mycursor = self.db.cursor()
#             mycursor.execute(sql)
#             self.db.commit()
#             print("SQL插入数据成功！")
#
#         except Exception as e:
#             print("SQL插入数据失败",e)
#             self.db.rollback()
#             mycursor.close()
#             self.db.close()
#
# if __name__ == '__main__':
#     # MysqlConnection().selcet("SELECT * from tb_user WHERE uname = 'niki'")
#
#     MysqlConnection().inser('INSERT INTO tb_affiliate_reward (`reward_name`, `uid`, `amount_usd`, `memo`, `create_staffer_id`, `create_time` ) VALUES ("Linkiee Reward", 2147486037, 200, NULL, 1008, current_timestamp()); ')
#
#
#
# import json
# data = '{"conflictMap":{"SL201SAS75786889609847248169":{"versionFlag":false,"defaultActivityName":"Add-on items"}}}'
# data_json = json.loads(data)
# d = data_json['conflictMap'].keys()
# print(d)




# -*- coding:utf-8 -*-
# @Time : 2023/1/18 上午10:33
# @Author : niki
# @File : dmeo.py
# @Software: PyCharm
import pymysql.connections


#
#
# class MysqlConnection():
#     def __init__(self,db=None):
#         self.db = pymysql.connect(
#             host="10.98.32.8",
#             port= 6329,
#             user="sales_test",
#             passwd="JO7c9m9gDTFKO7SxDW7SZ9ze",
#             database="outsee",
#         )
#
#     def selcet(self,sql):
#         try:
#             mycursor = self.db.cursor()
#             mycursor.execute(sql)
#             myresult = mycursor.fetchall()
#             rs_list = []
#             for x in myresult:
#                 rs_list.append(x)
#             print(rs_list)
#             print("SQL数据查询成功！")
#
#         except Exception as e:
#             print("SQL查询失败",e)
#             mycursor.close()
#             self.db.close()
#
#
#     def inser(self,sql):
#         try:
#             mycursor = self.db.cursor()
#             mycursor.execute(sql)
#             self.db.commit()
#             print("SQL插入数据成功！")
#
#         except Exception as e:
#             print("SQL插入数据失败",e)
#             self.db.rollback()
#             mycursor.close()
#             self.db.close()
#
# if __name__ == '__main__':
#     # MysqlConnection().selcet("SELECT * from tb_user WHERE uname = 'niki'")
#
#     MysqlConnection().inser('INSERT INTO tb_affiliate_reward (`reward_name`, `uid`, `amount_usd`, `memo`, `create_staffer_id`, `create_time` ) VALUES ("Linkiee Reward", 2147486037, 200, NULL, 1008, current_timestamp()); ')
#
# #
# #
# import json
# data = '{"conflictMap":{"SL201SAS75786889609847248169":{"versionFlag":false,"defaultActivityName":"Add-on items"}}}'
# data_json = json.loads(data)
# d = data_json['conflictMap'].keys()
# print(d)






import requests
import json

class MainRequests():
        def addProduct(self):
            """创建商品"""
            url = 'https://aaa123.myshoplinestg.com/admin/api/product/create'

            header = {'content-type': 'application/json;charset=UTF-8',
                      'cookie': '_BEAMER_USER_ID_whBStDUm30458=b99b65e5-1186-4c59-933d-f8e9e5f6f984; _BEAMER_FIRST_VISIT_whBStDUm30458=2023-02-01T06:40:35.843Z; r_b_ined=1; n_u=ff110b9f3695488dfe145340d8ff2d25; f_ds_info=dXmZ6pO9tXsmYKvGMYBigMFNBEGzEssCtDze73anxYC6fT1IcEj3q1EzqXmJuJgDYEZKj5kOO+OxU5eNBLt8HQ==; store_id=1671160678287; merchant_id=4211980454; currency_code=USD; currency_code.sig=nEGddW1-E-8oJfI_Pm_5XNzC2sMi1n3aVzZ3v01csyY; localization=SG; lang=en; lang.sig=HPZEXM6qRQA3fl9QF0Gl5KM_KZ7FwUtDpVV9UEUrrek; addressLang=en; addressLang.sig=fZhLaUxh_564Gt_Ygb8agf56cVb1lYYp6NMpk7wfgaM; userSelectLocale=en; userSelectLocale.sig=xaWhkiDLccJKOWtBx98z0KVVx7o_iP0WoEYPBrEqJCw; currency_code_userSetting=USD; currency_code_userSetting.sig=wreMdGqvcOcZfYXi-Fd1QDxl5OWoQm3s2QLyXkCpvxE; _tracking_consent=%7B%22con%22%3A%7B%22GDPR%22%3A%22%22%7D%2C%22v%22%3A%221.0%22%2C%22lim%22%3A%5B%5D%2C%22reg%22%3A%22%22%7D; lp_url={%22landingPageHtml%22:%22https://aaa123.myshoplinestg.com/404%22%2C%22occurredAt%22:1675390329558}; s_id=BE6EC5C8FDDA2AC9CC17216C2BA0B736; s_id.sig=e980d6922b556259ec7f02640cbf32db; t_cart=46282d42b07b43f78dda0ac79de9fe11; t_cart.sig=4a6ed1828c3f101f14cae918c81d8d4a; country_code=CN; osudb_lang=en; osudb_hdid=7133d12cafd9154b7b48fdb05fb926ad; osudb_appid=1163336839; osudb_uid=4213238579; osudb_oar=#01BKyGyL9g02xmYhbm7Xp+omDY4AmmD0dOLy5TFADuhM2zWcnY4HUVwseXSOakOtjgfUtqnM1sjvmuuEscmBV6ESYsovWgKl82LdHHyuqc3AjP4cf1tSaiJ10ocVQm/E1rZPHZue8yMwg6wm4kjdxT0WEGlH4lYjCikqajNA; osudb_subappid=1671160678287; _BEAMER_FIRST_VISIT_undefined=2023-02-06T06:09:10.546Z; intercom-device-id-fdjt8drx=14bde1d6-5ab3-454c-a73d-744b249d59a5; a_ste=cojkRTY6WaKlIU0NAQ9cq3SzLq78BTuO9zjtFsiIek8voaSwu0ct7PBO6Ba+W11xb8aFMObih5h5l/EAByfhmg==; intercom-session-fdjt8drx=NnBPdGJyQUR6alJTcUpDYWJmWVBOMjZMOE9mMDllL2pXb3Ewc05pajBDN1dGQndVd1AxSWpnQksveWZuNnJidi0tNC8yMG9FQlIrRGM4Z0JXVHhralVsQT09--dac63c341639943932c26d7c21c003e184b591c0; f_ds_info.sig=0Vq34zWAmy2fWX0ayZGVFshzpZ01n4B0vTo3uy1_geU; store_id.sig=JGwKZ2E-Zu0I48BGyvgVUg0ii-9hpIJcpJ76wu9HnYM; merchant_id.sig=8Abh69bSJhVsbKE6n2CzaQHM3Bbqs2lp2e40qKLBl3A; n_sess={"session_id":"30ef4e3c-90e3-4800-97ef-076395cde76f","created_at":1675926800841,"last_session_id":"80bb42db-ac1c-4f69-8cc5-c6cc7385a11f","session_create_type":102}; JSESSIONID=D62E1E7C66CFF5D3FE95BE885B4C287D; _BEAMER_FILTER_BY_URL_whBStDUm30458=false; a_lang=zh-hans-cn; a_osudb_appid=1163336839; a_osudb_csrf=#C01BHmz8ZX+h0vrohHUXyVhuMAaSYp4IN4EauGDj56SVlq61FmA6oihwDjlaJy45nHGw10x/fkEmp9WYk7SwShXHNnBJSumeKZGBzS4qWw0/DfV7Wv/9dBnUrINRe90PGxXPZCm71iueIzqu7fXYFRevl4gKDKOGw5P98FP/RlfSt2m; a_cstgc=1163336839_1_4211980454_1675934150967sf9z3c; a_osudb_uid=4211980454; a_osudb_oar=#01BBqSWMpBMAkxn8tVua/kmPCBDR60qRchffPPXczrhsPg8vAzpv7MFdeYvtO9xjVptpbBVUZjawATBT/ESBxORa4TPDVnXQRpniZxLsfNThupGTeolydSWih7Td04FUE86aaSGysPVVEe0fgOMJQoDg==; a_osudb_subappid=1; a_lce=1676538951097; a_dhch=aaa123; r_b_in=1'
                      }

            body = '{"product":{"media":[{"mediaType":"image","resourceId":"5798308097185513487","resourceUrl":"https://d2n979dmt31clo.cloudfront.net/image/store/4211980454/1671160678287/1000x-(15).png?w=750&h=750","alt":"自动化创建商品-上架不追踪库存"}],"videos":[],"defaultTitle":"自动化创建商品-上架不追踪库存","weight":0,"weightUnit":"g","shelves":true,"price":50000,"payFilter":[],"shippingFilter":[],"tags":[],"sortations":[],"uniqueKeyList":["自动化创建商品-上架不追踪库存"],"inquiry":false,"source":"SHOPLINE","templatePath":"templates/products/detail.json","productType":0},"extraData":{"off":0},"defaultSeo":{"title":"自动化创建商品-上架不追踪库存","desc":""},"skuList":[{"shelves":true,"price":50000,"locationStockList":[{"quantity":0,"status":1,"locationId":"5718221080097202204"}],"weight":0,"weightUnit":"g","skuAttributeValueList":[],"infiniteStock":true,"allowOversold":false,"taxable":true,"requiredShipping":true}],"publishedScopeList":["web","google","telegram","whatsapp","facebook"],"onlineTime":-1}'

            res = requests.post(url=url, json=json.loads(body), headers=header)
            res_json = res.json()
            spuSeq = res_json['data']['spuSeq']
            skuSeq = res_json['data']['skuList'][0]['skuSeq']
            return spuSeq,skuSeq

        def productList(self):
            """商品列表查询"""
            url = 'https://aaa123.myshoplinestg.com/admin/api/product/query/list'

            header = {'content-type': 'application/json;charset=UTF-8',
                      'cookie': '_BEAMER_USER_ID_whBStDUm30458=b99b65e5-1186-4c59-933d-f8e9e5f6f984; _BEAMER_FIRST_VISIT_whBStDUm30458=2023-02-01T06:40:35.843Z; r_b_ined=1; n_u=ff110b9f3695488dfe145340d8ff2d25; f_ds_info=dXmZ6pO9tXsmYKvGMYBigMFNBEGzEssCtDze73anxYC6fT1IcEj3q1EzqXmJuJgDYEZKj5kOO+OxU5eNBLt8HQ==; store_id=1671160678287; merchant_id=4211980454; currency_code=USD; currency_code.sig=nEGddW1-E-8oJfI_Pm_5XNzC2sMi1n3aVzZ3v01csyY; localization=SG; lang=en; lang.sig=HPZEXM6qRQA3fl9QF0Gl5KM_KZ7FwUtDpVV9UEUrrek; addressLang=en; addressLang.sig=fZhLaUxh_564Gt_Ygb8agf56cVb1lYYp6NMpk7wfgaM; userSelectLocale=en; userSelectLocale.sig=xaWhkiDLccJKOWtBx98z0KVVx7o_iP0WoEYPBrEqJCw; currency_code_userSetting=USD; currency_code_userSetting.sig=wreMdGqvcOcZfYXi-Fd1QDxl5OWoQm3s2QLyXkCpvxE; _tracking_consent=%7B%22con%22%3A%7B%22GDPR%22%3A%22%22%7D%2C%22v%22%3A%221.0%22%2C%22lim%22%3A%5B%5D%2C%22reg%22%3A%22%22%7D; lp_url={%22landingPageHtml%22:%22https://aaa123.myshoplinestg.com/404%22%2C%22occurredAt%22:1675390329558}; s_id=BE6EC5C8FDDA2AC9CC17216C2BA0B736; s_id.sig=e980d6922b556259ec7f02640cbf32db; t_cart=46282d42b07b43f78dda0ac79de9fe11; t_cart.sig=4a6ed1828c3f101f14cae918c81d8d4a; country_code=CN; osudb_lang=en; osudb_hdid=7133d12cafd9154b7b48fdb05fb926ad; osudb_appid=1163336839; osudb_uid=4213238579; osudb_oar=#01BKyGyL9g02xmYhbm7Xp+omDY4AmmD0dOLy5TFADuhM2zWcnY4HUVwseXSOakOtjgfUtqnM1sjvmuuEscmBV6ESYsovWgKl82LdHHyuqc3AjP4cf1tSaiJ10ocVQm/E1rZPHZue8yMwg6wm4kjdxT0WEGlH4lYjCikqajNA; osudb_subappid=1671160678287; _BEAMER_FIRST_VISIT_undefined=2023-02-06T06:09:10.546Z; intercom-device-id-fdjt8drx=14bde1d6-5ab3-454c-a73d-744b249d59a5; a_ste=cojkRTY6WaKlIU0NAQ9cq3SzLq78BTuO9zjtFsiIek8voaSwu0ct7PBO6Ba+W11xb8aFMObih5h5l/EAByfhmg==; intercom-session-fdjt8drx=NnBPdGJyQUR6alJTcUpDYWJmWVBOMjZMOE9mMDllL2pXb3Ewc05pajBDN1dGQndVd1AxSWpnQksveWZuNnJidi0tNC8yMG9FQlIrRGM4Z0JXVHhralVsQT09--dac63c341639943932c26d7c21c003e184b591c0; f_ds_info.sig=0Vq34zWAmy2fWX0ayZGVFshzpZ01n4B0vTo3uy1_geU; store_id.sig=JGwKZ2E-Zu0I48BGyvgVUg0ii-9hpIJcpJ76wu9HnYM; merchant_id.sig=8Abh69bSJhVsbKE6n2CzaQHM3Bbqs2lp2e40qKLBl3A; n_sess={"session_id":"30ef4e3c-90e3-4800-97ef-076395cde76f","created_at":1675926800841,"last_session_id":"80bb42db-ac1c-4f69-8cc5-c6cc7385a11f","session_create_type":102}; JSESSIONID=D62E1E7C66CFF5D3FE95BE885B4C287D; _BEAMER_FILTER_BY_URL_whBStDUm30458=false; a_lang=zh-hans-cn; a_osudb_appid=1163336839; a_osudb_csrf=#C01BHmz8ZX+h0vrohHUXyVhuMAaSYp4IN4EauGDj56SVlq61FmA6oihwDjlaJy45nHGw10x/fkEmp9WYk7SwShXHNnBJSumeKZGBzS4qWw0/DfV7Wv/9dBnUrINRe90PGxXPZCm71iueIzqu7fXYFRevl4gKDKOGw5P98FP/RlfSt2m; a_cstgc=1163336839_1_4211980454_1675934150967sf9z3c; a_osudb_uid=4211980454; a_osudb_oar=#01BBqSWMpBMAkxn8tVua/kmPCBDR60qRchffPPXczrhsPg8vAzpv7MFdeYvtO9xjVptpbBVUZjawATBT/ESBxORa4TPDVnXQRpniZxLsfNThupGTeolydSWih7Td04FUE86aaSGysPVVEe0fgOMJQoDg==; a_osudb_subappid=1; a_lce=1676538951097; a_dhch=aaa123; r_b_in=1'
                      }

            body = '{"pageNum":1,"pageSize":50,"condition":{"sortationId":"12257894819868773015993866","searchType":"SEARCH_TXT","statusList":[1,0,2]},"mightSkuBatchSearch":true,"needSortation":true}'

            res = requests.post(url=url, json=json.loads(body), headers=header)
            res_json = res.json()
            pro_list = res_json['data']['list']
            pro_id_list = []
            sku_id_list = []
            for x in range(len(pro_list)):
                product_id = pro_list[x]['spuSeq']
                pro_id_list.append(product_id)

                sku_list = pro_list[x]['skuList']

                for y in range(len(sku_list)):
                    sku_id =  sku_list[y]['skuSeq']
                    sku_id_list.append(sku_id)

            #
            # print('spuID：',pro_id_list)
            # print('skuID：',sku_id_list)

        def addActivity(self,spu,sku):
            """创建组合销售-加购品活动"""
            url = 'https://aaa123.myshoplinestg.com/admin/api/sale/activity/add_ons/save'

            header = {'content-type': 'application/json;charset=UTF-8',
                      'cookie':'_BEAMER_USER_ID_whBStDUm30458=b99b65e5-1186-4c59-933d-f8e9e5f6f984; _BEAMER_FIRST_VISIT_whBStDUm30458=2023-02-01T06:40:35.843Z; r_b_ined=1; n_u=ff110b9f3695488dfe145340d8ff2d25; f_ds_info=dXmZ6pO9tXsmYKvGMYBigMFNBEGzEssCtDze73anxYC6fT1IcEj3q1EzqXmJuJgDYEZKj5kOO+OxU5eNBLt8HQ==; store_id=1671160678287; merchant_id=4211980454; currency_code=USD; currency_code.sig=nEGddW1-E-8oJfI_Pm_5XNzC2sMi1n3aVzZ3v01csyY; localization=SG; lang=en; lang.sig=HPZEXM6qRQA3fl9QF0Gl5KM_KZ7FwUtDpVV9UEUrrek; addressLang=en; addressLang.sig=fZhLaUxh_564Gt_Ygb8agf56cVb1lYYp6NMpk7wfgaM; userSelectLocale=en; userSelectLocale.sig=xaWhkiDLccJKOWtBx98z0KVVx7o_iP0WoEYPBrEqJCw; currency_code_userSetting=USD; currency_code_userSetting.sig=wreMdGqvcOcZfYXi-Fd1QDxl5OWoQm3s2QLyXkCpvxE; _tracking_consent=%7B%22con%22%3A%7B%22GDPR%22%3A%22%22%7D%2C%22v%22%3A%221.0%22%2C%22lim%22%3A%5B%5D%2C%22reg%22%3A%22%22%7D; lp_url={%22landingPageHtml%22:%22https://aaa123.myshoplinestg.com/404%22%2C%22occurredAt%22:1675390329558}; s_id=BE6EC5C8FDDA2AC9CC17216C2BA0B736; s_id.sig=e980d6922b556259ec7f02640cbf32db; t_cart=46282d42b07b43f78dda0ac79de9fe11; t_cart.sig=4a6ed1828c3f101f14cae918c81d8d4a; country_code=CN; osudb_lang=en; osudb_hdid=7133d12cafd9154b7b48fdb05fb926ad; osudb_appid=1163336839; osudb_uid=4213238579; osudb_oar=#01BKyGyL9g02xmYhbm7Xp+omDY4AmmD0dOLy5TFADuhM2zWcnY4HUVwseXSOakOtjgfUtqnM1sjvmuuEscmBV6ESYsovWgKl82LdHHyuqc3AjP4cf1tSaiJ10ocVQm/E1rZPHZue8yMwg6wm4kjdxT0WEGlH4lYjCikqajNA; osudb_subappid=1671160678287; _BEAMER_FIRST_VISIT_undefined=2023-02-06T06:09:10.546Z; intercom-device-id-fdjt8drx=14bde1d6-5ab3-454c-a73d-744b249d59a5; a_ste=cojkRTY6WaKlIU0NAQ9cq3SzLq78BTuO9zjtFsiIek8voaSwu0ct7PBO6Ba+W11xb8aFMObih5h5l/EAByfhmg==; intercom-session-fdjt8drx=NnBPdGJyQUR6alJTcUpDYWJmWVBOMjZMOE9mMDllL2pXb3Ewc05pajBDN1dGQndVd1AxSWpnQksveWZuNnJidi0tNC8yMG9FQlIrRGM4Z0JXVHhralVsQT09--dac63c341639943932c26d7c21c003e184b591c0; f_ds_info.sig=0Vq34zWAmy2fWX0ayZGVFshzpZ01n4B0vTo3uy1_geU; store_id.sig=JGwKZ2E-Zu0I48BGyvgVUg0ii-9hpIJcpJ76wu9HnYM; merchant_id.sig=8Abh69bSJhVsbKE6n2CzaQHM3Bbqs2lp2e40qKLBl3A; n_sess={"session_id":"30ef4e3c-90e3-4800-97ef-076395cde76f","created_at":1675926800841,"last_session_id":"80bb42db-ac1c-4f69-8cc5-c6cc7385a11f","session_create_type":102}; JSESSIONID=D62E1E7C66CFF5D3FE95BE885B4C287D; a_lang=zh-hans-cn; a_osudb_appid=1163336839; a_osudb_csrf=#C01BHmz8ZX+h0vrohHUXyVhuMAaSYp4IN4EauGDj56SVlq61FmA6oihwDjlaJy45nHGw10x/fkEmp9WYk7SwShXHNnBJSumeKZGBzS4qWw0/DfV7Wv/9dBnUrINRe90PGxXPZCm71iueIzqu7fXYFRevl4gKDKOGw5P98FP/RlfSt2m; a_cstgc=1163336839_1_4211980454_1675934150967sf9z3c; a_osudb_uid=4211980454; a_osudb_oar=#01BBqSWMpBMAkxn8tVua/kmPCBDR60qRchffPPXczrhsPg8vAzpv7MFdeYvtO9xjVptpbBVUZjawATBT/ESBxORa4TPDVnXQRpniZxLsfNThupGTeolydSWih7Td04FUE86aaSGysPVVEe0fgOMJQoDg==; a_osudb_subappid=1; a_lce=1676538951097; a_dhch=aaa123; r_b_in=1'
                      }

            body = '{"primarySpu":{"productId":"%s","skus":[{"skuId":"%s","promotionPrice":50000}]},"addonsSpus":[{"productId":"%s","skus":[{"skuId":"%s","promotionPrice":10000}]}],"display":true,"defaultActivityName":"Add-on items"}' % (
            spu[0], sku[0], spu[1], sku[1])
            # print(body)
            res = requests.post(url=url, json=json.loads(body), headers=header)
            res_json = res.json()
            # print(res_json)
            activitySeq = res_json['data']['activitySeq']

            return activitySeq

        def updateDisplay(self,activitySeq):
            """批量更新加购品活动状态"""
            url = 'https://aaa123.myshoplinestg.com/admin/api/sale/activity/add_ons/update/display'

            header = {'content-type': 'application/json;charset=UTF-8',
                      'cookie':'_BEAMER_USER_ID_whBStDUm30458=b99b65e5-1186-4c59-933d-f8e9e5f6f984; _BEAMER_FIRST_VISIT_whBStDUm30458=2023-02-01T06:40:35.843Z; r_b_ined=1; n_u=ff110b9f3695488dfe145340d8ff2d25; f_ds_info=dXmZ6pO9tXsmYKvGMYBigMFNBEGzEssCtDze73anxYC6fT1IcEj3q1EzqXmJuJgDYEZKj5kOO+OxU5eNBLt8HQ==; store_id=1671160678287; merchant_id=4211980454; currency_code=USD; currency_code.sig=nEGddW1-E-8oJfI_Pm_5XNzC2sMi1n3aVzZ3v01csyY; localization=SG; lang=en; lang.sig=HPZEXM6qRQA3fl9QF0Gl5KM_KZ7FwUtDpVV9UEUrrek; addressLang=en; addressLang.sig=fZhLaUxh_564Gt_Ygb8agf56cVb1lYYp6NMpk7wfgaM; userSelectLocale=en; userSelectLocale.sig=xaWhkiDLccJKOWtBx98z0KVVx7o_iP0WoEYPBrEqJCw; currency_code_userSetting=USD; currency_code_userSetting.sig=wreMdGqvcOcZfYXi-Fd1QDxl5OWoQm3s2QLyXkCpvxE; _tracking_consent=%7B%22con%22%3A%7B%22GDPR%22%3A%22%22%7D%2C%22v%22%3A%221.0%22%2C%22lim%22%3A%5B%5D%2C%22reg%22%3A%22%22%7D; lp_url={%22landingPageHtml%22:%22https://aaa123.myshoplinestg.com/404%22%2C%22occurredAt%22:1675390329558}; s_id=BE6EC5C8FDDA2AC9CC17216C2BA0B736; s_id.sig=e980d6922b556259ec7f02640cbf32db; t_cart=46282d42b07b43f78dda0ac79de9fe11; t_cart.sig=4a6ed1828c3f101f14cae918c81d8d4a; country_code=CN; osudb_lang=en; osudb_hdid=7133d12cafd9154b7b48fdb05fb926ad; osudb_appid=1163336839; osudb_uid=4213238579; osudb_oar=#01BKyGyL9g02xmYhbm7Xp+omDY4AmmD0dOLy5TFADuhM2zWcnY4HUVwseXSOakOtjgfUtqnM1sjvmuuEscmBV6ESYsovWgKl82LdHHyuqc3AjP4cf1tSaiJ10ocVQm/E1rZPHZue8yMwg6wm4kjdxT0WEGlH4lYjCikqajNA; osudb_subappid=1671160678287; _BEAMER_FIRST_VISIT_undefined=2023-02-06T06:09:10.546Z; intercom-device-id-fdjt8drx=14bde1d6-5ab3-454c-a73d-744b249d59a5; a_ste=cojkRTY6WaKlIU0NAQ9cq3SzLq78BTuO9zjtFsiIek8voaSwu0ct7PBO6Ba+W11xb8aFMObih5h5l/EAByfhmg==; intercom-session-fdjt8drx=NnBPdGJyQUR6alJTcUpDYWJmWVBOMjZMOE9mMDllL2pXb3Ewc05pajBDN1dGQndVd1AxSWpnQksveWZuNnJidi0tNC8yMG9FQlIrRGM4Z0JXVHhralVsQT09--dac63c341639943932c26d7c21c003e184b591c0; f_ds_info.sig=0Vq34zWAmy2fWX0ayZGVFshzpZ01n4B0vTo3uy1_geU; store_id.sig=JGwKZ2E-Zu0I48BGyvgVUg0ii-9hpIJcpJ76wu9HnYM; merchant_id.sig=8Abh69bSJhVsbKE6n2CzaQHM3Bbqs2lp2e40qKLBl3A; n_sess={"session_id":"30ef4e3c-90e3-4800-97ef-076395cde76f","created_at":1675926800841,"last_session_id":"80bb42db-ac1c-4f69-8cc5-c6cc7385a11f","session_create_type":102}; JSESSIONID=D62E1E7C66CFF5D3FE95BE885B4C287D; a_lang=zh-hans-cn; a_osudb_appid=1163336839; a_osudb_csrf=#C01BHmz8ZX+h0vrohHUXyVhuMAaSYp4IN4EauGDj56SVlq61FmA6oihwDjlaJy45nHGw10x/fkEmp9WYk7SwShXHNnBJSumeKZGBzS4qWw0/DfV7Wv/9dBnUrINRe90PGxXPZCm71iueIzqu7fXYFRevl4gKDKOGw5P98FP/RlfSt2m; a_cstgc=1163336839_1_4211980454_1675934150967sf9z3c; a_osudb_uid=4211980454; a_osudb_oar=#01BBqSWMpBMAkxn8tVua/kmPCBDR60qRchffPPXczrhsPg8vAzpv7MFdeYvtO9xjVptpbBVUZjawATBT/ESBxORa4TPDVnXQRpniZxLsfNThupGTeolydSWih7Td04FUE86aaSGysPVVEe0fgOMJQoDg==; a_osudb_subappid=1; a_lce=1676538951097; a_dhch=aaa123; r_b_in=1'
                      }

            body = '{"display":true,"activitySeqList":%s}' % activitySeq
            # print(body)
            res = requests.post(url=url, json=json.loads(body), headers=header)
            res_json = res.json()
            seq = res_json['data']['activitySeq']

            return seq


if __name__ == '__main__':
    acc_list = []
    for x in range(2):

        spu_list = []
        sku_list = []
        for i in range(2):
            add_pro = MainRequests().addProduct()
            spu = list(add_pro)[0]
            sku = list(add_pro)[1]
            spu_list.append(spu)
            sku_list.append(sku)
        # print(spu_list,sku_list)

        add_act = MainRequests().addActivity(spu_list, sku_list)
        # print(add_act)
        acc_list.append(add_act)

    update_display = MainRequests().updateDisplay(acc_list)
    print(update_display)














