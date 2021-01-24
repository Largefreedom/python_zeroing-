<<<<<<< HEAD
### proxy_pool ip代理池
----
#### 参考来源：崔庆才《python3网阔爬虫开发实战》,github地址：[Proxy_pool](https://github.com/Germey/ProxyPool)
----
**各组分功能**
- Crawler.py 获取代理及代理端口，这里添加了两个代理网址：快代理和66代理；
- Redis_client.py 主要是利用redis数据库对代理的一些基本操作：储存、删除、溢满、获取，并且根据代理的优先级依次进行排序；
- proxy_getter.py  连接爬虫与redis数据库，把爬取的代理放入redis数据库中；
- texter.py  对redis众代理的可用性进行检测，能用的存下来，不可用的删除；
- flask_api.py 本地端web接口，可以将数据库中储存的代理获取出来，利用web接口直接进行访问；
- schedule.py python爬虫调度器，控制proxy_pool各组分的开关，使爬虫协调进行运行；

----

proxy_pool启动方法，同时运行flask_api.py与shedule.py文件，代理可以正常运行。

----

代理获取代码：




----
个人微信公众号：**zeroing说**，期待你的关注！

----


![image](https://i.loli.net/2019/08/24/UljexrzL3kSNXQy.jpg)
=======
### proxy_pool ip代理池
----
#### 参考来源：崔庆才《python3网阔爬虫开发实战》,github地址：[Proxy_pool](https://github.com/Germey/ProxyPool)
----
**各组分功能**
- Crawler.py 获取代理及代理端口，这里添加了两个代理网址：快代理和66代理；
- Redis_client.py 主要是利用redis数据库对代理的一些基本操作：储存、删除、溢满、获取，并且根据代理的优先级依次进行排序；
- proxy_getter.py  连接爬虫与redis数据库，把爬取的代理放入redis数据库中；
- texter.py  对redis众代理的可用性进行检测，能用的存下来，不可用的删除；
- flask_api.py 本地端web接口，可以将数据库中储存的代理获取出来，利用web接口直接进行访问；
- schedule.py python爬虫调度器，控制proxy_pool各组分的开关，使爬虫协调进行运行；

----

proxy_pool启动方法，同时运行flask_api.py与shedule.py文件，代理可以正常运行。

----

代理获取代码：




----
个人微信公众号：**zeroing说**，期待你的关注！

----


![image](https://i.loli.net/2019/08/24/UljexrzL3kSNXQy.jpg)
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
