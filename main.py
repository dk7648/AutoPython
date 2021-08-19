from selenium import webdriver


submit = []
no_submit = []
# 크롬 드라이버를 사용해 해당 URL에 접속
# URL = 'https://persistent-flavor-7ae.notion.site/9fb6da76f9e0462c848d24fac32ec253?v=10d3b04340b24ff6af977ae81630a660'
URL = 'https://underdogrev.notion.site/9d59854af81d401b8e1112d433af9216?v=f7c681689d7e42f0b6aec2a72404077a'
driver = webdriver.Chrome(executable_path=r'C:\Users\qjack\Desktop\chromedriver.exe')
driver.get(url=URL)

# 페이지가 표시를 최대 5초까지 기다림
driver.implicitly_wait(time_to_wait=5)

input = input("받아올 정보를 입력하세요: ")
# input = '4일차'

# 객체 얻기
checks = driver.find_elements_by_link_text(input)

count=0
for check in checks:

    count+=1
    check.click()
    driver.implicitly_wait(time_to_wait=5)

    notion_content = driver.find_element_by_class_name("notion-page-content")
    notion_name = driver.find_element_by_xpath('//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/div')

    if notion_content.text == '':
        no_submit.append(notion_name.text)
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

