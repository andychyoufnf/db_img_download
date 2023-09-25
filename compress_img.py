from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    image = Image.open(input_path)
    
    # Convert RGBA image to RGB
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    image.save(output_path, 'JPEG', quality=quality)

input_directory = './db_lower/'  # Provide the path to the directory containing input images
output_directory = './compressed_images/'  # Provide the path to the directory to save compressed images
compression_quality = 50  # Adjust the compression quality (0 to 100)

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_image_path = os.path.join(input_directory, filename)
        output_image_path = os.path.join(output_directory, filename.split('.')[0]+'.jpg')
        print(output_image_path)
        compress_image(input_image_path, output_image_path, quality=compression_quality)

print("Compression complete!")
