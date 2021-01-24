'''
@author:zeroing
@wx公众号：小张Python

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from pyquery import PyQuery as pq
import re



class JD_Spider:

    def __init__(self,item_name,txt_path):
        url = 'https://www.jd.com/' # 登录网址
        self.url = url
        self.item_name = item_name

        self.txt_file = open(txt_path,encoding='utf-8',mode='w+')

        options = webdriver.ChromeOptions() # 谷歌选项

        # 设置为开发者模式，避免被识别
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])
        self.browser  = webdriver.Chrome(executable_path= "C:/Program Files/Google/Chrome/Application/chromedriver.exe",
                                         options = options)
        self.wait   =  WebDriverWait(self.browser,2)


    def run(self):
        """登陆接口"""
        self.browser.get(self.url)

            # 这里设置等待：等待输入框
            # login_element = self.wait.until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, 'div.input-plain-wrap > .fm-text')))

        input_edit = self.browser.find_element(By.CSS_SELECTOR,'#key')
        input_edit.clear()
        input_edit.send_keys(self.item_name)


        search_button = self.browser.find_element(By.CSS_SELECTOR,'#search > div > div.form > button')
        search_button.click()# 点击
        time.sleep(2)

        html = self.browser.page_source # 获取 html
        self.parse_html(html)
        current_url = self.browser.current_url # 获取当前页面 url
        initial_url = str(current_url).split('&pvid')[0]

        for i in range(1,100):
            try:
                print('正在解析----------------{}图片'.format(str(i)))
                next_page_url = initial_url + '&page={}&s={}&click=0'.format(str(i*2+1),str(i*60+1))
                print(next_page_url)
                self.browser.get(next_page_url)

                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_goodsList > ul > li')))
                html = self.browser.page_source
                self.parse_html(html)# 对 html 网址进行解析
                time.sleep(2) # 设置频率
            except Exception as e:
                print('Error Next page',e)
                self.txt_file.close()# 关闭 txt 文件


    def parse_html(self,html):

        doc = pq(html)
        items = doc('#J_goodsList > ul > li').items()
        for item in items:
            try:


                product = {
                    'name': item.find('div > div.p-name > a > em').text().replace('\n','\t') if item.find('div > div.p-name > a > em').text() else "None",
                    'price': item.find('div > div.p-price > strong > i').text().replace('\n','\t') if item.find('div > div.p-price > strong > i').text() else "None",
                    'commit': item.find('div > div.p-commit > strong > a').text().replace('\n','\t') if item.find('div > div.p-commit > strong > a').text() else "None",
                    'author': item.find('div > div.p-bookdetails > span.p-bi-name > a').text()if item.find('div > div.p-bookdetails > span.p-bi-name > a').text() else "None",
                    'store': item.find('div > div.p-shopnum > a').text().replace(' |', '').replace('\n','\t') if item.find('div > div.p-shopnum > a').text() else "None",

                    'img': str(re.findall('.*?data-lazy-img="(//.*?.jpg)" source-data-lazy-img=.*?',str(item.find('div > div.p-img > a > img')))) or  str(re.findall('.*?"" src=(//.*?)" style="".*?',str(item.find('div > div.p-img > a > img')))) if item.find('div > div.p-img > a > img') else "None"
                }
                print(product)
                self.txt_file.write(','.join([product['name'],product['price'],product['commit'],product['author'],product['store'],product['img']]))
                self.txt_file.write('\n')
            except Exception as e:
                print('Error {}'.format(e))
            # self.txt_file.close()



if __name__ =='__main__':
    item_name = 'Python书籍'
    txt_name = 'jd_item.txt'
    spider = JD_Spider(item_name,txt_name)
    spider.run()