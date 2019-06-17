#!/user/bin/env python
# -*- coding:utf-8 -*-

# 不可以用
import requests
from bs4 import BeautifulSoup

response  = requests.get(
    url = 'https://v3.bootcss.com/components/'
)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text,'html.parser')
web = soup.find(attrs={'id':'web-application'})

icon_list = []

for item in web.find_all(attrs={'class':'glyphicon'}):
    tag = item.find('i')
    class_name = tag.get('class')[1]
    icon_list.append([class_name,str(tag)])

print(icon_list)