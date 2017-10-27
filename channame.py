#!/usr/bin/python
'''#!/usr/bin/python3 本机修改了，顾用python'''

import re,os

dirls = os.listdir()

for dirna in dirls:
    chana = re.match (r'*[*]*',dirna)
    #os.rename (dirna,chana)
    print ("%s 的名字改为了：%s" %(dirna,chana)

