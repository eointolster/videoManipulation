import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'colourIsolation.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    fps,
    (frame_width, frame_height),
    isColor=True  # Output will be in color
)

# Define the color range to isolate (e.g., red color)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks for the color
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Invert the mask to get the background
    mask_inv = cv2.bitwise_not(mask)

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Extract the colored part of the image using the mask
    color_part = cv2.bitwise_and(frame, frame, mask=mask)

    # Extract the grayscale part of the image using the inverted mask
    gray_part = cv2.bitwise_and(gray_bgr, gray_bgr, mask=mask_inv)

    # Combine the colored and grayscale parts
    final_frame = cv2.add(color_part, gray_part)

    # Write the frame to the output video
    out.write(final_frame)

    # Optional: Display the resulting frame
    # cv2.imshow('Color Isolation', final_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
