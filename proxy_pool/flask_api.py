<<<<<<< HEAD
from flask import Flask,g
from proxy_pool.Redis_client import Redisclient

__all__ = ['app']
app = Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis = Redisclient()
    return g.redis

@app.route('/')
def index():
    return '<h2>Welcome to Proxy pool</h2>'

@app.route('/random')
def get_proxy():

    '''
    获取随机代理
    :return:
    '''
    conn = get_conn()
    return conn.get_proxy()


@app.route('/count')
def get_counts():
    '''
    获取代理池总量；；
    :return:
    '''
    conn =get_conn()
    return str(conn.get_count_proxy())

if __name__ =='__main__':
=======
from flask import Flask,g
from proxy_pool.Redis_client import Redisclient

__all__ = ['app']
app = Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis = Redisclient()
    return g.redis

@app.route('/')
def index():
    return '<h2>Welcome to Proxy pool</h2>'

@app.route('/random')
def get_proxy():

    '''
    获取随机代理
    :return:
    '''
    conn = get_conn()
    return conn.get_proxy()


@app.route('/count')
def get_counts():
    '''
    获取代理池总量；；
    :return:
    '''
    conn =get_conn()
    return str(conn.get_count_proxy())

if __name__ =='__main__':
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
    app.run()