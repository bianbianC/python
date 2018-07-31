#!/usr/bin/python
# -*- coding: UTF-8 -*-
print (u"你好")
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup
import request
import re

import pandas as pd 
from pandas import Series
import math

def getHtml(url,values):
    user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    headers = {'User-Agent':user_agent}
    data = urllib.parse.urlencode(values)
    response_result = urllib.request.urlopen(url+'?'+data).read()
    html = response_result.decode('utf-8')
    return html


def requestHome(urlinput):
    # print(u"请求数据")
    index=0
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


def savetxt(filename,content):
    file=open(filename,'w',encoding='utf-8')
    file.write(content)
    file.close()

url='https://36kr.com/newsflashes'
result=requestHome(url)
savetxt('html.txt',result)
# print (result)


#################### beautiful soup doesn't work since embeded in javascript
# soup=BeautifulSoup(result,'html.parser')
# # print (soup.prettify())
# all_div=soup.find_all('span')
# # ,attrs={'class':'title'})
# print (all_div)
# record=[]
# for item in all_div:
# 	record.append(str(item))
# print (record)
# test=open('test.txt',"w")
# # test.write(','.join(record))
# test.write("ds")
# test.close()

# print (all_div)

####################reglar expression################
# pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
pattern=re.compile(r'is_top\":\"0\",\"pin\":\"0\",\"title\":\"(.*?)\",\"catch_title',re.S)
title_list = pattern.findall(result)
# print(title_list) 

# print (len(title_list))

pattern=re.compile(r'catch_title\":\"\",\"description\":\"(.*?)\",\"cover\":',re.S)
content_list = pattern.findall(result)
# print(content_list) 

pattern=re.compile(r'\"news_url\",\"news_url\":\"(.*?)\",',re.S)
url_list = pattern.findall(result)
# print(url_list) 


df=pd.DataFrame(columns=('title','description','link'))
print (df)
print (len(df))
print (df.columns.size)

insert_len=len(title_list)
print (insert_len)
print (title_list[10])
print (content_list[10])
print (url_list)

df_len=len(df)


# df['title'][0]='test'
for i in range(insert_len):
    print (df_len,i,title_list[i])
    df.loc[df_len+i]=(title_list[i],content_list[i],url_list[i])
    # df.insert(title_list[i],content_list[i],url_list[i])
print ("after")
print (df)