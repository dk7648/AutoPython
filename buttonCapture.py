import time

import selenium
import pyautogui as pg

time.sleep(5)
pg.screenshot('setting.png',region=(pg.position().x,pg.position().y,22,22))