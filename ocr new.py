import cv2
import pytesseract
from tkinter import Tk, filedialog
import os

# Set the path to Tesseract executable (change it based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set the language to Tamil
lang = 'tam'

# Set the path to the Tesseract data files (change it based on your installation)
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

# Tamil Braille mappings
tamil_braille_map = {
    'அ': '⠁', 'ஆ': '⠜', 'இ': '⠊', 'ஈ': '⠔', 'உ': '⠥', 'ஊ': '⠳', 'எ': '⠢', 'ஏ': '⠑',
    'ஐ': '⠌', 'ஒ': '⠭', 'ஓ': '⠕', 'ஔ': '⠪', 'க': '⠅', 'ங': '⠬', 'ச': '⠉', 'ஞ': '⠒',
    'ட': '⠾', 'ண': '⠼', 'த': '⠞', 'ந': '⠝', 'ப': '⠏', 'ம': '⠍', 'ய': '⠽', 'ர': '⠗',
    'ல': '⠇', 'வ': '⠧', 'ழ': '⠷', 'ள': '⠸', 'ற': '⠻', 'ன': '⠰', 'ஜ': '⠚', 'ஷ': '⠯',
    'ஸ': '⠎', 'ஹ': '⠓', '்': '⠈', 'ஃ': '⠠', 'ா': '⠜', 'ி': '⠊', 'ீ': '⠔', 'ு': '⠥',
    'ூ': '⠳', 'ெ': '⠢', 'ே': '⠑', 'ை': '⠌', 'ொ': '⠭', 'ோ': '⠪', 'ௌ': '⠪', ' ': ' ',
    ',': '⠂', ';': '⠆', ':': '⠒', '!': '⠖', '?': '⠦', '.': '⠲'
}

def convert_to_tamil_braille(tamil_text):
    return ''.join([tamil_braille_map.get(char, char) for char in tamil_text])

def select_image():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    if file_path:
        img = cv2.imread(file_path)
        if img is None:
            print(f"Error: Unable to load image from {file_path}")
        else:
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray_image, lang=lang)
            
            print("Extracted Tamil Text:")
            print(text)

            tamil_braille_text = convert_to_tamil_braille(text)
            print("\nTamil Braille Text:")
            print(tamil_braille_text)

# Call the function to select and process an image
select_image()
