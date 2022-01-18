import json, os
from tkinter.messagebox import *
from GUI.historiqueGUI import *
from GUI.changementRepertoirGUI import changement_repertoire_telechargement_GUI

def initialisation():
    '''
    Cette fonction regarde si le fichier de config est correct 
    '''
    
    try :
        os.stat("./config_Yt.json")
        with open('./config_Yt.json', 'r') as fichier:
            data = json.load(fichier)
            if data["mp3_file"] == "False" or data["mp3_file"] == "True"  :
                pass
            else :
                data["mp3_file"] = "False"
            if data["history"] == "False" or data["history"] == "True" :
                pass
            else :
                data["history"] = "False"
            if data["directory"] == "":
                changement_repertoire_telechargement_GUI()
        with open('./config_Yt.json', 'w') as fichier:
            json.dump(data, fichier, sort_keys=False, indent=5,
              ensure_ascii=False)    
    except: 
        with open("config_Yt.json","a", encoding='utf8') as file :
            file.close


def check_ffmpeg():                                             #execute commande ffmpeg -version pour voir si ffmpeg est installé 
    test_ffmpeg = os.system("ffmpeg -version")
    print("\n")
    if test_ffmpeg == 1 :
        print("Attention ! ffmpeg n'étant pas installé, les définitions proposées seront seulment : 360p et 720p.")
        showwarning("ffmpeg Warning", "ffmpeg n'étant pas installé, les définitions proposées seront seulment : 360p et 720p !")
        ffmpeg_not_installed = "True"
    else :
        ffmpeg_not_installed = "False"
    return ffmpeg_not_installed