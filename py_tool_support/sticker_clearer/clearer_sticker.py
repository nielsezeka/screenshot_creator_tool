import os
from PIL import Image

def colors_are_similar(color1, color2, tolerance=50):
    """Check if two colors are similar within a given tolerance."""
    return all(abs(color1[i] - color2[i]) <= tolerance for i in range(3))

def process_images(input_folder, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        # Ensure the output file has a .png extension
        output_filename = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_folder, output_filename)

        # Open the image
        try:
            with Image.open(input_path) as img:
                # Convert image to RGBA if not already
                img = img.convert("RGBA")
                pixels = img.load()
                width, height = img.size

                # Get the color of the top-left corner
                top_left_color = pixels[0, 0]

                # Flood-fill logic to find all connected pixels with a similar color
                to_check = [(0, 0)]  # Start with the top-left corner
                visited = set()
                transparent_pixels = set()

                while to_check:
                    x, y = to_check.pop()
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))

                    # Check if the pixel has a similar color
                    if colors_are_similar(pixels[x, y], top_left_color):  # Compare with tolerance
                        transparent_pixels.add((x, y))

                        # Add neighboring pixels to the stack
                        neighbors = [
                            (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
                            (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)
                        ]
                        for nx, ny in neighbors:
                            if 0 <= nx < width and 0 <= ny < height:
                                to_check.append((nx, ny))

                print(f"Identified {len(transparent_pixels)} transparent pixels.")
                # Make all identified pixels transparent
                for x, y in transparent_pixels:
                    pixels[x, y] = (0, 0, 0, 0)  # Transparent

                # Save the modified image as PNG
                img.save(output_path, "PNG")
                print(f"Processed and saved: {output_path}")
        except Exception as e:
            print(f"Failed to process {input_path}: {e}")

if __name__ == "__main__":
    input_folder = "./py_tool_support/sticker_clearer/input"  # Replace with your input folder path
    output_folder = "./py_tool_support/sticker_clearer/output"  # Replace with your output folder path
    process_images(input_folder, output_folder)