from python import method
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = test_data.data["url"]
username = test_data.data["username"]
password = test_data.data["password"]
key = test_data.data["key"]
num = method.sear_fun(driver,url,username,password,key)
if key in num:
    print("通过")
else:
    print("no")