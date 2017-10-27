import urllib.request
from bs4 import BeautifulSoup

class jihe :
    def __init__ (self,soup):
        self.author = soup.find_all ('a',{'class':'author'},limit = number)
        self.time = soup.find_all ('time',{'class':'time'},limit = number)
        self.title = soup.find_all ('a',{'class':'note-title'},limit = number)
        self.note = soup.find_all ('span',{'class':'note-preview-content'},limit = number)
        self.zan = soup.find_all ('span',{'class':'like-num'},limit = number)
        
    def give (self,huati,number):
        huati.title = self.title[number].get_text()
        huati.author = self.author[number].get_text()
        huati.time = self.time[number].get_text()
        huati.note_preview = self.note[number].get_text()
        huati.zan = self.zan[number].get_text()
        
class huati:
    def print_xijie(self):
        print ("-----------------------------------------------------------")
        print ("Title is :%s" % (self.title))
        print ("Author is :%s   Time:%s" % (self.author,self.time))
        print ("概要：%s" % (self.note_preview))
        print ("点赞数：%s" % (self.zan))
        print ("-----------------------------------------------------------")
    

url ="https://www.douban.com/gallery/"

uop = urllib.request.urlopen (url)

data = uop.read()

soup = BeautifulSoup (data,"html.parser",from_encoding = 'utf-8')
number = int(input ("请输入要抓取多少条话题："))

text = jihe(soup)

for n in list(range(number)):
    text0 = huati()
    text.give (text0,n)
    text0.print_xijie()


