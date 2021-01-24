<<<<<<< HEAD
import random
import requests
from pyquery import PyQuery as pq
from urllib.parse import urlencode,quote
import uuid
import time
from lxml import etree
import re


key ='亚马逊大火'
url_list = 'https://weixin.sogou.com/weixin?type=2&query={}'.format(quote(key))


headers_str='''
Host: weixin.sogou.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
'''


def headers_to_dict(headers_str):
    '''
    将headers_str字符串形式转化成字典；；
    :param headers_str:
    :return:
    '''
    headers_str =headers_str.strip()
    headers_dict =dict((i.split(':',1)[0].strip(),i.split(':',1)[1].strip()) for i in headers_str.split('\n'))
    return headers_dict

a_str ='''
uigs_cl	first_click
uigs_refer	https://weixin.sogou.com/
uigs_productid	vs_web
terminal	web
vstype	weixin
pagetype	result
channel	result_article
s_from	input
sourceid	
type	weixin_search_pc
uigs_cookie	SUID,sct
query	亚马逊大火
weixintype	2
exp_status	-1
exp_id_list	0_0
wuid	0071440178DB40975D3C689EE37C6784
rn	1
login	0
uphint	1
bottomhint	1
page	1
exp_id	null_0-null_1-null_2-null_3-null_4-null_5-null_6-null_7-null_8-null_9
time	20914
'''

def str_to_dict(a_str):
    '''
    将a_str形式的字符串转化为字典形式；
    :param a_str:
    :return:
    '''
    str_a =list( i for i in a_str.split('\n') if i !='' )
    str_b ={}
    for a in str_a:
        a1 = a.split('\t')[0]
        a2 =a.split('\t')[1]
        str_b[a1] =a2

    return str_b

b_data =str_to_dict(a_str)
headers =headers_to_dict(headers_str)


def get_suva(sunid):
    '''
    根据sunid来获取suv参数；并添加到cookie众
    :param a: sunid
    :return:
    '''
    b_data['snuid'] = sunid.split('=')[-1]
    b_data['uuid'] = uuid.uuid1()
    b_data['uigs_t'] = str(int(round(time.time() * 1000)))
    url_link = 'https://pb.sogou.com/pv.gif?' + urlencode(b_data)
    res = requests.get(url_link)
    cookie_s = res.headers['Set-Cookie'].split(',')
    cookie_list_s = []
    for i in cookie_s:
        for j in i.split(','):
            if 'SUV' in j:
                cookie_list_s.append(j)
            else:
                continue
    print(cookie_list_s[0].split(';')[0])
    headers['Cookie'] = cookie_list_s[0].split(';')[0]


def get_first_parse(url):
    '''
    1,构造'真'url;
    2,获取正确的动态cookie;
    3,返回真url,访问并解析文章内容
    :param url: 访问的初始url
    :return:
    '''
    #给headers中添加Referer参数；
    headers['Referer'] = url_list
    res =requests.get(url,headers=headers)
    cookies =res.headers['Set-Cookie'].split(';')
    cookie_list_long =[]
    cookie_list2 =[]
    for cookie in cookies:
        cookie_list_long.append(str(cookie).split(','))
    for i in cookie_list_long:
        for set in i:
            if 'SUID' in set or 'SNUID' in set:
                cookie_list2.append(set)
    sunid = cookie_list2[0].split(';')[0]
    get_suva(sunid)
    #构造动态Cookies
    headers['Cookie'] = headers['Cookie'] +';' + ';'.join(cookie_list2)
    url_list11  = pq(res.text)('.news-list li').items()
    for i in url_list11:
        #提取href属性标签
        url_list12 = pq(i('.img-box a').attr('href'))
        url_list12 =str(url_list12).replace('<p>','').replace('</p>','').replace('amp;','')
        print(url_list12)
        #构造参数k与h;
        b = int(random.random() * 100) + 1
        a = url_list12.find("url=")
        result_link = url_list12 + "&k=" + str(b) + "&h=" + url_list12[a + 4 + 21 + b: a + 4 + 21 + b + 1]
        a_url ="https://weixin.sogou.com" +result_link
        second_url =requests.get(a_url,headers=headers).text
        #  获取真实url
        url_text =re.findall("\'(\S+?)\';", second_url, re.S)
        best_url =''.join(url_text)
        last_text =requests.get(url = str(best_url.replace("@", ""))).text
        print(pq(last_text)('#activity-name').text())
        print(pq(last_text)('#js_content > p').text())
        print(pq(last_text)('#js_name').text())
        print(pq(last_text)('#meta_content > span.rich_media_meta.rich_media_meta_text').text())

