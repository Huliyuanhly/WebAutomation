'''
1.确认自己要操作的元素，是否在iframe中？
F12，定位元素后，看上方完整的元素路径是否有iframe或者两个以上的HTML
2.iframe是个元素，主HTML来讲，仍然是可以通过元素定位来找到的
1）name属性
2）index下标：从0开始
3）webElement对象
driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 开启了与浏览器的会话
driver = webdriver.Chrome()
# 切换
driver.switch_to.frame()
# 切换之后，新的HTML才是根节点
# 一次回到默认的主HTML
driver.switch_to.default_content()
# 切换回上一层iframe
driver.switch_to.parent_frame()
# 若要退出iframe,
'''
登录课堂派试试，补全代码
'''