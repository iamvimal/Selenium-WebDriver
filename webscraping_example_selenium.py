from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()

driver.get("https://github.com/yourusername")

timeout = 20
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))

except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

titles_element = driver.find_elements_by_xpath("//a[@class='text-bold']")
titles = [x.text for x in titles_element]

language_element = driver.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
languages = [x.text for x in language_element]

x=1
print("Repo name : Language")
for title,language in zip(titles, languages):
    print(str(x)+"."+title + ": " + language)
    x+=1

