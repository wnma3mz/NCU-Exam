#爬虫

import requests
from bs4 import BeautifulSoup as bs

#提取网页内容
url = 'https://www.douban.com/gallery/'
m =requests.get(url)
m.encoding = 'utf-8'
emmmm = m.text

#选择需要内容
soup = bs(emmmm,'html.parser')

author = soup.find_all('a',{'class':'author'})
time = soup.find_all('time',{'class':'time'})
title = soup.find_all('a',{'class':'note-title'})
content = soup.find_all('span',{'class':'note-preview-content'})
good = soup.find_all('span',{'class':'like-num'})


#输出内容
for x in range(len(author)):
    Lx = [title[x].text,time[x].text,author[x].text,content[x].text,good[x].text]
    print(Lx)




