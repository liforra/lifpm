import os
from shared import asroot

def pacinstall(package:str, operation:str):
    asroot('pacman', '-S', package)
def pacupgrade(package:str==None):
    if package:
        asroot('pacman', '-S', package)
    else:
        asroot('pacman -u')
def apt(packman:str, root:bool):
    os.system(f'apt install {package}')
