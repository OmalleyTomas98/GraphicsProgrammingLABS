# (2) - Import OpenCV, numpy and matplotlib
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# Change the following variables to any other two image names
# (3) Download gmit images and define For example Pyramids1.jpg and .jpg
imgName1 = 'palas1.jpeg'
imgName2 = 'palas2.jpeg'


#(14 Attempted this with palas1.jpg)
#(14 Attempted this with palas2.jpg)


# (4)Using OpenCV, convert the GMIT1 image to gray scale
imgOrig1 = cv2.imread(imgName1)
imgGray1 = cv2.cvtColor(imgOrig1, cv2.COLOR_BGR2GRAY)

# Plot the original non-grayscale image
plt.subplot(2, 1, 1)
plt.imshow(cv2.cvtColor(imgOrig1, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

#PLot grey image in single window
plt.subplot(2, 1, 2)
plt.imshow(imgGray1, cmap = 'gray')
plt.title('GrayScale')
plt.xticks([])
plt.yticks([])

plt.show()

# (7) Perform Harris corner detection on the grayscale input image
imgHarris = imgOrig1.copy()
dst = cv2.cornerHarris(imgGray1, 2, 3, 0.04)



threshold = 0.20; #number between 0 and 1
#(Given on paper ) loop over the features and create a circle on the found corner 
for i in range(len(dst)):
	for j in range(len(dst[i])):
		if dst[i][j] > (threshold*dst.max()):
			cv2.circle(imgHarris,(j,i),3,(0, 255, 255),-1)


#(9) Using the Shi Tomasi algoruthm 
#(10) Create a imgShiTomasi and Perform corner detection
imgShiTomasi = imgOrig1.copy()
#Showing 50 prominent corners
corners = cv2.goodFeaturesToTrack(imgGray1, 50, 0.01, 10)

#(11) Plot the corners algorithm given to on Q sheet 
# Loop through the corners array and plot a circle at each corner
for i in corners:
	x,y = i.ravel()
	#(12)Plot the corners in red
	cv2.circle(imgShiTomasi, (x,y), 3, (0, 0, 255), -1)


#(8) - Plot imgHarris in single Window
plt.subplot(3, 1, 1)
plt.imshow(cv2.cvtColor(imgHarris, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('---------Harris---------')
plt.xticks([])
plt.yticks([])	
#Plot the Imag

# Plot imgShiTomasi
plt.subplot(3, 1, 2)
plt.imshow(cv2.cvtColor(imgShiTomasi, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('------Shi Tomasi--------')
plt.xticks([])
plt.yticks([])
# Display imgShiTomasi
plt.show()

# (13) using (code given on spec sheet) -sift = cv2.xfeatures2d.SIFT_create()
#Initiate SIFT detector
#Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()
(kps, descs) = sift.detectAndCompute(gray, None)
print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))
#Draw keypoints
imgSift = cv2.drawKeypoints(imgSift,kps,outImage=None,color=(B,G,R),flags=4)

# (14) Plot imgSift
plt.subplot(3, 1, 3)
plt.imshow(cv2.cvtColor(imgSift, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('------imgSift--------')
plt.xticks([])
plt.yticks([])

plt.show()



# Display all


# Plot the original non-grayscale image
plt.subplot(2, 1, 1)
plt.imshow(cv2.cvtColor(imgOrig1, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

#PLot grey image in single window
plt.subplot(2, 1, 2)
plt.imshow(imgGray1, cmap = 'gray')
plt.title('GrayScale')
plt.xticks([])
plt.yticks([])

plt.show() 

# (8) - Plot imgHarris in single Window
plt.subplot(3, 1, 1)
plt.imshow(cv2.cvtColor(imgHarris, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('---------Harris---------')
plt.xticks([])
plt.yticks([])	
#Plot the Imag

# Plot imgShiTomasi
plt.subplot(3, 1, 2)
plt.imshow(cv2.cvtColor(imgShiTomasi, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('------Shi Tomasi--------')
plt.xticks([])
plt.yticks([])
# Display imgShiTomasi
plt.show()


# (14) Plot imgSift
plt.subplot(3, 1, 3)
plt.imshow(cv2.cvtColor(imgSift, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('------imgSift--------')
plt.xticks([])
plt.yticks([])

plt.show()
