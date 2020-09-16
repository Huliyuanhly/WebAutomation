from selenium.webdriver.remote.webdriver import WebDriver  # driver来历
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActualExecise4.PageLocators.bid_page_loc import BidPageLoc as loc


class BidPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.money_input))
        return self.driver.find_element(*loc.money_input).get_attribute("data-amount")

    # 获取标的余额
    def get_bid_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.bid_left_money_text))
        return self.driver.find_element(*loc.bid_left_money_text).text

    # 投标
    def invest(self, invest_amount):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.invest_button))
        self.driver.find_element(*loc.money_input).send_keys(invest_amount)
        self.driver.find_element(*loc.invest_button).click()

    # 点击 投资成功提示框中的 查看并激活
    def click_active_button_in_success_popup(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.pop_up_dialog_after_invest_success))
        self.driver.find_element(*loc.pop_up_dialog_after_invest_success).click()

