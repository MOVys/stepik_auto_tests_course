from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "http://suninjuly.github.io/file_input.html"	 

try:
    browser = webdriver.Chrome()
    browser.get(link)	#Открыть страницу 
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Marina")	#Заполнить текстовые поля: имя, фамилия, email
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Vysotskaya")	#Заполнить текстовые поля: имя, фамилия, email
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("vippmar@gmail.com")	#Заполнить текстовые поля: имя, фамилия, email
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')	# добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file")	#ищем элемент, куда заслать файл
    element.send_keys(file_path)
    button = browser.find_element("xpath", "//button[@type='submit']")
    button.click()

    

finally:
    time.sleep(60)
    browser.quit()
    

