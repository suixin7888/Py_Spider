#coding=utf-8
import urllib2

user = "suixin"

passwd = "passwd"

server_proxy = "10.0.0.6:7888"

passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

passwdmgr.add_password(None,server_proxy,user,passwd)

#如果是代理需要密码验证，使用下面方法
proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)


#如果是ftp或者http访问需要密码才可以访问，使用下面方法
#proxyauth_handler = urllib2.HTTPBasicAuthHandler(passwdmgr)

opener = urllib2.build_opener(proxyauth_handler)

request = urllib2.Request("http://www.baidu.com")

response = opener.open(request)

print response.read()
