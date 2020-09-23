from selenium.webdriver.remote.webdriver import WebDriver  # driver来历
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActualExecise5.PageLocators.bid_page_loc import BidPageLoc as loc
from ActualExecise5.Common.BasePage import BasePage


class BidPage(BasePage):

    # 获取用户余额
    def get_user_money(self):
        return self.get_text(*loc.money_input, "标页面_用户余额")
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.money_input))
        # return self.driver.find_element(*loc.money_input).get_attribute("data-amount")

    # 获取标的余额
    def get_bid_money(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.bid_left_money_text))
        # return self.driver.find_element(*loc.bid_left_money_text).text
        return self.get_text(*loc.bid_left_money_text, "标页面_获取标金额")

    # 投标
    def invest(self, invest_amount):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.invest_button))
        # self.driver.find_element(*loc.money_input).send_keys(invest_amount)
        # self.driver.find_element(*loc.invest_button).click()
        self.input_text(loc.money_input, invest_amount, "标页面_输入投资金额")
        self.click_element(*loc.invest_button, "标页面_点投标按钮")

    # 点击 投资成功提示框中的 查看并激活
    def click_active_button_in_success_popup(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.pop_up_dialog_after_invest_success))
        # self.driver.find_element(*loc.pop_up_dialog_after_invest_success).click()
        self.click_element(*loc.pop_up_dialog_after_invest_success, "标页面_点击查看并激活")

