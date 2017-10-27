#-*- coding: UTF-8 -*-

import os,sys,re

from os.path import join
 

dest = "F:\exam\Exam"
for root, dirs, files in os.walk( dest ):
    for OneFileName in files :
        if OneFileName.find( '.txt' ) == -1 :
            continue
        OneFullFileName = join( root, OneFileName )
        pattern = re.compile('\[\\w*\]')
        match = pattern.search(OneFileName)
        a = match.group()
        b =(a[1:-1])
        os.rename(OneFullFileName ,b+".txt")
