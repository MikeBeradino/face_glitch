import cv2
import os
import numpy as np
from PIL import Image, ImageSequence,ImageDraw
import sys
import random

cap = cv2.VideoCapture("test5.mp4")
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT


## size of frame
resize_pos_x = 50
resize_pos_y = 50
## place of frame
x = 0
y = 0
w=0
h=0

counter =0 


# get video dimentions
if cap.isOpened(): 

    width = cap.get(3)  # float
    height = cap.get(4) # float

def save():
    os.system("ffmpeg -i %d.png -f mp4 -vcodec h264 /Users/mikeberadino/Desktop/face_glitch/test.mp4")


def right():
#########draw right
    if x <= width/2:
        for i in range(resize_pos_x):
            print pix[int (mid_roi_pixel_x),int (mid_roi_pixel_y)]
            draw = ImageDraw.Draw(text_img)
            line_color = (pix[int (mid_roi_pixel_x),int (y +i)]) 
            draw.line([mid_roi_pixel_x, y +i, width ,y+i], fill=line_color, width=1)


    #########shift l/r
def left_right():
    for i in range(resize_pos_x):

        random_pos = random.randint(1, 10)
        line_copy = new_image.crop((0, i, 50, i+1))
        text_img.paste(line_copy, (x+ random_pos, i+y))

##################################################
##################################################
#########shift l/r
def up_down():
    for i in range(resize_pos_y):

        random_pos = random.randint(1, 10)
        line_copy = new_image.crop((i, 0, i+1, 50))
        text_img.paste(line_copy, (x+i, random_pos+y))

##################################################
##################################################
def clean_up_dir():
    # remove old files in frams dir    
    filelist = [ f for f in os.listdir("frames") if f.endswith(".png") ]
    for f in filelist:
        os.remove(os.path.join("frames", f))

    # remove old files in frams dir    
    filelist = [ f for f in os.listdir("bounce") if f.endswith(".png") ]
    for f in filelist:
        os.remove(os.path.join("bounce", f))



clean_up_dir()

face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.13/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.13/share/OpenCV/haarcascades/haarcascade_eye.xml')

frame_counter = 0

def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image
 
    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src


while(True):    
    # Capture frame-by-frame
    ret, frame = cap.read()
    counter = counter + 1
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    #print("faces")
    #print(len(faces))
    # Display the resulting frame
    for (x,y,w,h) in faces:
        #counter = counter +1
        if h > 0 and w > 0:
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            
            roi = frame[y:y+h, x:x+w]
            
            resized_image = cv2.resize(roi, (w, h))
            h1, w1 = resized_image.shape[:2]
            pip_h = h
            pip_w = w
            #frame[ pip_h: pip_h+h1, pip_w : pip_w + w1] = resized_image  # make it PIP
            x_offset=y_offset=100
            frame[y_offset:y_offset+pip_h, x_offset:x_offset+resized_image.shape[1]] = roi



                    
            cv2.imwrite(r'frames/umtdp_pip.png',roi)
            cv2.imwrite(r'frames/ump_pip.png',frame)

            #newImage = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            #median = cv2.medianBlur(frame,9)
            #roi_gray = gray[y:y+h, x:x+w]         
            roi_color = frame[y:y+h, x:x+w]
            


            #eyes = eye_cascade.detectMultiScale(roi_gray)
            #for (ex,ey,ew,eh) in eyes:
             #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    print "Number of faces detected: " + str(faces.shape[0])

    cv2.imshow('frame',frame)
   
    
    #cv2.imwrite( "frames/" + str (frame_counter) +'.png',frame)
    
    #####################################################
    #####################################################
    # saving full files to frames

    #image = Image.open("frames/"+str (frame_counter) +".png")
   
    #text_img = Image.new("RGBA", (int(width), int(height)), (0, 0, 0,0))

    #text_img.paste(image,(0,0))


    ## center value of roi frame
    #mid_roi_pixel_x = (x+(w/2))
    #mid_roi_pixel_y = (y+(h/2))

    #roi_pos_size_x = (x+w)
    #roi_pos_size_y = (y+h)

    #find mid pixel point
    #pix = text_img.load()



    #for i in range(h):

#        random_pos = random.randint(1, 10)
#        line_copy = image.crop((x, i+h, x+w, i+h+1))
#        text_img.paste(line_copy, (x+ random_pos, i+y))


    #########draw right
    #if x <= width/2:
    #    for i in range(w):
    #        #print pix[int (mid_roi_pixel_x),int (mid_roi_pixel_y)]
    #        draw = ImageDraw.Draw(text_img)
    #        line_color = (pix[int (mid_roi_pixel_x),int (y +i)]) 
    #        draw.line([mid_roi_pixel_x, y +i, width ,y+i], fill=line_color, width=1)

    #########draw left
    #if x >= width/2:
    #    for i in range(w):      
    #        draw = ImageDraw.Draw(text_img)
    #        line_color = (pix[int (mid_roi_pixel_x),int (y +i)]) 
    #        draw.line([mid_roi_pixel_x, y+i, 0 ,y+i], fill=line_color, width=1)

    #########draw up
    #if y >= height/2:
     #   for i in range(h):  
     #       draw = ImageDraw.Draw(text_img)
      #      line_color = (pix[int (x+i),int (mid_roi_pixel_y)]) 
       #     draw.line([x+i, mid_roi_pixel_y, x+i ,0], fill=line_color, width=1)

    #########draw down
    #if y <= height/2:
     #   for i in range(h):
        
     #       draw = ImageDraw.Draw(text_img)
     #       line_color = (pix[int (x+i),int (mid_roi_pixel_y)]) 
     #       draw.line([x+i, mid_roi_pixel_y, x+i ,height], fill=line_color, width=1)

    #text_img.save("bounce/"+str (frame_counter)+".png", format="png")



##################################################
#####################################################
#####################################################

    frame_counter = frame_counter + 1 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done,  release the capture
cap.release()
cv2.destroyAllWindows()
save()




