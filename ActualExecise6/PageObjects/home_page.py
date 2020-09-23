"""
home页面元素+操作
"""
from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver  # driver来历
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActualExecise5.PageLocators.home_page_locs import HomePageLocs as loc
from ActualExecise5.Common.BasePage import BasePage


class HomePage(BasePage):
    # 属性
    # 元素 我的账户
    my_user_name = (By.XPATH, '//a[contains(text(),"我的帐户")]')

    # 确认 我的账户 元素是否存在
    def user_is_existed(self):
        """

        :return: True 存在 False 不存在
        """
        try:
            # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.my_user_name))
            self.wait_ele_visible(self.my_user_name, "我的账户名")
        except:
            return False
        else:
            return True

    # 点击第一个标
    def click_first_bid(self):
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.bid_button))
        # self.driver.find_element(*loc.bid_button).click()
        self.click_element(*loc.bid_button, "首页_点击第一个标")

