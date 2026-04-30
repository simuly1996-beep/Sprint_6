import pytest
from pages.order_page import OrderPage
from pages.home_page import HomePage
from data.order_data import FIRST_ORDER, SECOND_ORDER



@pytest.mark.parametrize("order_data", [FIRST_ORDER, SECOND_ORDER])
class TestOrder:
    def test_order(self, driver, order_data):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_order_button(order_data["location"])

        order_page = OrderPage(driver)

        order_page.send_name(order_data["name"])
        order_page.send_surname(order_data["surname"])
        order_page.send_addres(order_data["address"])
        order_page.select_metro_station(order_data["metro"])
        order_page.send_phone(order_data["phone"])

        order_page.click_next()

        order_page.set_delivery_date()
        order_page.set_rental_period(order_data["rent_period"])
        order_page.sent_color(order_data["color"])
        order_page.send_comment(order_data["comment"])
        order_page.click_order()
        order_page.click_yes()
        assert order_page.display_order()
