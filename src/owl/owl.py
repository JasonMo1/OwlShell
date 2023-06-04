# Written by JasonMo on 2023.06.02
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

import sys
import os
import getpass
import socket

from commands.commandlist import *
import commands.progress_exit
import commands.file_operation
from owl_errors import *

class Owlshell_Main(object):

    def shellmain(self):
        
        usrname = getpass.getuser()
        pcname = socket.gethostname()
        path = os.getcwd()

        print(" 🦉 Thank you for using Owl shell!")
        print("    You can donate me at https://afdian.net/a/jasonmo666\n\n")

        while 1:
            print("╭──["+pcname+"◍"+usrname+"]")
            print('│')
            print('│')

            consolinput = input("╰──["+path+">")
            
            inptcommand = consolinput.split()

            if inptcommand.__len__() < 1:
                print("")

            else:

                if inptcommand[0] in commandlist.keys():

                    if inptcommand[0] == "cd":
                        path = commands.file_operation.owl_cd(path, inptcommand[1])
                        print("")

                    elif inptcommand[0] == 'owldbg_err':
                        owl_errors(int(inptcommand[1]))

                    else:
                        runcommand = commandlist[inptcommand[0]]
                        eval(runcommand)
                        print("")
                        
                elif inptcommand[0] not in commandlist.keys():
                    owl_errors(000)



if __name__ == "__main__":
    Owlshell_Main.shellmain(self=None)