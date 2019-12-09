import os
import random



names = [
"cristiano",
"rianagrande",
"selenagomez",
"kimkardashian",
"therock",
"kyliejenner",
"beyonce",
"taylorswift",
"leomessi",
"neymarjr",
"kendalljenner",
"justinbieber",
"natgeo",
"nickiminaj",
"khloekardashian",
"jlo",
"mileycyrus",
"katyperry",
"kourtneykardash",
"kevinhart4real",
"ddlovato",
"realmadrid",
"badgalriri",
]


# Function to rename multiple files 
def rename(): 
	path = '/Users/mikeberadino/Desktop/face_glitch/insta_dump'
	x = 0
	for filename in os.listdir(os.path.dirname(os.path.abspath(path))):
		#ext = filename.split('.')
		#extension = ext[1]
		os.rename(filename, str(x) + '.jpg' )
		x = x + 1
  		


def prep_insta_dump():
		# remove old files in insta_dump
    insta_dump_clean = [ f for f in os.listdir("insta_dump") if f.endswith(".jpg") ]
    for f in insta_dump_clean:
        os.remove(os.path.join("insta_dump", f))

def scrape():
	names_lenght = len(names)-1
	random_name = random.randint(0, names_lenght)
	print(names[random_name])
	os.system(" instagram-scraper -d /Users/mikeberadino/Desktop/face_glitch/insta_dump " +names[random_name]+ " -t image -m 10")


def check_clean_insta_dump():
	# remove non jpg files in insta_dump and rename by number
    insta_dump_clean = [ f for f in os.listdir("insta_dump") if f.endswith(".mp4") ]
    for f in insta_dump_clean:
        os.remove(os.path.join("insta_dump", f))
    #rename()

