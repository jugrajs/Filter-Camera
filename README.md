# Filter-Camera

Welcome to Filter-camera, a project that uses OpenCV to apply real-time filters to a camera feed. This Python script allows you to experiment with various filters like greyscale, edge detection, and blur, providing an interactive and educational experience.

# Features
**Greyscale Filter:** Press the 'g' key to toggle the greyscale filter on and off. This filter converts the camera feed to grayscale. <br />
**Edge Detection Filter:** Press the 'e' key to toggle the edge detection filter on and off. This filter applies edge detection to the camera feed, highlighting edges in the image. <br />
**Blur Filter:** Press the 'b' key to toggle the blur filter on and off. This filter applies a blur effect to the camera feed.
# Getting Started

1. Clone this repository to your local machine.
2. Make sure you have Python and OpenCV installed.
3. Install the required dependencies using the following command:
```
  pip install -r requirements.txt
```
4. Run the script using the following command:
```
python3 filter_camera.py [filter1] [filter2] [filter3]
```
Replace [filter1], [filter2], and [filter3] with the names of the filters you want to enable (e.g., greyscale, edge-detection, blur). <br /> You can enable multiple filters by separating them with spaces. <br />
Press the corresponding keys ('g', 'e', 'b') during the camera feed window to toggle the filters on and off. Press 'q' to quit the application.
# Dependencies
Python <br />
OpenCV <br />
NumPy  <br />
argparse

# Usage
filter_camera.py: The main script that captures the live camera feed and applies the selected filters based on user input.

# Notes
Adjust the filter parameters and behavior in the script to suit your preferences. <br /> <br /> <br />
Feel free to modify any part of the README to better match your project's information and style
