import requests
def download():
    rs = requests.get("https://www.baidu.com/img/bd_logo1.png")
    bs=rs.content
    with open("bd.png","wb") as f:
        f.write(bs)
def download2():
    rs = requests.get("http://wvioce.spriteapp.cn/voice/2016/0904/57cb989b1e3b4.mp3")
    bs = rs.content
    with open("first.mp3","wb") as f:
        f.write(bs)
def download4():
    data={
        "a":"list",
        "c":"data",
        "type":1
    }
    rs=requests.get("http://api.budejie.com/api/api_open.php?",params=data)
    x = rs.json()
    print(x)

download4()
