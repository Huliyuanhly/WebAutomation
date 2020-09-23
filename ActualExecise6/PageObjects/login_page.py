"""登录页面元素+操作"""
from selenium.webdriver.remote.webdriver import WebDriver  # driver来历
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActualExecise5.PageLocators.login_page_locs import LoginPageLoc as loc
from ActualExecise5.Common.BasePage import BasePage


class LoginPage(BasePage):

    # 登录行为
    def login(self, username, passwd):
        #     # 等待按钮出现
        #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.login_button))
        #     # 输入用户名
        #     self.driver.find_element(*loc.user_input).send_keys(username)
        #     self.driver.find_element(*loc.password_input).send_keys(passwd)
        #     self.driver.find_element(*loc.login_button).click()
        self.input_text(loc.user_input, username, "登陆页面输入用户名")
        self.input_text(loc.password_input, passwd, "登陆页面输入密码")
        self.click_element(loc.login_button, "登陆页面点击登录按钮")

    # 获取 登录表单区域的错误提示信息
    def get_error_msg_from_login_form(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.error_from_login_form))
        # 返回错误文本信息
        return self.get_text(loc.error_from_login_form, "登录页面获取登陆表单区域上的错误提示信息")

    def get_error_msg_from_pop_up(self):
        return self.get_text(loc.error_pop_up, "登录页面获取弹出区域错误提示信息")
