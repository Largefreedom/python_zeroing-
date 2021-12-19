import random
import re

import requests
import json
import pymongo
from datetime import datetime
import time
import urllib.request
from  bs4 import  BeautifulSoup


'''
微博评论爬取，连接 MongoDB，
'''
collection_name ='Weibo-wlh-Comment'
client =pymongo.MongoClient('localhost',27017)
db = client.admin
now_exits_collection = db.list_collection_names()
if(collection_name in  now_exits_collection):
    # 判断是否存在对应 Document
    collection = db[collection_name]
else:
    db.create_collection(name=collection_name)
    collection = db[collection_name]


headers = {
    "Cookie":"SCF=AjPpO2VnS6ahnqQv19xMZIwH-AHeK_w6F3VrIERc9_ZgqfIIqdLolwGShBysQqKVUi7obDv57sPIvrNJ6QK4gI0.; SUB=_2A25Muu4VDeRhGeFK4lEW8SrEzj2IHXVsRPJdrDV6PUNbktCOLXHTkW1NQteosSX-M-lLtwMbuhmvm2tOxBpFVTQa; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW980rRmxcBRCQR2hObu_gc5JpX5KzhUgL.FoMX1KeNeKBRSK22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMN1hz7eK-N1heR; SSOLoginState=1639882310; ALF=1642474310; _T_WM=43061669502",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "h-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    "Accept":"application/json",
    "Content-Type":"application/json;charset=UTF-8",
    "refer": "https://weibo.cn/",
}

def parseUrl(page):
    url = "https://weibo.cn/comment/hot/L6w2sfDXb"
    params = {
        "rl": 1,
        "page": page,
    }
    if(page != 1):
        # 更换 refer
        headers['refer'] = "https://weibo.cn/comment/hot/L6w2sfDXb?rl=1&page={}".format(page-1)
    # 格式转换;
    res = requests.get(url =url,headers=headers,params=params)
    print("request url is {}  page is {} response status is {}".format(url,page,res.status_code))
    resText = res.content.decode(encoding='utf-8')
    soup = BeautifulSoup(resText,'lxml')
    # select 正则匹配
    for comment_item in soup.select('div[id^="C_"]'):
        userName = comment_item.contents[0].text
        comment = comment_item.contents[-9].text
        likeInfo = comment_item.contents[-5].text
        timeInfo = comment_item.contents[-1].text.split("\xa0")[0]

        data_info  = {
            "userName": userName,
            "comment": comment,
            "likeCount": likeInfo,
            "timeInfo": timeInfo
        }
        if not (collection.find_one({"userName":userName})):
            '''查询之前进行一次过滤'''
            print("data _json is {}".format(data_info))
            collection.insert_one(data_info)


if __name__ =='__main__':
    # 爬取之前清空数据库
    # collection.delete_many({})
    time_unit = [0.5,1,2,0.2,0.4,1.2,1.3,0.9]
    for i in  range(100000):

        parseUrl(page=i)

