from PIL import Image
from py_tool_support.ultils import get_random_image 
def prepare_background_image(background_image, width, height):
    """Prepare the background image by resizing and cropping it to the specified dimensions."""
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