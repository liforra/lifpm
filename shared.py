import os
import shutil
import subprocess
import logging
import grp

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Common authentication tools and their config files
_AUTH_TOOLS = {
    "sudo": "/etc/sudoers",
    "doas": "/etc/doas.conf",
    "pkexec": None,  # polkit uses rules, no single config file
    "su": None,  # su doesn't require config files
}

def _is_root():
    """Check if the script is running as root."""
    return os.geteuid() == 0

def _is_installed(command):
    """Check if a command is installed (exists in PATH)."""
    return shutil.which(command) is not None

def _has_config(command):
    """Check if a command has a configuration file."""
    config_path = _AUTH_TOOLS.get(command)
    return config_path and os.path.isfile(config_path)

def _is_usable_by_user(command):
    """Check if a command is usable by the current user."""
    user = os.getlogin()
    
    if command == "sudo":
        try:
            sudo_group = grp.getgrnam("sudo").gr_mem
            return user in sudo_group
        except KeyError:
            return False  # sudo group doesn't exist

    elif command == "doas":
        return _has_config("doas")  # If doas.conf exists, assume it's configured

    elif command == "pkexec":
        return _is_installed("pkexec")  # polkit handles permissions differently

    elif command == "su":
        return True  # su is always usable if root allows switching

    return False

def _get_preferred_auth():
    """Find the best available and configured authentication tool."""
    for auth in _AUTH_TOOLS.keys():
        if _is_installed(auth) and (_AUTH_TOOLS[auth] is None or _has_config(auth)):
            return auth
    return None  # No valid auth tool found

def _elevate_and_run(command, *args):
    """Try to elevate privileges and run the command."""
    auth_tool = _get_preferred_auth()
    if auth_tool:
        logging.info(f"Attempting to escalate privileges using '{auth_tool}'...")
        return subprocess.run([auth_tool, command, *args]).returncode == 0
    else:
        logging.error("No valid authentication tool found to gain root privileges.")
        return False

def asroot(command, *args):
    """Run a command as root, escalating privileges if necessary."""
    if not _is_root():
        logging.warning("Not running as root. Attempting privilege escalation...")
        return _elevate_and_run(command, *args)

    if not _is_installed(command):
        logging.error(f"Command '{command}' is not installed.")
        return False

    if not _has_config(command):
        logging.warning(f"Command '{command}' has no configuration file, running anyway.")

    if not _is_usable_by_user(command):
        logging.error(f"Command '{command}' is not usable by the current user.")
        return False

    logging.info(f"Running command as root: {command} {' '.join(args)}")
    return subprocess.run([command, *args]).returncode == 0

__all__ = ["asroot"]

