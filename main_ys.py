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

def Q2(data):
    pass

def Q3():
    target_raw = urllib.request.urlopen(r'https://www.douban.com/gallery')
    soup = bs4.BeautifulSoup(target_raw.read(),'html.parser')
    topics = soup.findAll('div', {'class': 'topic-item item-note'})
    for item in topics:
        print((item.findAll('a', {'class': 'author'}))[0].get_text()[:-3]) #get author name
        print((item.findAll('time', {'class': 'time'}))[0].get_text()) #get time
        print((item.findAll('div', {'class': 'post-from'}))[0].findAll('a', {'target': '_blank'})[0].get_text()) #get topic
        print((item.findAll('a', {'class': 'note-title'}))[0].get_text()) #get title
        print((item.findAll('span', {'class': 'note-preview-content'}))[0].get_text()) #get text preview
        print('='*40) #division line


if __name__ == '__main__':
    print('currently running Q1')
    Q1('Exam')
    print('currently running Q3')
    Q3()
    print('currently running Q2')
    Q2('Null') #to be finished
