import time

import selenium
import pyautogui as pg

time.sleep(5)
pg.screenshot('video_stop.png',region=(pg.position().x+30,pg.position().y,100,18))