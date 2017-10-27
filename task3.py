# -*- coding:utf-8 -*-

import urllib2,time,re
print "Start : %s" % time.ctime()
url = 'https://www.douban.com/gallery/'

print'----------------第一步，加载网页内容----------------\n\n'
time.sleep(1)

count = 0 
a = 2
while (count < a):
    ncount = a - count 
    print'加载将于',ncount,'秒后开始'
    time.sleep(1)
    count += 1
print '\n\n----------------------加载开始----------------------\n\n' 
time.sleep(1)
r1 =True
while r1:
    try:
        response1 = urllib2.urlopen(url)
        code = response1.getcode()
        read = response1.read()
        print'状态码为',code,'\n加载成功!'
        time.sleep(2)
        print'\n目标网页已存入read变量'
        time.sleep(2)
        r1 = False
        print'\n\n----------------第二步，爬取请求内容----------------\n\n'
        time.sleep(1)

        count = 0 
        a = 2
        while (count < a):
            ncount = a - count 
            print'加载将于',ncount,'秒后开始'
            time.sleep(1)
            count += 1
        print '\n\n----------------------爬取开始----------------------\n\n'
        time.sleep(1)
        p1 = r"(<.+?note-title.+?>).+?(?=</a>)"
        pattern1 = re.compile(p1)
        matcher1 = re.search(pattern1,read)
        a=matcher1.group(0)
        print("话题的标题为:\n",a[106:-1])
        time.sleep(1)

        p2 = "(<.+class=\"time\">>).+?(?=</time>)"      
        pattern2 = re.compile(p2)
        matcher2 = re.search(pattern1,read)
        a=matcher1.group(0)
        print("话题的时间为:\n",a[19:-1])
        time.sleep(1)
        
        p1 = r"(<.+?author.+?>).+?(?=</a>)"
        pattern1 = re.compile(p1)
        matcher1 = re.search(pattern1,read)
        a=matcher1.group(0)
        print("话题的作者为:\n",a[82:-1])
        time.sleep(1)

        p1 = r"(<.+?note-preview-content.+?>).+?(?=</span>)"
        pattern1 = re.compile(p1)
        matcher1 = re.search(pattern1,read)
        a=matcher1.group(0)
        print("话题的概要为:\n",a[35:-1])
        time.sleep(1)
        
        p1 = r"(<.+?like-num.+?>).+?(?=</span>)"
        pattern1 = re.compile(p1)
        matcher1 = re.search(pattern1,read)
        a=matcher1.group(0)
        print("话题的点赞数为:\n",a[23:-1])
        time.sleep(1)
        print '\n\n----------------------爬取完毕----------------------\n\n'
        time.sleep(1)

        count = 0 
        a = 2
        while (count < a):
            ncount = a - count 
            print'程序将于',ncount,'秒后关闭'
            time.sleep(1)
            count += 1
        print'\n\n---------------------程序已被终止--------------------\n\nBy:张义主'


    except:
        print'加载失败，请检查网络及相关设置。'
        r2 = True
        while r2:
            r = raw_input('是否重试? Y or n:\n')
            if r == 'Y':
                r2 = False
                r1 = True
            elif r == 'n':
                r2 = False
                r1 = False
                print'/n---------------------程序已被终止----------------------'
                break
            else:
                print('输入错误，请重新输入！!')
                r2 = True

