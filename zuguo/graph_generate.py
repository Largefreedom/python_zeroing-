<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  : zeriong；
@个人公众号：Z先生点记；
'''
from pyecharts.charts import Bar
import pandas as pd
import numpy
from pyecharts.charts import Pie
from pyecharts.charts import Line
from pyecharts import options as opts



pd.set_option('display.max_rows', None)
pd.set_option('display.width',None)


def csv_to_txt(id):
    '''
    把csv文件中的评论信息写入txt中去；
    :param id:
    :return:
    '''
    fil_path = 'C:/Users/FREEDOM/Desktop/{}.txt'.format(id)
    csv_path = 'C:/Users/FREEDOM/Desktop/{}.csv'.format(id)
    f =  open(fil_path,'w',encoding='gbk')
    data = pd.read_csv(csv_path,encoding='gbk')
    for i in data['comment']:
        f.write(i)
def line_time_genera():
    '''
    根据三部电影影评的时间分布，
    绘制折线区域图；
    :return:
    '''
    csv_path = 'C:/Users/FREEDOM/Desktop/{}.csv'.format('pandeng')
    csv_path1 = 'C:/Users/FREEDOM/Desktop/{}.csv'.format('zuguo')
    csv_path2 = 'C:/Users/FREEDOM/Desktop/{}.csv'.format('jizhang')

    data_csv =pd.read_csv(csv_path,encoding = 'gbk')
    data_csv1 =pd.read_csv(csv_path1,encoding = 'gbk')
    data_csv2 =pd.read_csv(csv_path2,encoding = 'gbk')

    time_list =[]
    time_list1 =[]
    time_list2 =[]
    '''
    数据处理，时间处理为0：00-01：00的格式；
    '''
    for i,j,k in zip(data_csv['time'],data_csv1['time'],data_csv2['time']):
        new_i = str(i).split(' ')[1].split(':')[0]
        new_i1 = '{}:00-{}.00'.format(new_i,int(new_i)+1)
        new_j = str(j).split(' ')[1].split(':')[0]
        new_j1 = '{}:00-{}.00'.format(new_j, int(new_j) + 1)
        new_k1 = str(k).split(' ')[1].split(':')[0]
        time_list.append(new_i1)
        time_list1.append(new_j1)
        time_list2.append(new_k1)

    dict={}
    dict1 ={}
    dict2  ={}

    a_list =[]
    a_list.extend(sorted(set(time_list2))[:1])
    a_list.extend(sorted(set(time_list2))[-11:-10])
    a_list.extend(sorted(set(time_list2))[-6:])
    a_list.extend(sorted(set(time_list2))[1:-11])

    for j in a_list:
        '''
        若在列表中j存在，则就把j的数量匹配上去，
        否则直接设为0；
        '''
        if j in time_list:
            count =time_list.count(j)
            dict[j] =count
        else:
            dict[j] =0

        if j in time_list1:
            count1 =time_list1.count(j)
            dict1[j] =count1
        else:
            dict1[j] =0

        if j in time_list2:
            count2 =time_list2.count(j)
            dict2[j] =count2
        else:
            dict2[j] =0

    c = (
            Line()
            .add_xaxis(xaxis_data=[i for i in dict.keys()])
            .add_yaxis(
                "《我和我的祖国》",
                y_axis=[j for j in dict1.values()],
                linestyle_opts=opts.LineStyleOpts(width=2),
            )

            .add_yaxis(
                "《攀登者》",
                y_axis=[j for j in dict.values()],
                linestyle_opts=opts.LineStyleOpts(width=2),
            )
                .add_yaxis(
                "《中国机长》",
                y_axis=[j for j in dict2.values()],
                linestyle_opts=opts.LineStyleOpts(width=2),
            )
                .set_series_opts(
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="豆瓣暑假档影评时间分布",subtitle='数据来源：www.douban.com'),
                xaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                    is_scale=False,
                    boundary_gap=False,
                ),
            )
    )
    #生成html网页；
    c.render('line.html')






def generate_pie(id):
    '''
    计算平均分，并且绘制评分占比饼图；
    :param id:
    :return:
    '''
    csv_path = 'C:/Users/FREEDOM/Desktop/{}.csv'.format(id)
    data_csv =pd.read_csv(csv_path,encoding = 'gbk')
    star_list = [] #放置star
    for i in data_csv['star']:
        try:
            print(str(i).replace('0','').replace('[','').replace(']','').replace("'",''))
            if i:
                star_list.append(int(str(i).replace('0','').replace('[','').replace(']','').replace("'",''))*2)
        except:
            print('出局格式出现问题。。')
            pass
    avg = numpy.mean(star_list)#求评分的平均数；
    #求评分的基本分布；
    dict ={}
    for i in set(star_list):
        dict[str(i) +'分'] = star_list.count(i)
    c = Pie()
    c.add("",
                [list(z) for z in zip(dict.keys(), dict.values())],
                radius=["40%", "55%"],
                label_opts=opts.LabelOpts(
                    position="outside",
                    formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c} {per|{d}%}  ",
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=4,
                    rich={
                        "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                        "abg": {
                            "backgroundColor": "#e3e3e3",
                            "width": "100%",
                            "align": "right",
                            "height": 22,
                            "borderRadius": [4, 4, 0,],
                        },
                        "hr": {
                            "borderColor": "#aaa",
                            "width": "100%",
                            "borderWidth": 0.5,
                            "height": 0,
                        },
                        "b": {"fontSize": 16, "lineHeight": 33},
                        "per": {
                            "color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2,
                        },
                    },
                ),
            ).set_global_opts(title_opts=opts.TitleOpts(title="《攀登者》评分占比",subtitle='评分平均为：{}'.format(str(round(avg,1)))))
    c.render('{}_pie.html'.format(id))
    return avg
=======
# -*- encoding: utf-8 -*-
'''
@Author  : zeriong；
@个人公众号：Z先生点记；
'''
from pyecharts.charts import Bar
import pandas as pd
import numpy
from pyecharts.charts import Pie
from pyecharts.charts import Line
from pyecharts import options as opts



pd.set_option('display.max_rows', None)
pd.set_option('display.width',None)


def csv_to_txt(id):
    '''
    把csv文件中的评论信息写入txt中去；
    :param id:
    :return:
    '''
    fil_path = 'C:/Users/FREEDOM/Desktop/{}.txt'.format(id)
    csv_path = 'C:/Users/FREEDOM/Desktop/{}.csv'.format(id)
    f =  open(fil_path,'w',encoding='gbk')
    data = pd.read_csv(csv_path,encoding='gbk')
    for i in data['comment']:
        f.write(i)
def line_time_genera():
    '''
    根据三部电影影评的时间分布，
    绘制折线区域图；
    :return:
    '''
    csv_path = 'C:/Users/FREEDOM/Desktop/{}.csv'.format('pandeng')
    csv_path1 = 'C:/Users/FREEDOM/Desktop/{}.csv'.format('zuguo')
    csv_path2 = 'C:/Users/FREEDOM/Desktop/{}.csv'.format('jizhang')

    data_csv =pd.read_csv(csv_path,encoding = 'gbk')
    data_csv1 =pd.read_csv(csv_path1,encoding = 'gbk')
    data_csv2 =pd.read_csv(csv_path2,encoding = 'gbk')

    time_list =[]
    time_list1 =[]
    time_list2 =[]
    '''
    数据处理，时间处理为0：00-01：00的格式；
    '''
    for i,j,k in zip(data_csv['time'],data_csv1['time'],data_csv2['time']):
        new_i = str(i).split(' ')[1].split(':')[0]
        new_i1 = '{}:00-{}.00'.format(new_i,int(new_i)+1)
        new_j = str(j).split(' ')[1].split(':')[0]
        new_j1 = '{}:00-{}.00'.format(new_j, int(new_j) + 1)
        new_k1 = str(k).split(' ')[1].split(':')[0]
        time_list.append(new_i1)
        time_list1.append(new_j1)
        time_list2.append(new_k1)

    dict={}
    dict1 ={}
    dict2  ={}

    a_list =[]
    a_list.extend(sorted(set(time_list2))[:1])
    a_list.extend(sorted(set(time_list2))[-11:-10])
    a_list.extend(sorted(set(time_list2))[-6:])
    a_list.extend(sorted(set(time_list2))[1:-11])

    for j in a_list:
        '''
        若在列表中j存在，则就把j的数量匹配上去，
        否则直接设为0；
        '''
        if j in time_list:
            count =time_list.count(j)
            dict[j] =count
        else:
            dict[j] =0

        if j in time_list1:
            count1 =time_list1.count(j)
            dict1[j] =count1
        else:
            dict1[j] =0

        if j in time_list2:
            count2 =time_list2.count(j)
            dict2[j] =count2
        else:
            dict2[j] =0

    c = (
            Line()
            .add_xaxis(xaxis_data=[i for i in dict.keys()])
            .add_yaxis(
                "《我和我的祖国》",
                y_axis=[j for j in dict1.values()],
                linestyle_opts=opts.LineStyleOpts(width=2),
            )

            .add_yaxis(
                "《攀登者》",
                y_axis=[j for j in dict.values()],
                linestyle_opts=opts.LineStyleOpts(width=2),
            )
                .add_yaxis(
                "《中国机长》",
                y_axis=[j for j in dict2.values()],
                linestyle_opts=opts.LineStyleOpts(width=2),
            )
                .set_series_opts(
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="豆瓣暑假档影评时间分布",subtitle='数据来源：www.douban.com'),
                xaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                    is_scale=False,
                    boundary_gap=False,
                ),
            )
    )
    #生成html网页；
    c.render('line.html')






def generate_pie(id):
    '''
    计算平均分，并且绘制评分占比饼图；
    :param id:
    :return:
    '''
    csv_path = 'C:/Users/FREEDOM/Desktop/{}.csv'.format(id)
    data_csv =pd.read_csv(csv_path,encoding = 'gbk')
    star_list = [] #放置star
    for i in data_csv['star']:
        try:
            print(str(i).replace('0','').replace('[','').replace(']','').replace("'",''))
            if i:
                star_list.append(int(str(i).replace('0','').replace('[','').replace(']','').replace("'",''))*2)
        except:
            print('出局格式出现问题。。')
            pass
    avg = numpy.mean(star_list)#求评分的平均数；
    #求评分的基本分布；
    dict ={}
    for i in set(star_list):
        dict[str(i) +'分'] = star_list.count(i)
    c = Pie()
    c.add("",
                [list(z) for z in zip(dict.keys(), dict.values())],
                radius=["40%", "55%"],
                label_opts=opts.LabelOpts(
                    position="outside",
                    formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c} {per|{d}%}  ",
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=4,
                    rich={
                        "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                        "abg": {
                            "backgroundColor": "#e3e3e3",
                            "width": "100%",
                            "align": "right",
                            "height": 22,
                            "borderRadius": [4, 4, 0,],
                        },
                        "hr": {
                            "borderColor": "#aaa",
                            "width": "100%",
                            "borderWidth": 0.5,
                            "height": 0,
                        },
                        "b": {"fontSize": 16, "lineHeight": 33},
                        "per": {
                            "color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2,
                        },
                    },
                ),
            ).set_global_opts(title_opts=opts.TitleOpts(title="《攀登者》评分占比",subtitle='评分平均为：{}'.format(str(round(avg,1)))))
    c.render('{}_pie.html'.format(id))
    return avg
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
