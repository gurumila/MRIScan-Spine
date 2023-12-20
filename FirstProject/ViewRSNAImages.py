#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:31:33 2023

@author: milan
"""

import nifti_reader as nr
from PIL import Image
from pylab import *


#nr.read_nifti_file('../RSNA/data/train_images/1.2.826.0.1.3680043.14/1.dcm')

#nr.read_nifti_file('../RSNA/data/segmentations/1.2.826.0.1.3680043.780.nii')

volume = nr.process_scan('../RSNA/data/segmentations/1.2.826.0.1.3680043.780.nii')


#im = array(Image.open('images/profile.jpg').convert('L'))
#gray()
#im2 = 255 -im       #negative image
#im3 = (100.0/255) *im + 100 # Clamp to interval 100 ... 200
#im4 = 255.0 *(im/255.0)**2

#imshow(im4)

#https://nipy.org/nibabel/reference/nibabel.html

# This does not work
imshow(volume)
show();


##########
# TRY THIS
# Load the NIfTI file
file_path = 'path/to/your/file.nii'
img = nib.load(file_path)

# Get the data array
data = img.get_fdata()

# Display the slices of the NIfTI volume
num_slices = data.shape[-1]

# You can change the slice index to view different slices
slice_index = num_slices // 2

# Display the slice using matplotlib
plt.imshow(data[:, :, slice_index], cmap='gray')
plt.title(f'Slice {slice_index}')
plt.show()
