import os
def pacman(package:str, root:bool):
    if root:
        os.system(f'pacman -S {package}')
    else:
        os.system(f'sudo pacman -S {package}')

def apt(packman:str, root:bool):
    if root:
        os.system(f'apt install {package}')
    else:
        os.system(f'sudo apt install {package}')