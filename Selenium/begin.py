import time
from selenium import webdriver
from keyboard import press

PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://stackoverflow.com/')


search_box = driver.find_element_by_xpath('//*[@id="search"]/div/input')
search_box.send_keys('Python')

time.sleep(5)

press('enter')
