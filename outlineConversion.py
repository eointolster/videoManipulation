import cv2

# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'output_video.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height),
    isColor=False  # Output will be in grayscale
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

    # Write the processed frame to the output video
    out.write(edges)

    # Optional: Display the resulting frame
    # cv2.imshow('Edges', edges)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()