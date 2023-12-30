#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:05:33 2023

@author: milan
"""


import os
import tkinter as tk
from tkinter import filedialog
import pydicom
from PIL import Image, ImageTk

class DICOMViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DICOM Viewer")

        # Variables
        self.dicom_file_path = tk.StringVar()
        self.image_label = tk.Label(root)

        # Browse button
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=10)
        
        self.folder_path = tk.StringVar()
        self.folder_path.set("/Users/milan/Documents/GitHub/Kaggle/MRIScan-Spine/RSNA/data")

        # Label for displaying selected folder path
        self.folder_label = tk.Label(root, textvariable=self.folder_path, justify="center", wraplength=300)
        self.folder_label.pack(pady=10)


        # Label for displaying selected DICOM file path
        self.file_label = tk.Label(root, textvariable=self.dicom_file_path, justify="center", wraplength=300)
        self.file_label.pack(pady=10)

        # Display image button
        self.display_button = tk.Button(root, text="Next Image", command=self.display_next_dicom_image)
        self.display_button.pack(pady=10)
        
        self.file_index = 0
        self.dicom_files = []

    def browse_folder(self):
        self.file_index = 0
        selected_folder_path = filedialog.askdirectory(
            initialdir=self.folder_path.get(),
            title="Select a Directory", 
            mustexist=True)
        self.folder_path.set(selected_folder_path)
        if self.folder_path:
            self.dicom_files = [f for f in os.listdir(self.folder_path.get()) if f.lower().endswith('.dcm')]
            if self.dicom_files:
                self.dicom_files.sort(key=lambda x: int(x.split(".")[0]))
                selected_file = self.folder_path.get() + "/" + self.dicom_files[self.file_index]
#                selected_file = filedialog.askopenfilename(initialdir=self.folder_path, title="Select a DICOM file",
#                                                            filetypes=(("DICOM files", "*.dcm"), ("all files", "*.*")))
                self.dicom_file_path.set(selected_file)
                self.display_dicom_image()
            else:
                self.dicom_file_path.set("No DICOM files found in the selected folder.")

    def display_next_dicom_image(self):
        self.file_index += 1
        
        if self.file_index > len(self.dicom_files):
            self.file_index = 0
            
        selected_file = self.folder_path.get() + "/" + self.dicom_files[self.file_index]
        self.dicom_file_path.set(selected_file)
        self.display_dicom_image()
              

    def display_dicom_image(self):
        dicom_file_path = self.dicom_file_path.get()
        if os.path.isfile(dicom_file_path):
            dicom_data = pydicom.dcmread(dicom_file_path)
            pixel_array = dicom_data.pixel_array

            # Convert pixel array to Pillow Image
            image = Image.fromarray(pixel_array)

            # Display the image in the GUI
            tk_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image
            self.image_label.pack(pady=10)
        else:
            self.dicom_file_path.set("Invalid or no DICOM file selected.")


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DICOMViewerApp(root)

    # Set the size of the window (width x height)
    window_width = 400
    window_height = 300
    root.geometry(f"{window_width}x{window_height}")
    
    # Center the window on the screen
    center_window(root, window_width, window_height)

    root.mainloop()







"""

import os
import keyboard

def list_files(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def print_next_file(file_list, current_index):
    if current_index < len(file_list):
        print(file_list[current_index])
    else:
        print("No more files in the folder. Exiting.")
        exit()

# Provide the path to the folder you want to list files from
folder_path = "../RSNA/data/test_images/1.2.826.0.1.3680043.5876"

file_list = list_files(folder_path)
current_index = 0

# Print the first file
print_next_file(file_list, current_index)

while True:
    try:
        # Wait for the down arrow key press
        keyboard.wait("down")
        
        # Move to the next file
        current_index += 1
        print_next_file(file_list, current_index)

    except keyboard.KeyboardInterrupt:
        print("\nExiting.")
        break
    """