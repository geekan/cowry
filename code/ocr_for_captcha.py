#encoding=utf-8
import Image,ImageEnhance,ImageFilter
import sys

image_name = "./22.jpeg"

#去处 干扰点
im = Image.open(image_name)
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')

#im.show() #测试查看

s = 12      #启始 切割点 x
t = 2       #启始 切割点 y

w = 10      #切割 宽 +y
h = 15      #切割 长 +x

im_new = []
for i in range(4): #验证码切割
    im1 = im.crop((s+w*i+i*2,t,s+w*(i+1)+i*2,h))
    im_new.append(im1)

#im_new[0].show()#测试查看

xsize, ysize = im_new[0].size
gd = []
for i in range(ysize):
    tmp=[]
    for j in range(xsize):
        if( im_new[0].getpixel((j,i)) == 255 ):
            tmp.append(1)
        else:
            tmp.append(0)
    gd.append(tmp)

#看效果
for i in range(ysize):
    print gd[i]
