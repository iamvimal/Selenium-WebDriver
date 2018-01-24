from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Creating a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

#Navigating to the homepage
driver.get("http://google.co.in")

#Getting the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

#Enter the search keyword and submit
search_field.send_keys("vimal shetty")
search_field.submit()

#Get the list of elements obtained after searching
lists = driver.find_elements_by_class_name("_Rm")

#Display the number of elements found
print("Found: "+str(len(lists))+" results")

#Iterating and printing each search result
i=0
for listitems in lists:
    print(listitems)
    i=i+1
    if(i>10):
        break

driver.quit()