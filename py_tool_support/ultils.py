import os
import random
from enum import Enum

class FramePositionMode(Enum):
    ORIGINAL = "original"
    HALF = "1/2"
    ONE_THIRD = "1/3"
    THREE_QUARTERS = "3/4"
    def get_frame_position_mode_from_string(mode_str):
        """Convert a string input to the corresponding FramePositionMode enum value."""
        try:
            return FramePositionMode(mode_str)
        except ValueError:
            raise ValueError(f"Invalid frame position mode: {mode_str}. Valid modes are: {[mode.value for mode in FramePositionMode]}")

def ensure_folder_exists(folder_path):
    """Ensure the specified folder exists."""
    try:
        os.makedirs(folder_path, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder '{folder_path}': {e}")
        raise

def get_random_image(folder, valid_extensions=('.png', '.jpg', '.jpeg')):
    """Get a random image file from the specified folder."""
    try:
        if not os.path.exists(folder):
            print(f"Folder does not exist: {folder}")
            return None

        images = [f for f in os.listdir(folder) if f.lower().endswith(valid_extensions)]
        if not images:
            print(f"No images found in the folder: {folder}")
            return None

        return os.path.join(folder, random.choice(images))
    except Exception as e:
        print(f"Error accessing folder '{folder}': {e}")
        return None

def calculate_frame_position(width, height, frame_img, padding, mode=FramePositionMode.HALF):
    """Calculate the position of the frame on the canvas based on the specified mode."""
    if mode == FramePositionMode.ORIGINAL:
        frame_left = (width * 2 // 3) - (frame_img.width // 2)
        frame_top = ((height - frame_img.height) // 2) + padding
    elif mode == FramePositionMode.HALF:
        frame_left = (width // 2) - (frame_img.width // 2)
        frame_top = ((height - frame_img.height) // 2) + padding
    elif mode == FramePositionMode.ONE_THIRD:
        frame_left = (width // 3) - (frame_img.width // 2)
        frame_top = ((height - frame_img.height) // 2) + padding
    elif mode == FramePositionMode.THREE_QUARTERS:
        frame_left = (width * 3 // 4) - (frame_img.width // 2)
        frame_top = ((height - frame_img.height) // 2) + padding
    else:
        raise ValueError(f"Unsupported frame position mode: {mode}")

    return frame_left, frame_top