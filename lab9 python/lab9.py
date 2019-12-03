#(3)Import OpenCV, numpy and matplotlib
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

#Author : G00361128 
#------------------

#(2)Create a python file named pyhton.py

#(13) Attempted this using 'palas.ie'

#(4) Load coloured image named 'GMIT.jpg' from moodle
imgOrig = cv2.imread('palas.jpg')

#(5) Convert to gray scale using openCV
imgGray = cv2.cvtColor(imgOrig, cv2.COLOR_BGR2GRAY)


# (6)Plotting GMIT(coloured ) and GMIT(gray) images
plt.subplot(2, 1, 1)
plt.imshow(cv2.cvtColor(imgOrig, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])


#create and display GrayScale subplot
plt.subplot(2, 1, 2)
plt.imshow(imgGray, cmap = 'gray')
plt.title('GrayScale')
plt.xticks([])
plt.yticks([])
#Display
plt.show()

#(9) create blur for 3 * 3 && 13 * 13
imgBlurSmall = cv2.GaussianBlur(imgGray,(3, 3),0)
imgBlurLarge = cv2.GaussianBlur(imgGray,(13, 13),0)

# Plot the original, gray and blurred images all 4 in single window
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(imgOrig, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(imgGray, cmap = 'gray')
plt.title('GrayScale')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(imgBlurSmall, cmap = 'gray')
plt.title('3 x 3 Blur  ')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(imgBlurLarge, cmap = 'gray')
plt.title('13 x 13 Blur')
plt.xticks([])
plt.yticks([])


#Display the plotted images
plt.show()

# (9) using Sobel Edge Detection 
sobelVertical = cv2.Sobel(imgGray, cv2.CV_64F, 1, 0, ksize=5)	# x dir
sobelHorizontal = cv2.Sobel(imgGray, cv2.CV_64F, 0, 1, ksize=5)	# y dir
sobelSum = sobelHorizontal + sobelVertical


#(12) setting the cannyThreshold
canny = cv2.Canny(imgGray, 40, 200)

# Plot the sobel Images
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(imgOrig, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])


#(8) Plots results in 2 * 2 ratio in single window 
plt.subplot(2, 3, 2)
plt.imshow(imgGray, cmap = 'gray')
plt.title('GrayScale')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 3)
plt.imshow(sobelHorizontal, cmap = 'gray')
plt.title('Sobel X')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 4)
plt.imshow(sobelVertical, cmap = 'gray')
plt.title('Sobel Y')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 5)
plt.imshow(sobelSum, cmap = 'gray')
plt.title('Sobel Sum')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 6)
plt.imshow(canny, cmap = 'gray')
plt.title('Canny Edge image')
plt.xticks([])
plt.yticks([])

#Display the plotted images
plt.show()
