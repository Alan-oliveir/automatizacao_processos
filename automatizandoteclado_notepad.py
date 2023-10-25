import pyautogui
import time

pyautogui.hotkey("win","r")
pyautogui.write("notepad")
pyautogui.press("enter")

time.sleep(3)
pyautogui.press("enter")
pyautogui.typewrite("Hello world")
pyautogui.press("enter")
pyautogui.typewrite("Sejam bem vindos")

