import os
from shared import asroot


def pacinstall(package: str):
    asroot("pacman", "-S", package)


def pacupgrade(package: str == None):
    if package:
        asroot("pacman", "-S", package)
    else:
        asroot("pacman -u")


def pacupdate(package: str == None):
    if package:
        asroot("pacman", "-Sy", package)
    else:
        asroot("pacman" "-Sy")


def aptinstall(packman: str):
    asroot("apt", "install", package)
