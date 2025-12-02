import cv2

image = cv2.imread(r"C:\Users\Abhishek\OneDrive\Pictures\Screenshot 2025-06-21 213420.png")

if image is not None:
    cropped = image[100:200, 50:140]  # y1:y2, x1:x2
    cv2.imshow("Original image", image)
    cv2.imshow("Cropped image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found! Check the file path.")
