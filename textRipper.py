import pyautogui
import pytesseract
import cv2
import numpy as np

# Function to draw a red dot at the specified coordinates
def draw_red_dot(x, y):
    pyautogui.click(x, y)
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click(button='right')  # Right-click to draw a red dot

# Prompt the user to select the top-left corner
print("Please control-click the top-left corner of the region.")
top_left_x, top_left_y = pyautogui.position()
draw_red_dot(top_left_x, top_left_y)

# Prompt the user to select the bottom-right corner
print("Please control-click the bottom-right corner of the region.")
bottom_right_x, bottom_right_y = pyautogui.position()
draw_red_dot(bottom_right_x, bottom_right_y)

# Calculate the width and height of the selected region
width = bottom_right_x - top_left_x
height = bottom_right_y - top_left_y

# Take a screenshot of the selected area
screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, width, height))

# Convert the screenshot to a format that can be drawn on
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Save the screenshot with red dots for reference (optional)
cv2.imwrite('screenshot_with_dots.png', screenshot)

# Extract text from the screenshot using pytesseract
text = pytesseract.image_to_string(screenshot)

# Write the extracted text to a text file
with open('output.txt', 'w') as file:
    file.write(text)

print("Text extracted from the selected region has been saved to 'output.txt'.")
