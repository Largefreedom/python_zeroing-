<<<<<<< HEAD
from multiprocessing import Process
from proxy_pool.flask_api import app
from proxy_pool.texter import Tester
from proxy_pool.proxy_getter import Getter
import time

API_HOST = '127.0.0.1'
API_PORT =5000

TSTER_CYCLE = 20
GETTER_CYCLE =20
TESTER_ENABLED = True
GETTER_ENABLED =True
API_ENABLED =True


class Sheduler():
    def schedule_tester(self):
        '''
        定时测试代理
        :param cycle:
        :return:
        '''
        tester =Tester()

        print('开始测试代理')
        tester.run()


    def schedule_getter(self):
        '''
        定时获取代理；
        :param cycle:
        :return:
        '''
        getter = Getter()

        print('开始抓代理！！！！')
        getter.run()



    def shedule_api(self):
        '''
        开启代理：
        :return:
        '''

        app.run(API_HOST,API_PORT)


    def run(self):
        print('代理池正在运行')
        while True:
            if TESTER_ENABLED:
                tester_process = Process(target = self.schedule_tester())
                tester_process.start()
            print('抓取器开始运行：-----------')
            if GETTER_ENABLED:
                getter_process = Process(target=self.schedule_getter())
                getter_process.start()
            time.sleep(10)
            print('打开api_________________________')

if __name__ =='__main__':
    a =Sheduler()
=======
from multiprocessing import Process
from proxy_pool.flask_api import app
from proxy_pool.texter import Tester
from proxy_pool.proxy_getter import Getter
import time

API_HOST = '127.0.0.1'
API_PORT =5000

TSTER_CYCLE = 20
GETTER_CYCLE =20
TESTER_ENABLED = True
GETTER_ENABLED =True
API_ENABLED =True


class Sheduler():
    def schedule_tester(self):
        '''
        定时测试代理
        :param cycle:
        :return:
        '''
        tester =Tester()

        print('开始测试代理')
        tester.run()


    def schedule_getter(self):
        '''
        定时获取代理；
        :param cycle:
        :return:
        '''
        getter = Getter()

        print('开始抓代理！！！！')
        getter.run()



    def shedule_api(self):
        '''
        开启代理：
        :return:
        '''

        app.run(API_HOST,API_PORT)


    def run(self):
        print('代理池正在运行')
        while True:
            if TESTER_ENABLED:
                tester_process = Process(target = self.schedule_tester())
                tester_process.start()
            print('抓取器开始运行：-----------')
            if GETTER_ENABLED:
                getter_process = Process(target=self.schedule_getter())
                getter_process.start()
            time.sleep(10)
            print('打开api_________________________')

if __name__ =='__main__':
    a =Sheduler()
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
    a.run()