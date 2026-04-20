# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 10:10:52 2025

@author: Administrator
"""
#BEN Software Engineer
import cv2
import numpy as np

# Function to simulate UAV value based on the frame index (distance logic)
def get_uav_value(frame_index, max_distance=500, min_value=0.0):
    # Simulate that the UAV value decreases as the frame index increases
    # Distance decreases as the drone moves away
    distance = frame_index / max_distance  # distance grows with frame index
    uav_value = max(0.8232 - distance * 0.5, min_value)  # Decrease from 0.8232
    return round(uav_value, 4)

# Load the video
video_path = r"E:\JOB Interviews\Project\Recording 2025-04-18 111533.mp4"  # Use your video path
cap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_index = 0

# Process each frame of the video
while True:
    ret, frame = cap.read()
    
    if not ret:
        break  # Exit if the video has no more frames

    # Get the UAV value for this frame based on the "distance"
    uav_value = get_uav_value(frame_index)

    # Add the UAV value text overlay on the frame
    text = f"UAV Value: {uav_value}"

    # Define font, size, and color for the text overlay
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # White color
    thickness = 2

    # Get the text size and position to center it
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = int((frame.shape[1] - text_size[0]) / 2)  # Centered horizontally
    text_y = int(50)  # Placed at the top of the frame

    # Overlay the text on the frame
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, thickness)

    # Display the frame with the UAV value
    cv2.imshow("Drone Video with UAV Value", frame)

    # Increment frame index
    frame_index += 1

    # Wait for key press to continue (or exit on 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
