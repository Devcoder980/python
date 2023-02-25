import pyautogui




# currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
# currentMouseX, currentMouseY(1314, 345)

# pyautogui.moveTo(350, 260) # Move the mouse to XY coordinates.

        # Click the mouse.
# pyautogui.click(350, 260)

#
# pyautogui.doubleClick() # Move the mouse to XY coordinates and click it.
# pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

# pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
# pyautogui.doubleClick()     # Double click the mouse.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

# pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
#DD


# with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
#         pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# Shift key is released automatically.
#DDD



import  time
for i in range(25):
    if i==1:
        pyautogui.press("f12")
    # pyautogui.click(350, 260)
    pyautogui.rightClick(340, 250)
    pyautogui.write("i")
    pyautogui.press('enter')

    # pyautogui.hotkey('ctrl', 'r')
    time.sleep(3)# Press the Ctrl-C hotkey combination.
#
# pyautogui.alert('This is the message to display.')
# distance = 200
# while distance > 0:
#        pyautogui.drag(distance, 0, duration=0.5)   # move right
#        distance -= 5
#        pyautogui.drag(0, distance, duration=0.5)   # move down
#        pyautogui.drag(-distance, 0, duration=0.5)  # move left
#        distance -= 5
#        pyautogui.drag(0, -distance, duration=0.5)  # move up
