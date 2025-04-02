from PIL import ImageFont

def add_text_to_image_on_canvas(draw, text, font_path, max_text_width, max_text_height, canvas_height, horizontal_padding=10):
    """Add text to the image canvas with horizontal padding."""
    font_size = 1
    try:
        font = ImageFont.truetype(font_path, font_size)
        while True:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            if text_width > (max_text_width - 2 * horizontal_padding) or text_height > max_text_height:
                break
            font_size += 1
            font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"\033[91mFont not found. Using default font.\033[0m")
        font = ImageFont.load_default()
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

    # Adjust text_x to include horizontal padding
    text_x = (max_text_width - text_width) // 2 + horizontal_padding
    text_y = (canvas_height - text_height) // 2
    text_color = (255, 255, 255, 255)
    stroke_color = (0, 0, 0, 255)
    stroke_width = 3
    draw.text(
        (text_x, text_y),
        text,
        fill=text_color,
        font=font,
        align="center",
        stroke_width=stroke_width,
        stroke_fill=stroke_color
    )