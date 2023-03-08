from pyautogui import *
l=['+9183472392980','+919888341345']
# auto Whatapp msg sent web whatapp
rightClick(340, 180)
for i in l:
    sleep(3)
    hotkey('ctrl','alt','/')
    typewrite(i)
    # pyautogui.write(i)
    press('enter')
    sleep(2)
    press('enter')
    write('Your Are Lucky My Python Automation Test')
    sleep(1)
    press('enter')


