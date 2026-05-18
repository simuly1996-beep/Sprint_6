from selenium.webdriver.common.by import By

class OrderLocators:

    # ===== Блок "Для кого самокат" =====

    # Поле "Имя" 
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Имя')]")

    # Поле "Фамилия" 
    SURNAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]")

    # Поле "Адрес" 
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")

    # Поле "Станция метро" 
    METRO_INPUT = (By.XPATH, "//input[contains(@placeholder,'Станция метро')]")

    # Выбор станции метро из выпадающего списка
    @staticmethod
    def metro_option(station_name):
        return  (
        By.XPATH,
        f"//input[contains(@placeholder,'метро')]/ancestor::div[contains(@class,'select-search')]//div[contains(text(),'{station_name}')]"
    )

    # Поле "Телефон" 
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")
    
    # Кнопка "Далее" 
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']") 
    
    # ===== Блок "Про аренду" =====

    # Поле "Когда привезти самокат" 
    DATE_INPUT = (By.XPATH, "//input[contains(@placeholder,'Когда привезти')]")

    # Поле "Срок аренды"     
    RENT_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class,'Dropdown-placeholder')]")

    # Выбор срока аренды из выпадающего списка
    @staticmethod
    def rent_period_option(period):
        return  (
        By.XPATH, f"//div[contains(@class,'Dropdown-menu')]//div[contains(text(),'{period}')]")
    
    # Чек боксы "Цвет самоката"  
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")

    # Поле "Комментарий"
    COMMENT_INPUT = (By.XPATH, "//input[contains(@placeholder,'Комментарий')]")

    # Кнопка "Заказать"
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons__1xGrp')]//button[text()='Заказать']")

    # Кнопка "Да"
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # ===== Успешный заказ =====
    SUCCESS_ORDER = (By.XPATH, "//div[text()='Заказ оформлен']")

    
    # ===== Логотипы =====
    # Логотип Яндекс
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    # Логотип Самокат
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")