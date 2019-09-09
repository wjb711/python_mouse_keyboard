import pyautogui as p
import os
import time
def find_pic(pic):


        x0,y0=p.position()

        #position=p.locateCenterOnScreen(pic,confidence=0.9)
        position = p.locateOnScreen(pic, confidence=0.9)

        #print('pic',position,'here')

        if position is None:
            print('not find anything，未发现')
            return False
        else:
            print('got it，等待两分钟')
            os.system('lock.bat')
            time.sleep(120)
            
            #x,y=position
            #x,y,w,h=position
            #x=x+int(w/2)
            #y=y+int(h/2)
            #print(x,y)

            #p.moveTo(x,y)
            #p.click()
            #p.moveTo(x0,y0)
            #time.sleep(5)

            #print('hello')
            return True
while True:
    for pic in os.listdir('./'):
        if pic.endswith('.png'):
            find_pic(pic)
    #find_pic('lock1.png')
