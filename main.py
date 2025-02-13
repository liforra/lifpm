try:
    import sys
    import shutil
except ImportError:
    raise ImportError("Missing Modules, please try installing all dependencies")
try:
    import pms
except ImportError:
    raise ImportError("Something went terrible wrong, Internal modules missing.")
from update import selfupdate
# Classes


class ProgramNotFoundError(Exception):
    def __init__(self, program):
        super().__init__(f"Error: '{program}' is missing or not installed.")


# Functions
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


# Detect the installed package managers
def detect_pms():
    pms = ["pacman", "apt", "flatpak", "paru", "yay", "snap", "nix", "apk", "dnf", "yum"]
    installedpms = []
    for pm in pms:
        if shutil.which(pm):
            installedpms.append(pm)
    return installedpms


# Install a package using the specified package manager
def install(package: str, pm: str):  # Ensure we have the list of installed package managers
    if pm in installedpms:
        match pm:
            case "pacman":
                pacinstall(package)
            case "apt":
                aptinstall(package)
            case "flatpak":
                flatpakinstall(package)
            case "yum":
                yuminstall(package)
            case "dnf":
                dnfinstall(package)
            case _:
                raise NotImplementedError(f"Package Manager {pm} not supported yet for installing.")
    else:
        raise ProgramNotFoundError(pm)


# Remove a package using the specified package manager
def remove(package: str, pm: str):
    installedpms = detect_pms()  # Ensure we have the list of installed package managers
    if pm in installedpms:
        match pm:
            case "pacman":
                pacremove(package)
            case "apt":
                aptremove(package)
            case "flatpak":
                flatpakremove(package)
            case "yum":
                yumremove(package)
            case "dnf":
                dnfremove(package)
            case _:
                raise NotImplementedError(f"Package Manager {pm} not supported yet for removing.")
    else:
        raise ProgramNotFoundError(pm)


# Update a package using the specified package manager
def update(package: str, pm: str):
    installedpms = detect_pms()  # Ensure we have the list of installed package managers
    if pm in installedpms:
        match pm:
            case "pacman":
                pacupdate()
            case "apt":
                aptupdate()
            case "flatpak":
                flatpakupdate()
            case "yum":
                yumupdate()
            case "dnf":
                dnfupdate()
            case _:
                raise NotImplementedError(f"Package Manager {pm} not supported yet for updating.")
    else:
        raise ProgramNotFoundError(pm)


# Upgrade a package using the specified package manager
def upgrade(package: str, pm: str):
    installedpms = detect_pms()  # Ensure we have the list of installed package managers
    if pm in installedpms:
        match pm:
            case "pacman":
                pacupgrade(package)
            case "apt":
                aptupgrade(package)
            case "flatpak":
                flatpakupgrade(package)
            case "yum":
                yumupgrade(package)
            case "dnf":
                dnfupgrade(package)
            case _:
                raise NotImplementedError(f"Package Manager {pm} not supported yet for upgrading.")
    else:
        raise ProgramNotFoundError(pm)


if sys.platform == "win32":
    windows()
elif sys.platform == "linux":
    linux()
else:
    raise (OSError("Unsupported Operating System: " + sys.platform))
installedpms = detect_pms()
try:
    print(sys.argv[1])
except IndexError:
    print("No Argument provided. Exiting....")
    exit()

args = sys.argv[1].split(" ")

pkg = (args[1].split(":"))[0]
try:
    pm = (sys.argv[1].split(":"))[1]
except IndexError:
    if not pm:
        raise NotImplementedError("Unfortunetly, search is not implemented yet!")
        exit()


match args[0]:
    case "install":
        install(pkg, pm)
    case "update":
        update(pkg, pm)
    case "upgrade":
        upgrade(pkg, pm)
    case "remove":
        remove(pkg, pm)
    case "selfupdate":
        selfupdate()
    case _:
        raise SyntaxError(sys.argv[1] + ' is not a valid subcommand\nValid is "install", "update", "upgrade", "remove"')
