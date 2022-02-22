from typing import get_origin
import cv2
import aircv as ac
import numpy as np
import sys
import aircv as ac
import os
import time
from PIL import Image
from aip import AipOcr
from arguments import *
"""
 你的 APPID AK SK 
"""
APP_ID = 
API_KEY = 
SECRET_KEY = 
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def ckint():
            print("输入一个正整数(单位秒)")
            value = input("")
            while True:
                if (value.isdigit()):
                    t = int(value)
                    print("中途等待秒数为", t)
                    return t
                else:
                    print("存在错误输入,请重新开始")
                    print("输入一个正整数(单位秒)")
                    value = input("")  

def ftk(path):
    global k
    free = (370,115)
    re()
    os.system("adb shell am start  com.hypergryph.arknights/com.u8.sdk.U8UnityContext")
    sleep(lwait)#等待加载
    click(free)#随便点地方s
    sleep(wait)
    screanshoot()
    print("跑起来了")
    point1(2,path)#从开启APP到输入密码
    print("开始输入密码")
    screanshoot()
    sleep(wait)
    Point = place(waitForcheck,inpath +  "3" +way)
    print(Point)
    a = Point['confidence']
    print("匹配度为"+str(a))
    print("符合要求,开始点击")
    Point = click(Point['result'])
    k = k+1
    putin(password)
    pointx(2,path)#进入主页/找关卡
    print("准备点广告与签到")
    sleep(wait)
    cantono(inpath)#这段跑完的K应该是6
    print("进主页啦!")
    screanshoot() 
    changeK(10)
    daguanqia(inpath,lwait)#这里K应该是10,地址应该是9.png


def rename(place):#需要存储的文件夹
    screanshoot()
    picniame = '{}.png'.format(time.strftime('%Y-%m-%d-%H-%M-%S'))
    hpath = './print/'+ place + '/'
    if not os.path.exists(hpath):
            os.makedirs(hpath)
    print("截图已送至%s" % hpath)
    os.rename(scpath ,hpath+picniame )
    #准确的说这个rename是将前一个字段的文件移动到后一个文段的位置并重命名

def kill():#消灭模拟器进程

    os.system('taskkill /f /im dnplayer.exe')

def re():#重启ADB
    os.system("adb kill-server")

    sleep(swait)

    os.system("adb start-server")

    sleep(swait)

def Android():#开启模拟器
    openapp = r'D:/leidian/LDPlayer4\dnplayer.exe'
    #设定函数所在路径
    os.startfile(openapp)
    sleep(tlwait)
    #调用OS中的startfile函数执行括号内的命令

    
def arknight(path):
    global k
    free = (370,115)
    re()
    os.system("adb shell am start  com.hypergryph.arknights/com.u8.sdk.U8UnityContext")
    sleep(lwait)#等待加载
    click(free)#随便点地方s
    sleep(wait)
    screanshoot()
    print("跑起来了")
    point1(2,path)#从开启APP到输入密码
    print("开始输入密码")
    screanshoot()
    sleep(wait)
    Point = place(waitForcheck,inpath +  "3" +way)
    print(Point)
    a = Point['confidence']
    print("匹配度为"+str(a))
    print("符合要求,开始点击")
    Point = click(Point['result'])
    k = k+1
    putin(password)
    pointx(2,path)#进入主页/找关卡
    print("准备点广告与签到")
    sleep(wait)
    cantono(inpath)#这段跑完的K应该是6
    print("进主页啦!")
    screanshoot() 
    changeK(10)
    daguanqia(inpath,lwait)#这里K应该是10,地址应该是9.png
    point1(3,path)
    pointx(2,path)
    point1(1,path)
    click(shangci)
    pointx(2,path)
    point1(3,path)
    pointx(8,path)
    point1(3,path)
    pointx(5,path)
    screanshoot()
    rename("arknight")
    os.system("adb shell am force-stop com.hypergryph.arknights/com.u8.sdk.U8UnityContext")
    print("脚本结束")
    
