import os
import time
try :
    os.system("git clone https://github.com/lamouchedu94/Youtube-downloader-FR Downloader")
    os.system("rm /Downloader/updater.py")
    print("Mise à jour réussie !")
    time.sleep(5)
except :
    print("Un problème est survenu lors de la mise à jour.")
