from selenium.webdriver.common.by import By


class BidPageLoc:
    # 金额输入框 可用余额 元素
    money_input = (By.XPATH, "//input[contains(@class,'invest-unit-investinput')]")
    # 标的剩余金额文本 元素
    bid_left_money_text = (By.XPATH, "//div[contains(@class,'money_overplus')]//span[text()='剩余：']")
    # 投标按钮 元素
    invest_button = (By.XPATH, "//button[text()='投标']")
    # 投资成功弹出框 查看并激活 元素
    pop_up_dialog_after_invest_success = (By.XPATH, "//div[@class='layui-layer-content']//button[text()='查看并激活']")
    # 投资失败弹出框 提示 元素
    invest_failed_popup = (By.XPATH, "//div[text()='提示']")
    # 关闭失败弹出框 X 元素
    close_failed_popup = (By.XPATH, "/a[contains(@class,'layui-layer-close1')]")
