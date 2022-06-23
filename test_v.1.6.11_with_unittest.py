# Импортируем модули для работы со страницами браузера
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


# С помощью unittest создаем класс для проверки тестового сценария
class TestAbs(unittest.TestCase):
    # Позитивный сценарий тестирования
    def test_registration_form1(self):
        # Открываем окно браузера при помощи менеджера контекста
        with webdriver.Chrome() as b:
            # Передаем ссылку на веб-страницу с измененной формой регистрации
            b.get("https://suninjuly.github.io/registration1.html")

            # Заполняем обязательные поля формы
            b.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys("Boris")

            b.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys("Zatulovskiy")

            b.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys("zatulovskiy@mail.ru")

            # Отправляем заполненную форму
            b.find_element(By.CSS_SELECTOR, "button.btn").click()

            # Ждем загрузки страницы
            b.implicitly_wait(1)

            # Записываем в переменную welcome_text текст из соответствующего элемента
            welcome_text = b.find_element(By.TAG_NAME, "h1").text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Something gone wrong")

    # Негативный сценарий тестирования
    def test_registration_form2(self):
        # Открываем окно браузера при помощи менеджера контекста
        with webdriver.Chrome() as b:
            # Передаем ссылку на веб-страницу с измененной формой регистрации
            b.get("https://suninjuly.github.io/registration2.html")

            # Заполняем обязательные поля формы
            b.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys("Leonid")

            b.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys("Zatulovskiy")

            b.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys("zatulovskiy@mail.ru")

            # Отправляем заполненную форму
            b.find_element(By.CSS_SELECTOR, "button.btn").click()

            # Ждем загрузки страницы
            b.implicitly_wait(1)

            # Записываем в переменную welcome_text текст из соответствующего элемента
            welcome_text = b.find_element(By.TAG_NAME, "h1").text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Something gone wrong")


if __name__ == "__main__":
    unittest.main()
# Пустая строка в конце файла
