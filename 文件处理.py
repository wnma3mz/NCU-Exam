#1、文件处理
# -*- coding:utf-8 -*-

import os
import re


path="C:/Users/lenovo\Desktop\考核\Exam"
filelist =os.listdir(path)
for filename in filelist:
    if  os.path.isfile:
    
        oldpath = path +'/'+filename
        file = re.findall('\d+\....',filename)
        if len(file)>0:
            newname = file[0]
            newpath = path + '/' +newname
            os.rename(oldpath,newpath)
                        
    
    
    
