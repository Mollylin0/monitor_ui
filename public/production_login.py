import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from readconfig import ReadConfig
from public.logger import Logger


class ProductLogin:
    """登录线上环境，把获取的token写入配置文件"""

    def login_production(self):
        """selenium+chromeheadless获取线上环境Token"""
        logger = Logger.get_logger()
        config = ReadConfig()   # 获取配置
        vcc = config.get_userinfo("vcc").split(",")
        username = config.get_userinfo("username").split(",")
        password = config.get_userinfo("password")
        production_url = config.get_url("production_url")

        day = time.strftime("%d")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)  # 等待
        driver.get(production_url)
        driver.find_element_by_id("vcc").send_keys(vcc[0])  # 登录
        driver.find_element_by_id("username").send_keys(username[0])
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id('btn').click()

        manage_cookie = driver.get_cookie('manage_access_token')
        driver.quit()
        manage_cookies = json.dumps(manage_cookie)
        config.update_token("day", day)  # 写入日期和token
        config.update_token("manage_access_token", manage_cookies)
        logger.info("获取线上manage_access_token到配置文件")


if __name__ == '__main__':
    t1 = ProductLogin()
    # t1.open_browser()
