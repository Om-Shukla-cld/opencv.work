import cv2
import numpy as np

# Load image correctly
img = cv2.imread(r"C:\Users\Abhishek\OneDrive\Pictures\Screenshot 2025-06-21 213420.png")

if img is None:
    print("Image not found!")
    exit()

angle = 45

h, w = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)

rotated = cv2.warpAffine(img, rotation_matrix, (w, h))

cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
