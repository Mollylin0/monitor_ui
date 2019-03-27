import time
import unittest
from BeautifulReport import BeautifulReport

test_dir = './testcase'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*testcase.py')


if  __name__ == '__main__':
    # 从这里执行
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    html_file = "./report"

    runner = unittest.TextTestRunner()
    # runner.run(discover)
    BeautifulReport(discover).report(filename='测试报告' + now, description='职场监控测试', log_path=html_file)




