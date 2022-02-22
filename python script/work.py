###7.12修改,该版本目标是修订方舟的自动领取任务以及将三国杀由不稳定的模拟器记录转化为相对精度高的识图转化
import os
import time
import sys
from Unit import *
from arguments import *

class Logger(object):#控制台输出保存

    def __init__(self, stream=sys.stdout):
        output_dir = "log"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        log_name = '{}.log'.format(time.strftime('%Y-%m-%d-%H-%M'))
        filename = os.path.join(output_dir, log_name)

        self.terminal = stream
        self.log = open(filename, 'a+')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
sys.stdout = Logger(sys.stdout)  #  将输出记录到log
sys.stderr = Logger(sys.stderr)  # 将错误信息记录到log 

if __name__=='__main__':   
    os.chdir(now)
    print("当前CMD目录为",os.getcwd())
#更新模拟器状态
    kill()
    kill()
    Android()
    print("打开模拟器")
    re()
#FGO签到
    FGO()
    print("FG0完成签到")

#s三国杀签到
    three_kill()
    print("三国杀完成签到")

  #明日方舟签到
    screanshoot()
    arknight(inpath)
    print("明日方舟完成签到")
    kill()
    print("签到脚本运行结束")
