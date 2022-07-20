# Automating boring stuff is a great way to learn new language

import pyautogui as gui # Install it if not available
import os

# MacOS might ask you for extra permissions to record. 
gui.screenshot(os.path.dirname(__file__)+'/screenshot.png')
gui.moveTo(145, 249)
gui.click()

gui.click(1550, 245, clicks = 2)

gui.leftClick()
print(gui.position())

# More functions like mouse move, click, and everything can be done using this tool.
# More details can be found here, https://pyautogui.readthedocs.io/en/latest/quickstart.html