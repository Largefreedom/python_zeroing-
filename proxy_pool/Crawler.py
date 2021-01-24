<<<<<<< HEAD
import requests

from fake_useragent import UserAgent
from bs4 import BeautifulSoup as beau
import random
import re
import time

ua =UserAgent()
user_list =['Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14']

class  ProxyMetaclass(type):
    def __new__(cls,name,bases,attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] =count
        return type.__new__(cls,name,bases,attrs)


class Crawler(object,metaclass=ProxyMetaclass):

    def get_proxies(self,callback):
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理',proxy)
            proxies.append(proxy)
        return proxies


    def crawl_kuaidaili(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com/',
            'User-Agent': random.choice(user_list)
        }

        for i in range(5):
            url ='https://www.kuaidaili.com/free/inha/{}/'.format(str(i))
            time.sleep(2)
            res = requests.get(url,headers =headers)
            soup = beau(res.text, 'lxml')
            for j in soup.select('div > table > tbody > tr'):
                ip = re.findall('<td data-title="IP">(.*?)</td>', str(j))[0]
                port = re.findall('<td data-title="PORT">(.*?)</td>', str(j))[0]
                yield ':'.join([ip, port])



    def crawl__66(self):
        headers ={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'http://www.66ip.cn/2.html',
            'User-Agent': random.choice(user_list)
        }
        for i in range(5):
            url = 'http://www.66ip.cn/{}.html'.format(str(i))
            time.sleep(2)
            res = requests.get(url,headers =headers)
            soup = beau(res.text, 'lxml')
            for j in soup.select('div.containerbox > div > table > tr'):
                a = re.findall('<tr><td>(.*?)</td><td>', str(j))[0]
                if a == 'ip':
                    pass
                else:
                    port = re.findall('</td><td>(.*?)</td><td>', str(j))[0]
                    yield ':'.join([a, port])
=======
import requests

from fake_useragent import UserAgent
from bs4 import BeautifulSoup as beau
import random
import re
import time

ua =UserAgent()
user_list =['Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14']

class  ProxyMetaclass(type):
    def __new__(cls,name,bases,attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] =count
        return type.__new__(cls,name,bases,attrs)


class Crawler(object,metaclass=ProxyMetaclass):

    def get_proxies(self,callback):
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理',proxy)
            proxies.append(proxy)
        return proxies


    def crawl_kuaidaili(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com/',
            'User-Agent': random.choice(user_list)
        }

        for i in range(5):
            url ='https://www.kuaidaili.com/free/inha/{}/'.format(str(i))
            time.sleep(2)
            res = requests.get(url,headers =headers)
            soup = beau(res.text, 'lxml')
            for j in soup.select('div > table > tbody > tr'):
                ip = re.findall('<td data-title="IP">(.*?)</td>', str(j))[0]
                port = re.findall('<td data-title="PORT">(.*?)</td>', str(j))[0]
                yield ':'.join([ip, port])



    def crawl__66(self):
        headers ={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'http://www.66ip.cn/2.html',
            'User-Agent': random.choice(user_list)
        }
        for i in range(5):
            url = 'http://www.66ip.cn/{}.html'.format(str(i))
            time.sleep(2)
            res = requests.get(url,headers =headers)
            soup = beau(res.text, 'lxml')
            for j in soup.select('div.containerbox > div > table > tr'):
                a = re.findall('<tr><td>(.*?)</td><td>', str(j))[0]
                if a == 'ip':
                    pass
                else:
                    port = re.findall('</td><td>(.*?)</td><td>', str(j))[0]
                    yield ':'.join([a, port])
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
