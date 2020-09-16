from selenium.webdriver.remote.webdriver import WebDriver  # driver来历
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActualExecise3.PageLocators.my_account_page_locs import MyAccountPageLocs as loc


class MyAccountPage:

    # 会话对象是由用例创建的，因此driver采用外部传参,下面的语句声明了driver来自于Webdriver
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 获取当前用户可用余额
    def get_current_user_left_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.left_money))
        return self.driver.find_element(*loc.left_money).text
