import sys
import os
import time
import random

# step1 已经打开了抖音
# step2 已经访问了兔子178（涨粉直播间）
# 开始跑同样的话术

message_list = [
    "临渊羡鱼不如退而结网",
    "浅浅夕夕，好漂亮",
    "野花哪有，机器人有意思？",
    "我还年轻，让我测试下，别见怪"
    ]

message_list = [
    "真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友，真诚交友",
    # "the best gift is to meet you",
    "因为你是唯一，所以拿命珍惜",
    "只要快递还在路上，生活就充满了希望",
    "你闻，今夜的风是杜鹃花香……",
    "你要不要试着，做我的全世界",
    "一套喵喵拳送给你 biu~ biu~~~ biu~~~~~~",
    "眼睛为你下着雨，心却为你撑伞",
    "你要是喜欢别人我会哭，但还是喜欢你",
    "爱情的开始正好好奇",
    "我会喜欢到你需要我为止love you",
    "不跟你说了，我晕猪 Ha~Ha~Ha~Ha~",
    "像女孩子这种可爱的生物，当然要宠着",
    "有些人的出现是为了告诉你，你真好骗",
    "我不能逛街，一逛街发现自己什么都缺",
    "我们什么都没有，唯一的本钱就是青春",
    "虽不能感同身受，但愿做你的最佳听众",
    "我相信，路总会有平坦的一面",
    "愿有人与你立黄昏，愿有人问你粥可温",
    "我多想一个不下心就和你白头偕老",
    "鳄鱼在浅水区是靠走而不是游泳",
    "倘不奋发，唯有失败，顾影自怜",
    "什么布不剪断？瀑布",
    "你是世上最给我面子的人，因为你脸大",
    "我越努力越幸运,大家越努力也越幸运",
    "一路上有你，呆一点也愿意。缘分让你我在此相聚",
    "你༗若༗盛༗开༗，清༗风༗自༗来༗",
    "直至生死入眼帘，方知情字乃是贪",
    "亦余心之所善兮，虽九死其犹未悔",
    "外面的世界很精彩，请勇敢飞出来~~~~~~~~~~",
    "路的尽头，仍然是路，只要你愿意走，并不完美，但却自由~~~",
    "随遇而安，便会花开四季，明媚嫣然，加油加油",
    "诚信交友，有关必回！共同成长，有幸有你！诚信交友，有关必回！共同成长，有幸有你！",
    "临渊羡鱼不如退而结网",
    "抖音新号扶持，涨粉互暖，有关必回，共同加油！",
    "玉屏风冷愁人。醉烂漫、梅花翠云",
    "愿你可以找到那个与你长期共振，可以相互诉说废话的人",
    "凡事预则立，不预则废，待你强大，你给自己天下",
]



def adb_tap(x,y,sleep=0):
    cmd_str = "adb shell input tap %s %s"%(x,y)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)
def adb_swipe(x,y,x1,y1,t=1000,sleep=0):
    cmd_str = "adb shell input swipe %s %s %s %s %s"%(x,y,x1,y1,t)
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)
def adb_send_message(message,sleep=0):
    cmd_str = "adb shell am broadcast -a ADB_INPUT_TEXT --es msg '%s'"%message
    print(cmd_str)
    os.system(cmd_str)
    time.sleep(sleep)

# x,y
iptBox_x = 308
iptBox_y = 3000
sendBtn_x = 1360
sendBtn_y = 3004

# interval 
send_times = 777
base_sec = 0.55
uni_min = 0.2
uni_max = 0.9

for i in range(0,send_times):
    print("第%s次发送"%i)
    adb_tap(iptBox_x,iptBox_y,base_sec + random.uniform(uni_min,uni_max))
    current_message = int(random.random()*10*1000 % len(message_list))
    print("No- %s word--> go - %s"%(current_message,random.uniform(uni_min,uni_max)))
    adb_send_message(message_list[current_message],base_sec*2 + random.uniform(uni_min,uni_max))
    # adb_tap(sendBtn_x,sendBtn_y,base_sec + random.uniform(uni_min,uni_max))
    adb_tap(sendBtn_x,sendBtn_y,0)
    
