

import requests
import datetime
import json
import random
import pymongo
import os
from aiohttp_requests import requests
import asyncio
import aiofiles

Client = pymongo.MongoClient('localhost',27017)
maoyan = Client['maoyan']
item_info = maoyan['nezha']

UA_list =['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36', 'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36', 'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36']

headers = {
'Cookie': '_lxsdk_cuid=16c6776d9ffc8-0f9bbe627f53fd-e343166-100200-16c6776da00c8; uuid_n_v=v1; iuuid=B3E6C190B85B11E9B5E743EE3067BD88A1EE9920983B4A1DBB2B504303E60192; webp=true; ci=241%2C%E8%AE%B8%E6%98%8C; OUTFOX_SEARCH_USER_ID_NCOO=1844957131.3096576; _lxsdk=B3E6C190B85B11E9B5E743EE3067BD88A1EE9920983B4A1DBB2B504303E60192; _lxsdk_s=16c6ada73f3-65a-06f-788%7C%7C5',
'Referer': 'http://m.maoyan.com/movie/1211270/comments?_v_=yes',
'User-Agent':random.choice(UA_list)
}
sem =asyncio.Semaphore(10)
URL = 'http://m.maoyan.com/mmdb/comments/movie/1211270.json?_v_=yes&offset=15&startTime=2019-08-07%2014:42:21'
async def parse_url(url):
    with(await sem):
        try:
            res =await requests.get(url,headers =headers,timeout = 3)
        except:
            print('requests出错，访问出现问题')
            return  None
        try:
            commen = str(await res.read(),'utf-8')
            comment = json.loads(commen)['cmts']
            print(comment)
            for i in comment:
                try:
                    print(i)
                    user_pic = i['avatarurl']
                    cityName = i['cityName']
                    contend = i['content']
                    user_name = i['nickName']
                    if 'gender' in  i:
                        gender = i['gender']
                    else:
                        gender = 0
                    score = i['score']
                    starttime =i['startTime']
                    use_level =i['userLevel']
                    if user_pic:
                        print(user_pic)
                        await save_picurl(user_pic,str(user_name+str(gender)))
                    data = {
                        'name':user_name,
                        'gender':gender,
                        'city':cityName,
                        'user_level':use_level,
                        'socre':score,
                        'starttime':starttime,
                        'contend':contend }
                    item_info.insert_one(data)
                    print('Inserted  Successfully!!!!!!!!!!!')
                except:
                    print('数据出错，插入失败！！')
        except:
            print('json文件出错，请重新处理')
async def save_picurl(url,name):
    with(await sem):
            try:
                picpath = 'F:\pic_url'
                name = name
                filname = '{}\{}.jpg'.format(picpath,name)
                if not os.path.exists(filname):

                    res = await requests.get(url,headers=headers,timeout = 5)

                    async with aiofiles.open(filname,'wb') as fil:
                       await fil.write(await res.read())
                    print('图片{}写入成功!!'.format(name))

            except:
                print('{}   图片插入失败！！！！！'.format(name))


async def  run(url):
    with(await sem):
            start_time1 = '2019-08-06  08:00:00'
            start_time =start_time1
            end_time = '2019-07-26 00:00:00'
            while start_time > end_time:
                i = 1
                while i <= 5592:
                    num = 1
                    tasks =[]
                    while num<= 10:
                        start_time = datetime.datetime.strptime(start_time1, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(seconds=(-1)*15*i)
                        start_time =datetime.datetime.strftime(start_time,'%Y-%m-%d %H:%M:%S')
                        commen_api = url +start_time.replace(' ', '%20')
                        tasks.append(await parse_url(commen_api))
                        i += 1
                    await asyncio.gather(*tasks)

if __name__ =='__main__':
    url = 'http://m.maoyan.com/mmdb/comments/movie/1211270.json?_v_=yes&offset=15&startTime='
    programer =run(url)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(programer)


