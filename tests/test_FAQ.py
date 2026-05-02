import allure
import pytest
from pages.home_page import HomePage
from data.FAQ_data import FAQ_DATA

@pytest.mark.parametrize("question, answer", FAQ_DATA)
class TestFAQ:
    
    @allure.title("Проверка получения ответо на часто задаваемые вопросов на главной странице")
    def test_faq_answers(self, driver, question, answer):
        page = HomePage(driver)

        page.open_home_page()
        page.scroll_to_faq()
        page.click_question(question)

        actual_answer = page.get_answer_text(question)
        
        assert answer in actual_answer
