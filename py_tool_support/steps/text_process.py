from PIL import ImageFont, ImageDraw
import textwrap

def add_texts(image, texts, font_path):
    for aLineOfText in texts:
        text = aLineOfText.get("text", "")
        x = aLineOfText.get("x", 0)
        y = aLineOfText.get("y", 0)
        width = aLineOfText.get("width", 0)
        size  = aLineOfText.get("size", 0)
        try:
            font = ImageFont.truetype(font_path, size)
            draw = ImageDraw.Draw(image)
            text_color = (255, 255, 255, 255)
            stroke_color = (0, 0, 0, 255)
            stroke_width = 3

            # Calculate the average character width using font.getbbox
            avg_char_width = font.getbbox("A")[2]  # The width of a single character
            max_chars_per_line = int(width / avg_char_width)

            # Wrap the text to fit within the specified width
            wrapped_text = textwrap.fill(text, width=max_chars_per_line)

            # Draw the wrapped text line by line
            for line in wrapped_text.split("\n"):
                draw.text((x, y),
                          line,
                          fill=text_color,
                          font=font,
                          align="center",
                          stroke_width=stroke_width,
                          stroke_fill=stroke_color)
                y += font.getbbox(line)[3] - font.getbbox(line)[1]  # Move to the next line
        except Exception as e:
            print(f"\033[91mFailed to draw text: {text}. Error: {e}\033[0m")
    return image