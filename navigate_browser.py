from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\shefali\Drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")
print(driver.title) # print FACEBOOK
driver.get("https://www.netflix.com/")
print(driver.title)# print NETFLIX

driver.back()
print(driver.title) # print FACEBOOK

time.sleep(5)
driver.forward()
print(driver.title)# print NETFLIX

time.sleep(5)
driver.back()
print(driver.title)
driver.close()


