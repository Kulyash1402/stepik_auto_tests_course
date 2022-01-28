from selenium import webdriver
import os
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Kulyash")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Tleuken")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("2165@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
