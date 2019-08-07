import tkinter,cv2,PIL,numpy
from PIL import Image,ImageDraw,ImageFont,ImageGrab

import easygui
import os
import datetime
import _thread
import pyautogui as p
import time
   



#创建窗口   
def window():
    window=tkinter.Tk()
    window.wm_attributes('-topmost',1)
    #window.title('转文本')
    position_x=window.winfo_screenwidth()-150
    window.geometry('%dx%d+%d+%d' % (100,30,(window.winfo_screenwidth()-100), (window.winfo_screenheight() - 100) ))
    window.resizable(width=False, height=False)

    button0=tkinter.Button(window, text="自动点击", command=button_command).pack()
    window.mainloop()


#点击按钮后，截屏，并全屏显示    
def button_command():
    mode=0
    mouse=False
    print ('start here')
   
    global img,img_copy
    #filename = 'temp.png'
    im = ImageGrab.grab()
    #im.save(filename)
    #im.close()
    #im=pyautogui.screenshot()
    imgSize=im.size
    #font = ImageFont.truetype('song.ttf', int((imgSize[0])*0.025))
    draw = PIL.ImageDraw.Draw(im)
    #draw.text((imgSize[0]*0.7, (imgSize[1]*0.92)), '拖拽鼠标截图，敲回车键继续', (255,0,0), font=font)
    
    img=numpy.array(im)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_copy=img.copy()
        #img =  cv2.imread('1.png')
    cv2.namedWindow("ROI selector", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("ROI selector",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    r = cv2.selectROI(img_copy)
    imCrop = img_copy[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    #cv2.imshow('new',imCrop)
    cv2.destroyAllWindows()
    #cv2.setMouseCallback('window_full',self.mouse_action)
    print ('mid here')
    now1=str(datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S"))
    cv2.imwrite(now1+'.png',imCrop)
    #self.baidu_ocr()
     


def find_pic(pic):


        x0,y0=p.position()

        #position=p.locateCenterOnScreen(pic,confidence=0.9)
        position = p.locateOnScreen(pic, confidence=0.9)

        #print('pic',position,'here')

        if position is None:
            return False
        else:
            
            #x,y=position
            x,y,w,h=position
            x=x+int(w/2)
            y=y+int(h/2)
            print(x,y)

            p.moveTo(x,y)
            p.click()
            p.moveTo(x0,y0)
            time.sleep(5)

            #print('hello')
            return True

def pic():
    while True:
        for w in os.listdir('./'):
            if w.endswith('.png'):
                find_pic(w)





if __name__=='__main__':
    _thread.start_new_thread( window, () )
    pic()
    #window()

