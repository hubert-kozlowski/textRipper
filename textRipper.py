import pyautogui
import pytesseract

# Set the coordinates of the area to read from
x, y, width, height = 100, 100, 300, 200

# Take a screenshot of the specified area
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# Extract text from the screenshot using pytesseract
text = pytesseract.image_to_string(screenshot)

# Write the extracted text to a text file
with open('output.txt', 'w') as file:
    file.write(text)


