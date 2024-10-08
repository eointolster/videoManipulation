import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Handle cases where FPS is not read properly
if fps == 0 or fps is None or fps != fps:  # Checks for zero, None, or NaN
    fps = 30  # Default to 30 FPS if unable to read FPS

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'sepiaToneEffect.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height),
    isColor=True  # Output will be in color
)

# Define the sepia filter
sepia_filter = np.array([[0.272, 0.534, 0.131],
                         [0.349, 0.686, 0.168],
                         [0.393, 0.769, 0.189]])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the sepia filter
    sepia_frame = cv2.transform(frame, sepia_filter)
    sepia_frame = np.clip(sepia_frame, 0, 255).astype(np.uint8)

    # Write the frame to the output video
    out.write(sepia_frame)

    # Optional: Display the resulting frame
    # cv2.imshow('Sepia Frame', sepia_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
