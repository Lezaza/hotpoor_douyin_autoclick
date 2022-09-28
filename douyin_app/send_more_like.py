import sys
import os
import time
import random


def adb_tap(x,y,sleep=0):
    cmd_str = "adb shell input tap %s %s"%(x,y)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)


send_times = 100
for i in range(0,send_times):
    print("第%s次发送"%i)
    x = int(random.random()*10)+503
    y = int(random.random()*10)+1267
    adb_tap(x,y,0)