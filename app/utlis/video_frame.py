import cv2
import os

def extract_keyframes(video_path, output_dir="app/static/uploads/frames", frame_interval=60):

    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0
    saved = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % frame_interval == 0:
            frame_file = os.path.join(output_dir, f"frame_{count}.jpg")
            cv2.imwrite(frame_file, frame)
            saved.append(frame_file)
        count += 1

    cap.release()
    return saved
