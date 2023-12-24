#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:05:33 2023

@author: milan
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