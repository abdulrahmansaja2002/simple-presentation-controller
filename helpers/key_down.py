import ctypes
import time

import pyautogui

# Constants for key codes
VK_LEFT = 0x25
VK_RIGHT = 0x27

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Functions to press and release keys
def __press_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hexKeyCode, 0, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def __release_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hexKeyCode, 0, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def __press_and_release_key(hexKeyCode):
    __press_key(hexKeyCode)
    time.sleep(0.05)
    __release_key(hexKeyCode)

def left_arrow_key():
    # __press_and_release_key(VK_LEFT)
    pyautogui.press('left')

def right_arrow_key():
    # __press_and_release_key(VK_RIGHT)
    pyautogui.press('right')

# Main function
if __name__ == "__main__":
    for _ in range(5):
        __press_and_release_key(VK_LEFT)
        print("Left arrow key pressed and released")
        time.sleep(1)

        __press_and_release_key(VK_RIGHT)
        print("Right arrow key pressed and released")
        time.sleep(1)
