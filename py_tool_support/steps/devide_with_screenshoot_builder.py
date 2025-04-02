from PIL import Image, ImageDraw

def create_device_with_frame(input_frame, input_image, size ,rotate):
    border = 95
    try:
        frame_img = Image.open(input_frame).convert("RGBA")
        input_img = Image.open(input_image).convert("RGBA")
        frame_width, frame_height = frame_img.size
        frame_aspect_ratio = frame_width / frame_height
        input_width, input_height = input_img.size
        input_aspect_ratio = input_width / input_height

        if input_aspect_ratio > frame_aspect_ratio:
            new_height = frame_height
            new_width = int(new_height * input_aspect_ratio)
        else:
            new_width = frame_width
            new_height = int(new_width / input_aspect_ratio)

        input_img = input_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        offset_x = (new_width - frame_width) // 2
        offset_y = (new_height - frame_height) // 2
        cropped_img = input_img.crop((offset_x, offset_y, offset_x + frame_width, offset_y + frame_height))
        mask = Image.new("L", (frame_width, frame_height), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([(0, 0), (frame_width, frame_height)], radius=border, fill=255)
        combined_img = Image.new("RGBA", (frame_width, frame_height))
        combined_img.paste(cropped_img, (0, 0))
        clipped_img = Image.composite(combined_img, Image.new("RGBA", (frame_width, frame_height)), mask)
        clipped_img.paste(frame_img, (0, 0), frame_img)
        clipped_img.thumbnail((size, size), Image.Resampling.LANCZOS)
        clipped_img = clipped_img.rotate(rotate, expand=True, resample=Image.Resampling.BICUBIC)
        return clipped_img
    except Exception as e:
        print(f"Error creating device with frame: {e}")
        return None

def process_devices(devices, width, height):
    images = []
    for device in devices:
        final_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        frame = create_device_with_frame(device['device_frame'],
                                            device['screenshot'],
                                            device['size'],
                                            device['rotate'])
        if frame:
            x = device.get('x', 0)
            y = device.get('y', 0)
            final_image.paste(frame, (x, y), frame)
        images.append(final_image)
       
    return images