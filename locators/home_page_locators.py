from selenium.webdriver.common.by import By

class HomePageLocators:
    # Заголовок блока вопросов
    FREQUENTLY_ASKED_QUESTIONS = (By.XPATH, "//div[text()='Вопросы о важном']")

    # Функция генератор локатора вопроса 
    @staticmethod
    def question(index):
        return (By.ID, f"accordion__heading-{index}")

    # Функция генератор локатора ответа
    @staticmethod
    def answer(index):
        return (By.ID, f"accordion__panel-{index}")

    # Кнопка "Заказать" верхняя
    ORDER_TOP_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")

    # Кнопка "Заказать" верхняя
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")



    