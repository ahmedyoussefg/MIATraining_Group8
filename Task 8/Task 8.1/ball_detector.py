import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/ahmedyoussefg/Desktop/M.I.A/task81/balls/r_051.jpg')

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Define the lower and upper bounds for blue color
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

# Define the lower and upper bounds for red color
lower_red1 = np.array([160, 160, 200])
upper_red1 = np.array([180, 255, 255])

red_mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)

lower_red2 = np.array([0, 200, 200])
upper_red2 = np.array([20, 255, 255])

red_mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

mask_red = cv2.bitwise_or(red_mask1,red_mask2)    
mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)

result = cv2.bitwise_and(img, img, mask=mask_blue | mask_red)
result_red = cv2.bitwise_and(img, img, mask=mask_red)
result_blue=cv2.bitwise_and(img, img, mask=mask_blue)
gray_img = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
blur_img = cv2.medianBlur(gray_img,5)

cv2.imshow("Red and Blue Masks",cv2.cvtColor(result,cv2.COLOR_BGR2HSV))

# Setting parameter values
t_lower = 10  # Lower Threshold
t_upper = 400  # Upper threshold
  
# Applying the Canny Edge filter
edge = cv2.Canny(blur_img, t_lower, t_upper)
"""
circles = cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,1,1,param1=400,param2=10,minRadius=0,maxRadius=40)
if circles is not None:
    circles=np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(rgb_image,(i[0],i[1]),i[2],(0,255,0),2)
"""

gray_red = cv2.cvtColor(result_red,cv2.COLOR_BGR2GRAY)
blur_red = cv2.medianBlur(gray_red,5)
red_circles = cv2.HoughCircles(blur_red,cv2.HOUGH_GRADIENT,1,1,param1=400,param2=10,minRadius=0,maxRadius=100)

gray_blue = cv2.cvtColor(result_blue,cv2.COLOR_BGR2GRAY)
blur_blue = cv2.medianBlur(gray_blue,5)
blue_circles = cv2.HoughCircles(blur_blue,cv2.HOUGH_GRADIENT,1,1,param1=400,param2=10,minRadius=0,maxRadius=100)

if red_circles is not None:
    red_circles=np.uint16(np.around(red_circles))
    for i in red_circles[0,:]:
        cv2.circle(rgb_image,(i[0],i[1]),i[2],(255,0,0),2)

if blue_circles is not None:
    blue_circles=np.uint16(np.around(blue_circles))
    for i in blue_circles[0,:]:
        cv2.circle(rgb_image,(i[0],i[1]),i[2],(0,0,255),2)

rgb_image2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
circles = cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,1,1,param1=400,param2=10,minRadius=0,maxRadius=40)
if circles is not None:
    circles=np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(rgb_image2,(i[0],i[1]),i[2],(0,255,0),2)
rgb3=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Original",cv2.cvtColor(rgb3,cv2.COLOR_BGR2RGB))
cv2.imshow("Display Balls",cv2.cvtColor(rgb_image2,cv2.COLOR_BGR2RGB))
cv2.imshow("Display Colors",cv2.cvtColor(rgb_image,cv2.COLOR_BGR2RGB))
cv2.imshow("Canny",cv2.cvtColor(edge,cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
cv2.destroyAllWindows()