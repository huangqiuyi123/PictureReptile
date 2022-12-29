# -*- coding:utf-8 -*-
# @Time : 2022/12/29 下午5:10
# @Author : niki
# @File : api.py
# @Software: PyCharm

import json

f = open( './api.txt', 'r' )
data = f.read()
data_json = json.loads(data)


paths = data_json["paths"]
tags = data_json["tags"]
for key in tags:
    print(key["name"])

















