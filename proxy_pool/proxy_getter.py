<<<<<<< HEAD
from proxy_pool.Crawler import Crawler
from proxy_pool.Redis_client import Redisclient

full_num = 200

class Getter:

    def __init__(self):
        self.redis_cilent =Redisclient()
        self.crawer = Crawler()

    def _is_full(self):

        if self.redis_cilent.get_count_proxy() >= full_num:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行。。。。。。。。。。。')
        if not self._is_full():
            for callback_lable in range(self.crawer.__CrawlFuncCount__):
                callback = self.crawer.__CrawlFunc__[callback_lable]
                proxies =self.crawer.get_proxies(callback)
                for proxy in proxies:
                    self.redis_cilent.add(proxy)
if __name__ =='__main__':
    a =Getter()
    a.run()
=======
from proxy_pool.Crawler import Crawler
from proxy_pool.Redis_client import Redisclient

full_num = 200

class Getter:

    def __init__(self):
        self.redis_cilent =Redisclient()
        self.crawer = Crawler()

    def _is_full(self):

        if self.redis_cilent.get_count_proxy() >= full_num:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行。。。。。。。。。。。')
        if not self._is_full():
            for callback_lable in range(self.crawer.__CrawlFuncCount__):
                callback = self.crawer.__CrawlFunc__[callback_lable]
                proxies =self.crawer.get_proxies(callback)
                for proxy in proxies:
                    self.redis_cilent.add(proxy)
if __name__ =='__main__':
    a =Getter()
    a.run()
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
