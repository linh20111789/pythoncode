# https://fwt.fialda.com/co-phieu/VHC/giaodich
# from selenium.webdriver.common.by import By

# content = find_element(By.CLASS_NAME, "nav-link active")

# print(content)

# import webdriver
from selenium import webdriver
  
# create webdriver object
driver = webdriver.Chrome()
  

  
# get geeksforgeeks.org
driver.get("https://fwt.fialda.com/co-phieu/VHC/giaodich")
  
# get element 
# element = driver.find_element_by_class_name("nav-link active")
element = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div[4]/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div")

# print complete element
print(element)