from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запрашиваем у пользователя ввод
user_input1 = input("Введите ваш запрос для поиска информации в Википедии: ")

# Инициализация браузера
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title
time.sleep(2)

# Ищем поле поиска и вводим запрос
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(user_input1)
search_box.send_keys(Keys.RETURN)

time.sleep(2)  # Ждем, пока страница загрузится

try:
    while True:
        # Получаем все параграфы с текущей страницы
        paragraphs = browser.find_elements(By.XPATH, "//p")

        # Выводим текст параграфов
        for para in paragraphs:
            print(para.text)
            print()

        # Спрашиваем пользователя, хочет ли он продолжить или выйти
        user_input = input("Введите 'c' для продолжения пролистывания параграфов, или 'q' для выхода: ")
        if user_input.lower() == 'q':
            break

        # Прокручиваем страницу вниз
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Ждем, пока страница загрузится

finally:
    # Закрываем браузер
    browser.quit()