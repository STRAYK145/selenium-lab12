from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r"F:\лабораторные работы 3.2\Тестирование информационных систем\Новая папка\лр12\chrome-win64\chrome.exe"

service = Service(r"F:\лабораторные работы 3.2\Тестирование информационных систем\Новая папка\лр12\chromedriver.exe")

browser = webdriver.Chrome(service=service, options=options)
browser.get('https://ispi.cdo.vlsu.ru/login/index.php')
browser.close()