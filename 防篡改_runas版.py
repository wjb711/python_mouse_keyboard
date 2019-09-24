import easygui
import easygui as g
import os
import sys
import datetime

msg = "请输入用户名和密码"
title = "防篡改系统用户登录"
user_info = []
user_info = g.multpasswordbox(msg,title,("用户名","密码"))
username=user_info[0]
password=user_info[1]
#print(user_info)
path0=os.getcwd()
#command='lsrunas.exe /user:{} /password:{} /domain: /command:"echo.exe hello" /runpath:{}'.format(username,password,path0)
command='runas.exe /user:{} /savecred "echo.exe hello'.format(username)

print('here we go!')
button=g.buttonbox(msg="选择操作",title="防篡改系统",choices=("新增文件","新增文件夹","删除","普通查看"))
if button=="新增文件":

    msg = '选择一个文件，将会返上传到防篡改系统'
    title = '文件选择对话框'
    default = r'F:flappy-bird'
    full_file_path = easygui.fileopenbox(msg,title,default)
    print('选择的文件的完整的路径为：'+str(full_file_path))
    print(os.getcwd())
    path0=os.getcwd()
    folder="防篡改数据"
    path1=path0+'\\..\\'+folder
    #command='lsrunas.exe /user:{} /password:{} /domain: /command:"cp  {} {}" /runpath:{}'.format(username,password,full_file_path,path1,path0)
    command='runas.exe /user:{} /savecred "cp  {} {}"'.format(username,full_file_path,path1,path0)
    print(command)
    returnmassage=os.popen(command,'r').read()
    print(returnmassage)
    if returnmassage=="":
        print('nothing')
    else:
        print('***',returnmassage,'***')
    
    print('here we go!')
    
    g.msgbox(msg='防篡改文件上传成功', title=' ', ok_button='OK', image=None, root=None)
    command='runas.exe /user:{} /env /savecred  "python log.py {} {}" '.format(username,full_file_path,'upload')
    print(command)
    returnmassage=os.popen(command,'r').read()
    print(returnmassage)
    command0='start {}'.format(path1)
    os.popen(command0,'r').read()

elif button=="新增文件夹":

    msg = '选择一个文件夹，将会返上传到防篡改系统'
    title = '文件选择对话框'
    default = r'F:flappy-bird'
    full_file_path = easygui.diropenbox(msg,title,default)
    print('选择的文件的完整的路径为：'+str(full_file_path))
    print(os.getcwd())
    path0=os.getcwd()
    folder="防篡改数据"
    path1=path0+'\\..\\'+folder
    #command='lsrunas.exe /user:{} /password:{} /domain: /command:"cp  {} {}" /runpath:{}'.format(username,password,full_file_path,path1,path0)
    command='runas.exe /user:{} /savecred "cp  -r -f {} {}"'.format(username,full_file_path,path1,path0)
    print(command)
    returnmassage=os.popen(command,'r').read()
    print(returnmassage)
    if returnmassage=="":
        print('nothing')
    else:
        print('***',returnmassage,'***')
    
    print('here we go!')
    
    g.msgbox(msg='防篡改文件上传成功', title=' ', ok_button='OK', image=None, root=None)
    command='runas.exe /user:{} /env /savecred  "python log.py {} {}" '.format(username,full_file_path,'upload')
    print(command)
    returnmassage=os.popen(command,'r').read()
    print(returnmassage)
    command0='start {}'.format(path1)
    os.popen(command0,'r').read()
elif button=="删除":
    msg = '选择一个文件，将会返上传到防篡改系统'
    title = '文件选择对话框'
    default = r'F:flappy-bird'
    full_file_path = easygui.fileopenbox(msg,title,default)
    print('选择的文件的完整的路径为：'+str(full_file_path))
    print(os.getcwd())
    path0=os.getcwd()
    folder="防篡改数据"
    path1=path0+'\\..\\'+folder
    command='runas.exe /user:{} /savecred "rm -f {}"'.format(username,full_file_path)
    print(command)
    returnmassage=os.popen(command,'r').read()
    print(returnmassage)
    if returnmassage=="":
        print('nothing')
    else:
        print('***',returnmassage,'***')
    command='runas.exe /user:{} /env /savecred "python log.py {} {}"'.format(username,full_file_path,'delete')
    returnmassage=os.popen(command,'r').read()
    print(returnmassage)
    
    print('here we go!')
    g.msgbox(msg='删除文件成功', title=' ', ok_button='OK', image=None, root=None)
    command0='start {}'.format(path1)
    os.popen(command0,'r').read()
    #os.system('start {}'.format(path1))
    pass
else:
    full_file_path = easygui.fileopenbox('','','')
    command='{}'.format(full_file_path)
    returnmassage=os.popen(command,'r').read()
    print(returnmassage)
    #os.system('start {}'.format(path1))

