"""
#@Time：2022/5/7-19:20
#@file：webui_key
#@Project:Pythonselenium
#@Content:

"""
from time import sleep

'''
关键字驱动：讲selenium中常用的操作行为，封装成自定义的函数，以便于直接调用
    1、结构设计：
        1、逻辑代码的实现，本身不存在任何价值，需要结合业务才能体现价值
        2、只有测试代码才可以对系统的功能进行自动化测试
        3、数据和代码进行分离，但凡数据需要改动，直接修改数据文件即可，不会影响到原有代码的稳定性
在UI自动化中，我们关注的是每一个不同的流程
在接口自动化中，我们关注单一接口的测试与关联接口的业务测试
    
'''
from selenium import webdriver


# 创建浏览器对象的
def open_browser(type_):
    try:
        driver = getattr(webdriver, type_)() # 反射机制 如果在创建过程中报错了，默认返回Chrome
    except:
        driver = webdriver.Chrome()

    return driver


# 关键字驱动
class WebKeys:
    # # 启动浏览器
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self,type_):
        self.driver = open_browser(type_)

    #  访问url
    def open(self, url):
        self.driver.get(url)

    # 定位元素
    def locator(self, **kwargs):
        return self.driver.find_element(kwargs['name'],kwargs['value'])

    # 输入
    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    # 点击
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # 等待
    def wait(self, time_):
        sleep(time_)

    # 关闭
    def quit(self):
        self.driver.quit()
