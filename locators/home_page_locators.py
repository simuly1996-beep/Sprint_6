from selenium.webdriver.common.by import By

class HomePageLocators:
    # Заголовок блока вопросов
    FREQUENTLY_ASKED_QUESTIONS = (By.XPATH, "//div[text()='Вопросы о важном']")

    # Функция генератор локатора вопроса 
    @staticmethod
    def question(text):
        return (By.XPATH, f"//div[contains(@class, 'accordion__button') and contains(text(), '{text}')]")
    
    # Функция генератор локатора ответа    
    @staticmethod
    def answer(question):
        return (
            By.XPATH,
            f"//div[contains(@class,'accordion__button') and contains(., '{question}')]/parent::div/following-sibling::div//p"
        )
    
    # Кнопка "Заказать" верхняя
    ORDER_TOP_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")

    # Кнопка "Заказать" нижняя
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")
