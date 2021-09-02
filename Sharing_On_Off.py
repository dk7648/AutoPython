###########################
##      사용법          ####
###########################
# 각 if문 속 for문의 range범위는 n일차를 의미합니다. 이를 수정하여 원하는 범위를 지정해주세요
# 실행 후 표시된 페이지에서 로그인, 원하는 페이지 이동 후 콘솔에 on 또는 off를 입력해 주시면 됩니다!



from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\qjack\Desktop\chromedriver.exe')


# 페이지가 표시를 최대 5초까지 기다림
driver.implicitly_wait(time_to_wait=5)

# 노션 접근 및 로그인
#노션 접속
URL = 'https://underdogrev.notion.site/4fca319d81fc4f3d995845c9be7bc5c0'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=5)

input = input("공유 버튼 활성화 여부(on or off) : ")

if input == 'on' or input == 'On' or input == 'ON':
    ##############################################################   여기를 수정해주세요!!  - ex) range(1, 3) = 1일차~2일차
    for i in range(1, 2):
        checks = driver.find_elements_by_link_text(i.__str__() + '일차')

        for check in checks:
            check.click()
            driver.implicitly_wait(time_to_wait=5)

            share_button = driver.find_element_by_xpath(
                '//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]').click()
            restore_button = driver.find_element_by_xpath(
                '//*[@id="notion-app"]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/div/div[2]').click()
            access_restore_button = driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[2]/div[4]/div/div[2]/div/div[2]/div[1]').click()

            driver.back()
            driver.implicitly_wait(time_to_wait=5)


elif input == 'off' or input == 'Off' or input == 'OFF':
    ##############################################################   여기를 수정해주세요!!  - ex) range(1, 3) = 1일차~2일차
    for i in range(1, 2):
        checks = driver.find_elements_by_link_text(i.__str__()+'일차')

        for check in checks:
            check.click()
            driver.implicitly_wait(time_to_wait=5)

            share_button = driver.find_element_by_xpath(
                '//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]').click()
            web_share_button = driver.find_element_by_xpath(
                '//*[@id="notion-app"]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div/div').click()
            access_limmit_button = driver.find_element_by_xpath(
                '//*[@id="notion-app"]/div/div[2]/div[4]/div/div[2]/div/div[1]/div[1]').click()

            driver.back()
            driver.implicitly_wait(time_to_wait=5)


driver.close()

