# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 08:36:46 2019

@author: ADMIN
"""
import csv
with open('file2.csv','r') as f:
    reader=csv.reader(f)
    your_list=list(reader)
    h=[['0','0','0','0','0','0']]
    for i in your_list:
        print(i)
        if i[-1]=="TRUE":
            j=0
            for x in i:
                if x!="TRUE":
                    if x!=h[0][j] and h[0][j]=='0':
                        h[0][j]=x
                    elif x!=h[0][j] and h[0][j]!='0':
                        h[0][j]='?'
                    else:
                        pass
                    j=j+1
print("Most specific hypothesis")
print(h)
