import requests
def download():
    rs = requests.get("https://www.baidu.com/img/bd_logo1.png")
    bs=rs.content
    with open("bd.png","wb") as f:
        f.write(bs)