import pyautogui
import  time
for i in range(10):
    pyautogui.rightClick(1640,640)
    if i<10:
        pyautogui.hotkey("ctrl","w")
    pyautogui.rightClick(1640,640)
    time.sleep(5)

# for i in range(25):
#     if i==1:
#         pyautogui.press("f12")
#     # pyautogui.click(350, 260)
#     pyautogui.rightClick(340, 250)
#     pyautogui.write("i")
#     pyautogui.press('enter')
