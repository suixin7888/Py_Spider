#coding=utf-8
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider:
	def	__init__(self):
		
		self.page = 1
		self.switch = True

	def loadpage(self):
		"""
			下载页面
		"""
		print "正在下载数据"
		url = "http://www.neihan8.com/article/list_5_" + str(self.page) + ".html"
		
		headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

		request = urllib2.Request(url,headers = headers)
	
		response = urllib2.urlopen(request)

		html = response.read()

#		print html
		
		pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)

		content_list = pattern.findall(html)
		
		self.dealpage(content_list)

	def dealpage(self,content_list):
		"""
		处理模块
		"""
		for item in content_list:
			item = item.replace("<p>", "").replace("</p>", "").replace("<br>", "").replace("<br />","").replace("&ldquo;","").replace("&rdquo;","").replace("&hellip","")

#			print item.decode("gbk")
			self.writepage(item)

		print "正在写入数据"
	def writepage(self,item):
		"""
		写入文件
		"""
		with open("suixin.txt", "a") as f:
			f.write(item.decode("gbk"))

	def startwork(self):
		"""
		控制开关
		"""
		while self.switch:
			self.loadpage()
			command = raw_input("是否还要继续爬取，按回车继续(quit退出)")
			if command == "quit":
				self.switch = False
			
			self.page += 1			
		print "thanks use"


if __name__ == "__main__":
	duanzispider = Spider()
	duanzispider.startwork()
