from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *

def changement_repertoire_telechargement_GUI() :            #Fenetre pour chnager le répertoire 
    def intermediaire() : 
        repertoire = entry2.get()
        if changement_repertoire(repertoire) == 0:
            fenetre2.destroy()
    path3 = get_path()
    path3 = str(path3)
    print(path3)
    
    fenetre2 = Tk()
    fenetre2.title("Répertoire téléchargement")
    fenetre2.geometry('480x250')
    fenetre2.minsize(480, 250)
    fenetre2.config(background= '#f9f7f7')
    frame2 = Frame(fenetre2, bg = '#f9f7f7', borderwidth=0)
    label_title1 = Label(frame2, text= "Chemin actuel :", font=("Arial", 15), bg = '#f9f7f7', fg ='#000000')
    label_title1.pack(expand = YES )
    entry3 = Entry(frame2, text= "", font=("Arial", 14), bg = '#ececec', fg ='#000000', relief = SOLID)                                         #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
    entry3.pack(expand = YES,fill=X)
    entry3.delete(0,END)
    entry3.insert(0, path3)
    entry3.config(bg = "#f9f7f7")
    entry3.config(state=DISABLED)
    label_title = Label(frame2, text= "Entrez le répertoire de téléchargement :", font=("Arial", 15), bg = '#f9f7f7', fg ='#000000')
    label_title.pack(expand = YES)
    entry2 = Entry(frame2, text= "", font=("Arial", 14), bg = '#ececec', fg ='#000000', relief = SOLID)                                         #25 = taille police , bg = background texte ,  fg = front ground couleur texte.    On peut soit afficher dans la fenêtre soit dans la frame
    entry2.pack(expand = YES,fill=X)

    button_confirmation = Button(frame2, text = "Confirmer", font=("Arial", 20),bg = "#a8a8a8", borderwidth=0, fg ='#000000',activebackground = "#f7f7f7",highlightcolor = "#00aeff" ,command = intermediaire)                       #après command = mettre fonction
    button_confirmation.pack(fill = X, padx=20, pady=40)

    
    frame2.pack(expand = YES, padx=0, pady=0)
    fenetre2.mainloop()