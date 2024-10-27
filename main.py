from rembg import remove
from PIL import Image
import io

# Input and output paths
input_path = 'images/input/input.jpg'
output_path = 'images/output/output.png'

# Load the input image and process it
with open(input_path, 'rb') as input_file:
    input_image = input_file.read()
    output_image = remove(input_image)

# Save the processed image to the output path
with open(output_path, 'wb') as output_file:
    output_file.write(output_image)

print(f"Background removed and saved as {output_path}")
