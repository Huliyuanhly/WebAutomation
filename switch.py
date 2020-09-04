'''
1.你怎么知道自己要切换到哪儿？？
1）有一个行为触发了新的窗口出现
2）获取所有窗口的handles 放在列表里面  按照窗口出现的顺序，最新的窗口是最后一个
3）switch_to.window(新窗口的handle)
    从一个HTML切换到另一个HTML页面
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 开启了与浏览器的会话
driver = webdriver.Chrome()
# 隐性等待 - 1）等待元素被找到 find ele  2）等待命令执行完成   一个session只要调用一次
driver.implicitly_wait(20)
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys("QQ")
driver.find_element_by_id('su').click()  # 点击 百度一下
loc = (By.XPATH, '//a[text()=" - 每一天,乐在沟通"]')
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located(loc))
driver.find_element(*loc).click()  # 打开了新的窗口
time.sleep(1)  # 保证新窗口一定出现
wins = driver.window_handles
print('当前所有的句柄', wins)
# 获取当前窗口的句柄
cur = driver.current_window_handle
print('当前窗口的句柄', cur)
# 切换动作
driver.switch_to.window(wins[-1])
loc = (By.XPATH, '//ul[@id="topNav"]//a[text()="下载"]')
driver.find_element(*loc).click()  # 打开 下载 选项
time.sleep(3)
driver.quit()
