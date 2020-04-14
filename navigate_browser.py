from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\shefali\Drivers\chromedriver.exe")
driver.get("http://127.0.0.1:8000/eradicate/")
print(driver.title) # print FACEBOOK
driver.get("https://www.google.com/")
print(driver.title)# print google

#driver.execute_script("window.history.go(-1)")
driver.back()
time.sleep(5)
print(driver.title) # print FACEBOOK

driver.forward()
time.sleep(5)
print(driver.title)# print Google


driver.back()
time.sleep(5)
print(driver.title)
driver.close()


