
import os, shutil, random

test = 20

i = 0
pati = [2]
rgb = "D:/M2/Traitement_image/NEWDATA_NEWLIFE/fullTracks/RGBdatabase/"



pi = 1
for y in pati:
        y = str(y)
        for path, dirs, files in os.walk(y+"/train"):
                for f in files:
                    pi += 1
                    if (pi%2) == 0:
                            print(y+"/train/"+f)
                            print(rgb+y+"/train/"+f)
                            os.remove(y+"/train/"+f)
                            os.remove(rgb+y+"/train/"+f)
            
            
                
