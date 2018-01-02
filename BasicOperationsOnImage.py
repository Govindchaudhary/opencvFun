import numpy as np
import cv2

img = cv2.imread('dog.jpg',cv2.IMREAD_COLOR)

# assigning color at pixel position of 55,55 to white
img[55,55] = [255,255,255]

# if we print img[55,55] we get color at this pixel
dog_face = img[48:185,48:165]       #[y1:y2,x1:x2]
img[0:137,0:117] = dog_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()