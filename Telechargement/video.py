import Youtube_Downloader_GUI, shutil, ffmpeg, os, pytube,time
from tkinter.messagebox import *

class Download_merge :
    def __init__(self) :
        pass
    
    def download_low_def(self, url,resol,chemin,titre) :                        #Télécharger en 360p et 720p uniquement (les autres def n'ont pas d'audio)
        """
        Telecharge en 360p ou 720p la video
        """
        
        format = Youtube_Downloader_GUI.get_gpu()
        if format == "False" :
            youtube = Youtube_Downloader_GUI.pytube.YouTube(url)
            video = youtube.streams.filter(res=resol).first()
            video.download(chemin,filename= Youtube_Downloader_GUI.video_title(url)+ ".mp4")
        else :
            chemin_audio = chemin + "\\audio_only"
            youtube = pytube.YouTube(url)
            t=youtube.streams.filter(only_audio=True).all()
            t[0].download(chemin_audio, filename= titre + ".mp3")
            
            try :
                os.remove(chemin + "\\" +titre + ".mp3")
            except :
                pass
            shutil.move(chemin_audio,chemin)
    def merge_video_audio(self, titre, chemin, resol) :                   #Utilise ffmpeg pour coller piste audio/vidéo         
            """
            Colle la piste audio avec la piste video 
            """
            format = Youtube_Downloader_GUI.get_gpu()
            chemin_sans_backslash = chemin.replace("\\","/")

            if format == "False" :
                input_video = ffmpeg.input(chemin_sans_backslash+'/video_only/video.mp4')
                input_audio = ffmpeg.input(chemin_sans_backslash+'/audio_only/audio.mp3')
                ffmpeg.output(input_video, input_audio, chemin_sans_backslash + "/" + titre + '.mp4', codec='copy').run()
            else :
                input_audio = chemin_sans_backslash+'/audio_only/audio.mp3'
                #input_audio = input_audio.replace("/","\\")
                shutil.move(input_audio,chemin)
                try :
                    os.remove(chemin + "\\" +titre + ".mp3")
                except :
                    pass
                os.rename(chemin + "\\audio.mp3", chemin + "\\" +titre + ".mp3")
    def download_high_def(self, url, resol, chemin,titre) :               #Télécharger dans toutes les définitions sauf 360p et 720p avec audio
        """
        Telecharge dans les autres definitions un fichier video et un fichier a part avec le son
        """
        chemin_audio = chemin + "\\audio_only"
        chemin_video = chemin + "\\video_only"
        format = Youtube_Downloader_GUI.get_gpu()
        youtube = pytube.YouTube(url)
        video = youtube.streams.filter(res=resol).first()
        try :
            if format == "False" :
                video.download(chemin_video, filename= "video.mp4")
        except  :
            if format == "False" :
                print("Erreur : Essayez de changer la définition.")
                showerror("Erreur", "la définition demandé n'existe pas pour cette vidéo. La définition choisie par défaut est 144p.")
                video = youtube.streams.filter(res="144p").first()
                video.download(chemin_video, filename= "video.mp4")

        youtube = pytube.YouTube(url)
        t=youtube.streams.filter(only_audio=True).all()
        t[0].download(chemin_audio, filename= "audio.mp3")

        print("début de l'assemblage des pistes.")
        time.sleep(2)
        #merge_video_audio(titre, chemin, resol)