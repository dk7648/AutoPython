from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\qjack\Desktop\chromedriver.exe')


# 페이지가 표시를 최대 5초까지 기다림
driver.implicitly_wait(time_to_wait=5)

# 노션 접근 및 로그인
#노션 접속
URL = 'https://www.notion.so/underdogrev/21_2-49fc56791c66443192893134fabe63af'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=5)

email = 'email'
password = 'password'
notion_login= driver.find_element_by_xpath('//*[@id="notion-email-input-1"]')
notion_login.send_keys(email)
driver.implicitly_wait(time_to_wait=1)

notion_login = driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/main/div/div[3]/div[3]/form/div[4]')
notion_login.click()
driver.implicitly_wait(time_to_wait=1)

notion_login= driver.find_element_by_xpath('//*[@id="notion-password-input-2"]')
notion_login.send_keys(password)
driver.implicitly_wait(time_to_wait=1)

notion_login = driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[1]/div/main/div/div[3]/div[3]/form/div[4]')
notion_login.click()
driver.implicitly_wait(time_to_wait=1)

submit = []
no_submit = []

ban_keywords = ['여기에 생성한 블록을 클릭하거나 끌어서 다른 페이지에 붙여넣으면 콘텐츠를 동기화할 수 있습니다.', 'Enter 키를 눌러 빈 페이지를 사용하거나, ↑↓ 키를 이용해 템플릿을 선택하세요']

# 페이지가 표시를 최대 5초까지 기다림
driver.implicitly_wait(time_to_wait=5)

input = input("받아올 정보를 입력하세요: ")
# input = '4일차'

# 객체 얻기
checks = driver.find_elements_by_link_text(input)

count=0
for check in checks:
    driver.implicitly_wait(time_to_wait=5)
    count+=1
    check.click()
    driver.implicitly_wait(time_to_wait=5)

    notion_content = driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]')
    notion_name = driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/div/div')
    ban_checks = (ban_keyword in notion_content.text for ban_keyword in ban_keywords)
    for ban_check in ban_checks:
        if ban_check:
            no_submit.append(notion_name.text)
            break
    else:
        print('check :', count)
        print("name :", notion_name.text)
        print("content :", notion_content.text)
        print('-----------------')



    driver.back()
    driver.implicitly_wait(time_to_wait=5)

print("\n제출 X")
print(no_submit, sep=' / ')

driver.close()

