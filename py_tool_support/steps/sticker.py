from PIL import Image

def resize_sticker_to_fit(sticker_img, target_width, target_height):
    """
    Resize the sticker image to fit within the target dimensions while maintaining aspect ratio.
    """
    original_width, original_height = sticker_img.size

    # Calculate the scaling factor to maintain the aspect ratio
    scaling_factor = min(target_width / original_width, target_height / original_height)

    # Compute the new dimensions
    new_width = int(original_width * scaling_factor)
    new_height = int(original_height * scaling_factor)

    # Resize the sticker image
    return sticker_img.resize((new_width, new_height))

def draw_stickers(image, stickers):
    for sticker in stickers:
        try:
            sticker_img = Image.open(sticker["path"]).convert("RGBA")
            sticker_img = resize_sticker_to_fit(sticker_img, sticker["size"], sticker["size"])
            image.paste(sticker_img, (sticker["x"], sticker["y"]), sticker_img)
        except Exception as e:
            print(f"\033[91mFailed to draw sticker: {sticker['path']}. Error: {e}\033[0m")
    
    return image