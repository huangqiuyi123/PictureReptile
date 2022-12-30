# -*- coding:utf-8 -*-
# @Time : 2022/12/29 下午5:10
# @Author : niki
# @File : api.py
# @Software: PyCharm

import json,csv

f = open('./api.txt', 'r' )
data = f.read()
data_json = json.loads(data)


paths = data_json["paths"]

# # 接口模块
# module = []
# tags = data_json["tags"]
# for key in tags:
#     module.append(key["name"])
#     print(key["name"])

# # 接口路径
# for path in paths:
#     print(path)

with open(f'Linkiee-运营后台api.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=[
        '所属模块',
        '接口描述',
        '接口路径'
    ])
    csv_writer.writeheader()

    # 接口所属模块
    for i in paths:
        method = paths.get(i).get("post")

        if method == None:
            tag = paths.get(i).get("get")["tags"]
            description = paths.get(i).get("get")["summary"]
            print(i,tag)

        else:
            tag = paths.get(i).get("post")["tags"]
            description = paths.get(i).get("post")["summary"]
            print(i,tag)
        dict = {
            '所属模块': tag,
            '接口描述': description,
            '接口路径': i
        }
        csv_writer.writerow(dict)


















