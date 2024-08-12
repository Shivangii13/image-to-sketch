import numpy as np
import cv2
import scipy.ndimage

# Define the path to your image
img_path = "shisha.jpg"

# Function to convert RGB to grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

# Function to create a dodging effect
def dodge(front, back):
    result = front * 255 / (255 - back)
    result[back == 255] = 255  # Prevent division by zero
    return np.clip(result, 0, 255).astype('uint8')

# Read the image
img = cv2.imread(img_path)

# Convert the image to grayscale
gray = rgb2gray(img)

# Invert the grayscale image
inverted_gray = 255 - gray

# Apply Gaussian blur to the inverted image
blurred = scipy.ndimage.gaussian_filter(inverted_gray, sigma=15)

# Apply the dodge effect
sketch = dodge(blurred, gray)

# Save the resulting sketch image
cv2.imwrite('shisha-sketch.png', sketch)
