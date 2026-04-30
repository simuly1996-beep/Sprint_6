from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text
    
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator))
    
    # получить дату для календаря
    def get_tomorrow_date(self, days=1):
        today = datetime.now().date()
        return (today + timedelta(days=days)).strftime("%d.%m.%Y")
    
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def switch_to_new_tab(self):
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
    
    # ожидание загрузки новой вкладки
    def wait_url_contains(self, text):
        self.wait.until(lambda driver: text in driver.current_url)
    
