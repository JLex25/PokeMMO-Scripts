import pyautogui
import pytesseract
import time

# Constant
LANG = 'spa' 


# Configure Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 


def get_text(x1, y1, x2, y2):
    reg = (x1, y1, x2, y2)
    try:
        screenshot = pyautogui.screenshot(region=reg)
        #screenshot.save('dialog_screenshot.png') # Debug the screenshot
        text = pytesseract.image_to_string(screenshot, lang=LANG)
        return text.strip().lower() 
    except Exception as e:
        print(f"Error: {e}")
        return None
