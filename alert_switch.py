''''
弹出框：
HTML弹框：selenium webdriver
非HTML弹框：
alert是什么？ alert confirm prompt
1.某一个行为，触发了alert弹框
2.关闭它
3.继续HTML页面的操作
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 开启了与浏览器的会话
driver = webdriver.Chrome()
driver.get("")  # 写一个有弹框的HTML
#  1.某一个行为，触发了alert弹框
driver.find_element_by_id('').click()
# 2.切换
al = driver.switch_to.alert
# 3.关闭
al.accept()
# al.dismiss()
# al.text
# al.send_keys()
# 4.继续页面操作


