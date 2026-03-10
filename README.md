# Digital Image Histogram Processing

This repository contains a Python implementation of image enhancement techniques using **Histogram Equalization** and **Histogram Specification (Matching)**. This project was developed as a practical assignment for the Digital Image Processing course.

## 📌 Features

1. **Grayscale Image Loading**: Reads source and target images in grayscale mode.
2. **Manual Histogram Equalization**: Implements the equalization algorithm from scratch using Cumulative Distribution Function (CDF) without relying on built-in equalization functions.
3. **OpenCV Histogram Equalization**: Utilizes `cv2.equalizeHist()` for comparison and validation of the manual approach.
4. **Histogram Specification (Matching)**: Adapts the histogram of the source image to match the histogram of a target reference image using `scikit-image`.
5. **Data Visualization**: Displays each image along with its corresponding histogram in separate windows using `matplotlib`.

## 🛠️ Prerequisites

Before running the script, ensure you have Python 3 installed along with the required libraries. It is recommended to use a virtual environment.

### Required Libraries:
- `opencv-python`
- `numpy`
- `matplotlib`
- `scikit-image`

