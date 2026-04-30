from pages.base_page import BasePage
from locators.order_page_locators import OrderLocators
from selenium.webdriver.common.keys import Keys
from curl import ORDER_URL
class OrderPage(BasePage):
    # откыть страницу заказа   
    def open_order_page(self):
        self.open(ORDER_URL) 
    # ===== Блок "Для кого самокат" =====

    # ввод в поле имя
    def send_name(self, name):
        self.type(OrderLocators.NAME_INPUT, name)
    
    # ввод в поле фамилия
    def send_surname(self, surname):
        self.type(OrderLocators.SURNAME_INPUT, surname)
    
    # ввод в поле адрес
    def send_addres(self, addres):
        self.type(OrderLocators.ADDRESS_INPUT, addres)
    
    # ввод в поле станция метро
    def select_metro_station(self, station_name):
        self.click(OrderLocators.METRO_INPUT)
        self.type(OrderLocators.METRO_INPUT, station_name)

        option_locator = OrderLocators.metro_option(station_name)

        self.wait_visibility(option_locator)
        self.click(option_locator)

    # ввод в поле телефон
    def send_phone(self, phone):
        self.type(OrderLocators.PHONE_INPUT, phone)
    

    # нажать на кнопуку "далее"
    def click_next(self):
        self.click(OrderLocators.NEXT_BUTTON)

    # ===== Блок "Про аренду" =====

    # выбор даты в поле "когда привезти самокат"
    def set_delivery_date(self, days=1):
        date = self.get_tomorrow_date(days)
        self.type(OrderLocators.DATE_INPUT, date)
        self.find(OrderLocators.DATE_INPUT).send_keys(Keys.ENTER)

    # выбор срока аренды
    def set_rental_period(self, period):
        self.click(OrderLocators.RENT_PERIOD_DROPDOWN)

        option_locator = OrderLocators.rent_period_option(period)

        self.wait_visibility(option_locator)
        self.click(option_locator)
    
    # выбор цвета самоката 
    def sent_color(self, color):
        if color == "black":
            self.click(OrderLocators.BLACK_CHECKBOX)
        elif color == "grey":
            self.click(OrderLocators.GREY_CHECKBOX)

    # ввод кооментария
    def send_comment(self, comment):
        self.type(OrderLocators.COMMENT_INPUT, comment)

    # нажать "заказать"
    def click_order(self):
        self.click(OrderLocators.ORDER_BUTTON)

    # нажать "да"
    def click_yes(self):
        self.wait_clickable(OrderLocators.CONFIRM_BUTTON)
        self.click(OrderLocators.CONFIRM_BUTTON)
    
    # отображение надписи "Заказ оформлен"
    def display_order(self):
        return self.wait_visibility(OrderLocators.SUCCESS_ORDER)
    
    #  ===== Работа с логотипами ===== 

    # нажать лого яндекс
    def ckick_logo_yandex(self):
        self.wait_clickable(OrderLocators.YANDEX_LOGO)
        self.click(OrderLocators.YANDEX_LOGO)
        
    # нажать лого скутер
    def ckick_logo_scooter(self):
        self.wait_clickable(OrderLocators.SCOOTER_LOGO)
        self.click(OrderLocators.SCOOTER_LOGO)

