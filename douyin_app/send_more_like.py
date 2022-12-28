import sys
import os
import time
import random


def adb_tap(x,y,sleep=0):
    cmd_str = "adb shell input tap %s %s"%(x,y)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)

uni_min = 0.025
uni_max = 0.15

send_times = 1000
for i in range(0,send_times):
    print("第%s次发送"%i)
    x = int(random.random()*10)+303
    y = int(random.random()*10)+767
    adb_tap(x,y,random.uniform(uni_min,uni_max))