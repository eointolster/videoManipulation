import cv2

# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'PencilSketchEffect.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height),
    isColor=False  # Output will be in grayscale
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale and invert the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inverted_gray = 255 - gray

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

    # Create the pencil sketch
    inverted_blur = 255 - blurred
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    # Write the frame to the output video
    out.write(sketch)

    # Optional: Display the resulting frame
    # cv2.imshow('Edges', edges)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()