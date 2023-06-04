# Written by JasonMo on 2023.05.30
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

def owl_errors(errnum:int):
    if errnum == 000:
        print("\n    \033[31mOwl shell error 000: Command not exists\033[0m\n")

    elif errnum == 200:
        print("\n    \033[31mOwl shell error 200: Path not exists\033[0m")

    elif errnum == 201:
        print("\n    \033[31mOwl shell error 201: Path not exists\033[0m")
        