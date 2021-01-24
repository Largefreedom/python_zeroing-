<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  : zeriong；
@个人公众号：Z先生点记；
'''
from PIL import Image
import os

id ='jizhang'

img_path ='C:/Users/FREEDOM/Desktop/jizhang1.png'
#自己找的的模板图片存储地址，需要是矢量图

#这个是我获取图片存放的文件夹，根据自己情况进行设置；
folder ='C:/Users/FREEDOM/Desktop/{}'.format(id)

#拼接后图片的存放位置
save_pic_path ='C:/Users/FREEDOM/Desktop/{}.jpg'.format(id)

img =Image.open(img_path)
w,h =img.size#获取图片大小
new_img = Image.new('RGB',(w,h),'#FFFFFF')#创建新的图片，大小与原图片一样
unit_size =60

y_index = h//unit_size
x_index = w//unit_size#双斜杠表示：先做除法，再向下取整；

pic_list = []

for i in os.listdir(folder):
    print(i)
    if i.endswith('.jpg'):
        pic_list.append(i)

total =len(pic_list)
x = 0
y = 0

for i in range(x_index*y_index):
    '''
    把folder中存放的图片集贴入到你想要贴的图片上，
    '''
    print(f'目前进度为{i}\{x_index*y_index}')
    try:
        #利用 Image.resize()来规定图片大小，其中Image.ANATILAS表示的是高质量图片；
        test = Image.open('{}/{}'.format(folder,pic_list[i%total])).resize((unit_size,unit_size),Image.ANTIALIAS)
        new_img.paste(test, (x * unit_size, y * unit_size))
        x += 1
    except IOError:
        print('读取一张图片失败')
    #一排已经扫描完毕
    if x==x_index:
        x =0
        y +=1
print('素材扫描完毕')
new_img.save(save_pic_path,quality =100)
# src为刚刚保存的图片
src = Image.open(save_pic_path)

#src1为原来要贴的图片
src1 =Image.open(img_path)

#把scr1贴到scr上面；
src.paste(src1,(0,0),src1)

#图片进行保存；
src.save('{}.png'.format(id))
=======
# -*- encoding: utf-8 -*-
'''
@Author  : zeriong；
@个人公众号：Z先生点记；
'''
from PIL import Image
import os

id ='jizhang'

img_path ='C:/Users/FREEDOM/Desktop/jizhang1.png'
#自己找的的模板图片存储地址，需要是矢量图

#这个是我获取图片存放的文件夹，根据自己情况进行设置；
folder ='C:/Users/FREEDOM/Desktop/{}'.format(id)

#拼接后图片的存放位置
save_pic_path ='C:/Users/FREEDOM/Desktop/{}.jpg'.format(id)

img =Image.open(img_path)
w,h =img.size#获取图片大小
new_img = Image.new('RGB',(w,h),'#FFFFFF')#创建新的图片，大小与原图片一样
unit_size =60

y_index = h//unit_size
x_index = w//unit_size#双斜杠表示：先做除法，再向下取整；

pic_list = []

for i in os.listdir(folder):
    print(i)
    if i.endswith('.jpg'):
        pic_list.append(i)

total =len(pic_list)
x = 0
y = 0

for i in range(x_index*y_index):
    '''
    把folder中存放的图片集贴入到你想要贴的图片上，
    '''
    print(f'目前进度为{i}\{x_index*y_index}')
    try:
        #利用 Image.resize()来规定图片大小，其中Image.ANATILAS表示的是高质量图片；
        test = Image.open('{}/{}'.format(folder,pic_list[i%total])).resize((unit_size,unit_size),Image.ANTIALIAS)
        new_img.paste(test, (x * unit_size, y * unit_size))
        x += 1
    except IOError:
        print('读取一张图片失败')
    #一排已经扫描完毕
    if x==x_index:
        x =0
        y +=1
print('素材扫描完毕')
new_img.save(save_pic_path,quality =100)
# src为刚刚保存的图片
src = Image.open(save_pic_path)

#src1为原来要贴的图片
src1 =Image.open(img_path)

#把scr1贴到scr上面；
src.paste(src1,(0,0),src1)

#图片进行保存；
src.save('{}.png'.format(id))
>>>>>>> 440cb3c73b56b7f7ab170a9a061be8acbc44db7b
