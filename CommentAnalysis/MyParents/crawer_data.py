import requests
import json
import pymongo
import datetime
import time
import urllib.request
from  bs4 import  BeautifulSoup

'''
猫眼，我和我的父辈评论爬取
'''
# 创建的数据表名
collection_name ='shaonian'
client =pymongo.MongoClient('localhost',27017)
db = client.admin
now_exits_collection = db.list_collection_names()
if(collection_name in  now_exits_collection):
    # 存在的话直接创建
    collection = db[collection_name]
else:
    # 不存在的话先创建
    db.create_collection(name=collection_name)
    collection = db[collection_name]



# 删除mongo 中 collection 所有数据
collection.delete_many({})
headers = {
    "Cookie":"bid=tulFhUK9Lzo; douban-fav-remind=1; ll=\"118160\"; _vwo_uuid_v2=D55143433EAF6AF4EB29A904F8BE781A1|4d5d27125abfe3f6d29caa68ba504fed; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1632849782%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.52492667.1628212627.1629608096.1632849782.3; __utmc=30149280; __utmz=30149280.1632849782.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.788106722.1629608096.1629608096.1632849782.2; __utmb=223695111.0.10.1632849782; __utmc=223695111; __utmz=223695111.1632849782.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmb=30149280.3.10.1632849782; _pk_id.100001.4cf6=254979423a09aae4.1629608097.2.1632851386.1629608485.",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
#
#Part1 数据爬取改一下 id 即可
movieId = "35030151"
for offset in range(0,220,20):
    url = "https://movie.douban.com/subject/{}/comments?start={}&limit=20&status=P&sort=new_score".format(movieId,offset)
    res = requests.get(url,headers= headers)
    # print(res.text)
    soup = BeautifulSoup(res.text,'lxml')
    time.sleep(2)
    for comment_item in soup.select("#comments > .comment-item"):
        try:

            data_item = []
            avatar = comment_item.select(".avatar a img")[0].get("src")
            name = comment_item.select(".comment h3 .comment-info a")[0]
            rate = comment_item.select(".comment h3 .comment-info span:nth-child(3)")[0]
            date = comment_item.select(".comment h3 .comment-info span:nth-child(4)")[0]
            comment = comment_item.select(".comment .comment-content span")[0]
            # comment_item.get("div img").ge
            data_item.append(avatar)
            data_item.append(str(name.string).strip("\t"))
            data_item.append(str(rate.get("class")[0]).strip("allstar").strip('\t').strip("\n"))
            data_item.append(str(date.string).replace('\n','').strip('\t'))
            data_item.append(str(comment.string).strip("\t").strip("\n"))
            data_json ={
                'avatar':avatar,
                'name': str(name.string).strip("\t"),
                'rate': str(rate.get("class")[0]).strip("allstar").strip('\t').strip("\n"),
                'date' : str(date.string).replace('\n','').replace('\t','').strip(' '),
                'comment': str(comment.string).strip("\t").strip("\n")
            }
            if not (collection.find_one({'avatar':avatar})):
               print("data _json is {}".format(data_json))
               collection.insert_one(data_json)
        except Exception as e:
            print(e)
            continue

