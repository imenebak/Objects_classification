from siftdetector import detect_keypoints
import cv2
import os
pat = [2,3,4,5,6,7,8,9]
Class = ["bike","boat","canoe","car","human", "noise", "pickup", "truck", "van"]
Id = 119
def match_template(imagename, pos):
    img = cv2.imread(imagename)
    kpi = detect_keypoints(imagename)
    fichier = open(pos+"/sift.txt", "a")
    
        #print(kpi)
    if kpi is not None:
        fichier.write("\n"+str(Id)+","+str(Class[int(pos)-1])+",")
        f, n = 0, 0
        for i in kpi:
            f += 1
            for y in i:
                    n += 1
                    if(f == len(kpi)) & (n == len(i)):
                        fichier.write(str(y))
                    else :
                        fichier.write(str(y)+",")
    fichier.close()
    """else:
        os.remove(imagename)"""

for o in pat:
    pati = str(o)
    debut = pati+"/train"
    fichier = open(pati+"/sift.txt", "w")
    fichier.write("id,Class,texture1,texture2,texture3,texture4,texture5,texture6,texture7,texture8,texture9,texture10,texture11,texture12,texture13,texture14,texture15,texture16,texture17,texture18,texture19,texture20,texture21,texture22,texture23,texture24,texture25,texture26,texture27,texture28,texture29,texture30,texture31,texture32,texture33,texture34,texture35,texture36,texture37,texture38,texture39,texture40,texture41,texture42,texture43,texture44,texture45,texture46,texture47,texture48,texture49,texture50,texture51,texture52,texture53,texture54,texture55,texture56,texture57,texture58,texture59,texture60,texture61,texture62,texture63,texture64,texture65,texture66,texture67,texture68,texture69,texture70,texture71,texture72,texture73,texture74,texture75,texture76,texture77,texture78,texture79,texture80,texture81,texture82,texture83,texture84,texture85,texture86,texture87,texture88,texture89,texture90,texture91,texture92,texture93,texture94,texture95,texture96,texture97,texture98,texture99,texture100,texture101,texture102,texture103,texture104,texture105,texture106,texture107,texture108,texture109,texture110,texture111,texture112,texture113,texture114,texture115,texture116,texture117,texture118,texture119,texture120,texture121,texture122,texture123,texture124,texture125,texture126,texture127,texture128")
    fichier.close()
    for path, dirs, files in os.walk(debut):
        for f in files:
            Id += 1
            pos = pati+"/train/"+f
            print(pos)
            match_template(pos, pati)    
    

"""img = cv2.imread("25.png")
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
print(len(kp))"""

