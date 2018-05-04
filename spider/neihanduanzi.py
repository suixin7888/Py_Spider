#coding=utf-8
import urllib2
import re

class Spider():
	def __init__(self):
		self.page = 1
		self.switch = True
	def loadPage(self):
		print "正在下载数据"	
		url = "http://www.neihan8.com/article/list_5_" + str(self.page) +".html"
		header = {"Mozilla/5.0" : "(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}	
		request = urllib2.Request(url,headers = header)
		response = urllib2.urlopen(request)
		html = response.read()
		pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>',re.S)
		content_list = pattern.findall(html)
		self.dealPage(content_list)
	def dealPage(self,content_list):
		for item in content_list:
			item = item.replace("<p>","").replace("</p>","").replace("&ldquo;","").replace("&rdquo;","").replace("<br />","").replace("&hellip;","")
			self.writePage(item)
		print "正在处理数据"
	def writePage(self,item):
		with open("neihan.txt","a")as f:
			f.write(item.decode("gbk") + "\n" + "------------------------------------")
		print "正在写入数据到文件neihan.txt中"
	def startwork(self):
		while self.switch:
			self.loadPage()
			command = raw_input("您是否要继续爬取，按回车继续")
			if command == "quit":
				self.switch = False
			self.page += 1
		print "谢谢使用"	
if __name__ == "__main__":
	neihan = Spider()
	neihan.startwork()
