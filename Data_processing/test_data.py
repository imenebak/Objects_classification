
import os, shutil, random

test = 20

i = 0
pati = [8,9]
#5
rgb = "D:/M2/Traitement_image/NEWDATA_NEWLIFE/fullTracks/RGBdatabase/"

def fichier(k):
        ko = random.choice(os.walk(k))
        return ko
for o in pati:
    pi = 0
    pat = str(o)
    if not os.path.exists(pat+"/test"):
        os.makedirs(pat+"/test")
    if not os.path.exists(rgb+pat+"/test"):
        os.makedirs(rgb+pat+"/test")
    for path, dirs, files in os.walk(pat+"/train"):
        m = len(files)
        t = int((test * m)/100)
        for i in range(0, t):
            ko = random.choice(files)
            into = pat+"/train/"+ko
            out = pat+"/test"
            shutil.move(into,out)
            intoo = rgb+pat+"/train/"+ko
            outt =rgb+pat+"/test"
            
            shutil.move(intoo,outt)
            files.remove(ko)
            
            
                
