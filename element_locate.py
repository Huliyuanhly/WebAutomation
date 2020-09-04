from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
元素在页面的三种状态：
1)存在:能够找到,不一定可见
2)可见:一定是存在的,然后可见,在浏览器呈现的页面中可以看到它的大小
3)可用:特别关注输入框，按钮
'''
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 按照元素本身来找
# 8个元素定位方式：1类：只按照元素的一个特征来找 2类：多种组合方式：xpath,css选择器
# 单个属性定位：id, name, className, tagName, link,partialLink
# 1.id ：固定不变，动态变化的id
ele = driver.find_element_by_id("kw")  # 找元素
ele.send_keys("柠檬班")
'''
基本操作：click,send_keys,get_attribute,  .text
'''
# 2.tag_name 标签名称
driver.find_element_by_tag_name("input")  # 一个webElement对象
driver.find_elements_by_tag_name("input")  # 列表，所有匹配的元素
# 3.class_name class 属性
driver.find_element_by_class_name("bdsug")
driver.find_elements_by_class_name("bdsug")
# 4.name 属性
driver.find_element_by_name("wd")
driver.find_elements_by_name("wd")
# 5,6. 针对a元素
driver.find_element_by_link_text("更多产品")
driver.find_element_by_partial_link_text("产品")
#  7. xpath
driver.find_element_by_xpath()
driver.find_element(by=By.ID,value=id)
'''
By
ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
'''
'''
绝对定位：以/开头 （不用）
相对定位：相对于谁 以//开通，确认：有还是没有匹配的元素
        //标签名（一级筛选）
        //标签名[@属性名称=值] 
        
        逻辑运算：and or //标签名[@属性名称=值 and @属性名称=值]
        文本定位：//标签名[text()=文本值]
        包含定位：//标签名[contains(@属性，值)]
                //标签名[contains(text()，值))]
        层级定位：//标签名[@属性名称=值] //后代标签名[@属性名称=值] 
'''

