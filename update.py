import urllib.request
import os.system


def selfupdate():
    urllib.request.urlretrieve("https://github.com/liforra/lifpm/releases/latest/download/installer", "/tmp/lifpminstall")
    os.system("sudo chmod +x /tmp/lifpminstall")
    os.system("sudo /tmp/lifpminstall")

    
    
selfupdate()


print(f"Downloaded {filename}")


# https://github.com/liforra/lifpm/releases/latest/download/installer
