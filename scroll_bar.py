'''
滚动的目标：让要操作的元素到可视区域
事情：将我要操作的元素，拖动到可视区域 顶部或者底部
js语句：
  很多网站是可以自己滚的
  滚动到可视区域的基本语法：
  element.scrollIntoView();
'''
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id('kw').send_keys("柠檬班", Keys.ENTER)
loc = (By.XPATH, '//a[text()="班的微博_微博"]')
WebDriverWait(driver, 20).until(EC.invisibility_of_element_located(loc))
element = driver.find_element(*loc)
# 通过js语句将元素滚动到可视区域以后，再去点击
# 执行jS语句的函数   argument--列表
driver.execute_script("argument[0].scrollIntoView();", element)
element.click()
time.sleep(10)
driver.quit()

