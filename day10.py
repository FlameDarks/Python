import time

from selenium import webdriver

def abc():
    a = webdriver.Chrome()
    a.get("http://localhost:8080")
    time.sleep(10)
    print(a.page_source)
abc()