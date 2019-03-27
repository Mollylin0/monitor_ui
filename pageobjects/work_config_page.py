import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.login_page import LoginTestPage
from pageobjects.basepage import BasePage
from pageobjects.menu_page import MenuPage


class WorkConfigPage(BasePage):
    """职场配置page elements"""
    # 定位器
    workplace_loc = (By.CSS_SELECTOR, 'div.company-list-containers-toptile > div > span')  # 列表元素
    default_place_locs = (By.CSS_SELECTOR, 'div[aria-label="grid"] div[data-row="0"]')  # 默认列表
    default_place_name_loc = (By.CSS_SELECTOR, ':nth-child(2) span')  # 默认名称
    default_place_position_loc = (By.CSS_SELECTOR, ':nth-child(3) span')  # 默认地理位置
    default_place_picture_loc = (By.CSS_SELECTOR, ':nth-child(4) span')  # 默认工位图
    default_place_maxnum_loc = (By.CSS_SELECTOR, ':nth-child(5)>div')  # 默认最大工位数
    default_place_modify_loc = (By.CSS_SELECTOR, ':nth-child(7) span')  # 默认修改人
    default_place_edit_loc = (By.CSS_SELECTOR, ':nth-child(8) i[title="编辑"]')  # 默认编辑按钮
    default_place_delete_loc = (By.CSS_SELECTOR, ':nth-child(8) i[title="删除"]')  # 删除按钮

    add_place_loc = (By.CSS_SELECTOR, 'div.company-list-containers-toptile > div > button')  # 新建按钮
    place_name_loc = (By.CSS_SELECTOR, "#settingName")  # 名称
    place_location_loc = (By.CSS_SELECTOR, "#settingPosition")  # 位置
    max_work_num_loc = (By.CSS_SELECTOR, "#maxAgentNum")  # 最大工位数
    license_loc = (By.CSS_SELECTOR, "div > span > div > div:nth-child(2) > span")  # 不超过license数量
    upload_loc = (By.CSS_SELECTOR, 'div.ant-upload> span > input[type="file"]')  # 上传
    add_place_sure_loc1 = (By.CSS_SELECTOR, "body.icsoc>:nth-last-child(1) div button.ant-btn-primary")  # 有hidden时使用
    add_place_sure_loc = (By.CSS_SELECTOR, "div.ant-modal-footer>div>button.ant-btn.ant-btn-primary")  # 确定按钮

    add_place_cancel_loc = (By.CSS_SELECTOR, "div.ant-modal-footer > div > button:nth-child(1)")  # 取消按钮
    all_place_name_locs = (By.CSS_SELECTOR, 'div[aria-label="grid"] div[data-col="1"]')  # 所有的名称
    success_tips_loc = (By.CSS_SELECTOR, "div.ant-message>span>div:nth-last-child(1)>div>div>span")  # 新建成功提示

    delete_submit_loc1 = (By.CSS_SELECTOR, "body.icsoc>:nth-last-child(1) button.ant-btn-primary")  # 有hidden时使用
    delete_submit_loc = (By.CSS_SELECTOR, "div.ant-modal-footer>div>button.ant-btn.ant-btn-primary")  # 删除确定按钮
    delete_sucess_tips_loc = (By.CSS_SELECTOR, "div.ant-message>span>div:nth-last-child(1)>div>div>span")  # 删除按钮成功提示
    ant_modal_mask_hidden_loc = (By.CSS_SELECTOR, "body div > div.ant-modal-mask.ant-modal-mask-hidden")  # 隐藏属性
    name_tip_loc = (By.CSS_SELECTOR, "div:nth-child(1) > div.ant-col-19.ant-form-item-control-wrapper > div > div")  # 名字提示
    max_num_tip_loc = (By.CSS_SELECTOR, "div:nth-child(3) > div.ant-col-19.ant-form-item-control-wrapper > div > div")  # 工号为空提示
    location_tip_loc = (By.CSS_SELECTOR, "div:nth-child(2) > div.ant-col-19.ant-form-item-control-wrapper > div > div") # 地理位置tips

    def switch_frame_to_workplace(self):
        """切换到职场配置frame"""
        self.switch_frame('frame150')

    def workconfig_list(self):
        """职场列表元素"""
        # list_name = self.find_element(*self.workplace_loc).text
        list_name = self.get_text(*self.workplace_loc)
        return list_name

    def default_place_lists(self):
        """默认职场列表"""
        d_list = self.find_elements(*self.default_place_locs)
        return d_list

    def default_place_name(self):
        """默认职场名称"""
        d_list = self.default_place_lists()
        name = d_list[1].find_element(*self.default_place_name_loc).text
        return name

    def default_place_position(self):
        """默认职场位置"""
        d_list = self.default_place_lists()
        position = d_list[2].find_element(*self.default_place_position_loc).text
        return position

    def default_place_picture(self):
        """默认职场工位图"""
        d_list = self.default_place_lists()
        picture = d_list[3].find_element(*self.default_place_picture_loc).text
        return picture

    def default_place_maxnum(self):
        """默认职场最大工位数"""
        d_list = self.default_place_lists()
        maxnum = d_list[4].find_element(*self.default_place_maxnum_loc).text
        return maxnum

    def default_place_modify(self):
        """默认职场修改人"""
        d_list = self.default_place_lists()
        modify_man = d_list[6].find_element(*self.default_place_modify_loc).text
        return modify_man

    def default_place_edit(self):
        """默认职场编辑按钮"""
        d_list = self.default_place_lists()
        edit = d_list[7].find_element(*self.default_place_edit_loc).get_attribute('class')
        return edit

    def default_place_delete(self):
        """默认职场删除按钮class属性"""
        d_list = self.default_place_lists()
        delete = d_list[7].find_element(*self.default_place_delete_loc).get_attribute('class')
        return delete

    def add_place_button(self):
        """新建职场按钮"""
        try:
            self.click(*self.add_place_loc)
        except:
            self.driver.refresh()
            self.enter_work_config_page()
            self.click(*self.add_place_loc)
            self.logger.info("刷新页面，重新点击新建职场按钮")

    def place_name(self, value):
        """职场名称"""
        self.find_element(*self.place_name_loc).send_keys(value)

    def place_location(self, value):
        """职场位置"""
        self.find_element(*self.place_location_loc).send_keys(value)

    def max_work_num(self, value):
        """最大工位数"""
        self.find_element(*self.max_work_num_loc).send_keys(value)

    def license_num(self):
        """license数量"""
        license = self.get_text(*self.license_loc)
        return license

    def upload(self, value):
        """上传文件"""
        self.find_element_presence(*self.upload_loc).send_keys(value)
        self.logger.info("上传文件{}".format(value))

    def submit(self):
        """新建职场的确定按钮"""

        elements = self.driver.find_elements(*self.add_place_sure_loc)
        for i in elements:
            try:
                i.click()
            except:
                print("two Hidden")

    def delete_submit(self):
        """点击删除职场确定按钮"""
        elements = self.driver.find_elements(*self.add_place_sure_loc)
        for i in elements:
            try:
                i.click()
            except:
                print("two Hidden")

    def add_place_cancel(self):
        """取消按钮"""
        self.click(*self.add_place_cancel_loc)

    def success_tips(self):
        """新建成功职场提示"""
        tips = self.get_text(*self.success_tips_loc)
        return tips

    def delete_success_tips(self):
        """删除职场成功提示"""
        tips = self.get_text(*self.delete_sucess_tips_loc)
        return tips

    def delete_button(self, index):
        """点击删除按钮"""
        self.driver.find_element_by_css_selector('div[aria-label="grid"] div[data-row="%d"]>div>i[title="删除"]'
                                                 % index).click()

    def name_tip_text(self):
        """获取名字为空提示"""
        tips = self.get_text(*self.name_tip_loc)
        return tips

    def max_num_tip_text(self):
        """获取最大工位数为空提示"""
        tips = self.get_text(*self.max_num_tip_loc)
        return tips

    def location_tip_text(self):
        """获取位置Tips"""
        tips = self.get_text(*self.location_tip_loc)
        return tips

    # 方法实现
    def max_license_num(self):
        """获取最大license文字"""
        max_license = self.license_num()
        max_num = max_license.split("：")[1].replace(')', '')  # 获取license数
        return max_num

    def all_place_names(self):
        """所有的职场名称"""
        names = self.find_elements(*self.all_place_name_locs)
        names_list = []  # 职场名称列表
        for n in names:
            names_list.append(n.text)
        return names_list

    def enter_work_config_page(self):
        """进入职场配置页面"""
        menu_page = MenuPage(self.driver)
        menu_page.page_advance_setting()  # 点击高级设置菜单
        menu_page.page_work_config()  # 进入职场配置页面
        self.switch_frame_to_workplace()
        self.logger.info("进到职场配置页面")

    def add_workplace(self, work_name, num, location=None, filename=None):
        """新建职场"""
        try:
            self.add_place_button()
        except :
            # print("寻找新建职场元素失败")
            self.driver.refresh()
            self.enter_work_config_page()
            self.add_place_button()

        self.place_name(work_name)
        if location is not None:
            self.place_location(location)  # 输入职场位置
        self.max_work_num(num)  # 输入license
        if filename is not None:
            self.upload(filename)  # 上传图片
            time.sleep(0.5)
        self.submit()  # 点击确定按钮
        self.logger.info("提交新建职场按钮")
        time.sleep(1.25)

    def delete_workplace(self, name):
        """删除职场"""
        num = 0  # 删除按钮的坐标
        try:
            names = self.all_place_names()  # 获取所有的职场名称
            for index in range(len(names)):
                if name == names[index]:
                    num = index
            self.delete_button(num)  # 点击删除按钮
            time.sleep(0.5)
        except :
            print("Failed to find delete button element")  # 寻找删除按钮元素失败
            self.driver.refresh()
            self.enter_work_config_page()
            self.delete_button(num)
            time.sleep(0.5)

        self.delete_submit()  # 点击删除确定按钮
        self.logger.info("删除职场")


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    driver = webdriver.Chrome(options=option)
    t1 = LoginTestPage(driver)
    t1.open()




