from pageobjects.work_config_page import WorkConfigPage
from pageobjects.login_page import LoginTestPage
from public.driver import Driver
import unittest
from readconfig import ReadConfig
from public.logger import Logger


class Model(unittest.TestCase):
    """初始化清除"""

    @classmethod
    def setUpClass(cls):
        cls.config = ReadConfig()  # 读取配置
        cls.logger = Logger.get_logger()
        vcc = cls.config.get_userinfo("vcc").split(",")
        username = cls.config.get_userinfo("username").split(",")
        password = cls.config.get_userinfo("password")

        d = Driver("Chrome")
        cls.driver = d.selenium_driver()
        t = LoginTestPage(cls.driver)
        t.open()
        t.login_test(vcc[1], username[1], password) # 登录，切换token

        cls.work_config_page = WorkConfigPage(cls.driver)  # 进入职场配置页面
        cls.work_config_page.enter_work_config_page()

    def setUp(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.logger.info("关闭浏览器")
        cls.driver.quit()


