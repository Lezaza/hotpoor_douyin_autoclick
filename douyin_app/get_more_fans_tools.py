import sys
import os
import time
import random

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
