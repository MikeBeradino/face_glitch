

        for i in range(h):

            random_pos = random.randint(1, 20)
            line_copy = image.crop((x, i+h/2, x+w, i+h/2+1))
            text_img.paste(line_copy, (x+random_pos, y))




#########draw right
if x <= width/2:
	for i in range(resize_pos_x):
		print pix[int (mid_roi_pixel_x),int (mid_roi_pixel_y)]
		draw = ImageDraw.Draw(text_img)
		line_color = (pix[int (mid_roi_pixel_x),int (y +i)]) 
		draw.line([mid_roi_pixel_x, y +i, width ,y+i], fill=line_color, width=1)

#########draw left
if x >= width/2:
	for i in range(resize_pos_x):
	
		draw = ImageDraw.Draw(text_img)
		line_color = (pix[int (mid_roi_pixel_x),int (y +i)]) 
		draw.line([mid_roi_pixel_x, y+i, 0 ,y+i], fill=line_color, width=1)

#########draw up
if y >= height/2:
	for i in range(resize_pos_y):
	
		draw = ImageDraw.Draw(text_img)
		line_color = (pix[int (x+i),int (mid_roi_pixel_y)]) 
		draw.line([x+i, mid_roi_pixel_y, x+i ,0], fill=line_color, width=1)

#########draw down
if y <= height/2:
	for i in range(resize_pos_y):
	
		draw = ImageDraw.Draw(text_img)
		line_color = (pix[int (x+i),int (mid_roi_pixel_y)]) 
		draw.line([x+i, mid_roi_pixel_y, x+i ,height], fill=line_color, width=1)