import cv2
import numpy as np

# Load image correctly
img = cv2.imread(r"C:\Users\Abhishek\OneDrive\Pictures\Screenshot 2025-06-21 213420.png")
if img is None:
    print("Image not found!")
    exit()

flippedhz = cv2.flip(img, 1)   # horizontal flip
flippedv = cv2.flip(img, 0)    # vertical flip
flippedboth = cv2.flip(img, -1)

cv2.imshow("original img", img)
cv2.imshow("flipped horizontal", flippedhz)
cv2.imshow("flipped vertical", flippedv)
cv2.imshow("flipped_both", flippedboth)

cv2.waitKey(0)
cv2.destroyAllWindows()
