from io import BytesIO
import os
import requests
import base64
from PIL import Image

# Function for downloading PNGs stored as static
def scanStaticPNG(img_url, save_dir, img_tag):
    
    # Get the image content
    img_data = requests.get(img_url).content

    # Extract the image filename from the URL. 
    img_filename = os.path.join(save_dir, os.path.basename(img_url) + '.png')

    # Clean up any characters that cannot be used in a filename
    img_filename = ''.join(c for c in img_filename if c.isalnum() or c in ('_', '.', '-', '\\')) 
    
    # Create empty file then write image into the file
    with open(img_filename, 'wb') as img_file:
        img_file.write(img_data)
        
    print('Saved: ' + img_filename)

def scanGIFbase64(img_url, save_dir, img_tag):   
    src_data = img_tag.get('src', '')

    if src_data.startswith('data:image'):
        data_parts = src_data.split (';base64,')

    if len(data_parts) == 2:
        content_type = data_parts[0].split(':')[1]
        base64_data = data_parts[1]
        # Decode the base64 data
        decoded_data = base64.b64decode(base64_data)

        # Convert the decoded data to an image
        image = Image.open(BytesIO(decoded_data))

        # Create the directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)

        # Generate a unique filename
        img_filename = f'image_{hash(src_data)}.png'  # You can modify this as needed

        # Save the image to the specified directory
        img_path = os.path.join(save_dir, img_filename)
        image.save(img_path)

        return img_path
    