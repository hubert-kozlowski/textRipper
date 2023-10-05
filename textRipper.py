import pyautogui
import pytesseract

# Display a message to prompt the user to select the region
print("Please control-click the top-left corner of the region.")
top_left = pyautogui.confirm("Control-click the top-left corner of the region.")

print("Please control-click the bottom-right corner of the region.")
bottom_right = pyautogui.confirm("Control-click the bottom-right corner of the region.")

# Parse the coordinates of the selected region
top_left_x, top_left_y = map(int, top_left.split(','))
bottom_right_x, bottom_right_y = map(int, bottom_right.split(','))

# Calculate the width and height of the selected region
width = bottom_right_x - top_left_x
height = bottom_right_y - top_left_y

# Take a screenshot of the selected area
screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, width, height))

# Extract text from the screenshot using pytesseract
text = pytesseract.image_to_string(screenshot)

# Write the extracted text to a text file
with open('output.txt', 'w') as file:
    file.write(text)

print("Text extracted from the selected region has been saved to 'output.txt'.")
