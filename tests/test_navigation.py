from pages.order_page import OrderPage

class TestNavigation:
    def test_scooter_logo_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.ckick_logo_scooter()

        url = driver.current_url
        assert "qa-scooter.praktikum-services.ru" in url

    def test_yandex_logo_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.ckick_logo_yandex()

        order_page.switch_to_new_tab()
        order_page.wait_url_contains("dzen.ru")

        url = driver.current_url
        assert "dzen.ru" in url