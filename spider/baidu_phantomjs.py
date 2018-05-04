#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS(executable_path='/opt/phantomjs/bin/phantomjs')
driver.set_window_size(1120, 550)

driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys(u"python")

driver.find_element_by_id("su").click()

time.sleep(5)

driver.save_screenshot("baidu.png")

driver.quit()
