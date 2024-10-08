import cv2

# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'MotionDetection.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height),
    isColor=False  # Output will be in grayscale
)

# Initialize background subtractor
back_sub = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask = back_sub.apply(frame)

    # Write the frame to the output video
    out.write(fg_mask)

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()