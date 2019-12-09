import cv2
import os
import numpy as np
from PIL import Image, ImageSequence,ImageDraw
import sys
import random

### canvase
width = 500
height = 500
## sixe of frame
resize_pos_x = 50
resize_pos_y = 50
## plae of frame
x = 260
y = 260
## center value of roi frame
mid_roi_pixel_x = ((resize_pos_x/2) + x)
mid_roi_pixel_y = ((resize_pos_y/2) + y)

#right/left bounds

right_roi_pixel_x = ((resize_pos_y) + x)
left_roi_pixel_x = ((resize_pos_x))

#up/down bounds
down_roi_pixel_y = ((resize_pos_y) + y)
up_roi_pixel_y = ((resize_pos_y))


img2 = Image.new("RGBA", (int (width),int (height)), (255, 255, 255,255))
image = Image.open("nyan cat.png")
new_image = image.resize((resize_pos_x, resize_pos_y))
text_img = Image.new("RGBA", (int(width), int(height)), (0, 0, 0,0))

text_img.paste(img2,(int (width),int(height)))
#text_img.paste(new_image, (x,y))

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
#up_down()
left_right()

text_img.show()
text_img.save("nyan cat_paste.png", format="png")












