import cv2 
import numpy as np  #numpy is used to convert the picture to no
import matplotlib.pyplot as plt # used to show the picture

def cartoonify_image(image_path): #cartoonify is function to convert the colors
    original_image = cv2.imread(image_path) #cv2 identify the cartoon and the read the image.
    gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) # color has 3 range - red, green and blue  (RGB) and it converts into black and white (grayscale).
    gray = cv2.medianBlur(gray, 5) # apply median blur
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 9) # conversion the boundary of the pic, for every color there is different wavelenght
    color = cv2.bilateralFilter(original_image, 9, 300, 300) #bilateralfilter will convert the color image into bilateral filter
    cartoon = cv2.bitwise_and(color, color, mask=edges) 
    
    return cartoon

input_image_path = "7up.jpg"
cartoon_image = cartoonify_image(input_image_path)
plt.figure(figsize=(12, 6)) #display using matplot using 12 will be width and 6 is height
plt.subplot(1, 2, 1) #plot that image
plt.title('Original Image') #display the title on top of the image
plt.imshow(cv2.cvtColor(cv2.imread(input_image_path), cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Cartoonified Image')
plt.imshow(cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
