from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_elements_by_xpath(self.locator))
        driver.find_elements_by_xpath(self.locator).clear()
        driver.find_elements_by_xpath(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_elements_by_xpath(self.locator))
        element = driver.find_elements_by_xpath(self.locator)

        return element.get_attribute("value")