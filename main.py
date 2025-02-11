try:
    import egqgsys
except ImportError:
    raise ImportError("Missing Modules, please try installing all dependencies")
class UnsupportedOS(Exception):
    pass
def linux():
    OS = linux
def windows():
    OS = windows
if sys.platform == "win32":
    windows()
elif sys.platform == "linux":
    linux()
else:
    raise(OSError("Unsupported Operating System: " + sys.platform))