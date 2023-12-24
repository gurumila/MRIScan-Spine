#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:11:56 2023

@author: milan
"""

import os
import tkinter as tk
from tkinter import filedialog

class FileViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Viewer")

        self.current_index = 0
        self.file_list = []

        # Label to display the file name
        self.file_label = tk.Label(root, text="")
        self.file_label.pack(pady=10)

        # Button to select a folder
        self.select_folder_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=5)

        # Button to view the next file
        self.previous_file_button = tk.Button(root, text="Previous File", command=self.show_previous_file)
        self.previous_file_button.pack(pady=5)

        # Button to view the next file
        self.next_file_button = tk.Button(root, text="Next File", command=self.show_next_file)
        self.next_file_button.pack(pady=5)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            self.current_index = 0
            self.show_next_file()

    def show_next_file(self):
        if self.current_index < len(self.file_list):
            file_name = self.file_list[self.current_index]
            self.file_label.config(text=file_name)
            self.current_index += 1
        else:
            self.file_label.config(text="Try previous.")

    def show_previous_file(self):
        if self.current_index >= 0:
            file_name = self.file_list[self.current_index]
            self.file_label.config(text=file_name)
            self.current_index -= 1
        else:
            self.file_label.config(text="Try next.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileViewerApp(root)
    root.mainloop()