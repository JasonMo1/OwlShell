# Written by JasonMo on 2023.05.30
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

import time
from colorama import *
init(autoreset=True)

def owl_errors(errnum:int=None, errstate:str='e', errmsg:str=None):

    if errmsg != None:
        messagestr = errmsg

    elif errmsg == None:

        if errnum == 000:
            messagestr = ("\n    Owl shell error 000: Command not exists ::shellmain\n")

        elif errnum == 200:
            messagestr = ("\n    Owl shell error 200: Path not exists ::owl_cd")

        elif errnum == 201:
            messagestr = ("\n    Owl shell error 201: Path not exists ::owl_ls")
        
        else:
            messagestr = ("\n    Owl shell error "+str(errnum)+": Unknown error ::???")

    if errstate == 'f':
        message = Fore.RED+messagestr+Fore.RESET
    elif errstate == 'e':
        message = Fore.LIGHTRED_EX+messagestr+Fore.RESET
    elif errstate == 'w':
        message = Fore.YELLOW+messagestr+Fore.RESET
    elif errstate == 'r':
        message = Fore.LIGHTCYAN_EX+messagestr+Fore.RESET

    print(message)
    if errstate == 'f':
        exit()
    owl_write_cache(message)


def owl_write_cache(message):
    errcache = open('cache\\feedback.txt', 'a')
    errcache.write("\""+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+message+"\"")
    errcache.close

        