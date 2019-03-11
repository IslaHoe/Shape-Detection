import cv2
import numpy as np

def main():
	img, threshold_img = read_img('shapes.jpg', 220)
	#img, threshold_img = read_img('detect_circles_soda.jpg', 220)
	detectPolygon(img, threshold_img)
	#detectCircle(img, threshold_img)
	show_img('img', img)
	show_img('threshold', threshold_img)


def read_img(img_name, threshold_value):
	img = cv2.imread(img_name, 0) # reads image in gray scale
	_, threshold_img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY) # aplies a binary threshold
	return img, threshold_img

def show_img(window_name, img):
	cv2.imshow(window_name, img)
	key = cv2.waitKey(0)
	if key == 27:
		# pressed ESC
		cv2.destroyAllWindows()

def detectPolygon(img, threshold_img):
	contours, _ = cv2.findContours(threshold_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	font = cv2.FONT_HERSHEY_COMPLEX_SMALL

	for cnt in contours:
		approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
		print(len(approx))
		cv2.drawContours(img, [approx], 0, (0), 5)
		
		x = approx.ravel()[0]
		y = approx.ravel()[1]
 
		if len(approx) == 3:
			cv2.putText(img, "Triangle", (x, y), font, 1, (0))
		elif len(approx) == 4:
			cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
		elif len(approx) == 5:
			cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
		elif len(approx) == 10:
			cv2.putText(img, "Star", (x, y), font, 1, (0))
		else:
			cv2.putText(img, "Circle", (x, y), font, 1, (0))

def detectCircle(img, threshold_img, min_dist=5, min_radius=0, max_radius=0):
	circles = cv2.HoughCircles(threshold_img, cv2.HOUGH_GRADIENT, 1, param2=100, minDist=int(min_dist), minRadius=min_radius, maxRadius=max_radius)

	if circles is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")
	 
		# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circles:
			# draw the circle in the output image, then draw a rectangle
			# corresponding to the center of the circle
			cv2.circle(img, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

main()