import cv2
import numpy as np
# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'sharpening.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height),
    isColor=False  # Output will be in grayscale
)

# Define the sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the sharpening filter
    sharpened = cv2.filter2D(frame, -1, kernel)

    # Write the frame to the output video
    out.write(sharpened)

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()