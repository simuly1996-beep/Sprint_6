from pages.home_page import HomePage

class TestFAQ:
    def test_first_question_opens_correct_text(self,driver):
        page = HomePage(driver)

        page.open_home_page()
        page.scroll_to_faq()
        page.click_question(0)

        answer = page.get_answer_text(0)
        
        assert "400 рублей" in answer

    def test_second_question_opens_correct_text(self,driver):
        page = HomePage(driver)

        page.open_home_page()
        page.scroll_to_faq()
        page.click_question(1)

        answer = page.get_answer_text(1)
        
        assert "Пока что у нас так" in answer

    def test_third_question_opens_correct_text(self,driver):
        page = HomePage(driver)

        page.open_home_page()
        page.scroll_to_faq()
        page.click_question(2)

        answer = page.get_answer_text(2)
        
        assert "Отсчёт времени аренды начинается с момента" in answer
    
    def test_fourth_question_opens_correct_text(self,driver):
        page = HomePage(driver)

        page.open_home_page()
        page.scroll_to_faq()
        page.click_question(3)

        answer = page.get_answer_text(3)
        
        assert "Только начиная с завтрашнего дня" in answer

    def test_fifth_question_opens_correct_text(self,driver):
        page = HomePage(driver)

        page.open_home_page()
        page.scroll_to_faq()
        page.click_question(4)

        answer = page.get_answer_text(4)
        
        assert "Пока что нет!" in answer

    def test_sixth_question_opens_correct_text(self,driver):
        page = HomePage(driver)

        page.open_home_page()
        page.scroll_to_faq()
        page.click_question(5)

        answer = page.get_answer_text(5)
        
        assert "Самокат приезжает к вам с полной зарядкой" in answer

    def test_seventh_question_opens_correct_text(self,driver):
        page = HomePage(driver)

        page.open_home_page()
        page.scroll_to_faq()
        page.click_question(6)

        answer = page.get_answer_text(6)
        
        assert "Да, пока самокат не привезли" in answer

    def test_eighth_question_opens_correct_text(self,driver):
        page = HomePage(driver)

        page.open_home_page()
        page.scroll_to_faq()
        page.click_question(7)

        answer = page.get_answer_text(7)
        
        assert "Да, обязательно" in answer