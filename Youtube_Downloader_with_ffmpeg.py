from pytube import YouTube
import pytube
import time
import ffmpeg
import os

y = ''                                                                              #yes
n = ''                                                                              #no
resol = ''                                                                          #résolution
boucle = True
audio_titre = ''
video_titre = ''
fichier_config = os.getcwd() + "\config.txt"

#'https://www.youtube.com/watch?v=vG3_GIcIDbM&t=0s'

#s = os.stat('C:/Video/Youtube/video_only/1.mp4')

nom = os.name

def download1() :
    temps('debut', 0)
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(res=resol).first()
    video.download(chemin + "\\Youtube")
    
    temps(0, 'fin')

def download2() :
    
    temps('debut', 0)
    
    youtube = pytube.YouTube(url)
    t=youtube.streams.filter(only_audio=True).all()
    t[0].download(chemin + "\\Youtube\\audio_only", filename= 'audio')

    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(res=resol, file_extension='mp4').first()
    video.download(chemin + "\\Youtube\\video_only", filename= 'video')

    temps(0, 'fin')

def os_user() :
    
    if nom == 'posix' :
        print("mauvais os")
        time.sleep(5)
        quit()

def merge_video_audio() :

    input_video = ffmpeg.input(chemin_sans_backslash+'/Youtube/video_only/video.mp4')
    input_audio = ffmpeg.input(chemin_sans_backslash+'/Youtube/audio_only/audio.mp4')
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(chemin_sans_backslash + "/Youtube/" + titre + '.mp4').run()            #ffmpep ne gère pas les #, les ?

def temps(debut, fin) :
    
    if debut == 'debut' or debut == 1:
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print("Téléchargement démaré à :", result)
        debut = 0 
    
    if fin == 'fin' or fin == 1:
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print("Téléchargement terminé à :", result)
        fin = 0 

def changement_repertoire_telechargement() :
    with open("config.txt", "w+") as file :
        file.write("True\n")
        file.close()
        try :
            os.rmdir(chemin_video)
            os.rmdir(chemin_audio)
            os.rmdir(chemin_racine)
        except :
            print("dossiers non supprimables (manquants)")
        print("redémarez le programme pour changer le dossier de téléchargement.")
        time.sleep(5)
        quit()

def path() :
    boucle_path = True
    try : 
        os.stat("config.txt")
    except :
        print("Fichier config.txt inexistant.")
        with open("config.txt", "a") as file :
            file.write("True")
            file.close()
            print("config.txt à bien été crée")
    
    with open("config.txt", "r+") as file :
        def_chemin1 = file.readlines(1)
        def_chemin = str(def_chemin1[0])
        file.close()
    while boucle_path :
        if def_chemin == 'True' or def_chemin == 'True\n' :
            print("Définir le répertoire de téléchargement des vidéos :")
            rep = input()
            
            try :
                os.stat(str(rep))
            except :
                print("Le repertoire de destination n'existe pas. Le changer ? y ou n") 
                rep = input()
                if rep == "y" :
                    continue
                else :
                    print("Aucun chemin correct deffini. Fin.")
                    time.sleep(3)
                    quit() 
            print("le répertoire à bien été défini.")
            with open("config.txt", "w+") as file :
                file.write("False\n")
                file.write(str(rep))
                file.close()
                break
        else : 
            break
    with open("config.txt", "r+") as file :
        chemin1 = file.readlines()
        chemin1 = chemin1[1]
        file.close()
        return chemin1

os_user()


test_ffmpeg = os.system("ffmpeg -version")
print("")
if test_ffmpeg == 1 :
    print("ffmpeg n'est pas installé.")
    time.sleep(3)
    quit()

chemin = path()
chemin_sans_backslash = chemin.replace("\\", "/")

chemin_racine= chemin + "\\Youtube"
chemin_audio = chemin_racine + "\\audio_only"
chemin_video = chemin_racine + "\\video_only"



try :
    os.stat(chemin_racine)
    os.stat(chemin_audio)
    os.stat(chemin_video)
except :
    print("dossiers manquants. Les créer ? y ou n")
    demande = str(input())
    if demande == "y" :
        try : 
            os.stat(chemin)
        except : 
            changement_repertoire_telechargement()
    
        os.mkdir(chemin_racine)
        os.mkdir(chemin_audio )
        os.mkdir(chemin_video )
        print("dossiers crées dans " + chemin + ".")
    if demande == "n" :
        print("Impossible de continuer. Relancez le programme.")
        time.sleep(5)
        quit()

print("Pour changer le dossier de téléchagement rentrez 1 à la place de l'url.")

while True :
    boucle = True
    print('Url de la vidéo :')

    url = input()
    if url == "1" : 
        changement_repertoire_telechargement()
    
    try :
        yt = YouTube(url)
        titre_origine = yt.title
        titre = titre_origine.replace('#', "z")
        titre_origine = titre
        titre = titre_origine.replace('?', "a")
        print(yt.title)
    except :
        print('lien non valide.')
        time.sleep(0.5)
        continue
   
    print('C est la bonne video ? y ou n')
    demande = str(input())
    if demande == 'n' :
        print('réessayer ? y ou n')
        demande = str(input())
        if demande == 'n' :
            print("fin.") 
            time.sleep(5)
            quit()
        if demande == 'y' :
            print('redémarage')
            continue
        else :
            print('mauvaise entree.')
            continue
    
    
    if demande == 'y' :
        pass
    else :
        print('mauvaise entree.')
        print('C est la bonne video ? y ou n ?')
        demande = str(input())
        if demande == 'y' :
            pass
        else :
            continue
            print("redemarrage.")

    while boucle :
        
        print('telecharger en quel definition ? (144p / 240p / 360p / 480p / 720p / 1080p / 1440p / 2160p)')
        resol = str(input())

        if resol == '' or resol == '144p' or resol == '240p' or resol == '480p' or resol == '1080p' or resol == '1440p' or resol == '2160p' :
            try :
                os.remove(chemin_sans_backslash+"/Youtube/audio_only/audio.mp4")
                os.remove(chemin_sans_backslash+"/Youtube/video_only/video.mp4")
            except :
                pass
            print("video en cours de téléchargement")
            download2()
            print("Fin du téléchargement. Démarage de l'assemblage des pistes.")
            time.sleep(1)
            merge_video_audio()
            print("video telecharge avec succes dans" + chemin + "!")
            
            os.remove(chemin_sans_backslash+"/Youtube/audio_only/audio.mp4")
            os.remove(chemin_sans_backslash+"/Youtube/video_only/video.mp4")
            
            print("en télécharger une autre ? y ou n")
            demande = str(input())
            if demande == 'y' :
                boucle = False
                continue
            else :
                print("fin.")
                time.sleep(5)
                quit()             

        if resol == '360p' or resol == '720p':
            print("video en cours de téléchargement")
            
            download1()
        
            print("video telecharge avec succes dans" + chemin +"\YouTube !")
            
            print("en télécharger une autre ? y ou n")
            demande = str(input())
            if demande == 'y' :
                boucle = False
                continue
            else :
                print("fin.")
                
                time.sleep(5)
                quit()                    
        else :
            print('mauvaise entree. Quitter ? y ou n')          #affichage lors d'une mauvaise selection de la définition
            demande = str(input())
            if demande == 'y' :
                print("fin.") 
                
                time.sleep(5)
                quit()
            continue


