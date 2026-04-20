# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 20:30:48 2025

@author: Administrator
"""

#convert_xml_to_yolo.py
#Ben SoftwareEngineer

import os
import xml.etree.ElementTree as ET
import shutil

# Paths for your XML and Image directories
xml_dir = "E:/JOB Interviews/Project/train/xml"
img_dir = "E:/JOB Interviews/Project/train/img"
output_labels_dir = "E:/JOB Interviews/Project/train/labels"

# Create the output labels directory if it doesn't exist
if not os.path.exists(output_labels_dir):
    os.makedirs(output_labels_dir)

# Function to convert XML to YOLO format
def convert_xml_to_yolo(xml_file, img_width, img_height):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # This will hold the YOLO-formatted data for the current image
    yolo_data = []

    for obj in root.findall('object'):
        # Get the object name (class label)
        class_name = obj.find('name').text

        # Get the bounding box (xmin, ymin, xmax, ymax)
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        # Convert to YOLO format (center_x, center_y, width, height)
        x_center = (xmin + xmax) / 2 / img_width
        y_center = (ymin + ymax) / 2 / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        # In YOLO, classes start from 0, so make sure to map the class to an index.
        # For example, class 1 (drone) can be mapped to 0, class 2 to 1, etc.
        class_idx = 0  # If only one class, adjust accordingly.
        
        # Append the YOLO-formatted data
        yolo_data.append(f"{class_idx} {x_center} {y_center} {width} {height}")

    return yolo_data

# Function to convert all XML files in the directory to YOLO format
def convert_all_xml_to_yolo():
    for xml_file_name in os.listdir(xml_dir):
        if xml_file_name.endswith(".xml"):
            # Full path to the XML file
            xml_file_path = os.path.join(xml_dir, xml_file_name)
            
            # Corresponding image file path (ensure the image file exists)
            img_file_name = xml_file_name.replace(".xml", ".jpg")  # Adjust extension if needed
            img_file_path = os.path.join(img_dir, img_file_name)

            if os.path.exists(img_file_path):
                # Get image dimensions
                from PIL import Image
                img = Image.open(img_file_path)
                img_width, img_height = img.size

                # Convert the XML file to YOLO format
                yolo_data = convert_xml_to_yolo(xml_file_path, img_width, img_height)

                # Save YOLO-formatted data to a new text file in the labels folder
                yolo_file_name = xml_file_name.replace(".xml", ".txt")
                yolo_file_path = os.path.join(output_labels_dir, yolo_file_name)
                with open(yolo_file_path, "w") as yolo_file:
                    yolo_file.write("\n".join(yolo_data))

                print(f"Converted {xml_file_name} to {yolo_file_name}")

if __name__ == "__main__":
convert_all_xml_to_yolo()

