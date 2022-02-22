import sys
from Unit import *
import time
import os


"""
历史记录
"""

free = (370,115)
restart()
os.system("adb shell am start  com.hypergryph.arknights/com.u8.sdk.U8UnityContext")
time.sleep(600 )#等待加载
click(free)#随便点地方s
screanshoot()
print("跑起来了")
point1(3)#从开启APP到输入密码
print("开始输入密码")
putin(password)
pointx(2)#进入主页/找关卡
click(free)
print("准备X")
click(free)
screanshoot()
cantono()#这段跑完的K应该是6
print("进主页啦!")
click(free)
screanshoot() 
point1(4)
realwheel()#这里K应该是10,地址应该是9.png
point1(3)
pointx(2)
point1(1)
pointx(2)
point1(3)
pointx(8)
point1(3)
pointx(40)
screanshoot()
print("脚本结束")


