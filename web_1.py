from selenium import webdriver
import time

# 打开对应的浏览器，开启与浏览器的对话
# 非常干净的浏览器，没有任何用户数据
driver = webdriver.Chrome()  # 调用了接口：newsession

# jsonwireProtocol
# 打开网页
driver.get("http://www.baidu.com")  # driver代表了当前打开的浏览器
driver.maximize_window()  # 浏览器最大化
driver.get("http://www.taobao.com")  # 第二个页面
# 后退
driver.back()  # 历史记录
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
# driver.set_window_size() #设置浏览器大小
driver.close()  # 关闭当前窗口
driver.quit()  # 退出会话，关闭浏览器
