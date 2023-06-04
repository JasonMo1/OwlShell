# Written by JasonMo on 2023.05.30
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

import time

def owl_errors(errnum:int):
    if errnum == 000:
        message = ("\n    \033[31mOwl shell error 000: Command not exists\033[0m\n")

    elif errnum == 200:
        message = ("\n    \033[31mOwl shell error 200: Path not exists\033[0m\n")

    elif errnum == 201:
        message = ("\n    \033[31mOwl shell error 201: Path not exists\033[0m\n")
    
    else:
        message = ("\n    \033[33mOwl shell error "+str(errnum)+": Unknown error\033[0m\n")

    print(message)
    owl_error_cache(message)


def owl_error_cache(message):
    errcache = open('cache\\feedback.txt', 'a')
    errcache.write("\""+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+message+"\"")
    errcache.close

        