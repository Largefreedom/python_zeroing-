<<<<<<< HEAD
import aiohttp
import asyncio
from proxy_pool.Redis_client import Redisclient
import time


VAILD_SATTUS_CODES = [200]
TEXT_URL = 'http://www.baidu.com'
BATCH_TEXT_SIZE =100


class Tester(object):
    def __init__(self):
        self.redis =Redisclient()

    async def text_single_proxy(self,proxy):
        '''
        测试单个代理的可用性；
        :param proxy: 单个代理；
        :return:
        '''
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy =proxy.decode('utf-8')
                real_proxy = 'http://'+proxy
                async with session.get(TEXT_URL,proxy = real_proxy,timeout = 15) as response:
                    if response.status in VAILD_SATTUS_CODES:
                        self.redis.max(proxy)
                        print('代理可用',proxy)
                    else:
                        self.redis.decrease_proxy(proxy)
                        print('请求响应码不合法',proxy)
            except (TimeoutError,AttributeError):
                self.redis.decrease_proxy(proxy)
                print('代理请求失败')
    def run(self):

        '''
        调用主函数；
        :return:
        '''
        print('测试器开始运行')
        try:
            proxies = self.redis.get_all_prpxy()
            loop =asyncio.get_event_loop()
            #批量测试
            for i in range(0,len(proxies),BATCH_TEXT_SIZE):
                test_proxies = proxies[i:i+BATCH_TEXT_SIZE]
                tasks = [self.text_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
=======
import aiohttp
import asyncio
from proxy_pool.Redis_client import Redisclient
import time


VAILD_SATTUS_CODES = [200]
TEXT_URL = 'http://www.baidu.com'
BATCH_TEXT_SIZE =100


class Tester(object):
    def __init__(self):
        self.redis =Redisclient()

    async def text_single_proxy(self,proxy):
        '''
        测试单个代理的可用性；
        :param proxy: 单个代理；
        :return:
        '''
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy =proxy.decode('utf-8')
                real_proxy = 'http://'+proxy
                async with session.get(TEXT_URL,proxy = real_proxy,timeout = 15) as response:
                    if response.status in VAILD_SATTUS_CODES:
                        self.redis.max(proxy)
                        print('代理可用',proxy)
                    else:
                        self.redis.decrease_proxy(proxy)
                        print('请求响应码不合法',proxy)
            except (TimeoutError,AttributeError):
                self.redis.decrease_proxy(proxy)
                print('代理请求失败')
    def run(self):

        '''
        调用主函数；
        :return:
        '''
        print('测试器开始运行')
        try:
            proxies = self.redis.get_all_prpxy()
            loop =asyncio.get_event_loop()
            #批量测试
            for i in range(0,len(proxies),BATCH_TEXT_SIZE):
                test_proxies = proxies[i:i+BATCH_TEXT_SIZE]
                tasks = [self.text_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
            print('测试器发生错误',e.args)