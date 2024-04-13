import cv2
import os

def calculate_scale(image):
    """
    Calculate the scale based on the size of the image.
    """
    height, width = image.shape[:2]
    return min(1.0, 800.0 / max(width, height))

# Function to unblur the image
def unblur_image(image):
    # Adjusting blur parameters to reduce blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Applying unsharp masking to enhance clarity
    unsharp_image = cv2.addWeighted(image, 1.5, blurred_image, -0.5, 0)

    return unsharp_image

# Get the absolute path to the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the image file
# image_path = os.path.join(script_dir, "res", "wallpaper.jpeg")
image_path = os.path.join(script_dir, "source", "sij.jpg")

# Read the image
image = cv2.imread(image_path)

# Calculate the scale based on the size of the image
scale = calculate_scale(image)

# Resize the image
resized_image = cv2.resize(image, None, fx=scale, fy=scale)

# Unblur the resized image
unblurred_image = unblur_image(resized_image)

# Converting BGR image to grayscale
gray_image = cv2.cvtColor(unblurred_image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_image = 255 - gray_image

# Create a folder to save the images if it doesn't exist
unblurred_folder = os.path.join(script_dir, "unblurred")
os.makedirs(unblurred_folder, exist_ok=True)

inverted_folder = os.path.join(script_dir, "inverted")
os.makedirs(inverted_folder, exist_ok=True)

# Save the unblurred image to the output folder
unblurred_output_path = os.path.join(unblurred_folder, "unblurred_sij.jpg")
cv2.imwrite(unblurred_output_path, unblurred_image)

# Save the inverted unblurred image to the output folder
inverted_output_path = os.path.join(inverted_folder, "inverted_sij.jpg")
cv2.imwrite(inverted_output_path, inverted_image)

# Display images
cv2.imshow("Original Image", resized_image)
cv2.imshow("Unblurred Image", unblurred_image)
cv2.imshow("Inverted Image", inverted_image)
cv2.waitKey(0)