def FGO():
    freedom = (627,421)
    #os.system("adb shell input tap 545 109")不需要 这种方式打开了
    #点击模拟器里的545 109 坐标
    os.system("adb shell am start -n com.bilibili.fatego/.UnityPlayerNativeActivity")
    #打开FGO
    sleep(lwait)
    click(freedom)
    sleep(lwait)
    click(freedom)
    sleep(swait)
    click((545,109))
    print("点击进入登陆页面")
    #点击进入登陆页面
    sleep(tlwait)
    click((930,29))
    print("右上角关闭")
    #点击右上角关闭按钮
    sleep(tlwait)
    click((930,29))
    print("右上角关闭")
    #点击右上角关闭按钮
    sleep(tlwait)
    click((257,421))
    print("左下关闭")
    sleep(lwait)
    screanshoot()
    rename("FGO")
    os.system("adb shell am force-stop com.bilibili.fatego")
    #关闭FGO

def cleaner():
    global k
    k = 1

def sleep(waittime):
    showtime(waittime)

def point1(wtime,inpath):#循环wtime次
    for l in range(wtime):
        global k
        key =inpath +  "%i" % k +way
        print("现在的KEY为"+str(key))
        check(waitForcheck,key)
    
        print("现在的k值为%i" % k)
        k = k+1
        sleep(wait)

def showtime(endtime):#计时(新版可以手动调过计时)
    starttime = time.time()#获取当前时间戳
    print('开始%i秒钟等待' % endtime,end="\r")
    ends = endtime
    while True:
        try:
            while ends>0:
                time.sleep(1)
                timing =round(time.time() - starttime , 0)
                
                ends = endtime - timing 
                
                #print('计时: ',timing , '秒', end="\r")
                
            print('结束')
            endtime = time.time()
            print('总共的时间为:', round(endtime - starttime, 2),'secs')
            break
        except KeyboardInterrupt:
            print('结束')
            endtime = time.time()
            print('总共的时间为:', round(endtime - starttime, 2),'secs')
            break
    """
        starttime = time.time()#获取当前时间戳
        print('开始%i秒钟等待' % endtime,end="\r")
        ends = endtime
        while ends>0:
            timing =round(time.time() - starttime , 0)
            ends = endtime - timing 
            print('计时: ',timing , '秒', end="\r")
            time.sleep(1)
        #print("%i秒钟计时结束" % endtime)
    """

def pointx(x,inpath):#按X次
    global k
    for l in range(1):#进入主页/找关卡
        key =inpath +  "%s" % k +way
        #可以通过只写一半的方式把冗长的地址前缀放到循环外方便修改
        print("现在的KEY为"+str(key))
        b=place(waitForcheck,key)['result']
        y = x
        for q in range(y):
            sleep(swait)
            click(b)
            sb = q+1
            print("本次循环已经点了%i次啦" % sb)
            sleep(swait)
        k = k+1    
        print("运行完该段程序的KEY为"+str(key))
        sleep(wait)

def screanshoot():#截屏
    os.system(adbcut)
    os.system(adbsave)
    print("已截图")

def check(waitForcheck , key):#确认(包括点击)
    restart()
    sleep(swait)
    for j in range(6):
        sleep(wait)
        Point = place(waitForcheck,key)
        print(Point)
        a = Point['confidence']
        print("匹配度为"+str(a))
        if a>0.7:
            print("符合要求,开始点击")
            b = Point['result']
            Point = click(Point['result'])
            print("检测点击事件是否成功")
            while True:
                for r in range(2):
                    sleep(wait)
                    if place(waitForcheck,key)!=  {'confidence': 0}:
                        print(place(waitForcheck,key)['confidence'])
                        click(place(waitForcheck,key)['result'])
                        print("刚刚没点上,现在重新点一遍")
                        print("匹配的图片为 "+ str(key))
                        print(b)
                    else :
                        print("与线索图相似匹配不足70%")
                        break
                print("点击确认完成")
                print("匹配的图为"+str(key))
                break
            return b
        else:
            print("第%i次失败了!" % j)
            print("当前所匹配的图片为" + str(key))
    print("无匹配图片,终止程序")
    screanshoot()
    rename('error')
    sys.exit() 

def restart():#重启ADB

    os.system("adb kill-server")

    sleep(swait)

    os.system("adb start-server")

    sleep(swait)

def fact(waitForcheck , key):#图片坐标寻找
    screanshoot()
    imsrc = ac.imread(waitForcheck)#读目标图
    imobj = ac.imread(key)#读取中文路径及名称
    pos = ac.find_template(imsrc, imobj)
    #查找目标图中出现的源特征图
    return pos

def place( waitForcheck , key ):#寻找图片,前为待测后为待寻
    sleep(swait)
    screanshoot()
    pos = fact(waitForcheck , key)
    if pos is None:
        pos = {'confidence': 0}
        
    elif pos['confidence'] < 0.7:
        pos = {'confidence': 0}
    else:
        pos = pos
    sleep(swait)
    return pos
    #https://blog.csdn.net/killvirus007/article/details/90764463

