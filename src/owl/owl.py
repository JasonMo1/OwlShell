# Written by JasonMo on 2023.06.02
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

import os
import sys
import getpass
import socket
from colorama import *

from commands.commandlist import *
import commands.progress_exit
import commands.file_operation
from owl_errors import *

class Owlshell_Main(object):

    def shellmain(self):
        
        # colorama init
        init(autoreset=True)

        # load plugins
        owlpath = os.path.dirname(os.path.abspath(__file__))
        plugpath = os.listdir(owlpath+'\\plugins')
        plugdirs = []  # this is for debug
        
        for filepath in plugpath:
            pathname = os.path.join(owlpath+'\\plugins', filepath)

            if not os.path.isfile(pathname):
                plugdirs.append(pathname)

            plugname = os.path.split(pathname)[-1]
            plugmain = plugname+'_main'
            plugcmd = plugmain+'.'+plugname+'_commandlist'
            plugpath = owlpath+'\\plugins\\'+plugname
            cmdupdtstr = 'commandlist.update('+plugcmd+')'

            sys.path.append(plugpath)
            
            exec('import '+plugmain+'')
            eval(cmdupdtstr)

        # feedback commandlist
        owl_write_cache(str(commandlist))


        # init text on the command line
        usrname = getpass.getuser()
        pcname = socket.gethostname()
        path = os.getcwd()

        # Look at my owl!
        # {🦉}

        print(" {O,O}   Thank you for using Owl shell!")
        print("./)_)    You can donate me at https://afdian.net/a/jasonmo666")
        print("  \" \"    Our github is on https://github.com/JasonMo1/OwlShell\n\n")

        while 1:
            print(Fore.CYAN+"╭──["+Fore.GREEN+pcname+Fore.RESET+Fore.CYAN+"◍"+Fore.GREEN+usrname+Fore.CYAN+"]")
            print(Fore.CYAN+'│')
            print(Fore.CYAN+'│')

            consolinput = input(Fore.CYAN+"╰──["+Fore.GREEN+path+Fore.CYAN+">")
            
            inptcommand = consolinput.split()

            if inptcommand.__len__() < 1:
                print("")

            else:

                if inptcommand[0] in commandlist.keys():

                    if inptcommand[0] == "cd":
                        path = commands.file_operation.owl_cd(path, inptcommand[1])
                        print("")

                    else:
                        runcommand = commandlist[inptcommand[0]]
                        eval(runcommand)
                        print("")
                        
                elif inptcommand[0] not in commandlist.keys():
                    owl_errors(000, 'e')

    def owl_init_plugins(self):

        owlpath = os.path.dirname(os.path.abspath(__file__))
        plugpath = os.listdir(owlpath+'\\plugins')
        plugdirs = []
        
        for filepath in plugpath:
            pathname = os.path.join(owlpath+'\\plugins', filepath)

            if not os.path.isfile(pathname):
                plugdirs.append(pathname)

            plugname = os.path.split(pathname)[-1]
            plugmain = plugname+'_main'
            plugcmd = plugmain+'.'+plugname+'_commandlist'
            plugpath = owlpath+'\\plugins\\'+plugname
            cmdupdtstr = 'commandlist.update('+plugcmd+')'

            sys.path.append(plugpath)
            
            exec('import '+plugmain+'')
            eval(cmdupdtstr)

if __name__ == "__main__":
    Owlshell_Main.shellmain(self=Owlshell_Main)