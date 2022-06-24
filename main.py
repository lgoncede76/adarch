from pickletools import optimize
#Compresor de Imagenes

from PIL import Image

import os

downloadsFolder = "/Users/milla/Downloads/"
picturesFolder = "/Users/milla/Imagenes/"
musicFolder = "/Users/milla/Music/"
pdfsFolder = "/Users/milla/pdfs/"
exesFolder = "/Users/milla/exes/"
videosFolder = "/Users/milla/Videos/"


if __name__ == "__main__":
    #Listar los archivos que se encuentran en la ruta expesificada
    for filename in os.listdir(downloadsFolder):
        #Separa la Extensión del archivo de su ruta + nombre
        name, ext = os.path.splitext(downloadsFolder + filename)

        if ext in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_" + filename, optimize = True, quality = 60)
            os.replace(downloadsFolder + filename, picturesFolder + filename)
            print(name + ": " + ext)
        
        if ext in [".mp3"]:
            os.replace(downloadsFolder + filename, musicFolder + filename)
            print(name + ": " + ext)

        if ext in [".pdf"]:
            os.replace(downloadsFolder + filename, pdfsFolder + filename)
            print(name + ": " + ext)
        
        if ext in [".exe", ".msi"]:
            os.replace(downloadsFolder + filename, exesFolder + filename)
            print(name + ": " + ext)

        if ext in [".mp4", "mkv"]:
            os.replace(downloadsFolder + filename, exesFolder + filename)
            print(name + ": " + ext)
print("Done !!!")
