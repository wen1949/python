#coding=utf-8

from urllib.request import Request,urlopen
import urllib.request
#   response = urllib.request.urlopen('http://movie.douban.com/',None,2)
#   老方法已经被网站的烦爬虫机制阻挡，应使用新的方法
#   html = response.read().decode('utf8')

"""新方法是打开网址按F12找到网页请求头,找到User-Agent"""

url ='https://m.douban.com/movie/'
headers ={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36"}
#   注意"User-Agent": "Mozilla/5.0 ......中的"号，复制粘贴易出错，运行时报错

ret =Request(url,headers=headers)
respons =urlopen(ret)
print(respons)
html =respons.read().decode('utf8')

f = open('html.txt','w',encoding='utf8')
f.write(html)
f.close()