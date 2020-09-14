"""
home页面元素+操作
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver  # driver来历
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActualExecise3.PageLocators.home_page_locs import HomePageLocs as loc


class HomePage:
    # 属性
    # 元素 我的账户
    my_user_name = (By.XPATH, '//a[contains(text(),"我的帐户")]')

    # 会话对象是由用例创建的，因此driver采用外部传参,下面的语句声明了driver来自于Webdriver
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 确认 我的账户 元素是否存在
    def user_is_existed(self):
        """

        :return: True 存在 False 不存在
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.my_user_name))
        except:
            return False
        else:
            return True

    # 点击第一个标
    def click_first_bid(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.bid_button))
        self.driver.find_element(*loc.bid_button).click()
