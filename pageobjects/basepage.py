from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import unittest
import time
from readconfig import ReadConfig
from public.logger import Logger


class BasePage:
    """基类"""

    def __init__(self, selenium_driver):
        self.config = ReadConfig()
        self.logger = Logger.get_logger()
        self.driver = selenium_driver
        self.base_url = self.config.get_url("test_url")

    def _open(self, url):
        """以——为开头的方法，在使用import *时，该方法不会被导入，返回比较结果（True or False)"""
        self.driver.maximize_window()
        self.driver.get(url)

    def open(self):
        """调用——open()打开链接"""
        self._open(self.base_url)

    def find_element(self, *loc):
        """寻找元素"""
        try:
            # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            # print('找不到定位元素: %s' % loc[1])
            self.logger.warning('找不到定位元素: %s' % loc[1])
            raise
        except TimeoutException:
            # print('查找元素超时: %s' % loc[1])
            self.logger.warning('查找元素超时: %s' % loc[1])
            raise

    def find_element_presence(self, *loc):
        """元素存在dom中，即被找到"""
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))  # 显示等待
            return self.driver.find_element(*loc)
        except:
            # print(loc, '页面未找到元素')
            self.logger.warning(loc, '页面未找到元素')

    def find_elements(self, *loc):
        """寻找多个元素"""
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))  #显示等待
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            # print('%s页面未找到元素', loc)
            self.logger.warning('%s页面未找到元素', loc)
        except TimeoutException:
            self.logger.warning('查找元素超时: %s' % loc[1])

    def send_keys(self,  value, *loc , clear_first=True, click_first=True):
        """ 输入文本框
        :param value: 输入的文本
        :param clear_first: 是否清空文本框
        :param click_first: 是否点击文本框"""
        try:
            loc = getattr(self, *loc)
            if click_first:
                self.find_element(*loc).click()  # 点击
            if clear_first:
                self.find_element(*loc).clear()  # 清空文本框
                self.find_element(*loc).send_keys(value)  # 输入文本
        except AttributeError:
            # print("页面中未能找到元素", loc)
            self.logger.error("页面中未能找到元素", loc)

    def switch_frame(self, loc):
        """切换frame"""
        return self.driver.switch_to.frame(loc)

    def switch_default_frame(self):
        """返回默认iframe"""
        self.driver.switch_to_default_content()
        self.logger.info("返回默认iframe")

    def click(self, *loc):
        self.logger.info('点击元素 by {}'.format(loc[1]))
        try:
            self.find_element(*loc).click()
            time.sleep(0.5)
        except AttributeError as e:
            # print("无法点击元素: ", e)
            self.logger.error("无法点击元素: ", e)

    def wait(self, seconds):
        """隐式等待"""
        self.driver.implicitly_wait(seconds)
        # print("等待 %d 秒" % seconds)
        self.logger.info("等待 %d 秒" % seconds)

    def get_text(self, *loc):
        """获取文本"""
        element = self.find_element(*loc)
        return element.text

    def get_attribute(self, loc, name):
        '''获取属性'''
        element = self.find_element(*loc)
        return element.get_attribute(name)

    def is_element_exist(self, *loc):
        try:
            element = self.driver.find_element(*loc)
            if element==None:
                return False
            else:
                return True
        except:
            return False


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.参数化
    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_class, defName=None, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        if defName != None:
            for name in testnames:
                if name == defName:
                    suite.addTest(testcase_class(name, param=param))
        else:
            for name in testnames:
                suite.addTest(testcase_class(name, param=param))
        return suite
