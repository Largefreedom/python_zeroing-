<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  : zeriong；
@个人公众号：Z先生点记；
'''
import aiofiles
import asyncio
from aiohttp_requests import requests
import os
import datetime
import time
import pandas as pd
import re


num =0
async def down_pic(url,id,name):
        '''
        处理下载时间
        '''
        try:
            start = time.time()
            fil_path ='C:/Users/FREEDOM/Desktop/{}/{}.jpg'.format(id,name)
            fil_path1 ='C:/Users/FREEDOM/Desktop/{}'.format(id)
            if not os.path.exists(fil_path1):
                os.makedirs(fil_path1)#创建文件夹
            if not os.path.exists(fil_path):#文件夹不存在
                res =await requests.get(url)
                async with aiofiles.open(fil_path,'wb') as f:
                    await f.write(await res.read())
                end =time.time()
                print('图片{}下载成功!!!,用时{}秒'.format(name,str(end-start)))
            else:
                print('图片已存在，下一个')
        except:
            print('c出错了，下一个')


async  def get_url(id):
    '''
    获取url;;;
    :param id:
    :return:
    '''
    csv_path = 'C:/Users/FREEDOM/Desktop/{}.csv'.format(id)
    data = pd.read_csv(csv_path,encoding='gbk')
    tasks = []
    for i in data['name']:
        n = 1
        name = str(i)
        url1 =  str(data[data['name']==name]['img_url'])
        url = re.findall('.*?(https.*?.jpg).*?',url1)[0]
        tasks.append(await down_pic(url,id,name))
        if  n % 10 ==0:
            await asyncio.gather(*tasks)
            tasks = []
        n += 1

if __name__ =='__main__':
    id = 'zuguo'
    prog = get_url(str(id))
    loop = asyncio.get_event_loop()
=======
# -*- encoding: utf-8 -*-
'''
@Author  : zeriong；
@个人公众号：Z先生点记；
'''
import aiofiles
import asyncio
from aiohttp_requests import requests
import os
import datetime
import time
import pandas as pd
import re


num =0
async def down_pic(url,id,name):
        '''
        处理下载时间
        '''
        try:
            start = time.time()
            fil_path ='C:/Users/FREEDOM/Desktop/{}/{}.jpg'.format(id,name)
            fil_path1 ='C:/Users/FREEDOM/Desktop/{}'.format(id)
            if not os.path.exists(fil_path1):
                os.makedirs(fil_path1)#创建文件夹
            if not os.path.exists(fil_path):#文件夹不存在
                res =await requests.get(url)
                async with aiofiles.open(fil_path,'wb') as f:
                    await f.write(await res.read())
                end =time.time()
                print('图片{}下载成功!!!,用时{}秒'.format(name,str(end-start)))
            else:
                print('图片已存在，下一个')
        except:
            print('c出错了，下一个')


async  def get_url(id):
    '''
    获取url;;;
    :param id:
    :return:
    '''
    csv_path = 'C:/Users/FREEDOM/Desktop/{}.csv'.format(id)
    data = pd.read_csv(csv_path,encoding='gbk')
    tasks = []
    for i in data['name']:
        n = 1
        name = str(i)
        url1 =  str(data[data['name']==name]['img_url'])
        url = re.findall('.*?(https.*?.jpg).*?',url1)[0]
        tasks.append(await down_pic(url,id,name))
        if  n % 10 ==0:
            await asyncio.gather(*tasks)
            tasks = []
        n += 1

if __name__ =='__main__':
    id = 'zuguo'
    prog = get_url(str(id))
    loop = asyncio.get_event_loop()
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
    loop.run_until_complete(prog)