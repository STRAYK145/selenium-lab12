# selenium-lab12
selenium_tests

# Лабораторная работа №12. Selenium WebDriver

## Цель работы
Познакомиться с инструментом автоматизированного тестирования Selenium WebDriver.

## Используемые технологии
- Python 3.11
- Selenium
- Google Chrome + ChromeDriver

## Тестируемый сайт
https://store.steampowered.com — магазин Steam

## Тест-кейсы

### Тест-кейс 1 — Авторизация с некорректными данными
| Поле | Значение |
|---|---|
| Номер | 1 |
| Название | Авторизация с некорректными учётными данными |
| Предусловие | Пользователь не авторизован в системе |
| Шаги | 1. Перейти на страницу входа Steam; 2. Ввести логин `fake_user_123`; 3. Ввести пароль `wrongpassword`; 4. Нажать кнопку «Войти» |
| Ожидаемый результат | Пользователь остаётся на странице входа |
| Файл | `tests/test_1_invalid_login.py` |

### Тест-кейс 2 — Поиск игры в магазине
| Поле | Значение |
|---|---|
| Номер | 2 |
| Название | Поиск игры Counter-Strike 2 в магазине |
| Предусловие | Пользователь на главной странице Steam |
| Шаги | 1. Перейти на https://store.steampowered.com; 2. В поле поиска ввести `Counter-Strike 2`; 3. Нажать Enter |
| Ожидаемый результат | В результатах поиска отображается игра Counter-Strike 2 |
| Файл | `tests/test_2_search_game.py` |

### Тест-кейс 3 — Поиск предмета на торговой площадке
| Поле | Значение |
|---|---|
| Номер | 3 |
| Название | Поиск предмета AK-47 на торговой площадке |
| Предусловие | Пользователь на странице торговой площадки Steam |
| Шаги | 1. Перейти на https://steamcommunity.com/market; 2. В поле поиска ввести `AK-47`; 3. Нажать Enter |
| Ожидаемый результат | На странице отображается список предметов AK-47 |
| Файл | `tests/test_3_market_search.py` |

## Структура проекта
\```
selenium-lab12/
├── tests/
│   ├── test_1_invalid_login.py
│   ├── test_2_search_game.py
│   └── test_3_market_search.py
├── screenshots/
│   ├── test_1_result.png
│   ├── test_2_result.png
│   └── test_3_result.png
└── README.md
\```

## Установка и запуск
1. Установить зависимости:
\```
pip install selenium
\```
2. Скачать ChromeDriver под вашу версию Chrome:
   https://googlechromelabs.github.io/chrome-for-testing/
3. Указать пути к chrome.exe и chromedriver.exe в скриптах
4. Запустить тест:
\```
python tests/test_1_invalid_login.py
\```
