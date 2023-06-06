import sys
from owl_errors import *

sys.path.append('.')
sys.path.append('..')

owldbg_commandlist = {'owldbg_err' : 'owldbg_err(inptcommand)', \
                      'owldbg_eval' : 'owldbg_eval(inptcommand)'}

def owldbg_err(inptcommand):
    owl_errors(int(inptcommand[1]))

def owldbg_eval(inptcommand):

    print('')
    eval(inptcommand[1])
    print('')