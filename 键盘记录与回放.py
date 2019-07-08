from pynput import keyboard

from pynput.keyboard import Key, Controller

import datetime, time,sys
import pyautogui as p
from pyautogui import *
from PIL import ImageGrab
import datetime
import sys,time
import smtplib
import pyperclip
from email.header import Header

from email.mime.text import MIMEText


#返回上月第一天和上月最后一天
def date_functions():

    now_time = datetime.datetime.now()
    #now_time_mk = time.mktime(now_time.timetuple())# 当前时间戳
    begin_of_this_month=datetime.datetime.strptime(now_time.strftime('%Y-%m-01'),'%Y-%m-%d')
    #print(begin_of_this_month,type(begin_of_this_month))
    lastday_of_lastmonth=begin_of_this_month-datetime.timedelta(days=1)
    lastday_of_lastmonth0=lastday_of_lastmonth.strftime("%Y-%m-%d")
    #print(lastday_of_lastmonth,type(lastday_of_lastmonth))
    begin_of_lastmonth=lastday_of_lastmonth.strftime("%Y-%m-01")
    return begin_of_lastmonth,lastday_of_lastmonth0

def if_error():
    time1=datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

    ImageGrab.grab().save(time1+'.jpg')
    global content,title,receivers
    title="导出报表出错，请查看截图"

    content='\\10.102.10.28\d$\CV\20190520'

    #receivers=sys.argv[3:]
    receivers=['jianbo.wang@gi-de.com']



    #if title.startswith('0'):

        #pass

    #elif title.startswith('10.102'):

    internal_email()

    #else:

        #print(title, type(title))

    sendEmail()


def internal_email():



    #from email.mime.multipart import MIMEMultipart

    from email.mime.text import MIMEText

    #print ('hello')



    smtp = smtplib.SMTP()

    smtp.connect('10.4.172.3')

    #smtp.login(username, password)

    #msg = MIMEMultipart('mixed')

    msg = MIMEText(content, 'plain', 'utf-8')

    msg['Subject'] = title

    smtp.sendmail('jianbo.wang@gi-de.com', receivers, msg.as_string())

    smtp.quit()

    #print ('ok',email_address,'ok1')







def sendEmail():





    mail_host = "smtp.163.com"      # SMTP服务器

    mail_user = "18970078166"                  # 用户名

    mail_pass = "wjb711"               # 授权密码，非登录密码



    sender = '18970078166@163.com'    # 发件人邮箱(最好写全, 不然会失败)



    message = MIMEText(content, 'plain',"utf-8")  # 内容, 格式, 编码

    message['From'] = "{}".format(sender)

    message['To'] = ",".join(receivers)

    message['Subject'] = title



    try:

        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465

        smtpObj.login(mail_user, mail_pass)  # 登录验证

        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送

        print("mail has been send successfully.")

    except smtplib.SMTPException as e:

        print(e)



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
    elif str(key) == 'Key.delete':

        return Key.delete
    elif str(key) == 'Key.insert':

        return Key.insert
    elif str(key) == ',':

        return '.'
    elif str(key) == '\\\\':

        return '/'
    else:
        #print('not all', key)
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
            if str(key)=='Key.esc':
                pass
            else:
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
    if key == keyboard.Key.insert:

        list0.append('breakpoint')
        #pic=input('pic_name?:')
        #list0.append([pic,'pic','pic',5])

    if key == keyboard.Key.esc:
        #with open('1.txt','w') as f:
        #    f.write(str(list0))

        return False

    if str(key).startswith('Key'):
        #print('hotkey')
        print(str(key),'hotkey','released',delta_time)

        list0.append([str(key),'hotkey','released',delta_time])
    else:
        print(str(key).replace(',','.'),'normal_key','released',delta_time)

        list0.append([str(key).replace(',','.'),'normal_key','released',delta_time])

def find_pic(pic,i):
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
            if a>int(i):
                #if_error()
                break
            else:
                continue
        else:
            bool=False
            x,y=position
            print(x,y)
            #p.moveTo(x,y,1)
            p.click(x,y)
            #p.click()
            #time.sleep(1)





if __name__=='__main__':
    Y=time.strftime("%Y")
    m=time.strftime("%m")
    d=time.strftime("%d")
    H=time.strftime("%H")
    M=time.strftime("%M")
    S=time.strftime("%S")
    now=datetime.datetime.now()
    days=now.day
    d4=now-datetime.timedelta(days)
    D31=str(d4.strftime("%Y/%m/%d"))
    D1=str(datetime.datetime(d4.year,d4.month,1).strftime("%Y/%m/%d"))
    #print(D1,D31)

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
        time.sleep(3)
        with open(file,'r') as f:
            lines=f.readlines()
        #print(lines)
        for x in lines:
            print('Action:',x[:10])
            #加入#号注释功能
            if x[0]=='#':
                print('comments here:,',x)

            elif x[0]=='$':
                print('command here:',x)
                exec(x[1:])
            elif x=='\n':
                print('blank here:',x)
                #exec(x[1:])
            else:
                #print(x)
                y=x.split(',')
                print(y[0])
                key=key_change(y[0])
                time0=float(y[3].replace('\n',''))
                time.sleep(time0)
                if y[2]=='pressed':
                    #print('p')
                    keyboard1.press(key)


                if y[2]=='released':
                    #print('r')
                    keyboard1.release(key)
                if y[2]=='pic':
                    print('pic')
                    find_pic(y[0],y[1])
                if y[2]=='string':
                    if y[1]=='cmd':
                        cmd=y[0].replace(';',',')
                        print(cmd)
                        exec(cmd)

                    elif y[1]=='hotkey':
                        p.press(y[0])
                    else:
                        print('string')
                        new_y0=y[0].replace("$Y",Y).replace("$m",m).replace("$d",d).replace("$H",H).replace("$M",M).replace("$S",S).replace("$D1",D1).replace("$D31",D31)
                        p.typewrite(new_y0,interval=0.25)
                        #find_pic(y[0])
