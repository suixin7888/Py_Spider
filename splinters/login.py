#coding=utf-8
from splinter import Browser
import datetime

def login():
	browser = Browser()
	browser.visit("http://passport.cnblogs.com/user/signin")
	print("title:"%browser.title)
	browser.find_by_id("input1").fill(username)
	browser.find_by_id("input2").fill(username)
	browser.find_by_id("signin").fill(username)
	time.sleep(5)
	if browser.windows[0].title == "":
		print("登录成功")
	else:
		print("登录失败")

login()
