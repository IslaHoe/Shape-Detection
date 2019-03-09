import cv2
import matplotlib.pyplot as plt
import numpy as np

camera_port = 1
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
def main():


	print("Taking image...")
	# Take the actual image we want to keep
	for i in range (50):
		camera_capture = get_image()
		
	ret, frame =camera.read()
	print(ret)
	print(frame)

	for j in range (10):
		file = str(j) + ".png"
		cv2.imwrite(file, camera_capture)
	

	#opens image from file 
	image = openimage('0.png')
	#converts. to grey for processing 
	grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	#uses circleshape function to detect the circle from the grey image
	imagedetected = circleshape(grayimage,image)

	#shows the imge with shape detected 
	plt.imshow(imagedetected)
	plt.show()
	return



#img = greyscale image and im is image in colour 
def circleshape(img,im):


	#prints image width and height size 
	print(img.shape)

	#cv function to detect circle uses grey image, 1 = parater for math 
	circ=cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,2, round(img.shape[0],1))
	print('here')
	print(circ)
	#, #distance between circunferences
    #200, #min radius
    #img.shape[0]*0.6)#max radius


	if len(circ)>0:
		print('Circle detected')
	else:
		print(len(circ))

	print(circ)

	if circ is not None:
		#rounds numbers to ints for drawing on pixel map 
		circ=np.round(circ[0,:]).astype('int')
		#x = center. 
		cx, cy, r = circ[0]

		for (x,y,r) in circ:
			#draws circle 
			cv2.circle(im,(x,y),r,(0,255,0),round(int(im.shape[0]*0.01),1))

	return im

def squareshape():

	return

def triangleshape():

	return

def openimage(path):
	image = cv2.imread(path)
	return image

def takepicture():

	return

def get_image():
	retval, im = camera.read()
	return im

main()
sys.exit()
