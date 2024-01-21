#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 00:24:43 2024

@author: milan
"""

import os
import tkinter as tk
from tkinter import filedialog
import pydicom
from PIL import Image, ImageTk
import nibabel as nib

class NiiViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NIfTI File Viewer")

        # Variables
        self.nii_file_path = tk.StringVar()
        self.image_label = tk.Label(root)

        # Browse button
        self.browse_button = tk.Button(root, text="Load File", command=self.browse_folder)
        self.browse_button.pack(pady=10)
        
        self.folder_path = tk.StringVar()
        self.folder_path.set("/Users/milan/Documents/GitHub/Kaggle/MRIScan-Spine/RSNA/data/segmentations")

        self.message = tk.StringVar()
        self.message.set("/Users/milan/Documents/GitHub/Kaggle/MRIScan-Spine/RSNA/data/segmentations")

        # Label for displaying Messages
        self.message_label = tk.Label(root, textvariable=self.message, justify="center", wraplength=500)
        self.message_label.pack(pady=10)


        # Label for displaying selected DICOM file path
        self.file_label = tk.Label(root, textvariable=self.nii_file_path, justify="center", wraplength=500)
        self.file_label.pack(pady=10)

        # Display image button
        self.display_previous_button = tk.Button(root, text="Previous Section", command=self.display_previous_slice)
        self.display_previous_button.pack(pady=10)

        # Display image button
        self.display_button = tk.Button(root, text="Next Section", command=self.display_next_slice)
        self.display_button.pack(pady=10)
        
        self.slice_index = 0
        self.slice_count = 0

    def browse_folder(self):
        self.slice_index = 0
        self.slice_count = 0
        selected_file_path = filedialog.askopenfilename(
            title="Select NIfTI File",
            filetypes=[("NIfTI files", "*.nii"), ("All files", "*.*")]
            )
        
        self.nii_file_path.set(selected_file_path)
        if selected_file_path:
            self.message.set(selected_file_path)
            # Load NIfTI file
            self.nii_image = nib.load(self.nii_file_path.get())

            # Get the data array from the image
            self.nii_image_data = self.nii_image.get_fdata()

            self.slice_count = 50
            self.slice_index = 10

            self.display_nii_image_slice()
        else:
            self.message.set("No file slected")

    def display_next_slice(self):
        self.slice_index += 1
        
        if self.slice_index > self.slice_count:
            self.slice_index = 0
            
        self.display_nii_image_slice()
              
    def display_previous_slice(self):
        self.slice_index -= 1
        
        if self.slice_index < 0:
            self.slice_index = self.slice_count - 1
            
        self.display_nii_image_slice()
              

    def display_nii_image_slice(self):
        pixel_array = self.nii_image_data[:, :, self.slice_index]

        # Convert pixel array to Pillow Image
        image = Image.fromarray(pixel_array)
        
        if image:
            message = f"Image section loaded: {self.slice_index}"
            self.message.set(message)
        else:
            self.message.set("Image not loaded")
            return

        # Display the image in the GUI
        tk_image = ImageTk.PhotoImage(image)
        
        if tk_image:
            message = f"TK Image created for section: {self.slice_index}"
            self.message.set(message)
            
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image
        self.image_label.pack(pady=10)
        
        """
        self.nii_file_path.set(selected_file)

        nii_file_path = self.nii_file_path.get()
        if os.path.isfile(nii_file_path):
            dicom_data = pydicom.dcmread(nii_file_path)
            pixel_array = dicom_data.pixel_array

            # Convert pixel array to Pillow Image
            image = Image.fromarray(pixel_array)

            # Display the image in the GUI
            tk_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image
            self.image_label.pack(pady=10)
        else:
            self.nii_file_path.set("Invalid or no DICOM file selected.")
            """

    def read_nifti_data(file_path):
        try:
            # Load the NIfTI file
            img = nib.load(file_path)
    
            # Get the data array
            data = img.get_fdata()
    
            return data
        except Exception as e:
            print(f"Error reading NIfTI file: {e}")
            return None

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


if __name__ == "__main__":
    root = tk.Tk()
    app = NiiViewerApp(root)

    # Set the size of the window (width x height)
    window_width = 550
    window_height = 750
    root.geometry(f"{window_width}x{window_height}")
    
    # Center the window on the screen
    center_window(root, window_width, window_height)

    root.mainloop()


