from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\shefali\Drivers\chromedriver.exe") # chrome driver
driver.get("https://www.youtube.com/") # open website on chrome
print(driver.title)  # to get the title of the website
print(driver.current_url)  # to get the url of the website
driver.find_element_by_xpath("//*[@id='text']").click() # to get the button xpath
time.sleep(2)
driver.close()
