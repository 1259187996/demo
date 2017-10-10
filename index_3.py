#coding:utf-8
import sys,os
from PIL import Image,ImageDraw


def getPixel(image,x, y,n):
    points = []
    points.append(image.getpixel((x, y)))
    # points.append(image.getpixel((x - n, y - n)))
    # points.append(image.getpixel((x, y - n)))
    # points.append(image.getpixel((x + n, y - n)))
    # points.append(image.getpixel((x - n, y)))
    points.append(image.getpixel((x + n, y)))
    # points.append(image.getpixel((x - n, y + n)))
    points.append(image.getpixel((x, y + n)))
    points.append(image.getpixel((x + n, y + n)))
    return sum(points)/len(points)

# 降噪
def clearNoise(image,image1,n):
    draw = ImageDraw.Draw(image1)
    for x in range(0,image.size[0]-n):
        for y in range(0,image.size[1]-n):
            color = getPixel(image,x,y,n)
            draw.point((x,y),color)

#测试代码
def main():
    #打开图片
    image = Image.open("9.gif")

    #将图片转换成灰度图片
    image = image.convert("L")

    image1 = Image.new("L",(image.size[0],image.size[1]))

    clearNoise(image,image1,1)

    #保存图片
    image1.save("result_1.png")


if __name__ == '__main__':
    main()