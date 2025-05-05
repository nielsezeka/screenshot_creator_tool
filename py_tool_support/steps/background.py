from PIL import Image
from py_tool_support.ultils import get_random_image 
import os

def prepare_background_image(background_image, width, height):
    """Prepare the background image by resizing and cropping it to the specified dimensions."""
    try:
        # Check if the background image exists and is valid
        if background_image and os.path.isfile(background_image):
            with Image.open(background_image) as bg_img:
                bg_width, bg_height = bg_img.size
                aspect_ratio = max(width / bg_width, height / bg_height)
                new_size = (int(bg_width * aspect_ratio), int(bg_height * aspect_ratio))
                bg_img = bg_img.resize(new_size, Image.LANCZOS)

                left = (bg_img.width - width) // 2
                top = (bg_img.height - height) // 2
                right = left + width
                bottom = top + height
                return bg_img.crop((left, top, right, bottom))
        else:
            # Return an empty (transparent) image with the specified dimensions
            return Image.new('RGBA', (width, height), (0, 0, 0, 0))
    except Exception as e:
        print(f"Error processing background image: {e}")
        # Return an empty image in case of any error
        return Image.new('RGBA', (width, height), (0, 0, 0, 0))