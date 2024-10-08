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
    'HoughLineTransform.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height),
    isColor=True  # Output will be in color
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale and detect edges
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # Perform Hough Line Transform
    lines = cv2.HoughLinesP(
        edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10
    )

    # Create a copy of the frame to draw lines on
    line_frame = frame.copy()

    # Draw lines on the frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Write the frame to the output video
    out.write(line_frame)

    # Optional: Display the resulting frame
    # cv2.imshow('Hough Line Transform', line_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
