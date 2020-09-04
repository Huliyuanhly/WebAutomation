'''
1.为什么要等待？
元素尚未加载出来，无法操作
1）后台数据请求
2）网络很慢
3）页面渲染
2.如何等待  功能测试-什么时候出现什么时候操作
3种方式
1）time.sleep(指定时间s)
2）智能等待：什么时候出现什么时候就停止等待，到了上限抛出异常timeout
    A:隐性等待 implicity_wait  不能处理存在但是不可见的元素   等url改变也做不了   等Windows新窗口出现也不行
    B:显性等待 ：所有的条件都是明确说明的，等待条件存在之后，在进行后续代码的执行
      等待：WebdriverWait  条件：expected_condition  等待20秒，检测条件是否成立的间隔

3）
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

# 开启了与浏览器的会话
driver = webdriver.Chrome()
# 隐性等待 - 1）等待元素被找到 find ele  2）等待命令执行完成   一个session只要调用一次
driver.implicitly_wait(20)
driver.get("http://www.baidu.com")
# 点击登录链接
loc = (By.XPATH, '//div[@id="u1"]//a[@name="tj_login"')
driver.find_element(*loc).click()
# 最多等20秒
# 元素定位表达式
loc = (By.ID, 'TANGRAM__PSP_11__errorWrapper')
WebDriverWait(driver, 20).until(EC.invisibility_of_element_located(loc))
# 结束会话
driver.quit()