def click(pe):#点击事件,直接导入坐标数组就行
    x = pe[0]
    y = pe[1]
    os.system("adb shell input tap {0} {1}".format(x,y))
    print("点击的坐标为"+ str(pe))
    r = (0,0)
    return r

def putin(password):#ADB输入
    os.system("adb shell input text %i " % password)
    sleep(swait)
    
def cut(pic,A):#数组顺序是X.Y,高,宽
    x = A[0]
    y = A[1]
    h = A[2]
    w = A[3]
    im = Image.open(pic)
    region = im.crop((x, y, x+w, y+h))
    region.save(".\short\crop_test1.png")
    number =num(r".\short/crop_test1.png")
    return number

def num(picaddress):#输入的地址要在前面加R强转
    image = get_file_content(picaddress)
    number = client.basicGeneral(image)
    #格式这样的
    #{'words_result': [{'words': '194'}], 'log_id': 1401491669391507456, 'words_result_num': 1}
    #所以要加['words_result'][0]['words']后缀固定只输出所需要的数字194
    if number == None:
        number = {'words_result': [{'words': '0'}], 'log_id': 1401491669391507456, 'words_result_num': 1}
    return number['words_result'][0]['words']

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def wheel(alice,inpath,waittime):#循环关卡
    #nice = (847,476)可以公用的点
    for l in range(alice):
        s = l +1
        sleep(wait)
        print("准备开始第%i次" % s)
        key = inpath + "ready" +way
        check(waitForcheck,key)

        print("开始")
        key = inpath + "start" +way
        check(waitForcheck,key)
        sleep(waittime)
        restart()
        
        key = inpath + "finish" +way
        check(waitForcheck,key)
        sleep(wait)
        print("完成第%i次" % s)

def realwheel(path,waittime):
    sleep(wait)
    screanshoot()
    count = cut(waitForcheck,hp)
    print("当前体力为"+str(count))
    rcost = abs(int(cut(waitForcheck,cost)))
    print("关卡所需体力为"+str(rcost))
    work = int(int(count)/rcost)
    print("要打"+str(work)+"次")
    wheel(int(work),path,waittime)
    print("finish!")

def jiao(path,waittime):
    print("请选择要进行的次数(0-1800要打6次,需要150体力)")
    work = input()
    """
    screanshoot()
    count = cut(waitForcheck,hp)
    print("当前体力为"+str(count))
    rcost = abs(int(cut(waitForcheck,cost)))
    print("关卡所需体力为"+str(rcost))
    work = int(int(count)/rcost)
    print("要打"+str(work)+"次")
    """
    alice = int(work)
    inpath = path
    for l in range(alice):
        s = l +1
        sleep(wait)
        print("准备开始第%i次" % s)
        key = inpath + "ready" +way
        check(waitForcheck,key)

        print("开始")
        key = inpath + "start" +way
        check(waitForcheck,key)
        sleep(waittime)
        restart()
        
        click((847,476))
        sleep(wait)
        key = inpath + "finish" +way
        check(waitForcheck,key)
        sleep(wait)
        print("完成第%i次" % s)
    print("finish!")

def huishouye(inpath):
    print("开启快捷菜单")
    check(scpath,inpath+"caidan"+way)
    sleep(swait)
    print("点击返回按钮")
    check(scpath,inpath+"shouye"+way)
    sleep(swait)

def daguanqia(inpath,waittime):
    print("进入终端")
    screanshoot()
    check(scpath,inpath+"zhongduan"+way)
    print("重复上一次打的关卡")
    sleep(swait)
    click(shangci)
    print("开始作战")
    realwheel(inpath,waittime)
    realwheel(inpath,waittime)
    print("返回首页")
    #huishouye(inpath)

def changeK(s):
    global k
    k = s
    print("K的值现更改为%i" % k)

def cantono(inpath):
    global k
    sleep(wait)
    key =inpath +  "%i" % k +way
    sa = place( waitForcheck , key)['confidence']
    print("当前K为"+str(k))
    print("当前与X的匹配值为"+str(sa))
    if sa>0.7:
        print("符合要求")
        check( waitForcheck , key)
        sleep(wait)
        print("进入签到")
        click((370,115))#第一个X(广告)
        sb = place( waitForcheck , key)['confidence']
        if sb>0.7:
            print("这次有广告")
            check( waitForcheck , key)
    else :
        print("没有需要按X的地方")
        
    k = k+1
    #这里该是6
    print("加完的K值为%i" % k)

