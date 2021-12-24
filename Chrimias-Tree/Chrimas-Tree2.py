import turtle as t  # as就是取个别名，后续调用的t都是turtle
from turtle import *
import random as r
import time

n = 100.0

t.pensize(10)  # 修改画笔大小
speed("fastest")  # 定义速度
screensize(bg='black')  # 定义背景颜色，可以自己换颜色
left(90)
forward(3 * n)
color("orange", "yellow")  # 定义最上端星星的颜色，外圈是orange，内部是yellow
begin_fill()
left(126)

for i in range(5):  # 画五角星
    forward(n / 5)
    right(144)  # 五角星的角度
    forward(n / 5)
    left(72)  # 继续换角度
end_fill()
right(126)


def drawlight():  # 定义画彩灯的方法
    if r.randint(0, 30) == 0:  # 如果觉得彩灯太多，可以把取值范围加大一些，对应的灯就会少一些
        color('tomato')  # 定义第一种颜色
        circle(6)  # 定义彩灯大小
    elif r.randint(0, 30) == 1:
        color('orange')  # 定义第二种颜色
        circle(3)  # 定义彩灯大小
    else:
        linewidth = 5
        color('dark green')  # 其余的随机数情况下画空的树枝


color("dark green")  # 定义树枝的颜色
backward(n * 4.8)


def tree(d, s):  # 开始画树
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()  # 同时调用小彩灯的方法
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


tree(15, n)
backward(n / 2)

for i in range(200):  # 循环画最底端的小装饰
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if r.randint(0, 1) == 0:
        color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)

t.color("dark red", "red")  # 定义字体颜色
t.write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))  # 定义文字、位置、字体、大小


def drawsnow():  # 定义画雪花的方法
    t.ht()  # 隐藏笔头，ht=hideturtle
    t.pensize(2)  # 定义笔头大小
    for i in range(200):  # 画多少雪花
        t.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
        t.pu()  # 提笔，pu=penup
        t.setx(r.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
        t.sety(r.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
        t.pd()  # 落笔，pd=pendown
        dens = 6  # 雪花瓣数设为6
        snowsize = r.randint(1, 10)  # 定义雪花大小
        for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            # t.forward(int(snowsize))  #int（）取整数
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
            t.right(int(360 / dens))  # 转动角度


drawsnow()  # 调用画雪花的方法
t.done()  # 完成,否则会直接关闭