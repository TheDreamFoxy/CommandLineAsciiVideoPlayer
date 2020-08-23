import os 
import sys
import cv2
from PIL import Image

# Ascii characters used to create the output 
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resized_gray_image(image ,new_width=70):
	width,height = image.size
	aspect_ratio = height/width
	new_height = int(aspect_ratio * new_width)
	resized_gray_image = image.resize((new_width,new_height)).convert('L')
	return resized_gray_image

def pix2chars(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

def generate_frame(image,new_width=70):
	new_image_data = pix2chars(resized_gray_image(image))

	total_pixels = len(new_image_data)

	ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])

	sys.stdout.write(ascii_image)
	os.system('cls')



cap = cv2.VideoCapture("resources/blackdance.mp4")

while True:

	ret,frame = cap.read()
	cv2.imshow("frame",frame)
	generate_frame(Image.fromarray(frame))
	cv2.waitKey(10)
