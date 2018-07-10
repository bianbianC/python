#!/usr/bin/python
# -*- coding: UTF-8 -*-
print (u"你好")
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup
import request
import re

def getHtml(url,values):
    user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    headers = {'User-Agent':user_agent}
    data = urllib.parse.urlencode(values)
    response_result = urllib.request.urlopen(url+'?'+data).read()
    html = response_result.decode('utf-8')
    return html


def requestHome(urlinput):
    # print(u"请求数据")
    url = urlinput
    value= {
         'CategoryId':808,
         'CategoryType' : 'SiteHome',
         'ItemListActionName' :'PostList',
         'PageIndex' : index,
         'ParentCategoryId' : 0,
        'TotalPostCount' : 4000
    }
    result = getHtml(url,value)
    return result


url='https://36kr.com/newsflashes'
index=0
result=requestHome(url)
print (result)

soup=BeautifulSoup(result,'html.parser')
all_div=soup.find_all('span',attrs={'class':"title"})
print (all_div)
record=[]
for item in all_div:
	record.append(str(item))
print (record)
test=open('test.txt',"w")
# test.write(','.join(record))
test.write("ds")
test.close()

# print (all_div)
