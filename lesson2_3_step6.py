from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "http://suninjuly.github.io/redirect_accept.html"	

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

try:
    browser = webdriver.Chrome()
    browser.get(link)	#Открыть страницу 
    button = browser.find_element("xpath", "//button[@type='submit']")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    #confirm = browser.switch_to.alert
    #confirm.accept()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()    
    

finally:
    time.sleep(60)
    browser.quit()
    

