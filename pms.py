import os
from shared import asroot


def pacinstall(package: str):
    asroot("pacman", "-S", package)

def pacupgrade(package: str = None):
    if package:
        asroot("pacman", "-S", package)
    else:
        asroot("pacman", "-Su")

def pacupdate():
    asroot("pacman", "-Sy")

def pacremove(package: str):
    asroot("pacman", "-R", package)

def aptinstall(package: str):
    asroot("apt", "install", package)

def aptupgrade(package: str = None):
    if package:
        asroot("apt", "install", "--only-upgrade", package)
    else:
        asroot("apt", "upgrade")

def aptupdate():
    asroot("apt", "update")

def aptremove(package: str):
    asroot("apt", "remove", package)

def flatpakinstall(package: str):
    asroot("flatpak", "install", package)

def flatpakupgrade(package: str = None):
    if package:
        asroot("flatpak", "update", package)
    else:
        asroot("flatpak", "update")

def flatpakupdate():
    asroot("flatpak", "update")

def flatpakremove(package: str):
    asroot("flatpak", "uninstall", package)

def yuminstall(package: str):
    asroot("yum", "install", package)

def yumupgrade(package: str = None):
    if package:
        asroot("yum", "update", package)
    else:
        asroot("yum", "update")

def yumupdate():
    asroot("yum", "makecache")

def yumremove(package: str):
    asroot("yum", "remove", package)

def dnfinstall(package: str):
    asroot("dnf", "install", package)

def dnfupgrade(package: str = None):
    if package:
        asroot("dnf", "update", package)
    else:
        asroot("dnf", "upgrade")

def dnfupdate():
    asroot("dnf", "makecache")

def dnfremove(package: str):
    asroot("dnf", "remove", package)

