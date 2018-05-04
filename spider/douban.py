#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS(executable_path='/opt/phantomjs/bin/phantomjs')
driver.set_window_size(800, 1000)
driver.get("http://www.douban.com")

# 输入账号密码
driver.find_element_by_name("form_email").send_keys("15937727947")
driver.find_element_by_name("form_password").send_keys("s7758521s")

driver.find_element_by_xpath("//input[@class='bn-submit']").click()

# 等待3秒
time.sleep(10)

# 生成登陆后快照
driver.save_screenshot("douban.png")

#with open("douban.html", "w") as file:
#    file.write(driver.page_source)

driver.quit()
