import pyautogui
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image = cv2.imread('test_pytesseract.png')
image = cv2.resize(image, (0,0), fx=5, fy=5)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

txt = pytesseract.image_to_string(image, lang='eng',config='--psm 6')

print(txt)
