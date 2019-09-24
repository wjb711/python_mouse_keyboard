import pyautogui as g
import time
import datetime
import os
def record():
    now=datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    #print(now)
    command='.\\ffmpeg\\bin\\ffmpeg.exe -f gdigrab -i desktop -t 30 .\\record\\{}.mpg -loglevel quiet'.format(now)
    #os.system(command)
    x=os.popen(command,'r',1)
    time.sleep(30)
    print('x',x)
x0=1
y0=1
while True:
    x,y=g.position()
    print(x,y)
    if x==x0 and y==y0:
        print('same')
    else:
        print('mouse moved')
        record()
    time.sleep(1)
    x0=x
    y0=y
