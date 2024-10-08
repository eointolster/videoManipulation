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
    'opticalFlowVisualisation.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height),
    isColor=True  # Output will be in color
)

# Read the first frame
ret, first_frame = cap.read()
if not ret:
    print("Error: Could not read first frame.")
    cap.release()
    out.release()
    exit()

prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

hsv = np.zeros_like(first_frame)
hsv[..., 1] = 255

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate optical flow
    flow = cv2.calcOpticalFlowFarneback(
        prev_gray, gray, None,
        pyr_scale=0.5, levels=3, winsize=15,
        iterations=3, poly_n=5, poly_sigma=1.2, flags=0
    )

    # Compute magnitude and angle
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1], angleInDegrees=True)
    hsv[..., 0] = ang / 2  # Map angle from [0,360] to [0,180] for OpenCV HSV hue range
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

    # Convert HSV to BGR
    flow_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Write the frame to the output video
    out.write(flow_bgr)

    # Update previous frame
    prev_gray = gray

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
