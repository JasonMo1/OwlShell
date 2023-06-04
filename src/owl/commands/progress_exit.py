# Written by JasonMo on 2023.05.30
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

# Happy children's Day!🥳

def owl_exit(inptcmd:list, exitcode:int=100):
    ipcmlen = inptcmd.__len__()
    if ipcmlen >= 2:
        exitcode = inptcmd[1]
    print("\n    \033[33mExiting owl shell with exit code:"+str(exitcode)+"\033[0m\n")
    exit(exitcode)

if __name__ == "__main__":
    owl_exit(101)