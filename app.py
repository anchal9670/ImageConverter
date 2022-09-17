import cv2

img_location='img/'
filename='Anchal.png'

img=cv2.imread(img_location+filename)
#convert image location and the 
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#invert the image
inverted_gray_image=255-gray_image

#blur the image by gaussian function
blurred_img=cv2.GaussianBlur(inverted_gray_image,(21,21),0)

#invert the blur image
inverted_blurred_img=255-blurred_img

#create pencil sketch image
pencil_sketch_IMG=cv2.divide(gray_image,inverted_blurred_img, scale=256.0)
#show image
cv2.imshow('original Image',img)
cv2.imshow('New Image',pencil_sketch_IMG)
cv2.waitKey(0)