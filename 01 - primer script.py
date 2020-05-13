from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("unsj")
elem.send_keys(Keys.ENTER)
assert "asdasd" in driver.page_source
driver.close()
