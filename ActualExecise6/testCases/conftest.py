from selenium import webdriver
from ActualExecise6.PageObjects.login_page import LoginPage

from ActualExecise6.TestDatas import Common_datas as CD
import pytest


@pytest.fixture(scope="function")  # 声明这是一个夹测试函数的前置后置
def init_driver():
    # 打开谷歌浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 访问 系统登录页面
    driver.get(CD.login_url)
    lp = LoginPage(driver)
    yield driver, lp
    # 关闭浏览器 退出当前会话
    driver.quit()


@pytest.fixture(scope="class")
def myClass():
    print("-----------我是测试类级别的前置----------------")
    yield
    print("-----------我是测试类级别的后置----------------")
