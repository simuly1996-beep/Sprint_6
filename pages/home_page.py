import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from curl import BASE_URL


class HomePage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_home_page(self):
        self.open(BASE_URL)

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_faq(self):
        self.scroll_to_element(HomePageLocators.FREQUENTLY_ASKED_QUESTIONS)

    @allure.step("Клик по вопросу")    
    def click_question(self, question_text):
        locator = HomePageLocators.question(question_text)

        self.scroll_to_element(locator)
        self.wait_clickable(locator)
        self.click(locator)

    @allure.step("Получение текста ответа") 
    def get_answer_text(self, question_text):
        locator = HomePageLocators.answer(question_text)
        self.wait_visibility(locator)
        return self.get_text(locator)
      
    @allure.step("выбор одной из двух кнопкок заказать на главной странице")  
    def click_order_button(self, location):
        if location == "top":
            self.click(HomePageLocators.ORDER_TOP_BUTTON)
        elif location == "botton":
            self.scroll_to_element(HomePageLocators.ORDER_BOTTOM_BUTTON)
            self.wait_clickable(HomePageLocators.ORDER_BOTTOM_BUTTON)
            self.click(HomePageLocators.ORDER_BOTTOM_BUTTON)
    