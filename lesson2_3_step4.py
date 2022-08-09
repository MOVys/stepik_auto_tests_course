from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "http://suninjuly.github.io/alert_accept.html"	

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

try:
    browser = webdriver.Chrome()
    browser.get(link)	#Открыть страницу 
    #input1 = browser.find_element(By.NAME, "firstname")
    #input1.send_keys("Marina")	#Заполнить текстовые поля: имя, фамилия, email
    #input2 = browser.find_element(By.NAME, "lastname")
    #input2.send_keys("Vysotskaya")	#Заполнить текстовые поля: имя, фамилия, email
    #input3 = browser.find_element(By.NAME, "email")
    #input3.send_keys("vippmar@gmail.com")	#Заполнить текстовые поля: имя, фамилия, email
    #current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    #file_path = os.path.join(current_dir, 'file.txt')	# добавляем к этому пути имя файла
    #element = browser.find_element(By.ID, "file")	#ищем элемент, куда заслать файл
    #element.send_keys(file_path)
    button = browser.find_element("xpath", "//button[@type='submit']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
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
    

#На новой странице решить капчу для роботов, чтобы получить число с ответом

