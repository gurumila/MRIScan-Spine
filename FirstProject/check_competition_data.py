#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 16:25:21 2023

@author: milan

print file names in a given folder. it should check all sub folders as well.
"""

import os

import pydicom
import matplotlib.pyplot as plt

def list_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        print(f"Listing files for: {root}")
        print(f"Total directories: {len(dirs)}")
        print(f"Total files: {len(files)}")
            
"""
# Provide the path to the folder you want to search
print("Test Data:")
path = "../RSNA/data/test_images"

# Call the function with the specified folder path
list_files(path)

# Provide the path to the folder you want to search
print("Training Data:")
path = "../RSNA/data/train_images"

# Call the function with the specified folder path
list_files(path)
"""
"""
# Provide the path to the folder you want to search
print("Segmentations Data:")
path = "../RSNA/data/segmentations"

# Call the function with the specified folder path
list_files(path)
"""

def view_dicom_file(file_path):
    # Load the DICOM file
    dicom_data = pydicom.dcmread(file_path)

    # Display the image
    plt.imshow(dicom_data.pixel_array, cmap=plt.cm.gray)
    plt.axis('off')
    plt.show()

# Provide the path to the DICOM file you want to view
dicom_file_path = "../RSNA/data/test_images/1.2.826.0.1.3680043.5876/1.dcm"

# Call the function with the specified DICOM file path
view_dicom_file(dicom_file_path)