import os
import unittest
import time
from testcase.case_model import Model
from parameterized import parameterized


class WorkPlaceTestCase(Model):
    """职场配置测试用例"""
    img_path = os.getcwd()

    # @unittest.skip("暂时不测，跳过")
    def test_A0_openworkPlaceConfig(self):
        """是否进入职场列表页面"""
        name = self.work_config_page.workconfig_list()  # 职场列表元素
        self.assertEqual(name, '职场列表')

    # @unittest.skip("暂时不测，跳过")
    def test_A1_defaultWork(self):  # 初始化需要进入职场页面
        """检查默认职场"""
        self.assertEqual('示例职场', self.work_config_page.default_place_name())  # 职场名称
        self.assertEqual('--', self.work_config_page.default_place_position())  # 地理位置
        self.assertEqual('--', self.work_config_page.default_place_picture())  # 职场工位图
        self.assertEqual('--', self.work_config_page.default_place_maxnum())  # 最大工位数
        self.assertEqual('--', self.work_config_page.default_place_modify())  # 修改人
        self.assertIn('iconfont-no', self.work_config_page.default_place_edit())  # 编辑按钮
        self.assertIn('iconfont-no', self.work_config_page.default_place_delete())  # 删除按钮

    @parameterized.expand([  # 引用装饰器，准备参数，传入下方的函数
        ("test职场123abc!@#$%^&*", 100, '东侧1区b幢', img_path+r"\config\img\标准图片.jpg"),
        ("销售组", 100,"0123456789", img_path+r"\config\img\(zhaoxi.net).jpeg"),  # 255个字符
        ("kongge", 50, None, None),
        ("图片png", 0, "admin", img_path+r"\config\img\1-wps图片.png"),
    ])
    @unittest.skip("暂时不测，跳过")
    def test_A2_addplace(self, work_name, num, location, file):  # 初始化需要进入职场页面
        """新增职场"""
        self.work_config_page.add_workplace(work_name, num, location, file)  # 新增
        tips = self.work_config_page.success_tips()
        self.work_config_page.delete_workplace(work_name)  # 清除
        self.assertEqual("新建职场成功！", tips)

    @parameterized.expand([
        ("新增重名职场test", 1, "新增重名职场test已存在"),
    ])
    @unittest.skip("暂时不测，跳过")
    def test_A3_add_invalid_place(self, work_name, num, result):
        """新增重名职场验证"""

        self.work_config_page.add_workplace(work_name, num)  # 新增
        # 测试重名
        self.work_config_page.add_workplace(work_name, num)  # 新增
        sucess_tips = self.work_config_page.success_tips()
        self.assertEqual(result, sucess_tips)
        # 初始化清除
        self.work_config_page.delete_workplace(work_name)  # 删除职场

    @parameterized.expand([
        ("删除职场test", 1, "删除职场成功！"),
    ])
    @unittest.skip("暂时不测，跳过")
    def test_A4_delete_place(self, work_name, num, result):
        """成功删除职场验证"""
        self.work_config_page.add_workplace(work_name, num)  # 新增
        self.work_config_page.delete_workplace(work_name)  # 删除职场
        time.sleep(1)
        delete_tips = self.work_config_page.delete_success_tips()  # 删除职场成功提示
        self.assertEqual(result, delete_tips)

    @unittest.skip("暂时不测，跳过")
    def test_A5_name_null(self):
        """验证名称、工位数为空"""
        self.work_config_page.add_place_button()
        self.work_config_page.submit()
        name_tips = self.work_config_page.name_tip_text()  # 名字为空提示
        max_num_tips = self.work_config_page.max_num_tip_text()  # 最大工位数为空提示
        self.assertEqual("请输入职场名称", name_tips)
        self.assertEqual("请输入最大工位数", max_num_tips)

    @parameterized.expand([
        ("1234567890zxcvbnmasdf",
         '0123456789zxcvbnmkjh~!@#$%^&*(一二三四五六七八九十0123456789zxcvbnmkjh~!@#$%^&*(一二三四五六七八九十' \
         '0123456789zxcvbnmkjh~!@#$%^&*(一二三四五六七八九十0123456789zxcvbnmkjh~!@#$%^&*(一二三四五六七八九十' \
         '0123456789zxcvbnmkjh~!@#$%^&*(一二三四五六七八九十0123456789zxcvbnmkjh~!@#$%^&*(一二三四五六七八九十' \
         '012345678901234567890'),
    ])
    @unittest.skip("暂时不测，跳过")
    def test_A6_name_enough(self, work_name, location):
        """名字和工位号超过最大值"""
        self.work_config_page.add_place_button()
        self.work_config_page.place_name(work_name)
        self.work_config_page.place_location(location)
        name_tips = self.work_config_page.name_tip_text()  # 名字提示
        location_tips = self.work_config_page.location_tip_text()
        self.assertEqual("职场名称最多20字符", name_tips)
        self.assertEqual("职场位置最多256字符", location_tips)

    @parameterized.expand([
        (img_path+r"\config\img\1545698362241.jpg"),
    ])
    @unittest.skip("暂时不测，跳过")
    def test_A7_load_upload_img(self, file):
        """上传图片过大"""
        self.work_config_page.add_place_button()
        self.work_config_page.upload(file)
        time.sleep(1)
        img_tips = self.work_config_page.success_tips() # 提示
        self.assertEqual("图片大小限制500K以内！", img_tips)

    @parameterized.expand([
        (img_path + r"\config\img\test.txt"),
    ])
    @unittest.skip("暂时不测，跳过")
    def test_A8_upload_abnormal_file(self, file):
        """上传异常文件"""
        self.work_config_page.add_place_button()
        self.work_config_page.upload(file)
        time.sleep(1)
        img_tips = self.work_config_page.success_tips()  # 提示
        self.assertEqual("请确认上传的图片格式为jpeg、jpg或png!", img_tips)


if __name__ == '__main__':
    # WorkPlaceTestCase()
    unittest.main()
