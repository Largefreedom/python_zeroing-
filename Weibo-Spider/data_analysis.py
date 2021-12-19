
import jieba
import jieba.analyse
from datetime import datetime
from PIL import Image
import pymongo
import re
from wordcloud import WordCloud
from  collections import  Counter
import matplotlib.pyplot as plt
import numpy as np
import random
from collections import Counter

collection_name ='Weibo-wlh-Comment'
client =pymongo.MongoClient('localhost',27017)
db = client.admin
now_exits_collection = db.list_collection_names()
if(collection_name in  now_exits_collection):
    # 判断是否存在对应 Document
    collection = db[collection_name]
else:
    db.create_collection(name=collection_name)
    collection = db[collection_name]


def conver_timeformat(timeStr):
    '时间格式转换'
    if "今天" in timeStr:
        result  = re.search("今天[\s\S](\d{1,2}):(\d{1,2})",timeStr)
        if(len(result.groups()) ==2):
            timeInfo = format(datetime(year=2021,
                                month=12,
                                day=19,
                                hour=int(result.group(1)),
                                minute= int(result.group(2)),
                                second=0),
                              "%Y-%m-%d %H:%M:%S")
        else:
            timeInfo = format(datetime.now(),"%Y-%m-%d %H:%M:%S")
        return timeInfo
    if "分钟" in timeStr:
        timeInfo = format(datetime.now(), "%Y-%m-%d %H:%M:%S")
        return  timeInfo

    if "月" in timeStr:
        result = re.search("(\d{1,2})月(\d{1,2})日[\s\S](\d{1,2}):(\d{1,2})", timeStr)
        if (len(result.groups()) == 4):
            timeInfo = format(datetime(year=2021,
                                       month=int(result.group(1)),
                                       day=int(result.group(2)),
                                       hour=int(result.group(3)),
                                       minute=int(result.group(4)),
                                       second= 0),
                              "%Y-%m-%d %H:%M:%S")
            return timeInfo
    raise RuntimeError("{} 时间格式无法转换".format(timeStr))


def jieba_analysis(strText):
    # 设置停用词
    word_list = jieba.lcut(strText)
    return ' '.join(word_list)


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
    f = open("file/stop_words.txt", encoding="utf-8", mode="r")
    stop_words = f.readlines()
    wc = WordCloud(background_color = "white",  # 设置背景颜色
                   mode ="RGB",
                   mask=alic_coloring,  # 为None时，自动创建一个二值化图像，长400，宽200；
                   min_font_size=4,  #  使用词的最小频率限定；
                   stopwords = set(stop_words),

                   relative_scaling= 0.8,  # 词频与大小相关性
                   font_path="file/simkai.ttf",  # 字体路径，用于设置中文,
                   ).generate_from_frequencies(result_dict)

    wc.to_file(save_path)# 把生成的词云图进行保存
    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    plt.show()


def data_mine():
    # 数据清洗
    dictList = []
    content_list = []
    total_timeformat_list = []
    for userName in collection.distinct(key="userName"):
        item = collection.find_one({"userName":userName})
        item['timeInfo'] = conver_timeformat(item['timeInfo'])
        likeCount = re.search(r'(\d+)',item["likeCount"])
        item['likeCount'] = likeCount.group(1)
        # 时间格式转化为 '2021-12-18 00'
        time_format = datetime.strptime(item['timeInfo'][:-6],'%Y-%m-%d %H').replace(minute=0,second=0)
        time_format = time_format.strftime("%Y-%m-%d %H:%M:%S")
        total_timeformat_list.append(time_format)

        # item 转化为 {'_id': ObjectId('61bf5825d0df3b7b1e41a002'), 'userName': '鬼酱速报', 'comment': '多多少少听说过一些，我相信是真的', 'likeCount': '2515', 'timeInfo': '2021-12-17 23:18:00'}
        dictList.append(item)
        content_list.append(item['comment'])

    totalStr = ' '.join(content_list)
    jieba_result = jieba_analysis(totalStr)
    # AliceWord(jieba_result,"img/images.jpg","img/parent.png")
    print(totalStr)
    print(total_timeformat_list)
    dict_counter = dict(Counter(total_timeformat_list))
    result_list = []
    for item in dict_counter.items():
        list_item = []
        list_item.append(item[0])
        list_item.append(item[1])
        result_list.append(list_item)

    # 排序
    result_list.sort(key=lambda x:x[0])
    dictList.sort(key=lambda x:int(x['likeCount']))
    print(result_list)
    print(dictList)










