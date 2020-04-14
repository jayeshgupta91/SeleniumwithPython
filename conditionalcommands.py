from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\shefali\Drivers\chromedriver.exe")
driver.get("http://127.0.0.1:8000/eradicate/")
fname = driver.find_element_by_name("first_name")
print(fname.is_displayed())
print(fname.is_enabled())

lname= driver.find_element_by_name("last_name")
print(lname.is_displayed())
print(lname.is_enabled())

gender_male=driver.find_element_by_css_selector("input[value=M]")
print("male selected" , gender_male.is_selected())

gender_female=driver.find_element_by_css_selector("input[value=F]")
print("female selected" , gender_female.is_selected())
