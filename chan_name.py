#!/usr/bin/python3

import os,re,sys

'''获取文件夹内文件'''
dl = os.listdir ()

for cl in dl:
    if cl == 'chan_name.py' :
        continue

    if os.path.isdir (cl) == True :
        continue

    chan = re.match ('(.*)\[(.*)\](.*)',cl)
    chan = chan.group(1)+chan.group(3)
    os.rename (cl,chan)
    print (chan)
