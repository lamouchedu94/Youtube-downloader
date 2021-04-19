# Youtube-downloader (CLI / GUI)
C'est un projet en python pour télécharger des vidéos Youtube dans toutes les définitions avec le son.

Il y a deux fichier .py : Youtube_Downloader_with_ffmpeg et Youtube_Downloader_limited_without_ffmpeg.

⚠️ATTENTION : la v0.2, v0.3, v0.3-GUI et la v0.4-GUI peuvent fonctioner sans ffmpeg.

La v0.4-GUI peut utiliser le gpu pour ré-encoder les vidéos ! (pour cela il faut modifier le fichier "config_Yt.ini" (Ce fichier se générera tout seul (dans le même répertoire 
que le .py ou le .exe) après la première exécution) et remplacer "gpu usage = False" par "gpu usage = True"

Youtube_Downloader_with_ffmpeg utilise pytube et ffmpeg (il faut le télécharger ffmpeg) et permet de télécharger des vidéos dans toutes les résolutions souhaitées avec le son.

Youtube_Downloader_limited_without_ffmpeg utilise pytube, mais on ne peut télécharger que des vidéos en 360p et 720p avec le son.
