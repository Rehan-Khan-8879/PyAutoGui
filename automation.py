import time
import pyautogui

pyautogui.hotkey('win','r')
time.sleep(1);
pyautogui.write("notepad",interval=0.1)
pyautogui.hotkey('enter')
time.sleep(1)
#pyautogui.click(912,739)
time.sleep(0.1)
#pyautogui.click(500,500)
pyautogui.hotkey('ctrl','n')
pyautogui.write("YOUR COMPUTER HAS BEEN HACKED",interval=0.1)
time.sleep(3)
pyautogui.hotkey('alt','F4')

#print(pyautogui.position())



