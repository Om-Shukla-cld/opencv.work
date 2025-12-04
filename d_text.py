import cv2

img = cv2.imread(r"C:\Users\Abhishek\OneDrive\Pictures\Screenshot 2025-06-21 213420.jpg")

if img is None:
    print("Image not found!")
    exit()

# -----------------------------------
# Put Text on Image
# -----------------------------------
# cv2.putText(image, text, position, font, font_scale, color, thickness)
cv2.putText(
    img,
    "Hello Om!",        # text
    (150, 150),          # position (x, y)
    cv2.FONT_HERSHEY_SIMPLEX,  # font
    1.5,                # font scale
   (0 , 255, 0 ),        # color (Green)
    3,                  # thickness
    cv2.LINE_AA         # anti-aliased
)

cv2.imshow("Image with Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
