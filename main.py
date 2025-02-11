try:
    import sys
    import shutil
except ImportError:
    raise ImportError("Missing Modules, please try installing all dependencies")
def linux():
    return 0
def windows():
    raise OSError("Unfortunetly Windows is not yet Supported.")

def detect_pms():
    pms = ["pacman", "apt", "flatpak", "paru", "yay", "snap", "nix", "apk", "dnf", "yum"]
    installedpms = []
    for pm in pms:
        if shutil.which(pm):
            installedpms.append(pm)
    return installedpms

if sys.platform == "win32":
    windows()
elif sys.platform == "linux":
    linux()
else:
    raise(OSError("Unsupported Operating System: " + sys.platform))
installedpms = detect_pms()

