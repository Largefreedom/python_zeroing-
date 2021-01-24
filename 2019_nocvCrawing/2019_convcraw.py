import requests
import re
import json
import time
import  random
import os
from fake_useragent import  UserAgent
import datetime
import xlsxwriter
import traceback
from bs4 import BeautifulSoup as bs



class Crawer(requests.Session):

    def __init__(self,file_path,time1):
        super().__init__()

        User_Agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        self.time_out = 10
        self.headers =dict()
        self.headers['User-Agent'] = User_Agent
        self.file_path = file_path
        self.url = 'https://3g.dxy.cn/newh5/view/pneumonia'
        self.time_format = time.strftime('%Y_%m_%d_%H',time1)
        self.build_file()
        self.reauest_url(self.url)



    def build_file(self):

        file_path  = os.path.join(self.file_path,'virus_{}.xlsx'.format(self.time_format))
        self.workbook = xlsxwriter.Workbook(file_path)
        self.country_sheet = self.workbook.add_worksheet('World')
        self.province_sheet = self.workbook.add_worksheet('Province')
        self.area_sheet = self.workbook.add_worksheet('Area')
        self.total_sheet= self.workbook.add_worksheet('total')

    def reauest_url(self,url):
        try:

            res =requests.get(url,headers =self.headers,timeout = self.time_out)
            res_soup = bs(res.content,'lxml')
            total_conuntry = re.findall(r'\{("id".*?)\}',str(res_soup.find('script', attrs={'id': 'getListByCountryTypeService2'})))
            self.parse_country(total_conuntry)
            province_conuntry = re.findall(r'\{("id".*?)\}',str(res_soup.find('script', attrs={'id': 'getListByCountryTypeService1'})))
            self.parse_province(province_conuntry)
            area_conuntry = re.findall(r'\[({".*?})\]',str(res_soup.find('script', attrs={'id': 'getAreaStat'})))
            self.parse_area(area_conuntry)
            total_all = re.findall(r'("confirmedCount".*?"seriousIncr":\d+)',str(res_soup.find('script', attrs={'id': 'getStatisticsService'})))
            self.parse_total_all(total_all)
            self.workbook.close()
            print('解析结束！！！！！！！！！！！！！！！！！！！！！！')
        except Exception as e:
            print(e)
            print('错误地址为+'+ traceback.format_exc())
            print('访问错误！！！')

    def parse_area(self,area_conuntry):

        try:
            s1_row,s1_col = 0,0
            self.area_sheet.write(s1_row,s1_col,'Time')
            s1_col +=1
            self.area_sheet.write(s1_row,s1_col,'cityName')
            s1_col +=1
            self.area_sheet.write(s1_row, s1_col, 'confirmedCount')
            s1_col += 1
            self.area_sheet.write(s1_row, s1_col, 'suspectedCount')
            s1_col += 1
            self.area_sheet.write(s1_row, s1_col, 'curedCount')
            s1_col += 1
            self.area_sheet.write(s1_row, s1_col, 'deadCount')
            s1_col += 1

            area_list_total = list()
            for i in area_conuntry:
                area_list = dict()
                if '},{' in i:

                    a_list = [str(j).strip('}').strip('{') for j in i.split('},{')]
                    for l_11 in a_list:
                        s1_row += 1
                        s1_col = 0
                        for l_1 in l_11.split(','):
                            key_1 = str(l_1).split(':')[0].strip('[').strip('{').strip('"')
                            value_1 = str(l_1).split(':')[-1]

                            if key_1 == 'cityName':
                                area_list[key_1] =value_1
                            elif key_1 =='confirmedCount':
                                area_list[key_1] =int(value_1)
                            elif key_1 =='suspectedCount':
                                area_list[key_1] =int(value_1)
                            elif key_1 =='curedCount':
                                area_list[key_1] =int(value_1)
                            elif key_1 =='deadCount':
                                area_list[key_1] = int(value_1)
                            else:
                                pass
                        if  'cityName' not in area_list.keys():
                            area_list['cityName'] = '武汉'
                        print(area_list)

                        self.area_sheet.write(s1_row,s1_col,str(self.time_format))
                        s1_col +=1
                        self.area_sheet.write(s1_row, s1_col, str(area_list['cityName']))
                        s1_col += 1
                        self.area_sheet.write(s1_row, s1_col, str(area_list['confirmedCount']))
                        s1_col += 1
                        self.area_sheet.write(s1_row, s1_col, str(area_list['suspectedCount']))
                        s1_col += 1
                        self.area_sheet.write(s1_row, s1_col, str(area_list['curedCount']))
                        s1_col += 1
                        self.area_sheet.write(s1_row, s1_col, str(area_list['deadCount']))
                        s1_col += 1


                        area_list_total.append(area_list)
                else:
                    s1_col = 0
                    s1_row += 1
                    new_stri = str(i).strip('}').strip('{')
                    for j in new_stri.split(','):
                        key_1 = str(j).split(':')[0].strip('"')
                        value_1 = str(j).split(':')[-1].strip('"')

                        if key_1 == 'cityName':
                            area_list[key_1] = value_1
                        elif key_1=='confirmedCount':
                            area_list[key_1] = int(value_1)
                        elif key_1 =='suspectedCount':
                            area_list[key_1] =int(value_1)
                        elif key_1 == 'curedCount':
                            area_list[key_1] =int(value_1)
                        elif key_1 == 'deadCount':
                            area_list[key_1] =int(value_1)

                        else:
                            pass
                    print(area_list)
                    self.area_sheet.write(s1_row, s1_col, str(self.time_format))
                    s1_col += 1
                    self.area_sheet.write(s1_row, s1_col, str(area_list['cityName']))
                    s1_col += 1
                    self.area_sheet.write(s1_row, s1_col, str(area_list['confirmedCount']))
                    s1_col += 1
                    self.area_sheet.write(s1_row, s1_col, str(area_list['suspectedCount']))
                    s1_col += 1
                    self.area_sheet.write(s1_row, s1_col, str(area_list['curedCount']))
                    s1_col += 1
                    self.area_sheet.write(s1_row, s1_col, str(area_list['deadCount']))
                    s1_col += 1
                    area_list_total.append(area_list)
        except Exception as e:
            print(e)
            print('Error !!! Parse area error !!!!')


    def parse_province(self,province_conuntry):
        try:
            s1_row, s1_col = 0, 0
            self.province_sheet.write(s1_row, s1_col, 'Time')
            s1_col += 1
            self.province_sheet.write(s1_row, s1_col, 'provinceShortName')
            s1_col += 1
            self.province_sheet.write(s1_row, s1_col, 'confirmedCount')
            s1_col += 1
            self.province_sheet.write(s1_row, s1_col, 'suspectedCount')
            s1_col += 1
            self.province_sheet.write(s1_row, s1_col, 'curedCount')
            s1_col += 1
            self.province_sheet.write(s1_row, s1_col, 'deadCount')
            s1_col += 1
            province_list = list()
            # print(province_conuntry)
            for i in province_conuntry:
                s1_row += 1
                s1_col = 0
                item_list = dict()
                for j in i.split(','):
                    key_1 = str(j).split(':')[0].strip('"')
                    value_1 = str(j).split(':')[-1].strip('"')
                    if key_1 =='provinceShortName':
                        item_list[key_1] = value_1
                    elif key_1 =='confirmedCount':
                        item_list[key_1] = int(value_1)
                    elif key_1 =='suspectedCount':
                        item_list[key_1] = int(value_1)
                    elif key_1 =='curedCount':
                        item_list[key_1] = int(value_1)
                    elif key_1=='deadCount':
                        item_list[key_1] =int(value_1)
                    else:
                        pass
                print(item_list)
                self.province_sheet.write(s1_row, s1_col, str(self.time_format))
                s1_col += 1
                self.province_sheet.write(s1_row, s1_col, str(item_list['provinceShortName']))
                s1_col += 1
                self.province_sheet.write(s1_row, s1_col, str(item_list['confirmedCount']))
                s1_col += 1
                self.province_sheet.write(s1_row, s1_col, str(item_list['suspectedCount']))
                s1_col += 1
                self.province_sheet.write(s1_row, s1_col, str(item_list['curedCount']))
                s1_col += 1
                self.province_sheet.write(s1_row, s1_col, str(item_list['deadCount']))
                s1_col += 1
                province_list.append(item_list)
        except Exception as e:
            print(e)
            print('Error !!!!, Parse province error!')



    def parse_country(self,total_conuntry_list):
        total_country_lis = list()
        try:

            s1_row, s1_col = 0, 0
            self.country_sheet.write(s1_row, s1_col, 'Time')
            s1_col += 1
            self.country_sheet.write(s1_row, s1_col, 'provinceName')
            s1_col += 1
            self.country_sheet.write(s1_row, s1_col, 'confirmedCount')
            s1_col += 1
            self.country_sheet.write(s1_row, s1_col, 'suspectedCount')
            s1_col += 1
            self.country_sheet.write(s1_row, s1_col, 'curedCount')
            s1_col += 1
            self.country_sheet.write(s1_row, s1_col, 'deadCount')
            s1_col += 1
            for i in total_conuntry_list:
                item_dict =dict()
                s1_row += 1
                s1_col = 0
                i_list = [j for j in i.split(',')]
                for m in i_list:
                    key_1 = m.split(':')[0].strip('"')
                    value_1 = m.split(':')[-1].strip('"')
                    if key_1 =='provinceName':
                        item_dict[key_1] = value_1
                    elif key_1 =='confirmedCount':
                        item_dict[key_1] = int(value_1)
                    elif key_1 =='suspectedCount':
                        item_dict[key_1] =int(value_1)
                    elif key_1 =='curedCount':
                        item_dict[key_1] = int(value_1)
                    elif key_1=='deadCount':
                        item_dict[key_1] = value_1
                    else:
                        pass
                print(item_dict)
                self.country_sheet.write(s1_row, s1_col, str(self.time_format))
                s1_col += 1
                self.country_sheet.write(s1_row, s1_col, str(item_dict['provinceName']))
                s1_col += 1
                self.country_sheet.write(s1_row, s1_col, str(item_dict['confirmedCount']))
                s1_col += 1
                self.country_sheet.write(s1_row, s1_col, str(item_dict['suspectedCount']))
                s1_col += 1
                self.country_sheet.write(s1_row, s1_col, str(item_dict['curedCount']))
                s1_col += 1
                self.country_sheet.write(s1_row, s1_col, str(item_dict['deadCount']))
                s1_col += 1
                total_country_lis.append(item_dict)
        except Exception as e:
            print(e)
            print('Error !!!!! Parse Country failed')


    def parse_total_all(self,a_list):

        try:
            s1_row,s1_col = 0,0
            a_list = a_list[0]
            list_1 = [ i for i in a_list.split(',')]
            total_dict =dict()
            for i in list_1:
                key_1 = i.split(':')[0].strip('"')
                value_1 = int(i.split(':')[-1])
                total_dict[key_1] = value_1
            print(total_dict)
            for i in total_dict.keys():
                self.total_sheet.write(s1_row,s1_col,str(i))
                s1_col +=1
            s1_row +=1
            s1_col =0
            for j in total_dict.values():
                self.total_sheet.write(s1_row,s1_col,str(j))
                s1_col += 1
        except Exception as e:
            print(e)
            print('total_all解析错误！！！')

if __name__ =='__main__':
    time2 = int(time.time())
    time_1 = time.localtime(time2)
    file_path = 'E:/ceshi/feiyan'
    Crawer(file_path,time_1)
