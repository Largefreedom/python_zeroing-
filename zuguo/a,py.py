
# -*- encoding: utf-8 -*-
'''
@Author  : zeriong；
@个人公众号：Z先生点记；
'''
import re
from bs4 import BeautifulSoup as beau
import csv
import asyncio
import random
import requests
import time


ua_list =['Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15', 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36']


headers ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Connection': 'keep-alive',
'Cookie': 'bid=VxWY8TRs0K0; __utmc=30149280; __utmc=223695111; push_doumail_num=0; push_noty_num=0; __utmz=30149280.1569892691.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; ll="118160"; __utmz=223695111.1569892707.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=D37BE833BC1C68324A18CA351666D88A4|9adfe37829818d3773d81572112c3c10; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.656761499.1569843543.1569892691.1569909200.4; __utma=223695111.1271403162.1569843543.1569892707.1569909200.4; __utmb=223695111.0.10.1569909200; OUTFOX_SEARCH_USER_ID_NCOO=1982983110.2715187; douban-profile-remind=1; __utmt=1; dbcl2="204666044:gQPoRqgpVTw"; ck=Vi54; __utmv=30149280.20466; __utmb=30149280.5.10.1569909200; _pk_id.100001.4cf6=008259e8711b66a1.1569843542.4.1569911528.1569892728.',#cookie换成自己的
'User-Agent': random.choice(ua_list)
}
s =requests.session()
sem =asyncio.Semaphore(10)#设置等待时间；
csv_name = 'C:/Users/FREEDOM/Desktop/{}.csv'.format('pandeng')#csv文件储存位置；

logun_url ='https://accounts.douban.com/j/mobile/login/basic'

def login_in(url,username,password):
    data ={
        'name':username,
        'password':password,
        'remember':'false' ,
        }
    try:
        r =s.post(url,headers =headers,data= data)
        r.raise_for_status()
    except:
        print('登陆失败！')
    print(r.text)



def parge_url(url):
    with open(csv_name,'a',newline='',encoding='gbk') as f:#wb新建
        writer = csv.writer(f)
        response =requests.get(url,headers =headers)
        res =beau(response.text,'lxml')
        print(response.status_code)
        for i in res.select('#comments > div.comment-item'):
            try:
                mid = beau(str(i),'lxml')#中间再次解析
                name = mid.select('span.comment-info a')[0].text
                star = re.findall('allstar(.*?) rating',str(i))
                time =mid.find_all(class_ ='comment-time')[0].get('title').strip('')
                comment = mid.select('p span.short')[0].text
                img_url =mid.select('div.avatar a img')[0].get('src')
                list =[]
                list.append(name)
                list.append(star)
                list.append(time)
                list.append(comment)
                list.append(img_url)
                print(list)
                try:
                    writer.writerow(list)
                except:
                    print('数据请求失败*************************')
                    pass
            except:
                print('数据解析失败-----------')

def get_task(id):
    for i in range(0,20):
        url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(id,20*i)
        print('正在处理的url:{}'.format(url))
        time.sleep(3)
        parge_url(url)

if __name__ =='__main__':
    id = '30413052'
    get_task(id)

# login_in(logun_url,13243174991,'653331.zmf')



=======
# -*- encoding: utf-8 -*-
'''
@Author  : zeriong；
@个人公众号：Z先生点记；
'''
import re
from bs4 import BeautifulSoup as beau
import csv
import asyncio
import random
import requests
import time


ua_list =['Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15', 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36']


headers ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Connection': 'keep-alive',
'Cookie': 'bid=VxWY8TRs0K0; __utmc=30149280; __utmc=223695111; push_doumail_num=0; push_noty_num=0; __utmz=30149280.1569892691.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; ll="118160"; __utmz=223695111.1569892707.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=D37BE833BC1C68324A18CA351666D88A4|9adfe37829818d3773d81572112c3c10; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.656761499.1569843543.1569892691.1569909200.4; __utma=223695111.1271403162.1569843543.1569892707.1569909200.4; __utmb=223695111.0.10.1569909200; OUTFOX_SEARCH_USER_ID_NCOO=1982983110.2715187; douban-profile-remind=1; __utmt=1; dbcl2="204666044:gQPoRqgpVTw"; ck=Vi54; __utmv=30149280.20466; __utmb=30149280.5.10.1569909200; _pk_id.100001.4cf6=008259e8711b66a1.1569843542.4.1569911528.1569892728.',#cookie换成自己的
'User-Agent': random.choice(ua_list)
}
s =requests.session()
sem =asyncio.Semaphore(10)#设置等待时间；
csv_name = 'C:/Users/FREEDOM/Desktop/{}.csv'.format('pandeng')#csv文件储存位置；

logun_url ='https://accounts.douban.com/j/mobile/login/basic'

def login_in(url,username,password):
    data ={
        'name':username,
        'password':password,
        'remember':'false' ,
        }
    try:
        r =s.post(url,headers =headers,data= data)
        r.raise_for_status()
    except:
        print('登陆失败！')
    print(r.text)



def parge_url(url):
    with open(csv_name,'a',newline='',encoding='gbk') as f:#wb新建
        writer = csv.writer(f)
        response =requests.get(url,headers =headers)
        res =beau(response.text,'lxml')
        print(response.status_code)
        for i in res.select('#comments > div.comment-item'):
            try:
                mid = beau(str(i),'lxml')#中间再次解析
                name = mid.select('span.comment-info a')[0].text
                star = re.findall('allstar(.*?) rating',str(i))
                time =mid.find_all(class_ ='comment-time')[0].get('title').strip('')
                comment = mid.select('p span.short')[0].text
                img_url =mid.select('div.avatar a img')[0].get('src')
                list =[]
                list.append(name)
                list.append(star)
                list.append(time)
                list.append(comment)
                list.append(img_url)
                print(list)
                try:
                    writer.writerow(list)
                except:
                    print('数据请求失败*************************')
                    pass
            except:
                print('数据解析失败-----------')

def get_task(id):
    for i in range(0,20):
        url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(id,20*i)
        print('正在处理的url:{}'.format(url))
        time.sleep(3)
        parge_url(url)

if __name__ =='__main__':
    id = '30413052'
    get_task(id)

# login_in(logun_url,13243174991,'653331.zmf')



>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
