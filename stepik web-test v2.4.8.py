# Импортируем модули для работы со страницами браузера
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import math


# Определяем функцию для вычисления ответа на пример
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Открываем окно браузера при помощи менеджера контекста
with webdriver.Chrome() as b:
    # Задаём время неявного ожидания
    b.implicitly_wait(5)
    # Переходим по указанной ссылке
    b.get("https://suninjuly.github.io/explicit_wait2.html")
    # Задаем условие выполнения скрипта
    WebDriverWait(b, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    # Нажимаем на кнопку после выполнения условия выше
    b.find_element(By.CSS_SELECTOR, "button#book").click()
    # Вычисляем ответ по заданному значению переменной
    answer = str(calc(b.find_element(By.CSS_SELECTOR, "#input_value").text))
    # Заполняем поле для ответа
    b.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer)
    # Отправляем ответ нажатием на кнопку
    b.find_element(By.CSS_SELECTOR, "button#solve").click()
    # Выводим в терминал код из окна alert
    print(b.switch_to.alert.text.split()[-1])

# Пустая строка в конце файла