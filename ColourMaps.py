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
if fps == 0:
    fps = 30  # Default to 30 if FPS cannot be read

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'Colourmaps.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    fps,
    (frame_width, frame_height),
    isColor=True  # Output will be in color
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a color map (e.g., COLORMAP_JET)
    colored_frame = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    # Write the frame to the output video
    out.write(colored_frame)

    # Optional: Display the resulting frame
    # cv2.imshow('Color Map', colored_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
