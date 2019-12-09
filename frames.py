import cv2
import sys
import os
import numpy as np
from insta_get import scrape,prep_insta_dump,check_clean_insta_dump
from PIL import Image, ImageSequence,ImageDraw
import random


import sys, select
sleep = 60 # in min
loop = False
x = 0
y = 0
w=0
h=0

number_frames = 3


# Get user supplied values
face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.13/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
image = cv2.imread("face1.jpg")
# Read the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Get width and height
height, width = image.shape[:2]

def clean_up_dir():
    # remove old files in frams stack    
    filelist = [ f for f in os.listdir("stack") if f.endswith(".jpg") ]
    for f in filelist:
        os.remove(os.path.join("stack", f))


#while new .jpg make face==> make gif==> post
def get_images():
    for i in os.listdir("/insta_dump"):
        if i.endswith(".jpg"):
            print(("/insta_dump", i))






def make_face():

    face_count =0
    stack_counter =0
    text_img = Image.open("face1.jpg")
    
    #back_ground = Image.open("face3.jpg")
    
    

    blank_image = np.zeros((height, width, 3), np.uint8)
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        
    )

    print("Found {0} faces!".format(len(faces)))
    while stack_counter <= number_frames :
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:

            if h > 0 and w > 0:
                #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                #animate_roi()
                #loop counter for faces
                face_count = face_count+1
                print("faces==>"+ str (face_count))
                roi = image[y:y+h,x:x+w]


            
            blank_image[ y:y+h,x:x+w] = roi
            


            cv2.imwrite("stack/oi.jpg", blank_image)
            image_faces = Image.open("stack/oi.jpg")



            
            for i in range(h):
                random_pos = random.randint(-15, 15)
                line_copy = image_faces.crop((x, y+i, x+w, y+i+1))
                text_img.paste(line_copy, (x+ random_pos, y+i))


        

            if face_count == (len(faces)):
                
                text_img.save("stack/"+str (stack_counter)+".jpg", format="JPEG")
                face_count = 0
                print("stacks==>"+str (stack_counter))
                stack_counter = stack_counter +1
   


def start_y_or_n():
    print "++++++++++++++++++++++++++++++++++++++++++"
    start = raw_input('Start auto gifs y/n ?: ')
    print "++++++++++++++++++++++++++++++++++++++++++"

    if start == "y":
        loop = True 
    while loop == True:
        
        #clean_up_dir()
        #prep_insta_dump()
        
        check_clean_insta_dump()
        #get_images()
        #make_face()
        #gif_make()
        #scrape()
        #post2()

        
        random_time = random.randint(1 ,60) * sleep
        i, o, e = select.select( [sys.stdin], [], [], random_time )
        if (i):
            print "++++++++++++++++++++++++++++++++++++++++++"
            print "Goodbye"
            print "++++++++++++++++++++++++++++++++++++++++++"
            loop = False
        else:
            print "++++++++++++++++++++++++++++++++++++++++++"
            print "Making more art"
            print "++++++++++++++++++++++++++++++++++++++++++"

def gif_make():
    os.remove("stack/oi.jpg")
    path2, dirs2, files2 = next(os.walk("stack"))
    file_count2 = len(files2)
    frames2 = []
    print("++++++++++++++++++++")
    print("Creating Gifs...")
    
    for x in range(file_count2-1):

        image_file_2 = ("stack/"+str (x)+'.jpg')
        print(x)
        
        new_frame_2 = Image.open(image_file_2)
        
        frames2.append(new_frame_2)

        frames2[0].save("gifs/insta.gif", save_all=True, append_images=frames2[0:], duration=10, loop=0)


    print("New Gifs..Done")
    print("++++++++++++++++++++")





start_y_or_n()









