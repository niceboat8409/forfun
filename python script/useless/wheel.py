import cv2
import aircv as ac
import numpy as np
import sys
import aircv as ac
import os
import time
from PIL import Image
from aip import AipOcr

k = 0
swait = 5
wait = 30 
lwait = 200
tlwait = 600

APP_ID = '20417580'
API_KEY = 'lw5kukrdvC0AHYhjg8GV3w0H'
SECRET_KEY = 'c6HzSikSi4eZAVVdRkGvwj4Dia4bz2cx'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


"""
参数
"""
k = 1
way = ".png"
password=939117252
inpath = r"C:/Users/93911\Desktop/" 
key =inpath +  "%i" % k +way
findnum = r".\short/crop_test1.png"
waitForcheck = r"C:/Users/93911\Desktop\screen.png"
pointxpath = r"C:/Users/93911\Desktop/5.png" 



nice = (847,476)
#可以公用的点
ak = [572,101,62,86]
#主页体力格子
hp = [854,18,21,43]
#右上角体力点
cost = [890,509,16,30]
#关卡消耗
wpath = r"C:/Users/93911\Desktop/"
png = r".png "
cutpath = r"F:/pic\AK\short/crop_test1.png"
"""
不会直接用的
"""
adbcut = 'adb shell screencap -p /sdcard/screen.png'
adbsave =r'adb pull /sdcard/screen.png  C:\Users\93911\Desktop/screen.png'

def screanshoot():#截屏
    time.sleep(swait)
    os.system(adbcut)
    os.system(adbsave)
    time.sleep(swait)

def num(picaddress):#输入的地址要在前面加R强转
    image = get_file_content(picaddress)
    number = client.basicGeneral(image)
    #格式这样的
    #{'words_result': [{'words': '194'}], 'log_id': 1401491669391507456, 'words_result_num': 1}
    #所以要加['words_result'][0]['words']后缀固定只输出所需要的数字194
    return number['words_result'][0]['words']

def place( waitForcheck , key ):#寻找图片,前为待测后为待寻
    time.sleep(swait)
    imsrc = ac.imread(waitForcheck)#读目标图
    imobj = ac.imread(key)#读取中文路径及名称
    pos = ac.find_template(imsrc, imobj)#查找目标图中出现的源特征图
    time.sleep(swait)
    return pos

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def click(pe):#点击事件,直接导入坐标数组就行
    x = pe[0]
    y = pe[1]
    os.system("adb shell input tap {0} {1}".format(x,y))
    r = (0,0)
    return r

"""
直接调用的
"""


def cut(A):#数组顺序是X.Y,高,宽
    x = A[0]
    y = A[1]
    h = A[2]
    w = A[3]
    im = Image.open(waitForcheck)
    region = im.crop((x, y, x+w, y+h))
    region.save(cutpath)
    number =num(cutpath)
    return number

def restart():
    os.system("adb kill-server")

    time.sleep(swait)

    os.system("adb start-server")

    time.sleep(swait)

def check(waitForcheck , key):#确认
    time.sleep(swait)
    for j in range(6):
        screanshoot()
        time.sleep(wait)
        Point = place(waitForcheck,key)
        print(Point)
        a = Point['confidence']
        print("匹配度为"+str(a))
        if a>0.7:
            print("符合要求")
            b = Point['result']
            Point = click(Point['result'])
            return b
        else:
            print("等等!")
            print(key)
    print("无匹配图片,终止程序")
    screanshoot()
    sys.exit() 

def realwheel():


    screanshoot()
    count = cut(hp)
    print("当前体力为"+str(count))
    rcost = -int(cut(cost))
    print("关卡所需体力为"+str(rcost))
    work = int(int(count)/rcost)
    print("要打"+str(work)+"次")
    
    wheel(int(work))

    print("finish!")