"""
三国杀部分
"""
def three_kill():

    os.system("adb shell am start -n com.yoka.newsgs/org.cocos2dx.lua.AppActivity")
    sleep(lwait)
    qiandao()
    jinzhulu()
    jiangling()
    dazhulu()

    gonghui()
    lingrenwu()
    rename('tk')
    huanhao()
    qiandao()
    jinzhulu()
    jiangling()
    dazhulu()
    
    gonghui()
    lingrenwu()
    rename('tk')
    os.system("adb shell am force-stop com.yoka.newsgs/org.cocos2dx.lua.AppActivity")
    

def qiandao():
    print("开始签到")
    screanshoot()
    #签到页面,有月卡
    if place(scpath,tkinpath+"gold"+way) !=  {'confidence': 0}:#是签到页面
        print("领取月卡")
        check(scpath,tkinpath+"gold"+way)
        print("点击领取")
        sleep(swait)
        print("随便点个啥")
        click((740,179))
        sleep(swait)
        #签到页面有周卡
        if place(scpath,tkinpath+"gold"+way) !=  {'confidence': 0}:#是签到页面
            check(scpath,tkinpath+"gold"+way)
            sleep(swait)
            click((740,179))
            sleep(swait)
        else:
            print("没有其他领取按钮了")
        screanshoot()
        rename('tk')
        print("月卡签到完成")
        check(scpath,tkinpath+"back"+way)
        if place(scpath,tkinpath+"close"+way) !=  {'confidence': 0}:#是签到页面
            check(scpath,tkinpath+"close"+way)
            print("关闭战令广告")
        sleep(swait)
        print("返回主页成功")
    #签到页面无月卡
    elif place(scpath,tkinpath+"back"+way) !=  {'confidence': 0}:
        print("没有月卡,返回主页")
        check(scpath,tkinpath+"back"+way)
        sleep(swait)
        print("返回主页成功")
    #没有进签到页面
    elif place(scpath,tkinpath+"play"+way) !=  {'confidence': 0}:
        print("进入签到页面")
        check(scpath,tkinpath+"play"+way)
        print("不出意外现在该是领月卡界面")
        sleep(wait)
        if place(scpath,tkinpath+"gold"+way) !=  {'confidence': 0}:#是签到页面
            print("领取月卡")
            check(scpath,tkinpath+"gold"+way)
            sleep(swait)
            click((740,179))
            sleep(swait)
            if place(scpath,tkinpath+"gold"+way) !=  {'confidence': 0}:#是签到页面
                check(scpath,tkinpath+"gold"+way)
                sleep(swait)
                click((740,179))
                sleep(swait)
            else:
                print("没有其他领取按钮了")
            check(scpath,tkinpath+"back"+way)
            sleep(swait)
            print("返回主页成功")
        elif place(scpath,tkinpath+"back"+way) !=  {'confidence': 0}:
            print("没有月卡,返回主页")
            check(scpath,tkinpath+"back"+way)
            sleep(swait)
            print("返回主页成功")

def jinzhulu():
    print("开始打逐鹿")
    sleep(wait)
    check(scpath,tkinpath+"maoxian"+way)
    sleep(wait)
    check(scpath,tkinpath+"zhulu"+way)
    screanshoot()
    if place(scpath,tkinpath+"quxiao"+way)!=  {'confidence': 0}:
        print("烦人的玩意出来了")
        check(scpath,tkinpath+"quxiao"+way)
        sleep(wait)
        print("取消掉了")
        check(scpath,tkinpath+"zhulu"+way)
        sleep(wait)
    elif place(scpath,tkinpath+"zhulu"+way)!=  {'confidence': 0}:
        print("烦人的玩意没出来")
        check(scpath,tkinpath+"zhulu"+way)
        sleep(swait)
    elif place(scpath,tkinpath+"fight"+way)!=  {'confidence': 0}:
        print("已经在逐鹿里面了")
    else:
        print("出错了找不着逐鹿按钮")
        rename('error')

