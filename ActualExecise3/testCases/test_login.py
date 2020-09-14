"""
登录成功 用例
用例中不出现元素定位和元素操作
"""
import unittest
from selenium import webdriver
from ActualExecise3.PageObjects.login_page import LoginPage
from ActualExecise3.PageObjects.home_page import HomePage
import time
import ddt
from ActualExecise3.TestDatas import Common_datas as CD
from ActualExecise3.TestDatas import login_datas as LD


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 访问 系统登录页面
        self.driver.get(CD.login_url)
        self.lp = LoginPage(self.driver)

    def tearDown(self) -> None:
        # 关闭浏览器 退出当前会话
        self.driver.quit()

    def test_login_success(self):
        # 步骤
        # 1.登录页面-登录操作
        # lp= LoginPage(self.driver)
        self.lp.login(LD.success_data["username"], LD.success_data["passwd"])  # 初始化类，调用方法传参执行用例步骤
        # 断言
        # 1.URL发生改变(不属于页面行为)
        time.sleep(2)
        self.assertEqual(LD.success_data["check_url"], self.driver.current_url)
        # 2.首页-确认 我的账号 元素存在 (属于页面行为)
        self.assertTrue(HomePage(self.driver).user_is_existed())

    @ddt.data(*LD.wrong_data)
    def test_login_fail(self, case):
        # 步骤
        # lp= LoginPage(self.driver) # 放到setUp中
        self.lp.login(case["username"], case["passwd"])  # 初始化类，调用方法传参执行用例步骤
        # 断言
        self.assertEqual(self.lp.get_error_msg_from_login_form(), case["check"])

    def test_login_fail_pop_up(self):
        # 步骤
        self.lp.login(LD.wrong_passwd["username"], LD.wrong_passwd["passwd"])  # 初始化类，调用方法传参执行用例步骤
        # 断言
        self.assertEqual(self.lp.get_error_msg_from_pop_up(), LD.wrong_passwd["check"])
