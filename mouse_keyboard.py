import pyautogui as p
import time
def 等待图片(pic):
    while True:
        if p.locateCenterOnScreen(pic):
            break

def 移到图片(pic):

    location=p.locateCenterOnScreen(pic)

    #print ('img//'+pic+'.png',location)

    if location:

       

        #time.sleep(1)

        p.moveTo(location)

        #time.sleep(1)

def 右键单击():
    p.click()
def 键盘输入(string):
    p.typewrite(string)
def 热键(string):
    p.hotkey(string)
def 热键双键(string1,string2):
    p.hotkey(string1,string2)
def 等待时间(i):
    time.sleep(i)

        #time.sleep(1)
##等待图片('person.png')
##移到图片('person.png')
##右键单击()