def d105(alice):#105循环刷
    sleep(wait)
    click((303,218))
    #100
    sleep(wait)
    for i in range(alice):
        click( (827,355))
        #第五关
        sleep(wait)
        click((858,414))
        #开始挑战
        sleep(wait)
        click((858,414))
        #挑战
        sleep(wait)
        click((789,454))
        #开始挑战
        sleep(lwait)
        click((477,481))
        #打完随机点按钮
        sleep(wait)
        check(scpath,tkinpath+"zhuluqueding"+way)
        #打完以后的确定
        sb = i+1
        print("完成%i次逐鹿" % sb)
        sleep(wait)
    screanshoot()
    print("逐鹿结束")

def dazhulu(): 
    if place(scpath,tkinpath+"maoxian"+way)!=  {'confidence': 0}:
        print("还在首页呢,重新进逐鹿")
        jinzhulu()
    else:
        print("已经在逐鹿里面了")
    print("判断当前体力")
    screanshoot()
    check(scpath,tkinpath+"tili"+way)
    screanshoot()
    lhp = cut(scpath,lvtili)#判断当前体力值(这里出来的是字符串哦!)
    print("当前体力为%i" % int(lhp))
    check(scpath,tkinpath+"quxiao"+way)
    screanshoot()
    if place(scpath,tkinpath+"105no"+way)!=  {'confidence': 0}:
        for l in range(int(lhp)):
            screanshoot()
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            check(scpath,tkinpath+"fight"+way)
            print("向105冲锋")
            sleep(swait)
            screanshoot()
            #check(scpath,tkinpath+"fight"+way)
            #因为对点击事件的反复确认,,这里的手动双重确认废弃
            sleep(lwait)
            while True:
                screanshoot()
                if place(scpath,tkinpath+"hongbao"+way)!=  {'confidence': 0}:
                    pc = check(scpath,tkinpath+"hongbao"+way)
                    click(pc)
                else:
                    break
            screanshoot()
            print("打完一次了")
            pa = check(scpath,tkinpath+"fin"+way)
            print("结束标志为",pa)
            sleep(wait)
            check(scpath,tkinpath+"zhuluqueding"+way)
            sleep(wait)
        screanshoot()

    else:
        print("死命刷105啦")
        d105(int(lhp))
        #这里之后写个105的刷刷
#
def jiangling():#注意,该函数必须要在逐鹿页面方可正常运行
    screanshoot()
    if place(scpath,tkinpath+"tili"+way) !=  {'confidence': 0}:
        click(jiang)
        screanshoot()
        #聚宝盆
        check(scpath,tkinpath+"jubaopen"+way)
        screanshoot()
        if place(scpath,tkinpath+"lingqu"+way) !=  {'confidence': 0}:
            sb = check(scpath,tkinpath+"lingqu"+way)
            print("领取聚宝盆")
            sleep(swait)
            click(sb)
            sleep(swait)
            click(sb)
        else:
            print("聚宝盆没东西")
        #出征
        sleep(wait)
        restart()
        check(scpath,tkinpath+"chuzheng"+way)
        sleep(wait)
        screanshoot()
        if place(scpath,tkinpath+"lingqu"+way) !=  {'confidence': 0}:
            check(scpath,tkinpath+"lingqu"+way)
            print("领取出征")
            sleep(swait)
            screanshoot()
            check(scpath,tkinpath+"fanhui"+way)
            print("返回选择任务列表")
            sleep(swait)
            screanshoot()
        #新一次出征
            print("新的出征")
            check(scpath,tkinpath+"chuzhengqueding"+way)
            sleep(swait)
            check(scpath,tkinpath+"jiequ"+way)
            sleep(swait)
            check(scpath,tkinpath+"queding"+way)
            sleep(swait)
        elif  place(scpath,tkinpath+"chuzhengqueding"+way) !=  {'confidence': 0}:
            if place(scpath,tkinpath+"quxiao"+way)!=  {'confidence': 0}:
                print("烦人的玩意出来了")
                check(scpath,tkinpath+"quxiao"+way)
                sleep(wait)
                print("取消掉了")
            else:
                screanshoot()
                print("开始出征")
                check(scpath,tkinpath+"chuzhengqueding"+way)
                sleep(swait)
                check(scpath,tkinpath+"jiequ"+way)
                sleep(swait)
                check(scpath,tkinpath+"queding"+way)
                sleep(swait)
        elif place(scpath,tkinpath+"jiequ"+way) !=  {'confidence': 0}:
            screanshoot()
            check(scpath,tkinpath+"jiequ"+way)
            sleep(swait)
            check(scpath,tkinpath+"queding"+way)
            sleep(swait)
        else :
            print("出征出错了!!总之先跳过")
            screanshoot()
            rename('error')
        print("退出将灵页面")
        sleep(wait)
        check(scpath,tkinpath+"back"+way)
    else :
        print("注意!该页面非逐鹿页面")
        screanshoot()
        rename('error')

