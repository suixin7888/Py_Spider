#coding=utf-8

import urllib
import urllib2
from lxml import etree

def loadPage(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	html = response.read()
	content = etree.HTML(html)
	link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
	for link in link_list:
		fulllink = "http://tieba.baidu.com" + link
		imagePage(fulllink)

def imagePage(link):
	headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
	request = urllib2.Request(link, headers = headers)
	html = urllib2.urlopen(request).read()
	content = etree.HTML(html)
	link_list = content.xpath('//img[@class="BDE_Image"]/@src')
	for link in link_list:
		writePage(link)		

def writePage(link):
	headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
	request = urllib2.Request(link, headers = headers)
	image = urllib2.urlopen(request).read()
	filename = link[-10:]
	with open(filename, "wb")as f:
		f.write(image)
	print "已经成功下载" + filename

def tiebaSpider(url,beginPage,endPage):
	for page in range(beginPage, endPage + 1):
		pn = (page - 1) * 50
		fullurl = url + "&pn=" + str(pn)
		loadPage(fullurl)

if __name__ == "__main__":
	kw = raw_input("请输入要爬取的贴吧名：")
	beginPage = int(raw_input("请输入起始页:"))
	endPage = int(raw_input("请输入结束页:"))

	url = "http://tieba.baidu.com/f?"
	key = urllib.urlencode({"kw" : kw})
	fullurl = url + key
	tiebaSpider(fullurl,beginPage,endPage) 
