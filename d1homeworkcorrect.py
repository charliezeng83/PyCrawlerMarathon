#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 01:26:49 2020

@author: charliezeng
"""

#簡答題：檔案與api去得資料的方式是由資料提供者主動提供，爬蟲則是由取得資料者透過開放的資料自行(被動)取得。

#下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
import urllib #retrieve取回、找回
import os

urllib.request.urlretrieve("https://www.w3.org/TR/PNG/iso_8859-1.txt","./Homework2.txt") #在檔名前面加上./不會影響檔案的命名


#檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
first=os.listdir("./") #會列出所有./後接的檔案與目錄
for file in first:
    first=first
print(first)
    
#將「Hello World」字串覆寫到 Homework.txt 檔案
with open("Homework2.txt",mode="w",encoding="utf-8") as second:
    second.write("Hello World")


#檢查 Homework.txt 檔案字數是否符合 Hello World 字數
with open("Homework2.txt",mode="r",encoding="utf-8") as third:
    forth=third.read()

if len("Hello world")==len(forth):
    print("correct")
else:
    print("wrong")
        

