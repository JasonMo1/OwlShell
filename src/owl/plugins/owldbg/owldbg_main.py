# Written by JasonMo on 2023.06.06
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

import sys
from owl_errors import *

sys.path.append('.')
sys.path.append('..')

owldbg_commandlist = {'owldbg_err' : 'owldbg_main.owldbg_err(inptcommand)', \
                      'owldbg_eval' : 'owldbg_main.owldbg_eval(inptcommand)'}

def owldbg_err(inptcommand):
    incmdlen = inptcommand.__len__()
    if incmdlen > 1:
        if incmdlen > 2:
            if incmdlen > 3:
                owl_errors(int(inptcommand[1]), str(inptcommand[2]), str(inptcommand[3]))
            else:
                owl_errors(int(inptcommand[1]), str(inptcommand[2]))
        else:
            owl_errors(int(inptcommand[1]))
    else:
        owl_errors(errstate='e', errmsg='\n    Owl shell Debugger error 000: No arguments input ::owldbg_err')

def owldbg_eval(inptcommand):
    incmdlen = inptcommand.__len__()
    print('')
    if incmdlen > 1:
        eval(inptcommand[1])
    else:
        owl_errors(errstate='e', errmsg='\n    Owl shell Debugger error 001: No arguments input ::owldbg_eval')