try:
    import sys
    import shutil
except ImportError:
    raise ImportError("Missing Modules, please try installing all dependencies")
try:
    import pms
except ImportError:
    raise ImportError("Something went terrible wrong, Internal modules missing.")
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


def install(package: str, pm: str):
    if pm in installedpms:
        match pm:
            case "pacman":
                pms.pacinstall(package)
            case "apt":
                pms.aptinstall(package)
            case _:
                NotImplementedError(f"Package Manager {pm} not Supported yet.")
    else:
        raise ProgramNotFoundError(pm)
        exit()


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

pkg = (sys.argv[2].split(":"))[0]
try:
    pm = (sys.argv[2].split(":"))[1]
except IndexError:
    if not pm:
        raise NotImplementedError("Unfortunetly, search is not implemented yet!")
        exit()

match sys.argv[1]:
    case "install":
        install(pkg, pm)
    case "update":
        raise NotImplementedError("Coming Soon")
    case "upgrade":
        raise NotImplementedError("Coming Soon")
    case "remove":
        raise NotImplementedError("Coming Soon")
    case _:
        raise SyntaxError(sys.argv[1] + 'is not a valid subcommand\nValid is "update" "upgrade" "remove"')
