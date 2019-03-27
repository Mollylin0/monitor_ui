from selenium import webdriver
from public.logger import Logger


class Driver:
    """driver"""

    def __init__(self, driver_name):
        self.driver = driver_name
        self.logger = Logger.get_logger()

    def selenium_driver(self):
        web_driver = None
        if self.driver == "Chrome":
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            web_driver = webdriver.Chrome(options=option)
            self.logger.info("打开Chrome")

        elif self.driver == "Firefox":
            web_driver = webdriver.Firefox()
            self.logger.info("打开Firefox")
        elif self.driver == "Ie":
            web_driver = webdriver.Ie()
            self.logger.info("打开Ie")
        return web_driver

