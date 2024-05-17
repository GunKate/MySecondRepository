from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def search_wikipedia(query):
    # Путь до вашего chromedriver
    driver_path = '/path/to/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)

    try:
        # Открываем Википедию
        driver.get("https://www.wikipedia.org/")

        # Находим поле поиска и вводим запрос
        search_box = driver.find_element_by_id("searchInput")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)  # Ждем, пока страница загрузится

        while True:
            # Получаем все параграфы с текущей страницы
            paragraphs = driver.find_elements_by_xpath("//p")

            # Выводим текст параграфов
            for para in paragraphs:
                print(para.text)
                print()

            # Спрашиваем пользователя, хочет ли он продолжить или выйти
            user_input = input("Введите 'c' для продолжения пролистывания параграфов, или 'q' для выхода: ")
            if user_input.lower() == 'q':
                break

            # Прокручиваем страницу вниз
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Ждем, пока страница загрузится

    finally:
        # Закрываем браузер
        driver.quit()


if __name__ == "__main__":
    query = input("Введите запрос для поиска в Википедии: ")
    search_wikipedia(query)