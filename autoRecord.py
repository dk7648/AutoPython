import time

from selenium import webdriver
import pyautogui as pg
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

time_list = []
# 크롬 드라이버를 사용해 해당 URL에 접속
URL = 'https://classlion.net/'
driver = webdriver.Chrome(executable_path=r'C:\Users\qjack\Desktop\chromedriver.exe')
driver.get(url=URL)

# 페이지가 표시를 최대 5초까지 기다림
driver.implicitly_wait(time_to_wait=5)

# 객체 얻기
driver.find_element_by_link_text('로그인 / 회원가입').click()
driver.implicitly_wait(time_to_wait=5)

#로그인
login_email = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/form/input[1]')
login_email.click()
login_email.send_keys('id')

login_password = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/form/input[2]')
login_password.click()
login_password.send_keys('password')

login_button = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/form/div[5]')
login_button.click()

driver.implicitly_wait(time_to_wait=5)

#마이페이지
driver.find_element_by_link_text('마이페이지').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div/div[2]/div[2]/div').click()

time.sleep(3)

############################################################
# 버튼 캡처
# print(pg.position())
# pg.screenshot('play.png',region=(35,668,60,35))

#동영상 초기화
play_button_position = pg.center(pg.locateOnScreen('play.png'))
pg.click(play_button_position)
pg.press(['left']*100)

while pg.locateOnScreen('next_button.png') == None:
    time.sleep(3)
    print(pg.locateOnScreen('next_button.png'))

pg.click(pg.center(pg.locateOnScreen('next_button.png')))


# pg.leftClick(play_button_position)
# print('user pg')
# position = pg.position()
# pg.click(position)
