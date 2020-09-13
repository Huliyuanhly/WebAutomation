"""
登录成功 用例
用例中不出现元素定位和元素操作
"""
import unittest
from selenium import webdriver
from ActualExecise.PageObjects.login_page import LoginPage
from ActualExecise.PageObjects.home_page import HomePage
import time
import ddt


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 访问 系统登录页面
        self.driver.get("http://120.78.128.25:8765/index/login.html")
        self.lp = LoginPage(self.driver)

    def tearDown(self) -> None:
        # 关闭浏览器 退出当前会话
        self.driver.quit()

    def test_login_success(self):
        # 步骤
        # 1.登录页面-登录操作
        # lp= LoginPage(self.driver)
        self.lp.login("18684720553", "python")  # 初始化类，调用方法传参执行用例步骤
        # 断言
        # 1.URL发生改变(不属于页面行为)
        time.sleep(2)
        self.assertEqual("http://120.78.128.25:8765/Index/index", self.driver.current_url)
        # 2.首页-确认 我的账号 元素存在 (属于页面行为)
        self.assertTrue(HomePage(self.driver).user_is_existed())

    wrong_data = [
        {"username": "", "passwd": "python", "check": "请输入手机号"},  # 用户名为空
        {"username": "18684720553", "passwd": "", "check": "请输入密码"},  # 密码为空
        {"username": "186847205", "passwd": "python", "check": "请输入正确的手机号"}  # 用户名格式不正确
    ]

    @ddt.data(*wrong_data)
    def test_login_fail(self, case):
        # 步骤
        # lp= LoginPage(self.driver) # 放到setUp中
        self.lp.login(case["username"], case["passwd"])  # 初始化类，调用方法传参执行用例步骤
        # 断言
        self.assertEqual(self.lp.get_error_msg_from_login_form(), case["check"])

    def test_login_fail_pop_up(self):
        # 步骤
        self.lp.login("18684720553", "11111111")  # 初始化类，调用方法传参执行用例步骤
        # 断言
        self.assertEqual(self.lp.get_error_msg_from_pop_up(), "帐号或密码错误!")
