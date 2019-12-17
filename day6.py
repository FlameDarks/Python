# import time
# from threading import Thread
# def sum(x,y):
#     time.sleep(5)
#     print("在子线程中执行",x+y)
# print("线程执行之前")
# t=Thread(target=sum,args=(3,4))
# t.start()
# print("线程执行之后")

# def write():
#     f = open("data.txt","a")
#     f.write("abc")
#     f.close()
# write()

# def read():
#     f = open("data.txt","r",encoding="utf-8")
#     s = f.read(2)
#     print(s)
#     f.close()
# read()

import requests
from lxml import etree
def download():
    rs = requests.get("http://www.baidu.com")
    rs.encoding="utf-8"
    return rs.text
def parse():
    doc=download()
    root=etree.HTML(doc)
    v = root.xpath("//title/text()")
    save(v[0])
def save(v):
    with open("data.txt","w")as f:
        f.write(v)
parse()