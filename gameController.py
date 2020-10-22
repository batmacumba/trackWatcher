import threading
import time
import pyautogui
import pydirectinput
from win32gui import GetWindowText, GetForegroundWindow

class GameController(threading.Thread):
    RUN = True
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while self.RUN:
            # Check if game window is active
            if 'Sturmovik' in GetWindowText(GetForegroundWindow()):
                pydirectinput.keyDown('ctrlleft')
                pydirectinput.press('r')
                pydirectinput.keyUp('ctrlleft')
            time.sleep(0.5)
    def stop(self):
        self.RUN = False