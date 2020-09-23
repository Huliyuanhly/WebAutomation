"""
登录成功 用例
用例中不出现元素定位和元素操作
"""
from ActualExecise6.PageObjects.home_page import HomePage
import time
from ActualExecise6.TestDatas import login_datas as LD
import pytest


# conftest不用导入

@pytest.mark.usefixtures("init_driver")  # 这个类下面的函数都是这个前置后置
class TestLogin:
    # @pytest.mark.usefixtures("init_driver")  # 执行init_driver的前置后置代码
    def test_login_success(self, init_driver):  # init_driver  = (driver, lp)
        # 步骤
        # 1.登录页面-登录操作
        init_driver[1].login(LD.success_data["username"], LD.success_data["passwd"])  # 初始化类，调用方法传参执行用例步骤
        # 断言
        # 1.URL发生改变(不属于页面行为)
        time.sleep(2)
        assert LD.success_data["check_url"] == init_driver[0].current_url
        # 2.首页-确认 我的账号 元素存在 (属于页面行为)
        assert HomePage(init_driver[0]).user_is_existed() is True

    # @ddt.data(*LD.wrong_data)
    def test_login_fail(self, case):
        # 步骤
        init_driver[1].login(case["username"], case["passwd"])  # 初始化类，调用方法传参执行用例步骤
        # 断言
        assert init_driver[1].get_error_msg_from_login_form() == case["check"]

    def test_login_fail_pop_up(self):
        # 步骤
        init_driver[1].login(LD.wrong_passwd["username"], LD.wrong_passwd["passwd"])  # 初始化类，调用方法传参执行用例步骤
        # 断言
        assert init_driver[1].get_error_msg_from_pop_up() == LD.wrong_passwd["check"]
