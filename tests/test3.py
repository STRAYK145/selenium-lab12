from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.binary_location = r"F:\лабораторные работы 3.2\Тестирование информационных систем\Новая папка\лр12\chrome-win64\chrome.exe"
service = Service(r"F:\лабораторные работы 3.2\Тестирование информационных систем\Новая папка\лр12\chromedriver.exe")

browser = webdriver.Chrome(service=service, options=options)
browser.get('https://ispi.cdo.vlsu.ru/login/index.php')

username = browser.find_element(by=By.NAME, value='username')
username.send_keys('ВАШ_ЛОГИН')  # <-- вставить свой логин

password = browser.find_element(by=By.ID, value='password')
password.send_keys('ВАШ_ПАРОЛЬ')  # <-- вставить свой пароль

button = browser.find_element(by=By.CSS_SELECTOR, value='#loginbtn')
button.click()

# Проверка результата
try:
    assert 'Учебный сайт кафедры ИСПИ' in browser.title
    assert 'Фамилия Имя Отчество' in browser.page_source  # <-- вставить своё ФИО
    print('The test was completed successfully')
except Exception as err:
    print('The test was failed')

browser.close()