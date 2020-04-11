from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\shefali\Drivers\chromedriver.exe") # chrome driver
driver.get("https://www.netflix.com/") # open website on chrome
print(driver.title)  # to get the title of the website
print(driver.current_url)  # to get the url of the website
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='appMountPoint']/div/div/div/div/div/div[1]/div/a").click() # to get the button xpath
time.sleep(5)
driver.close()
