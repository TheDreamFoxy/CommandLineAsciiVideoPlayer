import sys
import os
import time
import cv2
from PIL import Image
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import config

sys.tracebacklimit=0

os.system('cls' if os.name == 'nt' else 'clear')
print('\033[91mUse fullscreen console for better experience. | Made for Windows command line.\033[37m')

try:
	pygame.mixer.init()
	pygame.mixer.music.load(config.song)
	print('\033[32mSong found.\033[37m')
except:
	print('\033[93mNot using song.\033[37m')

time.sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]

try:
	pygame.mixer.music.play()
except:
	pass

def resized_gray_image(image ,new_width=config.size):
	width,height = image.size
	width = width*2
	aspect_ratio = height/width
	new_height = int(aspect_ratio * new_width)
	resized_gray_image = image.resize((new_width,new_height)).convert('L')
	return resized_gray_image

def pix2chars(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

def generate_frame(image,new_width=config.size):
	new_image_data = pix2chars(resized_gray_image(image))
	total_pixels = len(new_image_data)
	ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])
	sys.stdout.write("\n"*20+ascii_image+'\n')

	#os.system('cls' if os.name == 'nt' else 'clear')

cap = cv2.VideoCapture(config.video)

if config.videoframe == True:
	try:
		while True:
			ret,frame = cap.read()
			cv2.imshow("Real time video frame",frame)
			generate_frame(Image.fromarray(frame))
			cv2.waitKey(config.waitkey)
	except:
		print('\n\033[32mEND\033[37m\n')
		exit

if config.videoframe == False:
	try:
		while True:
			ret,frame = cap.read()
			#cv2.imshow("Real time video frame",frame)
			generate_frame(Image.fromarray(frame))
			cv2.waitKey(config.waitkey)
	except:
		print('\n\033[32mEND\033[37m\n')
		exit
