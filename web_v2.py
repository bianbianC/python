
#!/usr/bin/python
# -*- coding: UTF-8 -*-
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


url='https://36kr.com/newsflashes'
result=requestHome(url)
savetxt('html.txt',result)


pattern=re.compile(r'{\"id\".*?,\"column_id\".*?,\"post_id\".*?,\"is_top\".*?,\"pin\".*?,(.*?),\"created_at',re.S)
rawlist = pattern.findall(result)

#parse raw list
patitle=re.compile(r'\"title\":\"(.*?)\",',re.S)
padesc=re.compile(r'\"description\":\"(.*?)\",',re.S)
paurl=re.compile(r'\"news_url\":\"(.*?)\",',re.S)
padate=re.compile(r'\"published_at\":\"(.*?)\"',re.S)
# print(rawlist)
# for i in range(len(rawlist)):
#     print (patitle.findall(rawlist[i]))
#     print (padesc.findall(rawlist[i]))
#     print (paurl.findall(rawlist[i]))
#     print (padate.findall(rawlist[i]))

#build data frame
df=pd.DataFrame(columns=('title','desc','url','date'))

dflen=len(df)
for i in range(len(rawlist)):
    title=patitle.findall(rawlist[i])
    desc=padesc.findall(rawlist[i])
    url=paurl.findall(rawlist[i])
    date=padate.findall(rawlist[i])
    df.loc[i+dflen]=[title,desc,url,date]

print(df)
df.to_csv('36kr.csv',header=True, index=True)
