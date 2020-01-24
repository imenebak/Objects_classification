from siftdetector import detect_keypoints
import cv2
import os
pat = [1,2,3,4,5,6,7,8,9]
rgb = "D:/M2/Traitement_image/NEWDATA_NEWLIFE/fullTracks/RGBdatabase/"


for o in pat:
    s = 0
    pati = str(o)
    fichier2 = open(pati+"/siftHu.txt", "w")
    fichier2.close()
    fichier = open(pati+"/sift.txt", "r")
    fichier1 = open(rgb+pati+"/Hu.txt", "r")
    lines = fichier.readlines()
    lines1 = fichier1.readlines()
    fichier.close()
    fichier1.close()
    fichier2 = open(pati+"/siftHu.txt", "a")
    print(len(lines), len(lines1))
    for line in lines:
        t = line[:-1]+","+lines1[s]
        fichier2.write(t)
        s += 1
    fichier2.close()


