import cv2

# Load image
img = cv2.imread("C:\Users\Abhishek\OneDrive\Pictures\Screenshot 2025-06-21 213420.jpg")   # change path

if img is None:
    print("Image not found!")
    exit()

# -----------------------------
# Draw a LINE
# -----------------------------
# cv2.line(image, start_point, end_point, color(BGR), thickness)
cv2.line(img, (50, 50), (300, 50), (0, 0, 255), 3)  # Red line

# -----------------------------
# Draw a CIRCLE
# -----------------------------
# cv2.circle(image, center, radius, color(BGR), thickness)
cv2.circle(img, (200, 200), 80, (255, 0, 0), 4)  # Blue circle

# -----------------------------
# Show the image
# -----------------------------
cv2.imshow("Image with Line & Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save output
# -----------------------------
cv2.imwrite("C:\Users\Abhishek\OneDrive\Pictures\Screenshot 2025-06-21 213420.jpg", img)
