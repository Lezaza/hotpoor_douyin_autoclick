import sys
import os
import time
import random

from config_oppoReno7pro import conf_devices
from config_oppoReno7pro import conf_default_device
from config_oppoReno7pro import conf_default_device_id

# step1 已经打开了抖音
# step2 已经访问了兔子178（涨粉直播间）
# 开始跑同样的话术

message_list = [
    "真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友。",
    "主播辛苦了，真诚交友，真诚交友，真诚交友。。。",
    "交朋友！交朋友！交朋友！",
    "喜欢主播的风格，感谢有这样的直播间互通有无，诚心交朋友",
    "庆幸能在这样的地方和朋友们相识相遇，互帮互助，关注好友",
    "诚意交朋友，主播666，主播666，感恩相识，共同进步。",
    #"诚信交友，有关必回！共同成长，有幸有你！诚信交友，有关必回！共同成长，有幸有你！",
    "直播辛苦，努力有价值，成长有同伴，温暖有直播间~~~ 一路畅行",
    "感谢朋友们今天的陪伴，感谢所有进入这里相互交流的大家，谢谢关注，谢谢主播，今天很开心！",
    "支持主播，诚意交友，直播间老铁，热情弹幕刷起来~~~666~~~999，感谢主播气氛带动",
    "666 666 666 666 666 666 666 666",
    "[玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰]。",
    "[加油][加油][加油][加油][加油][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰]。",
    "[比心][比心][比心][比心][比心][比心][赞][赞][赞][赞][赞][赞][加油][加油]。",
    "[赞][赞][赞][赞][赞][赞][加油][加油][加油][比心][比心][比心]",
    "交朋友，交朋友 交朋友，交朋友 交朋友，交朋友 交朋友，交朋友 交朋友，交朋友",
    "[玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰]xx",
    "[加油][加油][加油][加油][加油][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰]xx",
    "[比心][比心][比心][比心][比心][比心][赞][赞][赞][赞][赞][赞][加油]xxx",
    "[赞][赞][赞][赞][赞][赞][加油][加油][加油][比心][比心][比心]",
    "交朋友，交朋友 交朋友，交朋友 交朋友，交朋友 交朋友，交朋友 交朋友，交朋友",
    "正能量 主播赞 [赞][赞][赞] 正能量 主播赞 [赞][赞][赞] 正能量 主播赞 [赞][赞][赞]",
    #"只要快递还在路上，生活就充满了希望。只要抖音直播还在，成长就有目标。",
    #"鞠躬君子 胸怀何坦荡; 疾风知劲草 世乱鉴忠良; 沧浪水浊兮 以吾心濯沧浪; 千载犹闻侠骨香...",
    #"像女孩子这种可爱的生物，当然要宠着",
    #"我不能逛街，一逛街发现自己什么都缺，不如刷刷直播间。。。",
    #"我们什么都没有，唯一的本钱就是青春",
    #"虽不能感同身受，但愿做你的最佳听众",
    #"我相信，路总会有平坦的一面",
    #"愿有人与你立黄昏，愿有人问你粥可温",
    #"倘不奋发，唯有失败，顾影自怜",
    #"我越努力越幸运,大家越努力也越幸运",
    #"一路上有你，呆一点也愿意。缘分让你我在此相聚",
    #"你༗若༗盛༗开༗，清༗风༗自༗来༗",
    #"直至生死入眼帘，方知情字乃是贪",
    #"亦余心之所善兮，虽九死其犹未悔",
    #"外面的世界很精彩，请勇敢飞出来~~~~~~~~~~",
    #"路的尽头，仍然是路，只要你愿意走，并不完美，但却自由~~~",
    #"随遇而安，便会花开四季，明媚嫣然，加油加油",
    #"抖音新号扶持，涨粉互暖，有关必回，共同加油！",
    #"玉屏风冷愁人。醉烂漫、梅花翠云",
    #"愿你可以找到那个与你长期共振，可以相互诉说废话的人",
    #"凡事预则立，不预则废，待你强大，你给自己天下",
    #"在没人喝彩的时候我们要学会给自己喝彩，在没人鼓掌的时候我们要学会给自己鼓掌",
    #"一份信心，一份成功，一份努力；十分信心，十分成功，十分努力。",
    #"人生像攀登一座山，而找寻出路，却是一种学习的过程，我们应当在这过程中，学习稳定、冷静，学习如何从慌乱中找到生机。",
    #"记住：你是你生命的船长，走自己的路，何必在乎其它。",
    #"莫听穿林打叶声，何妨吟啸且徐行。竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。",
    #"主播我来了，感知正能量！",
    #"关注主播不迷路，主播带你上高速！谢谢主播带队互动！！感谢提供交友平台！！！",
    #"大家好，我是新人，特来向大家学习，希望大家混个眼熟，常互动哟~~~~",
    #"相见是缘分，相交更是缘分，虽然不知道你何时出现，不如借主播的这方热土，先行动起来。热情点赞，友情互关！",
]

def adb_tap(x,y,sleep=0,devID=''):
    if devID=='':
        cmd_str = "adb shell input tap %s %s"%(x,y)
    else:
        cmd_str = "adb -s %s shell input tap %s %s"%(devID,x,y)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)
def adb_swipe(x,y,x1,y1,t=1000,sleep=0,devID=''):
    if devID=='':
        cmd_str = "adb shell input swipe %s %s %s %s %s"%(x,y,x1,y1,t)
    else:
        cmd_str = "adb -s %s shell input swipe %s %s %s %s %s"%(devID,x,y,x1,y1,t)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)
def adb_send_message(message,sleep=0,devID=''):
    if devID=='':
        cmd_str = "adb shell am broadcast -a ADB_INPUT_TEXT --es msg '%s'"%message
    else:
        cmd_str = "adb -s %s shell am broadcast -a ADB_INPUT_TEXT --es msg '%s'"%(devID,message)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)

# 选用设备
device_con = conf_devices[conf_default_device]
device_id = conf_default_device_id


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
    adb_tap(iptBox_x,iptBox_y,base_sec + random.uniform(uni_min,uni_max),device_id)
    current_message = int(random.random()*10*1000 % len(message_list))
    print("No- %s word--> go - %s"%(current_message,random.uniform(uni_min,uni_max)))
    adb_send_message(message_list[current_message],base_sec + random.uniform(uni_min,uni_max),device_id)
    # adb_tap(sendBtn_x,sendBtn_y,base_sec + random.uniform(uni_min,uni_max))
    adb_tap(sendBtn_x,sendBtn_y,base_sec,device_id)
    # adb_tap(sendBtn_xAddition,sendBtn_yAddition,0.05)
    # 每次确保发送按钮之后输入框回归原始状态
    # adb_tap(sendBtn_xOther,sendBtn_yAddition,base_sec,device_id)
