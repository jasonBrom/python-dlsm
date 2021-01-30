# -*- coding: utf-8 -*-


import time
import re
import os


f = open("jg.txt")
line = f.readline()
while line:
    #print line,
    yms=line
    //print(line, end = '')
    line = f.readline()
    if "open" in yms:
       yms = yms.replace("\n","")
       sj = yms.split( )
       wc = sj[3] + ":3128"
       //print("\033[7;32;41m%s\033[0m"%wc)
       with open("wc.txt", "a") as write:
           write.write(wc + "\n")
     
    
    //time.sleep(0.00000001)

f.close()
