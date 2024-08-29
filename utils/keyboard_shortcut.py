import keyboard
from utils.screenshot import take_screenshot
from utils.ocr import extract_text_from_image
from utils.llm_integration import generate_response

def on_shortcut_pressed():
    # Take a screenshot
    filename = take_screenshot()
    print(f"Screenshot saved as {filename}")
    
    # Extract text from the screenshot
    ocr_text = extract_text_from_image(filename)
    
    # Generate a response from the LLM
    llm_response = generate_response(ocr_text)
    print(f"LLM Response: {llm_response}")

def setup_keyboard_shortcut():
    # Define the keyboard shortcut (e.g., Ctrl + Shift + S)
    keyboard.add_hotkey('ctrl+shift+s', on_shortcut_pressed)
    
    # Keep the script running in the background
    keyboard.wait('esc')  # Press 'esc' to stop the script
