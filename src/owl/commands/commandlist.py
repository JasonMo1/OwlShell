# Written by JasonMo on 2023.06.02
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

commandlist =  {"exit" : "commands.progress_exit.owl_exit(inptcommand)", \
                "cd" : "special command", \
                "ls" : "commands.file_operation.owl_ls(inptcommand)", \
                'mkdir' : 'commands.file_operation.owl_mkdir(inptcommand[1])', \
                'mkfile' : 'commands.file_operation.owl_mkfile(inptcommand[1])', \
                'owldbg_err' : 'special command', \
                'owldbg_eval' : 'special command', \
                'rmdir' : 'commands.file_operation.owl_rmdir(inptcommand[1])', \
                'rmfile' : 'commands.file_operation.owl_rmfile(inptcommand[1])'}