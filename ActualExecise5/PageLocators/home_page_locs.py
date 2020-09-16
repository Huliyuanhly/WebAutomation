from selenium.webdriver.common.by import By


class HomePageLocs:
    # 退出
    exit = (By.XPATH, "//span//a[text()='退出']")
    # 关于我们
    about_us = (By.XPATH, "//span//a[text()='关于我们']")
    # 用户昵称
    user_nick = (By.LINK_TEXT, "Member/index.html")
    # 抢投标按钮
    bid_button = (By.XPATH, "//a[@class='btn btn-special']")  # 定位出3个，选哪个？
