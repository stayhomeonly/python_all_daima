'''
---------------------------
File Name:ddt1
Author:FENGXIN
date:2022/4/19-19:53

---------------------------

'''
import unittest

from ddt import ddt, file_data


# 读取txt的内容
def read_file():
    file = open('params.txt', 'r', encoding='utf-8')
    li = []
    for line in file.readlines():
        print(line)
        li.append(line.strip('\n').split(','))  # strip 处理掉分隔符\n
    for l in li:
        print(l)
    file.close()
    return li


@ddt
class TestLogin(unittest.TestCase):
    # 前置条件
    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
    #     self.driver.implicitly_wait(100)
    #
    # def tearDown(self) -> None:
    #     self.driver.quit()
    #
    # @data(*read_file())  # 参数化txt的内容,已元组的形式去解读
    # @unpack  # 参数数据，然后分别赋值给username,pwd,如果需要多个参数直接给用多个列表
    # def test_1(self, username, pwd):
    #     self.driver.find_element_by_xpath('//input[@name="accounts"]').send_keys(username)
    #     sleep(2)
    #     self.driver.find_element_by_xpath('//input[@name="pwd"]').send_keys(pwd)
    #     self.driver.find_element_by_xpath('//button[text()="登录"]').click()
    #     sleep(5)

    # 传入的参数是字典格式，就不需要unpack解包
    @file_data('test1.yaml')
    def test_03(self, **user):  # **参数化成字典形式
        name = user.get("name")
        pwd = user.get("pwd")
        print(name)
        print(pwd)
        # if name == 123456:
        #     print('Successful')
        # else:
        #     print('false')
        self.assertEqual(name, 123456, msg='登录名')
        print('这是断言成功之后的内容')  # 如果不成功就不会到这一步

    # 无条件跳过本条的执行
    @unittest.skip('不想他运行')
    def test_4(self):
        pass

    # 有条件跳过本条用例运行1=False
    @unittest.skipUnless(1 > 2, '这是Unless的理由')  # 条件为false则执行
    def test_5(self):
        pass

    # 有条件跳过本条用例执行2=True
    @unittest.skipIf(1 > 2, '这是if的理由')  # 条件为True则执行
    def test_6(self):
        pass

    @unittest.expectedFailure  # 预期失败自动跳过
    def test_7(self):
        print("test_7")
        self.assertEqual(1223, 2222, msg='Not Equal')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()  # 如果要用测试套件，必须新建一个file才能用，如果在当前页面Unittest用，默认执行所有
    # 添加测试用例
    # suite.addTest(TestLogin('test_03'))
    suite.addTest(TestLogin('test_6'))
    suite.addTest(TestLogin('test_7'))

    # 基于Runner来运行测试套件

    runner = unittest.TextTestRunner()
    runner.run(suite)
