import cv2
import os

video_path = "...mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video tidak dapat dibuka")
    exit()

output_folder = "extracted_frames"
os.makedirs(output_folder, exist_ok=True)

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imwrite(
        os.path.join(output_folder, f"frame_{frame_count:04d}.jpg"),
        frame
    )

    frame_count += 1

cap.release()

print(f"Berhasil mengekstrak {frame_count} frame")