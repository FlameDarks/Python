import csv

import requests
from lxml import etree
# def download():
#     rs = requests.get("https://www.baidu.com/img/bd_logo1.png")
#     bs=rs.content
#     with open("bd.png","wb") as f:
#         f.write(bs)
# def download2():
#     rs = requests.get("http://wvioce.spriteapp.cn/voice/2016/0904/57cb989b1e3b4.mp3")
#     bs = rs.content
#     with open("first.mp3","wb") as f:
#         f.write(bs)
# def download4():
#     data={
#         "a":"list",
#         "c":"data",
#         "type":1
#     }
#     rs=requests.get("http://api.budejie.com/api/api_open.php?",params=data)
#     x = rs.json()
#     print(x)
#
# download4()

# def download():
#     for i in range(1,5):
#         rs = requests.get("https://sou.zhaopin.com/?p="+str(i)+"&jl=719&kw=python&kt=3&sf=0&st=0")
#         rs.encoding = "utf-8"
#         bs = rs.content
#         with open("date.txt", "wb") as f:
#             f.write(bs)
# download()
#
# def download():
#     rs = requests.get("http://39.100.133.77/contest/retail/retail_web/product_1.html")
#     rs.encoding="utf-8"
#     return rs.text
# def parse2():
#     doc=download()
#     root=etree.HTML(doc)
#     vs = root.xpath("//table/thead/tr/th/text()")
#     trs=root.xpath("//table/tr")
#     data=[]
#     for tr in trs:
#         ts=tr.xpath("./td/text()")
#         data.append(ts)
#     with open("product.csv","w",newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow(vs)
#         writer.writerows(data)
# parse2()

def download():
     rs = requests.get("http://book.dangdang.com/01.54.htm")
     rs.encoding="utf-8"
     return rs.text
def parse():
    doc = download()
    root = etree.HTML(doc)
    # for i in range(1,6):
    x = root.xpath("//a[@target='_blank']/text()")

    print(str(x).encode(encoding="utf-8"))
parse()