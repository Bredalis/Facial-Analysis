
import cv2


# Capture video from camera
cap = cv2.VideoCapture(0)

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(
    "../data/videos/facial_expressions.avi",
    fourcc,
    20.0,
    (640, 480)
)

while cap.isOpened():
    ret, frame = cap.read()

    # If frame could not be read
    if not ret:
        break

    # Save frame to video
    out.write(frame)

    # Display video on screen
    cv2.imshow("Recording video...", frame)

    # Detect key to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources (close camera, video file and windows)
cap.release()
out.release()
cv2.destroyAllWindows()
