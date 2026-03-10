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

## 🚀 Installation & Setup

1. **Clone the repository** (or download the source code):
   ```bash
   git clone https://github.com/rahmatsigma/histogram_equalization_matching.git
   cd histogram_equalization_matching

   
2. **Create and activate a virtual environment** (optional but recommended):

  ```bash
  python -m venv .venv


# On Windows:
.\.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate


3. Install the dependencies:

  ```bash
pip install opencv-python numpy matplotlib scikit-image


💻 Usage
Place two image files in the root directory of this project:

source.jpg: The original image you want to enhance.

target.jpg: The reference image whose histogram you want to match.

4. Run the Python script:

  ```bash
python histogram_processing.py


The program will open 5 separate windows sequentially showing:

Original Image & Histogram

Manual Equalization Result & Histogram

OpenCV Equalization Result & Histogram

Target Reference Image & Histogram

Histogram Specification (Matched) Result & Histogram
