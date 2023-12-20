#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:31:33 2023

@author: milan
"""

import nifti_reader as nr

#nr.read_nifti_file('../RSNA/data/train_images/1.2.826.0.1.3680043.14/1.dcm')

#nr.read_nifti_file('../RSNA/data/segmentations/1.2.826.0.1.3680043.780.nii')

nr.process_scan('../RSNA/data/segmentations/1.2.826.0.1.3680043.780.nii')