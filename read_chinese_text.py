##Setup
#pip install unidecode
#pip install pytesseract

from unidecode import unidecode

from PIL import Image
#import unicode
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

text = pytesseract.image_to_string(Image.open("chinese.png"), lang = "chi_sim")
txt = unidecode(((pytesseract.image_to_string(Image.open("chinese.png"), lang = "chi_sim"))))


print(text.encode('utf8'))

with open("converted_text.txt", 'w', encoding='utf_8') as f:
    f.write(text)

print(txt)
