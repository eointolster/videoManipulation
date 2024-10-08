import cv2

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
    'HistogramEqualization.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height),
    isColor=True  # Output will be in color
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to YUV color space
    yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

    # Equalize the histogram of the Y channel
    yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])

    # Convert back to BGR color space
    hist_eq_frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)

    # Write the frame to the output video
    out.write(hist_eq_frame)

    # Optional: Display the resulting frame
    # cv2.imshow('Histogram Equalization', hist_eq_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
