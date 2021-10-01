import pymongo
import  pandas as pd
from collections import Counter
import datetime
import time

# 连接数据库
client =pymongo.MongoClient('localhost',27017)
db = client.admin
db.authenticate("admin", "password")
collection = db['doubanComment']


def comment_count():
    # 获取日期中，评论个数
    def sort_date(date_str):
        # fmt = '%Y-%m-%d'
        # print("data_str is {}".format(date_str))
        # time_format = time.strptime(date_str,fmt)
        # print("data_str format is {}".format(time_format))
        if(len(date_str.split('-')) !=3):
            print('not demand str is {}'.format(date_str))
        year, month, day = date_str.split('-')
        timeformat  =int(str(year)+ str(month) + str(day))
        return timeformat

    date_list = []
    for item in collection.find({}):
        date_list.append(item.get('date'))
    date_dict = dict(Counter(date_list))
    new_date_list = [[key,value] for key,value in zip(date_dict.keys(),date_dict.values())]

    new_data_list = sorted(new_date_list,key=lambda value:sort_date(value[0]))
    for item in new_data_list:
        print(item,",")


def star_count():
    # 评论星级分布
    star_dict = {
        '50':'五星',
        '10':'一星',
        '20':'二星',
        '30':'三星',
        '40':'四星',
    }
    print(star_dict.values())
    star_list = []
    for item in collection.find({}):
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

