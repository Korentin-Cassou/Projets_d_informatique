from mutagen.mp3 import MP3
from mutagen.id3 import ID3

# filename contient le chemin vers un fichier MP3

lenghtLine = 70

"""-----------------------------------------------------------------"""

from os import walk

files = []
for (dirpath, dirnames, filenames) in walk("."):
    for file in filenames:
        files.append(dirpath+"/"+file)

files.sort()

"""-----------------------------------------------------------------"""




"""-----------------------------------------------------------------"""

def centerText(text, lenght):
    
    firstPlace = (lenght - len(text)) // 2
    lastPlace = lenght - firstPlace - len(text)
    
    return " " * firstPlace + text + lastPlace * " "

"""-----------------------------------------------------------------"""


"""-----------------------------------------------------------------"""

def alignedText(text, alignValue = 21):
    
    nbOfPoints = alignValue - len(text) - 1
    
    return text + nbOfPoints * "." + ":"

"""-----------------------------------------------------------------"""



generalInfoFile = files[0]
searchedFile = 0

while files[searchedFile][-1] != "3":
    
    searchedFile = searchedFile + 1
    generalInfoFile = files[searchedFile]


info = ID3(generalInfoFile)
# Numero de la pistes
numero = info["TRCK"].text[0]
# Titre de la piste
titre = info["TIT2"].text[0]
# Nom de l'artiste ou du goupe
artiste = info['TPE1'].text[0]
# Nom de l'album
album = info["TALB"].text[0]
# Genre de l'album
genre = info["TCON"].text[0]
# Année de sortie
year = info["TDRC"].text[0]


audio = MP3(generalInfoFile)
# Longugeur en secondes de la piste
longueur = audio.info.length
# Le nombre de channels audio
channels = audio.info.channels
# Le débit (bitrate) en bits par seconde
audio.info.bitrate
# Le sampling rate (fréquence d'échantillonnage) en Hz
audio.info.sample_rate
# Le bitrate mode (on ne l'utilisera pas ici)
bit_rate_type = str(audio.info.bitrate_mode)[-3:]
# Le ripper (extracteur) utilisé
ripper = audio.info.encoder_info
# Le mode (0 : Stereo ; 1 : Joint stereo ; 2 : Dual channel ; 3 : Mono)
mode = audio.info.mode

fichier = open(album + " - by " + artiste + ".nfo", "w")

fichier.write(lenghtLine * "-" + "\n")
toWrite = centerText(artiste + " - " + album, lenghtLine)
fichier.write(toWrite+ "\n")

fichier.write(lenghtLine * "-" + "\n\n")


toWrite = alignedText("Artist", 21)

fichier.write(toWrite + " " + artiste)

fichier.close()


for elements in files:
    
    # filename contient le chemin vers un fichier MP3
    filename = elements
    
    if filename[-4:] == ".mp3":
    
        info = ID3(filename)
        # Numero de la pistes
        numero = info["TRCK"].text[0]
        # Titre de la piste
        titre = info["TIT2"].text[0]
        # Nom de l'artiste ou du goupe
        artiste = info['TPE1'].text[0]
        # Nom de l'album
        album = info["TALB"].text[0]
        # Genre de l'album
        genre = info["TCON"].text[0]
        # Année de sortie
        year = info["TDRC"].text[0]


        audio = MP3(filename)
        # Longugeur en secondes de la piste
        longueur = audio.info.length
        # Le nombre de channels audio
        channels = audio.info.channels
        # Le débit (bitrate) en bits par seconde
        audio.info.bitrate
        # Le sampling rate (fréquence d'échantillonnage) en Hz
        audio.info.sample_rate
        # Le bitrate mode (on ne l'utilisera pas ici)
        bit_rate_type = str(audio.info.bitrate_mode)[-3:]
        # Le ripper (extracteur) utilisé
        ripper = audio.info.encoder_info
        # Le mode (0 : Stereo ; 1 : Joint stereo ; 2 : Dual channel ; 3 : Mono)
        mode = audio.info.mode
