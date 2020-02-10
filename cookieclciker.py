#-----------------------------#
# Cookie_clicker bot
# Autor: Michal Findra
# Mail: xfindr00@fit.vutbr.cz
# version: 0.2
#-----------------------------#

#import modules
from selenium import webdriver
import time
import random
import keyboard
#-----------------------------#
#load Chrome webdriver
browser = webdriver.Chrome()
#-----------------------------#
#load cookieclicker page
browser.get('https://orteil.dashnet.org/cookieclicker/')
#-----------------------------#
#import hash form hash.txt file
setings = browser.find_element_by_xpath('//*[@id="prefsButton"]')
time.sleep(1)
setings = browser.find_element_by_xpath('//*[@id="prefsButton"]')
setings.click()
impo = browser.find_element_by_xpath('//*[@id="menu"]/div[3]/div[3]/a[2]')
impo.click()
f = open("hash.txt", "r")
hashtext = f.read()
f.close()
textarea = browser.find_element_by_xpath('//*[@id="textareaPrompt"]')
textarea.send_keys(hashtext)
importbuttonsend = browser.find_element_by_xpath('//*[@id="promptOption0"]')
importbuttonsend.click()
#-----------------------------#
#click on cookie until q key is pressed, error if other key is pressed is not shown
cookie = browser.find_element_by_xpath('//*[@id="bigCookie"]')
while True:
    try:
        cookie.click()
        y = random.random() / 10.0 + 0.05
        time.sleep(y)
        if keyboard.is_pressed('q'):
            break
    except:
        break
#-----------------------------#
'''
shopitem1 = browser.find_elements_by_xpath('//*[@id="product0"]')
shopitem1.click()
'''
