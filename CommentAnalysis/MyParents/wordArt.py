# -*- encoding: utf-8 -*-
'''
@Author  : zeriong；
@个人公众号：小张Python；
'''
import random

from PIL import Image
import os
import pymongo
import requests
from io import  BytesIO
import re
from wordcloud import WordCloud
from  collections import  Counter
import matplotlib.pyplot as plt
import numpy as np


# 连接数据库
client =pymongo.MongoClient('localhost',27017)
db = client.admin
sn_collect = db['shaonian']
parent_collect = db['myParent']
changjinhu_collect = db['changjinhu']



def calcate_word_freq(word_path):
    word_list = []
    with open(word_path, encoding='utf-8') as f:
        words = f.read()
        for word in words.split('\n'):
            for item_value in word.split(','):  #
                if re.findall('[\u4e00-\u9fa5]+', str(item_value), re.S) and len(item_value) > 1:  # 正则表达式匹配中文字符
                    word_list.append(item_value)
    return word_list



def AliceWord(word_list,open_path,save_path):
    # 生成词云图
    counter = Counter(word_list)  # 计算词频；
    start = random.randint(0, 15)  # 随机取0-15中间一个数字;
    result_dict = dict(counter.most_common()[start:])  # 在 counter 中取前start 个元素；

    # x, y = np.ogrid[:300, :300]  # 创建0-300二维数组；
    # mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2  # 创建以 150，150为圆心，半径为130的Mask；
    # mask = 255 * mask.astype(int)  # 转化为 int

    # 读取图片作为 Mask
    alic_coloring = np.array(Image.open(open_path))
    # 对某些不是纯白色的背景置为 255
    # alic_coloring[alic_coloring<10] =255
    # alic_coloring[alic_coloring!=10] = 255
    wc = WordCloud(background_color = "black",# 设置背景颜色

                   mode ="RGB",
                   mask=alic_coloring,# 为None时，自动创建一个二值化图像，长400，宽200；
                   min_font_size=4,#  使用词的最小频率限定；
                   relative_scaling= 0.8,# 词频与大小相关性
                   font_path="img/simkai.ttf",  # 字体路径，用于设置中文,
                   ).generate_from_frequencies(result_dict)

    wc.to_file(save_path)# 把生成的词云图进行保存
    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    plt.show()


word_list = calcate_word_freq("img/parent.txt")
AliceWord(word_list,"img/images.jpg","img/parent.png")


