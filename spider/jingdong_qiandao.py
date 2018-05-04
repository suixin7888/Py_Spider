#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)

driver = webdriver.PhantomJS(desired_capabilities=dcap,executable_path='/opt/phantomjs/bin/phantomjs')
driver.set_window_size(1280, 1024)
driver.get("http://vip.jd.com/home.html")


jumplogin = driver.find_element_by_css_selector("#content > div.login-wrap > div.w > div > div.login-tab.login-tab-r > a")

loginname = driver.find_element_by_id("loginname")
password = driver.find_element_by_id("nloginpwd")
submit = driver.find_element_by_id("loginsubmit")

jumplogin.click()

loginname.send_keys("17317530910")
password.send_keys("Robin@788")
submit.click()
driver.implicitly_wait(8)

if len(driver.find_elements_by_css_selector("body > div.dloor-vip > div.w.clearfix > div.user-welfare > div.sign-in.signed > div.title")):
	print("今日已领取!无需重复领取")
else:
	signsubmit = driver.find_element_by_class_name("icon-sign")
	signsubmit.click()
	print("领取成功!")

# 生成登陆后快照
#driver.save_screenshot("jingdong2.png")
time.sleep(5)
driver.quit()

