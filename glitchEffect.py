import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'glitchEffect.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    fps,
    (frame_width, frame_height),
    isColor=True  # Output will be in color
)

# Read the first frame to get rows and cols
ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame.")
    cap.release()
    out.release()
    exit()

rows, cols = frame.shape[:2]

# Reset the video capture to the first frame
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Process the video frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Split the channels
    b_channel, g_channel, r_channel = cv2.split(frame)

    # Create translation matrices
    M_b = np.float32([[1, 0, 5], [0, 1, 0]])    # Shift right by 5 pixels
    M_r = np.float32([[1, 0, -5], [0, 1, 0]])   # Shift left by 5 pixels

    # Shift blue and red channels
    b_channel_shifted = cv2.warpAffine(b_channel, M_b, (cols, rows))
    r_channel_shifted = cv2.warpAffine(r_channel, M_r, (cols, rows))

    # Merge back the shifted channels
    glitch_frame = cv2.merge((b_channel_shifted, g_channel, r_channel_shifted))

    # Write the frame to the output video
    out.write(glitch_frame)

    # Optional: Display the frame
    # cv2.imshow('Glitch Effect', glitch_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
