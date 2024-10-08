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
    'Edge-Preserving.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    fps,
    (frame_width, frame_height),
    isColor=True  # Output will be in color
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply edge-preserving filter
    smoothed_frame = cv2.edgePreservingFilter(frame, flags=1, sigma_s=60, sigma_r=0.4)

    # Write the frame to the output video
    out.write(smoothed_frame)

    # Optional: Display the resulting frame
    # cv2.imshow('Edge-Preserving', smoothed_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