=======
import random
import requests
from pyquery import PyQuery as pq
from urllib.parse import urlencode,quote
import uuid
import time
from lxml import etree
import re


key ='亚马逊大火'
url_list = 'https://weixin.sogou.com/weixin?type=2&query={}'.format(quote(key))


headers_str='''
Host: weixin.sogou.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
'''


def headers_to_dict(headers_str):
    '''
    将headers_str字符串形式转化成字典；；
    :param headers_str:
    :return:
    '''
    headers_str =headers_str.strip()
    headers_dict =dict((i.split(':',1)[0].strip(),i.split(':',1)[1].strip()) for i in headers_str.split('\n'))
    return headers_dict

a_str ='''
uigs_cl	first_click
uigs_refer	https://weixin.sogou.com/
uigs_productid	vs_web
terminal	web
vstype	weixin
pagetype	result
channel	result_article
s_from	input
sourceid	
type	weixin_search_pc
uigs_cookie	SUID,sct
query	亚马逊大火
weixintype	2
exp_status	-1
exp_id_list	0_0
wuid	0071440178DB40975D3C689EE37C6784
rn	1
login	0
uphint	1
bottomhint	1
page	1
exp_id	null_0-null_1-null_2-null_3-null_4-null_5-null_6-null_7-null_8-null_9
time	20914
'''

def str_to_dict(a_str):
    '''
    将a_str形式的字符串转化为字典形式；
    :param a_str:
    :return:
    '''
    str_a =list( i for i in a_str.split('\n') if i !='' )
    str_b ={}
    for a in str_a:
        a1 = a.split('\t')[0]
        a2 =a.split('\t')[1]
        str_b[a1] =a2

    return str_b

b_data =str_to_dict(a_str)
headers =headers_to_dict(headers_str)


def get_suva(sunid):
    '''
    根据sunid来获取suv参数；并添加到cookie众
    :param a: sunid
    :return:
    '''
    b_data['snuid'] = sunid.split('=')[-1]
    b_data['uuid'] = uuid.uuid1()
    b_data['uigs_t'] = str(int(round(time.time() * 1000)))
    url_link = 'https://pb.sogou.com/pv.gif?' + urlencode(b_data)
    res = requests.get(url_link)
    cookie_s = res.headers['Set-Cookie'].split(',')
    cookie_list_s = []
    for i in cookie_s:
        for j in i.split(','):
            if 'SUV' in j:
                cookie_list_s.append(j)
            else:
                continue
    print(cookie_list_s[0].split(';')[0])
    headers['Cookie'] = cookie_list_s[0].split(';')[0]


def get_first_parse(url):
    '''
    1,构造'真'url;
    2,获取正确的动态cookie;
    3,返回真url,访问并解析文章内容
    :param url: 访问的初始url
    :return:
    '''
    #给headers中添加Referer参数；
    headers['Referer'] = url_list
    res =requests.get(url,headers=headers)
    cookies =res.headers['Set-Cookie'].split(';')
    cookie_list_long =[]
    cookie_list2 =[]
    for cookie in cookies:
        cookie_list_long.append(str(cookie).split(','))
    for i in cookie_list_long:
        for set in i:
            if 'SUID' in set or 'SNUID' in set:
                cookie_list2.append(set)
    sunid = cookie_list2[0].split(';')[0]
    get_suva(sunid)
    #构造动态Cookies
    headers['Cookie'] = headers['Cookie'] +';' + ';'.join(cookie_list2)
    url_list11  = pq(res.text)('.news-list li').items()
    for i in url_list11:
        #提取href属性标签
        url_list12 = pq(i('.img-box a').attr('href'))
        url_list12 =str(url_list12).replace('<p>','').replace('</p>','').replace('amp;','')
        print(url_list12)
        #构造参数k与h;
        b = int(random.random() * 100) + 1
        a = url_list12.find("url=")
        result_link = url_list12 + "&k=" + str(b) + "&h=" + url_list12[a + 4 + 21 + b: a + 4 + 21 + b + 1]
        a_url ="https://weixin.sogou.com" +result_link
        second_url =requests.get(a_url,headers=headers).text
        #  获取真实url
        url_text =re.findall("\'(\S+?)\';", second_url, re.S)
        best_url =''.join(url_text)
        last_text =requests.get(url = str(best_url.replace("@", ""))).text
        print(pq(last_text)('#activity-name').text())
        print(pq(last_text)('#js_content > p').text())
        print(pq(last_text)('#js_name').text())
        print(pq(last_text)('#meta_content > span.rich_media_meta.rich_media_meta_text').text())

>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
get_first_parse(url_list)