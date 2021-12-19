import pymongo
import  pandas as pd
from collections import Counter
import datetime
import time
import numpy as np

# 连接数据库
client =pymongo.MongoClient('localhost',27017)
db = client.admin
sn_collect = db['shaonian']
parent_collect = db['myParent']
changjinhu_collect = db['changjinhu']



def comment_count():
    # 获取日期中，评论个数
    def sort_date(date_str):
        if(len(date_str.split('-')) !=3):
            print('not demand str is {}'.format(date_str))
        year, month, day = date_str.split('-')
        timeformat  =int(str(year)+ str(month) + str(day))
        return timeformat

    date_list = []
    for item in sn_collect.find({}):
        date_list.append(item.get('date'))
    date_dict = dict(Counter(date_list))

    new_date_list = [[key,value] for key,value in zip(date_dict.keys(),date_dict.values())]

    new_data_list = sorted(new_date_list,key=lambda value:sort_date(value[0]))    # print(new_data_list[:,1])
    value_list = []
    date_list1 = []
    for item in new_data_list:
        value_list.append(item[1])
        date_list1.append(item[0])
        print("{},".format(item))
    print(date_list1)
    print(value_list)

def star_count():
    # 评论星级分布
    star_dict = {
        '10':'一星',
        '20':'二星',
        '30':'三星',
        '40':'四星',
        '50': '五星',
    }
    print(star_dict.values())
    star_list = []
    for item in changjinhu_collect.find({}):
        if (str(item.get('rate') in star_dict.keys())):
            star_list.append(star_dict[str(item.get('rate'))])
        else:
            print("item star is {}".format(item.get("rate")))

    star_count_dict = dict(Counter(star_list))
    new_star_list = [[key, value] for key, value in zip(star_count_dict.keys(), star_count_dict.values())]

    for item in new_star_list:
        data_json = {
            'value':item[1],
            'name':item[0],
        }
        print(data_json)

# star_count()

sn_sell_amount  = [101,509,408,471,494,511,504]
parent_sell_amount = [6003,16817,15050,13975,12611,11748,11237]
changjinhu_sell_amount = [19090,38062,40674,43897,44969,45844,47534]

sn_add_amount = [sum(sn_sell_amount[:index+1]) for index,item in enumerate(sn_sell_amount)]
parent_add_amount = [sum(parent_sell_amount[:index+1]) for index,item1 in enumerate(parent_sell_amount)]
changjinhu_add_amount = [sum(changjinhu_sell_amount[:index+1]) for index,item2 in enumerate(changjinhu_sell_amount)]

print(sn_add_amount)
print(parent_add_amount)
print(changjinhu_add_amount)


