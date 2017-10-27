#! /usr/bin/python3

import urllib.request
import chardet
import pymysql
import bs4
import os 
import re


def Q1(path):
    filelist = os.listdir(path)
    for item in filelist:
        if os.path.isfile(path + os.sep + item):
            if re.search('\[.*\]',item):
                os.rename(path + os.sep + item, path + os.sep + re.sub('\[.*\]','',item))
        else:
            Q1(path + os.sep + item)

def Q2():
    conn = pymysql.connect(user='exam',password='exam@lu',database='exam',host='182.254.242.102', charset = 'utf8')
    curr = conn.cursor()
    start = curr.execute('SELECT * FROM ys')
    for item in tosql:
        pack=[item + start]
        pack.extend(list(tosql[item]))
        curr.execute('INSERT INTO ys (id, author_name, time, topic, title, text) VALUES (%s,%s,%s,%s,%s,%s)', tuple(pack))
        conn.commit()
    conn.close()

def Q3():
    target_raw = urllib.request.urlopen(r'https://www.douban.com/gallery')
    soup = bs4.BeautifulSoup(target_raw.read(),'html.parser')
    topics = soup.findAll('div', {'class': 'topic-item item-note'})
    global tosql
    tosql={}
    num = 1
    for item in topics:
        authname = '\'' + (item.findAll('a', {'class': 'author'}))[0].get_text() + '\'' #get author name
        time = '\'' + (item.findAll('time', {'class': 'time'}))[0].get_text() + '\'' #get time
        topic = '\'' + (item.findAll('div', {'class': 'post-from'}))[0].findAll('a', {'target': '_blank'})[0].get_text() + '\'' #get topic
        title = '\'' + (item.findAll('a', {'class': 'note-title'}))[0].get_text() + '\'' #get title
        prvw = '\'' + (item.findAll('span', {'class': 'note-preview-content'}))[0].get_text() + '\'' #get text preview
        tosql[num] = (authname, time, topic, title, prvw)
        print('%s\n%s\n%s\n%s\n%s\n' % (authname, time, topic, title, prvw))
        print('='*40)
        num = num+1


if __name__ == '__main__':
    print('currently running Q1')
    Q1('Exam')
    print('currently running Q3')
    Q3()
    print('currently running Q2')
    Q2() #to be finished
