import pyautogui
from datetime import datetime
import os

def take_screenshot():
    # Ensure the screenshots directory exists
    screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Generate a filename based on the current date and time
    filename = os.path.join(screenshot_dir, f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

    # Capture and save the screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    
    return filename
