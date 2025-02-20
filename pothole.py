from IPython import get_ipython
from IPython.display import display
# %%
import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow from google.colab.patches

# Load the image
image_path = '/content/pot'  # Replace with the actual path to your image
image = cv2.imread(image_path)

# Check if image loading was successful
if image is None:
    print(f"Error: Could not load image from {image_path}. Please check the path and file permissions.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Display the edge-detected image using cv2_imshow
    cv2_imshow(edges) # Replace cv2.imshow with cv2_imshow
    #cv2.waitKey(0) # These lines are not needed with cv2_imshow
    #cv2.destroyAllWindows() 
# %%