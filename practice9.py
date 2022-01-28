from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[value='robots']")
    radiobutton.click()
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()