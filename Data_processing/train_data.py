
import os, shutil, random


train = 80
pati = [8,9]
i = 0
size = []
rgb = "D:/M2/Traitement_image/NEWDATA_NEWLIFE/fullTracks/RGBdatabase/"
for o in pati:
    pat = str(o)
    for path, dirs, files in os.walk(pat):
        for file in files:
            op = pat+"/train"
            if not os.path.exists(op):
                os.makedirs(op)
            if not os.path.exists(rgb+op):
                os.makedirs(rgb+op)
            kl = pat+"/"+file
            kll = rgb+pat+"/"+file
            shutil.move(kl,pat+"/train")
            shutil.move(kll,rgb+pat+"/train")
                
