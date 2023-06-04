# Written by JasonMo on 2023.06.02
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

commandlist = {"exit" : "commands.progress_exit.owl_exit(inptcommand)", \
               "cd" : "special command", \
               "ls" : "commands.file_operation.owl_ls(path, inptcommand)", \
               'mkdir' : 'commands.file_operation.owl_mkdir(path, inptcommand[1])', \
               'mkfile' : 'commands.file_operation.owl_mkfile(path, inptcommand[1])', \
               'owldbg_err' : 'special command'}