from selenium import webdriver
import time
import random
browser = webdriver.Chrome()
browser.get('https://orteil.dashnet.org/cookieclicker/')
cookie = browser.find_element_by_xpath('//*[@id="bigCookie"]')
setings = browser.find_element_by_xpath('//*[@id="prefsButton"]')
for i in range(0, 10):
    cookie.click()
    y = random.random() / 10.0 + 0.05
    time.sleep(y)
setings = browser.find_element_by_xpath('//*[@id="prefsButton"]')
setings.click()
impo = browser.find_element_by_xpath('//*[@id="menu"]/div[3]/div[3]/a[2]')
impo.click()
f = open("hash.txt", "r")
hashtext = f.read()
textarea = browser.find_element_by_xpath('//*[@id="textareaPrompt"]')
textarea.send_keys(hashtext)
importbuttonsend = browser.find_element_by_xpath('//*[@id="promptOption0"]')
importbuttonsend.click()
