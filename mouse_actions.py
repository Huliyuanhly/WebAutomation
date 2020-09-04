'''
actionChains 类
点击
双击
悬浮
右键 context_click
拖拽
暂停 pause
1)要操作的动作放在 列表中
2）调用perform（） 去执行动作
'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

# 开启了与浏览器的会话
driver = webdriver.Chrome()
# 隐性等待 - 1）等待元素被找到 find ele  2）等待命令执行完成   一个session只要调用一次
driver.get("http://www.baidu.com")
driver.maximize_window()
# 设置 元素
loc = (By.XPATH, '//*[@id="s-usersetting-top"]')
# 1.实例化actionChains类
ac = ActionChains(driver)
# 2.要操作的行为放到列表中
ele = driver.find_element(*loc)
ac.move_to_element(ele).pause(0.5).click(ele)
# 3.调用perform()去执行动作
ac.perform()
# 等待  高级搜索  出现
loc = (By.XPATH, '//a[text()="高级搜索"]')
WebDriverWait(driver, 20).until(EC.invisibility_of_element_located(loc))
driver.find_element(*loc).click()
# select 下拉列表：select/option成对出现
# 1)实例化select类
loc = (By.XPATH, '//select[@name="ft"]')
WebDriverWait(driver, 20).until(EC.invisibility_of_element_located(loc))
select_ele = driver.find_element(*loc)
s = Select(select_ele)
# 2)使用它提供的选择方法，选择下拉列表的值
'''
1.下标       s.select_by_index()
2.文本       s.select_by_visible_text()
3.value      s.select_by_value()
'''
s.select_by_index(6)
time.sleep(10)
s.select_by_visible_text("")
time.sleep(10)
s.select_by_value("ppt")
driver.quit()
