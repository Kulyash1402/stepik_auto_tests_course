from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()