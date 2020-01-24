import cv2
import os
import numpy as np
pat = [1,2,3,4,5,6,7,8,9]
Class = ["bike","boat","canoe","car","human", "noise", "pickup", "truck", "van"]
Id = 0

from skimage.feature import hog
from skimage import data, color, exposure


    
def hogg(imagename, pos):
    hog_image = np.array([[],[]])
    img = cv2.imread(imagename)
    img = cv2.resize(img, (10,10))
    fd, hog_image = hog(img, orientations=6, pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1), visualize=True)
    fichier = open(pos+"/HOG.txt", "a")
    
        #print(kpi)
    print(hog_image.shape)
    if hog_image is not None:
        fichier.write("\n"+str(Id)+","+str(Class[int(pos)-1])+",")
        f, n = 0, 0
        #hog_image = np.reshape(hog_image, -1)
        #print(hog_image.shape)
        
        for i in hog_image:
            f += 1
            for y in i:
                    n += 1
                    if(f == len(hog_image)) & (n == len(i)):
                        fichier.write(str(y))
                    else :
                        fichier.write(str(y)+",")
    fichier.close()
    """else:
        os.remove(imagename)"""

for o in pat:
    pati = str(o)
    debut = pati+"/train"
    fichier = open(pati+"/HOG.txt", "w")
    fichier.write("id,Class,pixel1,pixel2,pixel3,pixel4,pixel5,pixel6,pixel7,pixel8,pixel9,pixel10,pixel11,pixel12,pixel13,pixel14,pixel15,pixel16,pixel17,pixel18,pixel19,pixel20,pixel21,pixel22,pixel23,pixel24,pixel25,pixel26,pixel27,pixel28,pixel29,pixel30,pixel31,pixel32,pixel33,pixel34,pixel35,pixel36,pixel37,pixel38,pixel39,pixel40,pixel41,pixel42,pixel43,pixel44,pixel45,pixel46,pixel47,pixel48,pixel49,pixel50,pixel51,pixel52,pixel53,pixel54,pixel55,pixel56,pixel57,pixel58,pixel59,pixel60,pixel61,pixel62,pixel63,pixel64,pixel65,pixel66,pixel67,pixel68,pixel69,pixel70,pixel71,pixel72,pixel73,pixel74,pixel75,pixel76,pixel77,pixel78,pixel79,pixel80,pixel81,pixel82,pixel83,pixel84,pixel85,pixel86,pixel87,pixel88,pixel89,pixel90,pixel91,pixel92,pixel93,pixel94,pixel95,pixel96,pixel97,pixel98,pixel99,pixel100")
    fichier.close()
    for path, dirs, files in os.walk(debut):
        for f in files:
            Id += 1
            pos = pati+"/train/"+f
            
            hogg(pos, pati)
    

"""img = cv2.imread("25.png")
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
print(len(kp))"""

