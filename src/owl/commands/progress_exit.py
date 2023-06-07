# Written by JasonMo on 2023.05.30
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

# Happy children's Day!🥳

from owl_errors import *

def owl_exit(inptcmd:list, exitcode:int=100):
    ipcmlen = inptcmd.__len__()
    if ipcmlen >= 2:
        exitcode = inptcmd[1]
    owl_errors(errmsg="\n    Exiting owl shell with exit code:"+str(exitcode)+"\n", errstate='r')
    exit(exitcode)

if __name__ == "__main__":
    owl_exit(101)