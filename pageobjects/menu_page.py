from pageobjects.basepage import BasePage
from selenium.webdriver.common.by import By


class MenuPage(BasePage):
    """导航菜单"""

    advance_setting_loc = (By.CSS_SELECTOR, 'div.nav-wrap > div > ul > li:nth-last-child(2)')  # 高级设置页面
    page_workconfig_loc = (By.CSS_SELECTOR, 'div.nav-wrap>div>ul>li:nth-last-child(2)>ul>:nth-child(8)')  # 职场配置
    max_license_loc = (By.XPATH, '//*[@id="main-container"]//tbody/tr[3]/td[1]')  # 最多创建人数

    def max_license(self):
        """最大创建人数"""
        text = self.get_text(*self.max_license_loc)
        num = text.split("最多创建: ")[1].replace(" ]","")
        return num

    def switch_frame_to_main(self):
        self.switch_frame("frame仪表盘 scrolling=")

    def page_advance_setting(self):
        """进入高级设置页面"""
        # self.find_element(*self.advance_setting_loc).click()  # 元祖，不可变
        self.click(*self.advance_setting_loc)
        self.logger.info("进入高级设置页面")

    def page_work_config(self):
        """进入职场配置页面"""
        # self.find_element(*self.page_workconfig_loc).click()
        self.click(*self.page_workconfig_loc)
        self.logger.info("进入职场配置页面")
