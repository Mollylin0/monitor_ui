from threading import Thread
from public.production_login import ProductLogin
from pageobjects.basepage import BasePage
from selenium.webdriver.common.by import By
import time
import json


class LoginTestPage(BasePage):
    """登录测试环境"""

    def open(self):
        """打开网页，通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。"""
        self._open(self.base_url)
        self.logger.info('打开网址：{}'.format(self.base_url))

    def input_vcc_code(self, vcc_code):
        """输入企业代码"""
        self.find_element(By.ID, 'vcc_code').send_keys(vcc_code)

    def input_username(self, username):
        """输入用户名"""
        self.find_element(By.ID, 'username').send_keys(username)

    def input_password(self, password):
        """输入密码"""
        self.find_element(By.ID, 'password').send_keys(password)

    def click_submit(self):
        """点击登录按钮"""
        self.find_element(By.ID, 'btn').click()

    def login(self, vcc_code, username, password):
        """登录测试环境，添加线上Token"""
        self.input_vcc_code(vcc_code)
        self.input_username(username)
        self.input_password(password)
        self.click_submit()
        self.logger.info("登录成功")
        self.driver.delete_cookie('manage_access_token')  # 删除测试环境的token
        self.logger.info("删除测试环境Token")

    def add_test_cookie(self):
        """读取线上manage_token，写入cookie"""
        new_token = self.config.get_token()
        new_token = json.loads(new_token)
        self.driver.add_cookie(new_token)
        self.logger.info("线上token写入线上环境cookie")

    def login_test(self, vcc_code, username, password):
        """登录测试环境，若日期是今天，直接取配置文件token。若不是，则获取线上环境token"""
        product = ProductLogin()
        last_time = self.config.get_day()  # 获取日期
        if (time.strftime("%d")) == last_time:
            self.login(vcc_code, username, password)
            self.add_test_cookie()
            self.logger.info("日期有效，直接读取配置文件token")
        else:
            t = Thread(target=product.login_production)  # 运行线上环境线程
            t.start()
            self.login(vcc_code, username, password)
            t.join()  # 等待
            self.add_test_cookie()
            self.logger.info("日期过期，重新获取Token")

    def close_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    pass
