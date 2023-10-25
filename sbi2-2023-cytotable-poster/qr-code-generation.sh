#!/bin/bash

# Script for generating qr codes related to poster

# Install required package
pip install "qrcode[pil]"

# Generate QR codes
qr "https://github.com/WayScience/CytoSnake" > "images/qr_cytosnake.png"
qr "https://github.com/WayScience/nf1_cellpainting_data" > "images/qr_nf1.png"
qr "https://github.com/WayScience/pyroptosis_signature" > "images/qr_pyroptosis.png"
qr "https://github.com/WayScience/CFReT_data" > "images/qr_cfret.png"
