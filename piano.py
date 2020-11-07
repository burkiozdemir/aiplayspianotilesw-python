import pyautogui
import keyboard
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    
while keyboard.is_pressed('esc') == False:
    
    if pyautogui.pixel(500, 334)[0] == 0:
        click(500, 334)
    if pyautogui.pixel(600, 334)[0] == 0:
        click(600, 334)
    if pyautogui.pixel(700, 334)[0] == 0:
        click(700, 334)
    if pyautogui.pixel(800, 334)[0] == 0:
        click(800, 334)