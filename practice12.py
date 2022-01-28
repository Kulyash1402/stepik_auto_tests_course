from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    x_element = browser.find_element_by_css_selector("#num1")
    y_element = browser.find_element_by_css_selector("#num2")
    x = x_element.text
    y = y_element.text
    z = str(int(x) + int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()