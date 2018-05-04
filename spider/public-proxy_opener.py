#coding=utf-8
import urllib2

url = "http://www.baiud.com"

httpproxy_handler = urllib2.ProxyHandler({"http" : "10.0.0.6:7888"})
nullpoxy_handler = urllib2.ProxyHandler({})

proxySwitch = True

if proxySwitch:
	opener = urllib2.build_opener(httpproxy_handler)
else:
	opener = urllib2_build_opener(nullproxy_handler)

request = urllib2.Request(url)


#只有opener.open才使用代理
response = opener.open(request)

#全局代理，urlopen也可以使用
#urllib2.install_opener(opener)
#response = urllib2.urlopen(response)

print response.read()

