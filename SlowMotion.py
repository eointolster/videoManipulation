import cv2

# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'slow_motion_video.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps / 2,  # Halve the frames per second
    (frame_width, frame_height)
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Duplicate each frame
    out.write(frame)
    out.write(frame)

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()