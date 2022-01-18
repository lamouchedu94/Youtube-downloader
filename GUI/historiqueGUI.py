from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *

from Youtube_Downloader_GUI import hist_download

def hist_GUI(entry_url) :
    with open("history_Yt.txt", "r") as file :
        long_hist = file.readlines()
        file.close
    fenetre3 = Tk()
    fenetre3.title("Historique")
    fenetre3.geometry("875x400")
    fenetre3.minsize(300, 200)
    fenetre3.maxsize(1500, 1500)
    fenetre3.config(background= '#f9f7f7')
    frame3 = Frame(fenetre3, bg = '#f9f7f7', borderwidth=0)
    
    label_title1 = Label(frame3, text= "Voici l'historique :", font=("Arial", 20), bg = '#f9f7f7', fg ='#000000')          #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
    label_title1.pack(padx=0, pady=10)
    nbligne = (len(long_hist)-1) / 2
    nbligne = int(nbligne)
    liste1 = Listbox(frame3,selectbackground = "#a7a7a7",bg = "#f9f7f7", width = 95, font=("Arial", 13),borderwidth=0, height = nbligne)
    ligne = 1
    button = Button(frame3, text = "Télécharger", font=("Arial", 20),bg = "#a8a8a8", borderwidth=0, fg ='#000000',activebackground = "#f7f7f7",highlightcolor = "#00aeff",command=(lambda *args:(hist_download(liste1.get(ACTIVE), fenetre3, entry_url, long_hist))))                       #après command = mettre fonction
    
    try :
        for i in range(len(long_hist)) :
            liste1.insert(i, long_hist[ligne])
            ligne += 2
    except :
        pass
    
    liste1.pack(expand = YES)
    button.pack(fill = X)
    frame3.pack(expand = YES)