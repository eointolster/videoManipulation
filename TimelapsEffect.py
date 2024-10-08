import cv2

# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'TimeLapse.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height),
    isColor=False  # Output will be in grayscale
)

frame_skip = 5  # Skip every 5 frames
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_skip == 0:
        out.write(frame)

    frame_count += 1

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()