def gonghui():
    print("开始工会模块")
    screanshoot()
    if place(scpath,tkinpath+"back"+way) !=  {'confidence': 0}:
        check(scpath,tkinpath+"back"+way)
        print("返回上一层")
    else:
        print("已经在首页")
    screanshoot()
    if place(scpath,tkinpath+"gonghui"+way) !=  {'confidence': 0}:
        check(scpath,tkinpath+"gonghui"+way)
        sleep(swait)
        check(scpath,tkinpath+"huodong"+way)
        #擂鼓
        #检测模块可能出现程序冲突,所以只按一次
        print("第%i次擂鼓" % k)
        check(scpath,tkinpath+"leigu"+way)
        sleep(swait)
        """
        因为无法分辨出已领取与未领取,该段废弃 
        另,根据Python中其他master,似乎有其他的分辨方法,RGB之类的,有时间再来换吧
        while True:
            screanshoot()
            if place(scpath,tkinpath+"gonghuilingqu"+way)!=  {'confidence': 0}:
                ok = check(scpath,tkinpath+"gonghuilingqu"+way)
                sleep(wait)
                click(ok)
                sleep(swait)
            else:
                print("无可领取项目")
                break
        """
        print("退出工会页面")
        check(scpath,tkinpath+"back"+way)
        print('返回主页面')

    else :
        print("出错了找不着工会按钮")
        rename('error') 

def lingrenwu():
    
    while True:
        screanshoot()
        if place(scpath,tkinpath+"back"+way) !=  {'confidence': 0}:
            check(scpath,tkinpath+"back"+way)
        else :
            break
    screanshoot()
    if place(scpath,tkinpath+"renwu"+way) !=  {'confidence': 0}:
        check(scpath,tkinpath+"renwu"+way)
        screanshoot()
        fbi = check(scpath,tkinpath+"yijianlingqu"+way)
        for p in range(20):
            click(fbi)
            sleep(swait)
        screanshoot()
        check(scpath,tkinpath+"close"+way)
        print("返回主页")
    else:
        print("出错了找不着任务按钮")
        rename('error')

def huanhao():
    screanshoot()
    if place(scpath,tkinpath+"gengduo"+way) !=  {'confidence': 0}:
        print("准备换号")
        
        check(scpath,tkinpath+"gengduo"+way)
        screanshoot()
        check(scpath,tkinpath+"shezhi"+way)
        screanshoot()
        check(scpath,tkinpath+"tuichudenglu"+way)
        screanshoot()
        check(scpath,tkinpath+"qiehao"+way)
        screanshoot()
        check(scpath,tkinpath+"qiehuan"+way)
        click(huanhuanhuan)
        sleep(wait)
        check(scpath,tkinpath+"denglu"+way)
        check(scpath,tkinpath+"jinyouxi"+way)
        sleep(lwait)
    else:
        print("出错了找不着换号按钮")
        rename('error')
        sys.exit()

if __name__=='__main__':   
    os.chdir(now)
    print("当前CMD目录为",os.getcwd())
    while True:
        print("请选择要进行的循环类别")
        print("1.方舟单关卡循环    2.逐鹿循环   3.FGO单关卡循环")
        a = input()#input默认是输入STR
        if a =="1":
            print("是否为剿灭?")
            print(" ")
            print("1.是  2.否")
            while True:
                b = input("")
                if b =="1":
                    print("切换为剿灭进程")
                    wtime = ckint()
                    jiao(inpath,wtime)
                    break
                elif b == "2":
                    print("切换威威一般关卡进程")
                    print("开始方舟单关卡循环")
                    wtime = ckint()
                    realwheel(inpath,wtime)
                    break
                else :
                    print("输入错误,请输入正确的数字")
                    print("是否为剿灭?")
                    print(" ")
                    print("1.是  2.否")
            print("打完了")
            break
        elif a == "2":
            print("开始逐鹿循环")
            dazhulu()
            print("打完了")
            break
        elif a == "3":
            print("开始FGO关卡循环")
            break
        else:
            print("输入错误,请输入正确的数字")
            
    print("按任意键退出程序")
    input("")
