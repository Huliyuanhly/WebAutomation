from selenium import webdriver
import time
from_station_js = 'var a = document.getElementById("fromStationText");a.value = "苏州";'
to_station_js = 'var b = document.getElementById("toStationText");b.value = "北京";'
start_date_js = 'var c = document.getElementById("train_date");c.readOnly = false;c.value = "2020-10-01";'
choose_high_speed_train_js = 'var  d= document.getElementById("isHighDan"); d.class = "active";'
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/")
driver.implicitly_wait(10)
driver.execute_script(from_station_js)
driver.execute_script(to_station_js)
driver.execute_script(start_date_js)
# driver.execute_script(choose_high_speed_train_js)
