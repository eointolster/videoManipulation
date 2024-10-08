import cv2

# Load the video
cap = cv2.VideoCapture('original.MOV')  # Replace with your video file path

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(
    'ColourInversion.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    fps,
    (frame_width, frame_height),
    isColor=True  # Output will be in color
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Invert colors
    inverted_frame = cv2.bitwise_not(frame)

    # Write the frame to the output video
    out.write(inverted_frame)

    # Optional: Display the resulting frame
    # cv2.imshow('Inverted Frame', inverted_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
