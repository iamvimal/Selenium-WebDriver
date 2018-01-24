from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user="your username here"
password="your password here"

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://facebook.com")
assert "Facebook" in driver.title
field = driver.find_element_by_id("email")
field.send_keys(user)
field = driver.find_element_by_id("pass")
field.send_keys(password)
field.send_keys(Keys.RETURN)

logout1=driver.find_element_by_id("userNavigationLabel")
logout1.click()
logout1 = driver.find_element_by_css_selector("._w0d[action='https://www.facebook.com/logout.php?button_name=logout&button_location=settings']").submit()

#driver.close()