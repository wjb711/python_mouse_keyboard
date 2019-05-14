
from pynput import keyboard

from pynput.keyboard import Key, Controller

import datetime, time,sys
import pyautogui as p


def key_change(key):

    if str(key) == 'Key.enter':

       

        return Key.enter

    elif str(key) =='Key.cmd':

        return Key.cmd
        
    elif str(key) == 'Key.alt_l':

        return Key.alt_l
    elif str(key) == 'Key.esc':

        return Key.esc
    elif str(key) == 'Key.f1':

        return Key.f1
    elif str(key) == 'Key.f2':

        return Key.f2
    elif str(key) == 'Key.f3':

        return Key.f3
    elif str(key) == 'Key.f4':

        return Key.f4
    elif str(key) == 'Key.f5':

        return Key.f5
    elif str(key) == 'Key.f6':

        return Key.f6
    elif str(key) == 'Key.f7':

        return Key.f7
    elif str(key) == 'Key.f8':

        return Key.f8
    elif str(key) == 'Key.f9':

        return Key.f9
    elif str(key) == 'Key.f10':

        return Key.f10
    elif str(key) == 'Key.f11':

        return Key.f11
    elif str(key) == 'Key.f12':

        return Key.f12
    elif str(key) == 'Key.right':

        return Key.right
    elif str(key) == 'Key.left':

        return Key.left
    elif str(key) == 'Key.up':

        return Key.up
    elif str(key) == 'Key.down':

        return Key.down
    elif str(key) == 'Key.space':

        return Key.space
    elif str(key) == 'Key.shift':

        return Key.shift
    elif str(key) == 'Key.tab':

        return Key.tab
    elif str(key) == 'Key.backspace':

        return Key.backspace
    elif str(key) == 'Key.ctrl_l':

        return Key.ctrl_l
    elif str(key) == 'Key.pause':

        return Key.pause
    elif str(key) == ',':

        return '.'
    else:
        print('not all', key)
        return key

    

def on_press(key):

    var_exists_b = 'b' in locals() or 'b' in globals()

    var_exists_a = 'a' in locals() or 'a' in globals()

    if not var_exists_a:

        global a

        a=datetime.datetime.now()

        delta_time=0

        #print('time is:',a)

    else:

        delta_time=(datetime.datetime.now()-a).total_seconds()

        #print('delta_time:',delta_time)

        a=datetime.datetime.now()

    try:

        #print('alphanumeric key  {0} pressed'.format(key.char))

        #keyboard1.press('A')

        #keyboard1.release('A')
        if str(key).startswith('Key'):
            print(str(key),'hotkey','pressed',delta_time)

            list0.append([str(key),'hotkey','pressed',delta_time])
        else:
            print(str(key).replace(',','.'),'normal_key','pressed',delta_time)

            list0.append([str(key).replace(',','.'),'normal_key','pressed',delta_time])

        ##print(list0)
        #print('key is:',key)



    except AttributeError:

        #break

        #print('special key {0} pressed'.format(key), key, type(key))

        print(key,'hotkey','pressed',delta_time)

       

        list0.append([key,'hotkey','pressed',delta_time])

        #print(list0)
        #print('key is:',key)

 

def on_release(key):

    #print(datetime.datetime.now())

    #print('{0} released'.format(key))
    global a
    delta_time=(datetime.datetime.now()-a).total_seconds()

    #print('delta_time:',delta_time)

    a=datetime.datetime.now()
    #print('keytype',type(key))
    if key == keyboard.Key.pause:


        pic=input('pic_name?:')
        list0.append([pic,'pic','pic',5])
        
    if key == keyboard.Key.esc:
        with open('1.txt','w') as f:
            f.write(str(list0))

        return False
        
    if str(key).startswith('Key'):
        #print('hotkey')
        print(str(key),'hotkey','released',delta_time)
    
        list0.append([str(key),'hotkey','released',delta_time])
    else:
        print(str(key).replace(',','.'),'normal_key','released',delta_time)
    
        list0.append([str(key).replace(',','.'),'normal_key','released',delta_time])
        
def find_pic(pic):
    #with open('z:/log.log','a') as f:
    #    f.write(pic+'\n')
    bool=True
    a=0
    while bool:
        position=p.locateCenterOnScreen(pic,confidence=0.9)
        print(pic,position)
        if position is None:
            time.sleep(1)
            a=a+1
            if a>8:
                break
            else:
                continue
        else:
            bool=False
            x,y=position
            print(x,y)
            p.moveTo(x,y,1)
            
            p.click()
            time.sleep(0.5)



 

if __name__=='__main__':

    keyboard1 = Controller()
    if len(sys.argv)==1:

        list0=[]

        

     

        with keyboard.Listener(

            on_press = on_press,

            on_release = on_release) as listener:

            listener.join()

        #file=input('keyboard record is finished, please input script name:')
        file='script.txt'
        with open(file,'w') as f:
            for i in list0:
                f.write(str(i).strip('[').strip(']').replace('\'','').replace(' ','').replace('\"','')+'\n')
    else:
        file=sys.argv[1]
        time.sleep(2)
        with open(file,'r') as f:
            lines=f.readlines()
        #print(lines)
        for x in lines:
            #print(x)
            y=x.split(',')
            print(y[0])
            key=key_change(y[0])
            time0=float(y[3].replace('\n',''))
            time.sleep(time0)
            if y[2]=='pressed':
                print('p')
                keyboard1.press(key)
                
                
            if y[2]=='released':
                print('r')
                keyboard1.release(key)
            if y[2]=='pic':
                print('pic')
                find_pic(y[0])
    
                #    keyboard1.release(y0)
                #except:
                #    pass
                #time.sleep(float(y[1]))
                
