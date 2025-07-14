from PIL import ImageGrab
import datetime
import json
import os
from typing import Dict, Any


def create_screenshot_filename(folder: str) -> str:
    current_time = datetime.datetime.now()
    file_name = str(current_time).replace(":", "-")
    dotpos = file_name.find('.')
    file_name = file_name[:dotpos]
    file_name = f"{folder}\\{file_name} screenshot.jpg"
    return file_name

def load_config() -> Dict[str, Any]:
    try:
        with open("ini.json", 'r') as ini_file:
            ini_data = json.load(ini_file)

        # Validate required configuration keys
        if not all(key in ini_data for key in ['bbox', 'save_all_screens', 'folder_to_save']):
            raise ValueError("Invalid configuration file: missing required keys")

        return ini_data
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error in ini.json: {e}")
        raise



config = load_config()
#{"bbox": "0,0,1920,1080", "save_all_screens": true, "folder_to_save": "D:/Folder for screenshots/new_test"}
bbox_data=tuple(map(int,config['bbox'].split(',')))
save_all_screens_data=config['save_all_screens']
folder_to_save_data=config['folder_to_save']


os.makedirs(folder_to_save_data,exist_ok=True)

if save_all_screens_data:
    screenshot = ImageGrab.grab(all_screens=save_all_screens_data)
else:
    screenshot = ImageGrab.grab(bbox=bbox_data)

file_name=create_screenshot_filename(folder_to_save_data)
screenshot.save(file_name)




