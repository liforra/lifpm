try:
    import sys
except ImportError:
    raise ImportError("Missing Modules, please try installing all dependencies")
def linux():
    return 0
def windows():
    raise OSError("Unfortunetly Windows is not yet Supported.")
if sys.platform == "win32":
    windows()
elif sys.platform == "linux":
    linux()
else:
    raise(OSError("Unsupported Operating System: " + sys.platform))




