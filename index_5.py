#coding:utf-8
import sys,os
from PIL import Image,ImageDraw
import random

colors = []


# 降噪
def clearNoise(image):
    for x in range(0,image.size[0]):
        for y in range(0,image.size[1]):
            color = image.getPixel((x,y))
            colors.append(color)


#测试代码
def main():
    #打开图片
    image = Image.open("9.gif")

    #将图片转换成灰度图片
    image = image.convert("L")

    clearNoise(image)
    # print getRadnomPoint(1000)



def kmeans(k,data):

    return data


def getRadnomPoint(max):
    start = random.randint(0,max)
    return start,random.randint(start,max)



if __name__ == '__main__':
    main()