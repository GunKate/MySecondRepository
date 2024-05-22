from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запрашиваем у пользователя ввод
user_query = input("Введите ваш запрос для поиска информации в Википедии: ")

# Инициализация браузера
browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title
time.sleep(2)

# Ищем поле поиска и вводим запрос
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(user_query)
search_box.send_keys(Keys.RETURN)

time.sleep(2)  # Ждем, пока страница загрузится

# Переходим по первой ссылке в результатах поиска
first_link = browser.find_element(By.CSS_SELECTOR, "ul.mw-search-results li a")
first_link.click()

# Ждем загрузки страницы
time.sleep(10)

user_choice = input("Введите вариант работы со статьей: 1 - переход по параграфам текущей статьи, 2 - переход на одну из связанных страниц, 0 - выход из программы ")

if user_choice == '1':
    # Получаем все параграфы с текущей страницы
    paragraphs = browser.find_elements(By.XPATH, "//p")
    # Выводим текст параграфов
    for para in paragraphs:
        print(para.text)
        print()
elif user_choice == '0':
    browser.quit()
elif user_choice == '2':
    # Получаем связанные ссылки в разделе "См. также"
    related_links = browser.find_elements(By.XPATH, "//div[@id='bodyContent']//ul/li/a")
    # Выводим связанные ссылки
    print("Связанные страницы:")
    for idx, link in enumerate(related_links):
        print(f"{idx + 1}. {link.text}")
    # Запрашиваем у пользователя выбор связанной страницы
    choice = int(input("Введите номер связанной страницы для перехода (или 0 для выхода): "))
    if 0 < choice <= len(related_links):
        related_links[choice - 1].click()
        time.sleep(2)  # Ждем загрузки страницы
        # Получаем все параграфы с текущей страницы
        paragraphs = browser.find_elements(By.XPATH, "//p")
        # Выводим текст параграфов
        for para in paragraphs:
            print(para.text)
            print()
else:
    browser.quit()