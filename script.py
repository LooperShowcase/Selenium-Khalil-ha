from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https://typing-speed-test.aoeu.eu/")


box = browser.find_element(By.XPATH,'//*[@id="words"]')

words = box.find_elements(By.TAG_NAME,"span")

for word in words:
    inp = browser.find_element(By.XPATH,'//*[@id="input"]')
    inp.send_keys(word.text + " ")

