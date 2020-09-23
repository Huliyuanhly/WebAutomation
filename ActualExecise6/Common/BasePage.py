import logging
from selenium.webdriver.remote.webdriver import WebDriver  # driver来历
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from ActualExecise6.Common.dir_config import pageshots_dir


class BasePage:
    # 会话对象是由用例创建的，因此driver采用外部传参,下面的语句声明了driver来自于Webdriver
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        logging.info("等待{}元素可见".format(loc))
        start_time = datetime.time()  # 开始等待的时间
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
        except:
            # 输出异常信息
            logging.exception("等待元素可见失败")
            # 截图
            self._save_page_shot(img_doc)
            raise
        else:
            end_time = datetime.time()  # 结束等待的时间
            logging.info("起始时间为{},结束时间{},等待时长{}")

    def _save_page_shot(self, img_doc):
        # 截图 命名要见名知意 一看名称就知道在哪个失败截的图
        # img_doc 格式：页面名称_行为名称_年月日时分秒.png
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        file_path = pageshots_dir + "{}_{}.png".format(img_doc, now)
        logging.info("截图保存在：{}".format(file_path))
        try:
            self.driver.save_screenshot(file_path)  # 文件格式名称不要有  ： 空格
        except:
            logging.exception("保存截图失败")
        else:
            logging.info("保存截图成功")

    # 查找元素
    def get_element(self, loc, img_doc):
        logging.info("{}查找{}元素".format(img_doc, loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            # 输出异常信息
            logging.exception("查找元素失败：")  # Error级别
            # 查找失败截图
            self._save_page_shot(img_doc)
            raise
        else:
            return ele

    # 点击操作
    def click_element(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        # 1.元素要可见  2.查找元素  3.元素的操作
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        try:
            logging.info("对{}元素进行点击".format(loc))
            ele.click()
        except:
            logging.exception("点击{}模块的{}元素失败".format(img_doc, loc))
            self._save_page_shot(img_doc)
            raise

    # 输入文本操作
    def input_text(self, loc, text, img_doc, timeout=20, poll_frequency=0.5):
        # 1.等待元素可见 2. 找到元素 3. 输入文本
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        try:
            logging.info("向{}模块下的{}元素输入{}".format(img_doc, loc, text))
            ele.send_keys(text)
        except:
            logging.exception("向{}模块下的{}元素输入{}失败".format(img_doc, loc, text))
            self._save_page_shot(img_doc)
            raise

    # 获取文本操作
    def get_text(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        # 1.等待元素可见 2.找到元素 3.获取文本
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        try:
            logging.info("获取{}模块的{}元素的文本".format(img_doc, loc))
            value = ele.text
        except:
            logging.exception("获取{}模块的{}元素的文本失败".format(img_doc, loc))
            raise
        else:
            return value

    # 获取元素属性
    def get_element_attribute(self, loc, attr_name, img_doc, timeout=20, poll_frequency=0.5):
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(img_doc, loc)
        try:
            logging.info("获取{}模块下的{}元素的属性".format(img_doc, loc))
            value = ele.get_attribute(attr_name)
        except:
            logging.exception("获取{}模块下的{}元素的属性失败".format(img_doc, loc))
            self._save_page_shot(img_doc)
            raise
        else:
            return value

    def get_windows_handles(self):
        logging.info("获取当前打开的所有窗口")
        try:
            wins = self.driver.window_handles
        except:
            pass
        else:
            logging.info("窗口列表为{}".format(wins))
            return wins

    def switch_to_new_window(self):
        time.sleep(2)
        wins = self.get_windows_handles()
        logging.info("切换到最新的窗口{}".format(wins[-1]))
        try:
            self.driver.switch_to.window(wins[-1])
        except:
            pass


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    loc = (By.ID, "kw")
    button_loc = (By.ID, "su")
    bp = BasePage(driver)
    bp.wait_ele_visible(loc, "百度首页搜索输入框", timeout=10)
    bp.input_text(loc, "百度首页输入搜索内容", "柠檬班")
    bp.click_element(button_loc, "点击 百度一下")
    time.sleep(10)
    driver.quit()
