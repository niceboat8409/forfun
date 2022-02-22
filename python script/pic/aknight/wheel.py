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
nice = (847,476)
#可以公用的点
hp = [854,18,21,43]
#右上角体力点
cost = [890,509,16,30]
#关卡消耗
waitForcheck = r"C:/Users/93911\Desktop\screen.png"
wpath = r"C:/Users/93911\Desktop/"
png = r".png "
cutpath = r"F:/pic\AK\short/crop_test1.png"
adbcut = 'adb shell screencap -p /sdcard/screen.png'
adbsave =r'adb pull /sdcard/screen.png  C:\Users\93911\Desktop/screen.png'

def showtime(times):
    while True:
        starttime = time.time()#获取当前时间戳
        print('开始等待')
        gooing = 0
        while gooing <= times:
            print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
            gooing = round(time.time() - starttime)
            time.sleep(1)
        print("本次等待%i" % gooing)
        break

def screanshoot():#截屏
    time.sleep(swait)
    os.system(adbcut)
    os.system(adbsave)
    time.sleep(swait)

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

def num(picaddress):#输入的地址要在前面加R强转
    image = get_file_content(picaddress)
    number = client.basicGeneral(image)
    #格式这样的
    #{'words_result': [{'words': '194'}], 'log_id': 1401491669391507456, 'words_result_num': 1}
    #所以要加['words_result'][0]['words']后缀固定只输出所需要的数字194
    return number['words_result'][0]['words']

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

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
        firsta = Point['confidence']
        firsta = str(firsta)
        if firsta.replace(".","").isdigit():
            a =float(firsta)
        else:
            a = 0
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

def place( waitForcheck , key ):#寻找图片,前为待测后为待寻
    time.sleep(swait)
    imsrc = ac.imread(waitForcheck)#读目标图
    imobj = ac.imread(key)#读取中文路径及名称
    pos = ac.find_template(imsrc, imobj)#查找目标图中出现的源特征图
    time.sleep(swait)
    return pos

def click(pe):#点击事件,直接导入坐标数组就行
    x = pe[0]
    y = pe[1]
    os.system("adb shell input tap {0} {1}".format(x,y))
    r = (0,0)
    return r

def wheel(alice,whtime):#循环关卡
    #nice = (847,476)可以公用的点
    for l in range(alice):
        k = l +1
        showtime(wait)
        time.sleep(wait)
        print("准备开始第%i次" % k)
        key = wpath + "ready" +png
        check(waitForcheck,key)
        print("本次等待%i秒" % whtime)
        print("开始")
        key = wpath + "start" +png
        check(waitForcheck,key)
        showtime(whtime)
        time.sleep(run)
        restart()
        key = wpath + "weekfin" +png
        check(waitForcheck,key)
        showtime(wait)
        time.sleep(wait)
        print("完成第%i次" % k)




if __name__=='__main__':
    screanshoot()
    count = cut(hp)
    print("当前体力为"+str(count))
    rcost = abs(int(cut(cost)))
    print("当前选中关卡所需体力为"+str(rcost))
    number = input("请输入想循环的次数(打空体力请直接敲回车)\n")
    if number.isdigit():
        work = str(number)
        print("准备开始"+str(work)+"次循环")
    else:
        work = int(int(count)/rcost)
        print("使用全部体力循环,要打"+str(work)+"次")
    second = input("一把要打多少秒呢?\n")
    if second.isdigit():
        run = abs(int(second))
        print("一把打%i秒" % run)
    else :
        run = lwait
        print("未检测到合规输入,默认%i秒" % run)
    wheel(int(work),run)

    print("finish!")




print("没跑动")






...