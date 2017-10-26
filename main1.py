import os
import shutil
import random
import string


"""
当前目录下生成Exam文件夹
在Exam文件夹下生成随机个数的txt文件，和一个随机名字的文件夹
随机名字的文件夹中，也有随机个数的txt文件
要求：
去除所有文件名[]中的内容（包括[]）
使用正则表达式
提示：
使用os、re模块
不需要考虑重名情况
注意：
所有文件的名字，长度不确定
"""

chars = string.ascii_uppercase + string.digits + string.ascii_lowercase

def new_dir():
    try:
        shutil.rmtree('Exam')
    except:
        pass
    os.mkdir('Exam')
    os.chdir('Exam')

def new_file(path):
    os.chdir(path)
    for num in range(random.randint(8, 12)):
        filename = '[' + ''.join(random.choice(chars) for _ in range(random.randint(10, 24))) + ']%d.txt' % num
        f = open('%s' % filename, 'w')



if __name__ == '__main__':
    new_dir()
    os.mkdir(''.join(random.choice(chars) for _ in range(random.randint(10, 24))))
    new_file('.')   
    name = [item for item in os.listdir() if os.path.isdir(item)][0]
    new_file(name)
