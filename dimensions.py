import cv2

print("Starting program...")

image = cv2.imread(r"C:\Users\Abhishek\OneDrive\Pictures\Screenshot 2025-06-21 213420.jpg", 1)

print("After loading image:", image)

if image is not None:
    height, width, channels = image.shape
    print(f"Image loaded:\n Height: {height}\n Width: {width}\n Channels: {channels}")
else:
    print("Could not load image")
