import sys
import os
import time
import random

from config import conf_devices
from config import conf_message_list

import get_more_fans_tools

# step1 已经打开了抖音
# step2 已经访问了兔子178（涨粉直播间）
# 开始跑同样的话术
message_list = conf_message_list

default_device = "Xiaomi11SPro"
default_device_id = "60649497"

# 选用设备
device_con = conf_devices[default_device]
device_id = default_device_id

# x,y
iptBox_x = device_con["iptBox_x"]
iptBox_y = device_con["iptBox_y"]
sendBtn_x = device_con["sendBtn_x"]
sendBtn_y = device_con["sendBtn_y"]
# 自动语音输入弹出后发送按钮的位置改变
sendBtn_xAddition = device_con["sendBtn_xAddition"]
sendBtn_yAddition = device_con["sendBtn_yAddition"]
# 空白处的x坐标位置，确保卡壳的时候输入框能正确收回
sendBtn_xOther = device_con["sendBtn_xOther"]

# interval 
send_times = 1200
base_sec = 0.85 # * 20
uni_min = 1.0
uni_max = 3.5

for i in range(0,send_times):
    print("第%s次发送"%i)
    get_more_fans_tools.adb_tap(iptBox_x,iptBox_y,base_sec + random.uniform(uni_min,uni_max),device_id)
    current_message = int(random.random()*10*1000 % len(message_list))
    print("No- %s word--> go - %s"%(current_message,random.uniform(uni_min,uni_max)))
    get_more_fans_tools.adb_send_message(message_list[current_message][:49],base_sec + random.uniform(uni_min,uni_max),device_id)
    # adb_tap(sendBtn_x,sendBtn_y,base_sec + random.uniform(uni_min,uni_max))
    get_more_fans_tools.adb_tap(sendBtn_x,sendBtn_y,base_sec,device_id)
    # adb_tap(sendBtn_xAddition,sendBtn_yAddition,0.05)
    # 每次确保发送按钮之后输入框回归原始状态
    # adb_tap(sendBtn_xOther,sendBtn_yAddition,base_sec,device_id)
