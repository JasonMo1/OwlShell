# Written by JasonMo on 2023.05.31
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

import os
import sys
import time
import datetime
from colorama import *
from prettytable import *

sys.path.append("..") 
init(autoreset=True)

from owl_errors import *


def owl_cd(oldpath:str, newpath:str):


    if os.path.exists(newpath):
        os.chdir(newpath)
        return newpath
    else: 
        owl_errors(200)
        return oldpath
    
def owl_ls(inptcommand:list):

    path = os.getcwd()

    if os.path.exists(path):
        if '-dirsize' in inptcommand:
            dirsize = True
            owl_ls_createtable(path, dirsize)
        elif '-h' in inptcommand:
            print('\nusage: ls [-h][-dirsize]\n\n[-h]:show help message\n[dirsize]:show the size of the directory')
        else:
            dirsize = False
            owl_ls_createtable(path, dirsize)
        

    else: 
        owl_errors(201)

def owl_ls_createtable(path:str, dirsize:bool=False):
    table = PrettyTable(['#','name','type', 'size', 'modified','created'])

    table.align = 'l'

    objarg = owl_ls_getobjarg(path, dirsize)

    table.add_rows(objarg)

    # 用PrettyTable的哪有不疯的? 妈的,忍不了,一拳把地球打爆!
    # Every person who use Prettytable are all mad. Damn it!

    table.border = True
    table.left_junction_char = '├'
    table.right_junction_char = '┤'
    table.top_left_junction_char = '╭'
    table.top_right_junction_char = '╮'
    table.bottom_left_junction_char = '╰'
    table.bottom_right_junction_char = '╯'
    table.top_junction_char = '┬'
    table.bottom_junction_char = '┴'
    table.junction_char = '┼'
    table.horizontal_char = '─'
    table.vertical_char = '│'

    print('')
    print(table)

def owl_ls_getobjarg(path:str, dirsize:bool=False):
    listeddir = os.listdir(path)
    index = 0
    objalllist = []

    for filepath in listeddir:

        pathname=os.path.join(path,filepath)

        state = os.stat(pathname)

        objctimes = time.strftime("%Y-%m-%d %X", time.localtime(state[-1]))
        objmtimes = time.strftime("%Y-%m-%d %X", time.localtime(state[-2]))

        objctime = str(owl_ls_timepassed_normal(objctimes))
        objmtime = str(owl_ls_timepassed_normal(objmtimes))
        
        objname = filepath
        objsize = ("%d" %state[-4])

        if not os.path.isfile(pathname):
            objtype = 'dir' 

            if dirsize == True:
                objsize = owl_ls_getdirsize(pathname)
            else:
                objsize = 'Disabled'


        elif os.path.isfile(pathname):
            objtype = 'file'

        objreslist = [index, objname, objtype, objsize, objmtime, objctime]

        objalllist.append(objreslist)

        index += 1

    return objalllist

def owl_ls_getdirsize(dir:str):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

def owl_ls_timepassed_normal(time1):
    
    nowtime = datetime.datetime.now() 
    time2 = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")

    passedsecs = (nowtime - time2).seconds
    passeddays = (nowtime - time2).days
    passedmonths = int(passeddays/30)
    passedyears = int(passedmonths/12)
    passedweeks = int(passeddays/7)
    passedmins = int(passedsecs/60)
    passedhours = int(passedmins/60)

    if passedyears > 0:
        passedtime = str(passedyears)+' years ago'
    elif passedmonths > 0:
        passedtime = str(passedmonths)+' months ago'
    elif passedweeks > 0:
        passedtime = str(passedweeks)+' weeks ago'
    elif passeddays > 0:
        passedtime = str(passeddays)+' days ago'
    elif passedhours > 0:
        passedtime = str(passedhours)+' hours ago'
    elif passedmins > 0:
        passedtime = str(passedmins)+' minutes ago'
    else:
        passedtime = 'Just now'

    return passedtime

def owl_ls_timepassed_corlor(time1):

    # Colorful time output

    nowtime = datetime.datetime.now() 
    time2 = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")

    passedsecs = (nowtime - time2).seconds
    passeddays = (nowtime - time2).days
    passedmonths = int(passeddays/30)
    passedyears = int(passedmonths/12)
    passedweeks = int(passeddays/7)
    passedmins = int(passedsecs/60)
    passedhours = int(passedmins/60)

    if passedyears > 0:
        passedtime = Fore.RED+str(passedyears)+' years ago'+Fore.RESET
    elif passedmonths > 0:
        passedtime = Fore.LIGHTRED_EX+str(passedmonths)+' months ago'+Fore.RESET
    elif passedweeks > 0:
        passedtime = Fore.YELLOW+str(passedweeks)+' weeks ago'+Fore.RESET
    elif passeddays > 0:
        passedtime = Fore.LIGHTYELLOW_EX+str(passeddays)+' days ago'+Fore.RESET
    elif passedhours > 0:
        passedtime = Fore.GREEN+str(passedhours)+' hours ago'+Fore.RESET
    elif passedmins > 0:
        passedtime = Fore.LIGHTGREEN_EX+str(passedmins)+' minutes ago'+Fore.RESET
    else:
        passedtime = 'Just now'

    return passedtime

def owl_mkdir(name:str):
    path = os.getcwd()
    mkpath = path+"\\"+name
    os.mkdir(mkpath)

def owl_mkfile(name:str):
    path = os.getcwd()
    mkpath = mkpath = path+"\\"+name
    open(mkpath, 'w')

def owl_rmdir():

    path = os.getcwd()

    for i in os.listdir(path):
        # 如果是文件夹就递归下去
        if os.path.isdir(os.path.join(path,i)):
            owl_rmdir(os.path.join(path,i))
        # Delete file
        else:
            os.remove(os.path.join(path,i))
    os.rmdir(path)

def owl_rmfile():
    path = os.getcwd()
    os.remove(path)
