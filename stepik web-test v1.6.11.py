# Импортируем модули для работы со страницами браузера
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Передаем ссылку на веб-страницу с измененной формой регистрации
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля формы
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys("Boris")
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Zatulovskiy")
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys("zatulovskiy@mail.ru")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # Ждем загрузки страницы
    time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, "Something gone wrong"

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Пустая строка в конце файла