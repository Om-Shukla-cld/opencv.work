import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Abhishek\OneDrive\Pictures\Screenshot 2025-06-21 213420.jpg", 1)

if image is None:
    print("Image not found! Check file path.")
else:
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
