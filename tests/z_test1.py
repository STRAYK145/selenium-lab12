from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = r"F:\лабораторные работы 3.2\Тестирование информационных систем\Новая папка\лр12\chrome-win64\chrome.exe"
service = Service(r"F:\лабораторные работы 3.2\Тестирование информационных систем\Новая папка\лр12\chromedriver.exe")

browser = webdriver.Chrome(service=service, options=options)
browser.get('https://store.steampowered.com/login')

time.sleep(2)

# Вводим логин
username = browser.find_element(by=By.CSS_SELECTOR, value='input._2GBWeup5cttgbTw8FM3tfx[type="text"]')
username.send_keys('fake_user_123')

# Вводим пароль
password = browser.find_element(by=By.CSS_SELECTOR, value='input._2GBWeup5cttgbTw8FM3tfx[type="password"]')
password.send_keys('wrongpassword')

# Нажимаем кнопку Войти
button = browser.find_element(by=By.CSS_SELECTOR, value='button[type="submit"]')
button.click()

time.sleep(3)

try:
    # Проверяем что остались на странице входа
    assert 'login' in browser.current_url
    print('Тест 1 пройден успешно: пользователь остался на странице входа')
except Exception as err:
    print('Тест 1 не пройден:', err)

browser.close()