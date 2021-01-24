<<<<<<< HEAD
import random
import redis

REDIS_HOST ='Localhost'
REDIS_PORT = 6379
REDIS_KEY = 'proxies'
#初始的分数
INITIAL_SCORE = 10
#最小分数
MIN_SCORE = 0
#最大分数
MAX_SCORE = 100
class Redisclient:


    def __init__(self,host =REDIS_HOST,port =REDIS_PORT):
        self.redisdb =redis.StrictRedis(host,port)

    def add(self,proxy,score =INITIAL_SCORE):
        '''
        proxy若没有添加到redis数据库中，
            利用redisdb.zadd函数进行添加；
        '''
        if not self.redisdb.zscore(REDIS_KEY,proxy):
            print('保存代理', proxy, '成功！')
            return self.redisdb.zadd(REDIS_KEY,score,proxy)


    def get_proxy(self):

        #利用zrangebyscore函数REDIS_KEY进行排序；
        res =self.redisdb.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)

        if len(res):
            proxy = random.choice(res)
            print('正在获取代理：',proxy)
        else:
            '''
            redis中没有分数为100的代理，      
                利用zrevrange函数对REDIS_KEY进行从大到小排序，取前10个代理中的一个；
            '''
            if self.redisdb.zrevrange(REDIS_KEY,0,10):
                proxy = random.choice(self.redisdb.zrevrange(REDIS_KEY,0,10))
            else:
                print('获取代理出错，ERROR')
                raise Exception
        return proxy


    #删除无用代理；
    def decrease_proxy(self,proxy):
        '''
        模块目的删除redis数据库中无用代理；
        ，获取代理分数，若不可用，降10分，
            若为0分时，代理直接删除；
        '''
        score = self.redisdb.zscore(REDIS_KEY,proxy)

        if score  > MIN_SCORE:
            print('代理',proxy,'当前分数',score,'减10')
            self.redisdb.zincrby(REDIS_KEY,proxy,-10)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            self.redisdb.zrem(REDIS_KEY,proxy)


    def exist_proxy(self,proxy):

        score = self.redisdb.zscore(REDIS_KEY,proxy)

        if score:
            return True
        else:
            return False

    def max(self,proxy):
        '''

        检测到代理可用，直接将分数设置为100；
        '''
        print('代理',proxy,'可用','设置为',MAX_SCORE)
        self.redisdb.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def get_count_proxy(self):

        #获取redis数据库中的代理数量；
        return self.redisdb.zcard(REDIS_KEY)

    def  get_all_prpxy(self):
        '''
        获取全部代理；；
        :return:
        '''
=======
import random
import redis

REDIS_HOST ='Localhost'
REDIS_PORT = 6379
REDIS_KEY = 'proxies'
#初始的分数
INITIAL_SCORE = 10
#最小分数
MIN_SCORE = 0
#最大分数
MAX_SCORE = 100
class Redisclient:


    def __init__(self,host =REDIS_HOST,port =REDIS_PORT):
        self.redisdb =redis.StrictRedis(host,port)

    def add(self,proxy,score =INITIAL_SCORE):
        '''
        proxy若没有添加到redis数据库中，
            利用redisdb.zadd函数进行添加；
        '''
        if not self.redisdb.zscore(REDIS_KEY,proxy):
            print('保存代理', proxy, '成功！')
            return self.redisdb.zadd(REDIS_KEY,score,proxy)


    def get_proxy(self):

        #利用zrangebyscore函数REDIS_KEY进行排序；
        res =self.redisdb.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)

        if len(res):
            proxy = random.choice(res)
            print('正在获取代理：',proxy)
        else:
            '''
            redis中没有分数为100的代理，      
                利用zrevrange函数对REDIS_KEY进行从大到小排序，取前10个代理中的一个；
            '''
            if self.redisdb.zrevrange(REDIS_KEY,0,10):
                proxy = random.choice(self.redisdb.zrevrange(REDIS_KEY,0,10))
            else:
                print('获取代理出错，ERROR')
                raise Exception
        return proxy


    #删除无用代理；
    def decrease_proxy(self,proxy):
        '''
        模块目的删除redis数据库中无用代理；
        ，获取代理分数，若不可用，降10分，
            若为0分时，代理直接删除；
        '''
        score = self.redisdb.zscore(REDIS_KEY,proxy)

        if score  > MIN_SCORE:
            print('代理',proxy,'当前分数',score,'减10')
            self.redisdb.zincrby(REDIS_KEY,proxy,-10)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            self.redisdb.zrem(REDIS_KEY,proxy)


    def exist_proxy(self,proxy):

        score = self.redisdb.zscore(REDIS_KEY,proxy)

        if score:
            return True
        else:
            return False

    def max(self,proxy):
        '''

        检测到代理可用，直接将分数设置为100；
        '''
        print('代理',proxy,'可用','设置为',MAX_SCORE)
        self.redisdb.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def get_count_proxy(self):

        #获取redis数据库中的代理数量；
        return self.redisdb.zcard(REDIS_KEY)

    def  get_all_prpxy(self):
        '''
        获取全部代理；；
        :return:
        '''
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
        return self.redisdb.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)