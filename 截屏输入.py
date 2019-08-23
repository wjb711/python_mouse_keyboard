import os
import pyautogui as p
import time
import pyperclip
import win32clipboard
import os
import json
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header
from PIL import ImageGrab
import sys

#发生错误，截屏，发送告警邮件，退出
def if_error():
    screen_capture()
    title='SAP机器人代录入发生错误，请查看附件截图'
    internal_email('sn.jpg',a2,title)
    tile.sleep(10)
    sys.exit()

#发送内部邮件
def internal_email(new_filename,receivers,title):



    smtp = smtplib.SMTP()
    smtp.connect('10.4.172.3')
    #smtp.login(username, password)
    #msg = MIMEMultipart('mixed')
    message = MIMEMultipart()
    #message.attach(MIMEText(str(dict0).replace(',','\n')+'<br><a href="http://1                                                                             0.102.10.16:5002">ServiceNow机器人代录入系统</a></br>','HTML','utf-8'))
    message.attach(MIMEText('<br><a href="http://10.102.10.16:5003">机器代报工系                                                                             统</a></br>','HTML','utf-8'))
    sender = 'NC-Robort@gi-de.com'
    message['From'] = "{}".format(sender)
    message['To'] = receivers
    #title='SAP机器人代录入发生错误，请查看附件截图'
    message['Subject'] = title
    #message['Content'] = str(dict0)
    att2 = MIMEApplication(open(new_filename, 'rb').read())

    att2.add_header('Content-Disposition', 'attachment', filename=new_filename )
    message.attach(att2)
    msg = MIMEText('详情见附件', 'plain', 'utf-8')
    #message['Subject'] = 'hello123'
    smtp.sendmail(sender, receivers, message.as_string())
    smtp.quit()

#截取屏幕
def screen_capture():
    img=ImageGrab.grab()
    img.save('sn.jpg')
    
#读取json，获得字典
def readjson(file):
    with open(file,"r",encoding = 'UTF-8') as f:


        dict0= json.load(f)
    return dict0
    
#读取剪贴板    
def clipboard():
    win32clipboard.OpenClipboard()
    data=win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    #print(data)
    return data
    
#找图，移动到图片上方，点击确定， 找不到，报错，退出    
def find_pic(pic,i):
    bool=True
    a=0
    while bool:
        position=p.locateCenterOnScreen(pic,confidence=0.9)
        print(pic,position)
        if position is None:
            time.sleep(1)
            a=a+1
            if a>int(i):
                if_error()
                break
            else:
                continue
        else:
            bool=False
            x,y=position
            print(x,y)
            p.moveTo(x,y)

            time.sleep(0.5)
            p.click()
            time.sleep(0.5)
#找图，移动到图片上方，点击确定， 找不到，跳过，继续 
def find_pic0(pic,i):
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
                return False
                break
            else:
                continue
        else:
            bool=False
            x,y=position
            print(x,y)
            p.moveTo(x,y)

            time.sleep(0.5)
            #p.click()
            time.sleep(0.5)
            return True

def do_something():
    pass

#登陆界面找图片，找不到，跳过，继续
def logon_pic(pic,i):
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
            p.hotkey("enter")
            
#写入字符串， 再复制，从剪贴板中获取数据做对比， 确保输入的值是正确的，如果不一致， 报错退出
def write(string):
    p.typewrite(string)
    time.sleep(0.5)
    p.hotkey('ctrl','a')
    time.sleep(0.5)
    p.hotkey('ctrl','c')
    time.sleep(0.5)
    data=clipboard()
    time.sleep(0.5)
    if data==string:
        print('same',string)
        return True
    else:
        print('different, error',string,data)
        if_error()
        return False
#退出
def logoff():
    time.sleep(1)
    p.hotkey('shift','F3')
    time.sleep(3)
    p.hotkey('shift','F3')
    find_pic('images\logoff0.png',10)
#保存
def save():
    time.sleep(1)
    p.hotkey('ctrl','s')
    time.sleep(1)
#找到相应名字的图片，并输入对应的值
def items(name,string):
    print(name,string)
    find_pic('images/'+name+'.png',20)
    time.sleep(0.5)
    p.hotkey('tab')
    time.sleep(0.5)
    write(string)

#工作流，连续输入订单号，工序号，产量，废品量
def workflow(dingdan,gongxu,chanliang,baofei):
    print('***',dingdan,gongxu,chanliang,baofei)
    items('dingdan',dingdan)
    items('gongxu',gongxu)
    items('chanliang',chanliang)
    items('baofei',baofei)
#输入工作流的list，执行， 并判断结果是否争产， 如果有error0的红色标识，退出， 如果遇到error1的黄色标识，输入回车继续。    
def baogong(list1):
    a0,a1,a2,a3=str(list1[0]),str(list1[1]),str(list1[2]),str(list1[3])
    print(a0,a1,a2,a3)
    workflow(a0,a1,a2,a3)
    save()
    if find_pic0('images\error0.png',6):
        #if_error()
        p.hotkey('F3')
        find_pic('images\fou.png',10)

    if find_pic0('images\error1.png',3):
        #if_error()
        p.hotkey('enter')
        time.sleep(4)
        #find_pic('images\quxiao.png',10)
        #if_error()
    time.sleep(2)

#主函数
if __name__=='__main__':

    #从json文件里， 读出若干个工作流列表
    for file in os.listdir('x:/job/'):
        if file.endswith('.json'):
        #file='x:/job/20190720145953.json'
            dict0=readjson('x:/job/'+file)
            a1,a2,a3=dict0
            a1=dict0[a1]
            a2=dict0[a2]
            a3=dict0[a3]
            print(a1,a2,a3)
            list0=[]
            for item in a3.replace('\r','').split('\n'):
                x=item.split('\t')
                if len(x)>=3:
                    list0.append(x)
                print(x)
            print(list0)

    打开应用界面
    os.system('.\CO11N.SAP')
    logon_pic('images\logon0.png',10)
    #针对每个json文件中的工作流， 执行报工操作
    for y in list0:
        baogong(y)
    screen_capture()
    title='顺利完成录入'
    internal_email('sn.jpg',a2,title)
    print("*************end*********")
