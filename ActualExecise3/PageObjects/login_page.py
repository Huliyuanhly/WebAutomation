"""登录页面元素+操作"""
from selenium.webdriver.remote.webdriver import WebDriver  # driver来历
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ActualExecise3.PageLocators.login_page_locs import LoginPageLoc as loc


class LoginPage:

    # 会话对象是由用例创建的，因此driver采用外部传参,下面的语句声明了driver来自于Webdriver
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 登录行为
    def login(self, username, passwd):
        # 等待按钮出现
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.login_button))
        # 输入用户名
        self.driver.find_element(*loc.user_input).send_keys(username)
        self.driver.find_element(*loc.password_input).send_keys(passwd)
        self.driver.find_element(*loc.login_button).click()

    # 获取 登录表单区域的错误提示信息
    def get_error_msg_from_login_form(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.error_from_login_form))
        # 返回错误文本信息
        return self.driver.find_element(*loc.error_from_login_form).text

    def get_error_msg_from_pop_up(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.error_pop_up))
        return self.driver.find_element(*loc.error_pop_up).text
