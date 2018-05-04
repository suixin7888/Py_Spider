#coding=utf-8
import urllib2
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider:
	def	__init__(self):
		"""
		控制开关
		"""
		self.page = 1
		self.switch = True

	def loadpage(self):
		"""
		提取网站第一页的每个帖子的链接
		"""
		print "正在下载数据"
		url = "http://www.zuanke8.com/forum-15-" + str(self.page) + ".html"
		
		headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

		request = urllib2.Request(url,headers = headers)
	
		response = urllib2.urlopen(request)

		html = response.read()

		content = etree.HTML(html)

		content_list = content.xpath('//th[@class="new"]/a/@href')

		for link in content_list:
			self.dealpage(link)

	def dealpage(self,link):
		"""
		把提取的每个链接再进行取楼层文字操作
		"""
		headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
		request = urllib2.Request(link, headers = headers)
		html2 = urllib2.urlopen(request).read()
		content2 = etree.HTML(str(html2))

		link_list = content2.xpath('//td[@class="t_f"]/text()')
		self.writepage(link_list)

	def writepage(self,link_list):
		"""
		写入文件
		"""
		for item in link_list:
			with open("1_zk8.txt", "a") as f:
				f.write(item+'\n')
		with open("1_zk8.txt","a") as f:
			f.write('-----------------------------------------------')
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
