import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator))
    
    @allure.step("Найти несколько элементов")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.find(locator).click()

    @allure.step("Ввести текст в поле")
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step("Прокрутить до элемента")
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Дождаться видимости элемента")
    def wait_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator))
    
    @allure.step("Получить дату для календаря")   
    def get_tomorrow_date(self, days=1):
        today = datetime.now().date()
        return (today + timedelta(days=days)).strftime("%d.%m.%Y")
    
    @allure.step("Дождаться, когда элемент станет кликабельным")    
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Переключиться на новую вкладку")   
    def switch_to_new_tab(self):
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
    
    @allure.step("Дождаться, что URL содержит '{text}'")
    def wait_url_contains(self, text):
        self.wait.until(EC.url_contains(text))
    
