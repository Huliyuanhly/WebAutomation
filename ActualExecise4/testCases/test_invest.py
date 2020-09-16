"""
!!!!断言部分完成
投资 用例
用例中不出现元素定位和元素操作
"""
import unittest
from selenium import webdriver
from ActualExecise4.PageObjects.login_page import LoginPage
from ActualExecise4.PageObjects.home_page import HomePage
from ActualExecise4.PageObjects.bid_page import BidPage
from ActualExecise4.PageObjects.my_account_page import MyAccountPage
import time
import ddt
from ActualExecise3.TestDatas import Common_datas as CD
from ActualExecise3.TestDatas import login_datas as LD


class TestInvest(unittest.TestCase):

    def setUp(self) -> None:
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 登录
        self.driver.get(CD.login_url)
        LoginPage(self.driver).login(CD.user, CD.passwd)
        # 调用接口--加标--用户充值

    def tearDown(self) -> None:
        # 关闭浏览器 退出当前会话
        self.driver.quit()

    def test_invest_success(self):
        """
        投资正向场景--投资成功，投资金额固定为20000
        :return:
        """
        # 步骤
        # 1.首页选择第一个标
        HomePage(self.driver).click_first_bid()
        # 2.标页面 - 获取输入框中投资前的用户余额
        bp = BidPage(self.driver)
        user_money_before_invest = bp.get_user_money()
        # 3.获取标剩余可投资金额
        bid_money_before_invest = bp.get_bid_money()
        # 4.标页面输入20000，点击投标
        bp.invest(20000)
        # 5.标页面 - 成功弹出框，点击查看并激活
        bp.click_active_button_in_success_popup()
        # 断言
        # 1.用户余额少了20000
        left_money_after_invest = MyAccountPage(self.driver).get_current_user_left_money()
        invest_amount = left_money_after_invest - user_money_before_invest
        self.assertEqual(invest_amount, 20000)
        # 2.个人页面 - 用户当前余额
        # 3.个人页面回退到上一页，刷新
        self.driver.back()
        # 4.标页面 - 标的可投资余额减少20000
        bid_money_after_bid = bp.get_bid_money()
        bid_money = bid_money_after_bid - bid_money_after_bid
        self.assertEqual(bid_money, 20000)
