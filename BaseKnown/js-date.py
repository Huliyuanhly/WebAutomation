from selenium import webdriver
js_pha = "var a = document.getElementById('train_date');a.readOnly = false;a.value = '2020-10-01';"
js_pha = "var a = document.getElementById('train_date');a.readOnly = false;a.value = 'arguments[0]';"
driver = webdriver.Chrome()
# 获取今天加10天以后日期，转换成xxxx-xx-xx类型的时间戳
driver.execute_script(js_pha)
