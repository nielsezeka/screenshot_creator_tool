from PIL import Image, ImageDraw
import os
import json
import yaml
from py_tool_support.ultils import *
from py_tool_support.steps.additional_text import *
from py_tool_support.steps.background import *
from py_tool_support.steps.sticker import *
from py_tool_support.steps.text_process import *
from py_tool_support.steps.devide_with_screenshoot_builder import *

def export_image(new_img):
    output_path = os.path.join(output_folder, output_name)
    new_img.save(output_path)
    print(f"Image created at: \033[92m{output_path}\033[0m")

def create_image_with_background_frame_and_screenshot():
    ensure_folder_exists(output_folder)
    bg_img = prepare_background_image(background, width, height)  
    if not bg_img :
        print("Failed to process images.")
        return
    new_img = Image.new("RGBA", (width, height))
    new_img.paste(bg_img)
    draw = ImageDraw.Draw(new_img)
    devices_image = process_devices(devices,width, height)
    for device_img in devices_image:
        if device_img:
            new_img.paste(device_img, (0, 0), device_img)
    add_stickers(new_img, stickers)
    add_texts(new_img, texts,font_path)
    export_image(new_img)

if __name__ == "__main__":
     # Load the YAML configuration file
    with open('configuration.yaml', 'r') as yaml_file:
        yaml_config = yaml.safe_load(yaml_file)
        application_files = yaml_config.get('application_files', [])

    for application_file in application_files:
        # Read the JSON file and load its content
        with open(application_file, 'r') as file:
            config = json.load(file)

        # Extract variables from the JSON configuration
        width = config.get("width", 800)
        height = config.get("height", 600)
        output_folder = config.get("output_folder", "")
        output_name = config.get("output_name", "")
        background = config.get("background", "")
        text = config.get("text", "")
        font_path = config.get("font_path", "")
        mode = config.get("mode", "")
        stickers = config.get("sticker", [])
        devices = config.get("devices", [])
        texts = config.get("texts", "")
        print('---------------------START---------------------------------')
        print(f"Processing config: \033[92m{application_file}\033[0m")
        print(f"\tSize: \033[36m{width} - {height}\033[0m")
        print(f"\tBackground: \033[36m{background}\033[0m")
        print(f"\tStickers: \033[36m{len(stickers)}\033[0m")
        
        # Call the function with the loaded configuration
        create_image_with_background_frame_and_screenshot()
        print('---------------------END---------------------------------\n\n')