# Youtube-downloader (CLI / GUI)
C'est un projet en python pour télécharger des vidéos Youtube dans toutes les définitions avec le son.

Il y a deux fichier .py : Youtube_Downloader_with_ffmpeg et Youtube_Downloader_limited_without_ffmpeg.

Youtube_Downloader_with_ffmpeg utilise pytube et ffmpeg (il faut le télécharger ffmpeg) et permet de télécharger des vidéos dans toutes les résolutions souhaitées avec le son.

Youtube_Downloader_limited_without_ffmpeg utilise pytube, mais on ne peut télécharger que des vidéos en 360p et 720p avec le son.

Pour utiliser ffmpeg merci de le télécharger (https://ffmpeg.org/download.html) et mettre les .exe dans le même répertoire que le programme.

⚠️Il faut au minimum la version v10.8.2 de pytube (ou supérieur) pour fonctioner.
⚠️Les .exe des versions antérieur à la v0.7.1-GUI ne fonctionne plus ! (pytube pas à jour)

# Nouveautées 🆕
* Les versions supérieurs à la v0.3 GUI ont une interface graphique !
* Les versions supérieurs à la v0.4 peuvent être utilisées sans ffmpeg 
* La v0.6-GUI, v0.5-GUI et la v0.4-GUI peuvent utiliser le gpu pour ré-encoder les vidéos !
* La v0.6-GUI créer un fichier dans lequel est écrit l'historique des vidéos téléchargés !(accessible depuis l'onglet fichier > consulter l'historique)
* La v0.7-GUI donne le % d'avancement du téléchargement !
* La v0.7-GUI fonctionne avec plus d'un thread ! Grâce à cela nous pouvons continuer à utiliser le programme lors du téléchargement. (Sur les anciennes versions la fenêtre affichier : ne répond pas) Un thread est utilisé pour l'interface graphique, un autre pour l'avancement du téléchargement et un dernier permet de télécharger la vidéo.
* La v0.7.1-GUI affiche une barre de progression du téléchargement.
