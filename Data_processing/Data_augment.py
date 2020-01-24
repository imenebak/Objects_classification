import cv2
import os

pati = [7]
rgb = "D:/M2/Traitement_image/NEWDATA_NEWLIFE/fullTracks/RGBdatabase/"


for o in pati:
    for path, dirs, files in os.walk(str(o)+"/train"):
        pi = 0
        for f in files:
            pi += 1
            pat = str(o)+"/train/"+f
            pat1 = rgb+str(o)+"/train/"+f

            pot = str(o)+"/train/"
            pot1 = rgb+str(o)+"/train/"
            print(pat)
            print(pat1)
            # read image as grey scale
            img = cv2.imread(pat)
            img1 = cv2.imread(pat1)
            # get image height, width
            (h, w) = img.shape[:2]
            # calculate the center of the image
            center = (w / 2, h / 2)
         
            angle90 = 90
            angle180 = 180
            #angle270 = 270
             
            scale = 1.0
             
            # Perform the counter clockwise rotation holding at the center
            # 90 degrees
            M = cv2.getRotationMatrix2D(center, angle90, scale)
            rotated90 = cv2.warpAffine(img, M, (h, w))
            rotated901 = cv2.warpAffine(img1, M, (h, w))
         
            # 180 degrees
            M = cv2.getRotationMatrix2D(center, angle180, scale)
            rotated180 = cv2.warpAffine(img, M, (w, h))
            rotated1801 = cv2.warpAffine(img1, M, (h, w))
         
            # 270 degrees
            """M = cv2.getRotationMatrix2D(center, angle270, scale)
            rotated270 = cv2.warpAffine(img, M, (h, w))
            rotated2701 = cv2.warpAffine(img1, M, (h, w))"""

            cv2.imwrite( pot+str(pi)+str(90)+"r.png", rotated90 )
            cv2.imwrite( pot+str(pi)+str(180)+"r.png", rotated180 )
            #cv2.imwrite( pot+str(pi)+str(270)+"r.png", rotated270 )

            cv2.imwrite( pot1+str(pi)+str(90)+"r.png", rotated901 )
            cv2.imwrite( pot1+str(pi)+str(180)+"r.png", rotated1801 )
            #cv2.imwrite( pot1+str(pi)+str(270)+"r.png", rotated2701 )


