# -----------------------------#
# CookieClicker_bot
# Autor: Michal Findra
# Mail: xfindr00@fit.vutbr.cz
# version: 0.3
# -----------------------------#
# to do:
# upgrade clicker
# move cursor randomly on cookie
# use classes instead of hardcode
# change loop for clicking
# random crashes (no log for crash)
# add options to launch script with:
#   -a (amount of cookie clicked between checking accessibility of shop items)(default: 50)
#   -ns (dont generate a file with output)
#   -sc (no upgrade just clicking)
# -----------------------------#
# import modules
from selenium import webdriver
import time
import random
import keyboard

# -----------------------------#
# load Chrome webdriver
browser = webdriver.Chrome()
# -----------------------------#
# load cookieclicker page
browser.get("https://orteil.dashnet.org/cookieclicker/")
# -----------------------------#
# import hash form hash.txt file
setings = browser.find_element_by_xpath('//*[@id="prefsButton"]')
time.sleep(1)
setings = browser.find_element_by_xpath('//*[@id="prefsButton"]')
setings.click()
impo = browser.find_element_by_xpath('//*[@id="menu"]/div[3]/div[3]/a[2]')
impo.click()
# -----------------------------#
# read initial values from hash.txt
f = open("hash.txt", "r")
hashtext = f.read()
f.close()
textarea = browser.find_element_by_xpath('//*[@id="textareaPrompt"]')
textarea.send_keys(hashtext)
importbuttonsend = browser.find_element_by_xpath('//*[@id="promptOption0"]')
importbuttonsend.click()
time.sleep(1)
# -----------------------------#
# import items and get amount and accessibility of individual items
item0button = browser.find_element_by_xpath('//*[@id="product0"]')
item0counter = browser.find_element_by_xpath('//*[@id="productOwned0"]')
state0 = item0button.get_attribute("class")
content0 = item0counter.get_attribute("innerHTML")
content0 = 0 if content0 == "" else int(item0counter.get_attribute("innerHTML"))
item1button = browser.find_element_by_xpath('//*[@id="product1"]')
item1counter = browser.find_element_by_xpath('//*[@id="productOwned1"]')
state1 = item1button.get_attribute("class")
content1 = item1counter.get_attribute("innerHTML")
content1 = 0 if content1 == "" else int(item1counter.get_attribute("innerHTML"))
item2button = browser.find_element_by_xpath('//*[@id="product2"]')
item2counter = browser.find_element_by_xpath('//*[@id="productOwned2"]')
state2 = item2button.get_attribute("class")
content2 = item2counter.get_attribute("innerHTML")
content2 = 0 if content2 == "" else int(item2counter.get_attribute("innerHTML"))
item3button = browser.find_element_by_xpath('//*[@id="product3"]')
item3counter = browser.find_element_by_xpath('//*[@id="productOwned3"]')
state3 = item3button.get_attribute("class")
content3 = item3counter.get_attribute("innerHTML")
content3 = 0 if content3 == "" else int(item3counter.get_attribute("innerHTML"))
item4button = browser.find_element_by_xpath('//*[@id="product4"]')
item4counter = browser.find_element_by_xpath('//*[@id="productOwned4"]')
state4 = item4button.get_attribute("class")
content4 = item4counter.get_attribute("innerHTML")
content4 = 0 if content4 == "" else int(item4counter.get_attribute("innerHTML"))
item5button = browser.find_element_by_xpath('//*[@id="product5"]')
item5counter = browser.find_element_by_xpath('//*[@id="productOwned5"]')
state5 = item5button.get_attribute("class")
content5 = item5counter.get_attribute("innerHTML")
content5 = 0 if content5 == "" else int(item5counter.get_attribute("innerHTML"))
item6button = browser.find_element_by_xpath('//*[@id="product6"]')
item6counter = browser.find_element_by_xpath('//*[@id="productOwned6"]')
state6 = item6button.get_attribute("class")
content6 = item6counter.get_attribute("innerHTML")
content6 = 0 if content6 == "" else int(item6counter.get_attribute("innerHTML"))
item7button = browser.find_element_by_xpath('//*[@id="product7"]')
item7counter = browser.find_element_by_xpath('//*[@id="productOwned7"]')
state7 = item7button.get_attribute("class")
content7 = item7counter.get_attribute("innerHTML")
content7 = 0 if content7 == "" else int(item7counter.get_attribute("innerHTML"))
item8button = browser.find_element_by_xpath('//*[@id="product8"]')
item8counter = browser.find_element_by_xpath('//*[@id="productOwned8"]')
state8 = item8button.get_attribute("class")
content8 = item8counter.get_attribute("innerHTML")
content8 = 0 if content8 == "" else int(item8counter.get_attribute("innerHTML"))
item9button = browser.find_element_by_xpath('//*[@id="product9"]')
item9counter = browser.find_element_by_xpath('//*[@id="productOwned9"]')
state9 = item9button.get_attribute("class")
content9 = item9counter.get_attribute("innerHTML")
content9 = 0 if content9 == "" else int(item9counter.get_attribute("innerHTML"))
item10button = browser.find_element_by_xpath('//*[@id="product10"]')
item10counter = browser.find_element_by_xpath('//*[@id="productOwned10"]')
state10 = item10button.get_attribute("class")
content10 = item10counter.get_attribute("innerHTML")
content10 = 0 if content10 == "" else int(item10counter.get_attribute("innerHTML"))
item11button = browser.find_element_by_xpath('//*[@id="product11"]')
item11counter = browser.find_element_by_xpath('//*[@id="productOwned11"]')
state11 = item11button.get_attribute("class")
content11 = item11counter.get_attribute("innerHTML")
content11 = 0 if content11 == "" else int(item11counter.get_attribute("innerHTML"))
item12button = browser.find_element_by_xpath('//*[@id="product12"]')
item12counter = browser.find_element_by_xpath('//*[@id="productOwned12"]')
state12 = item12button.get_attribute("class")
content12 = item12counter.get_attribute("innerHTML")
content12 = 0 if content12 == "" else int(item12counter.get_attribute("innerHTML"))
item13button = browser.find_element_by_xpath('//*[@id="product13"]')
item13counter = browser.find_element_by_xpath('//*[@id="productOwned13"]')
state13 = item13button.get_attribute("class")
content13 = item13counter.get_attribute("innerHTML")
content13 = 0 if content13 == "" else int(item13counter.get_attribute("innerHTML"))
item14button = browser.find_element_by_xpath('//*[@id="product14"]')
item14counter = browser.find_element_by_xpath('//*[@id="productOwned14"]')
state14 = item14button.get_attribute("class")
content14 = item14counter.get_attribute("innerHTML")
content14 = 0 if content14 == "" else int(item14counter.get_attribute("innerHTML"))
item15button = browser.find_element_by_xpath('//*[@id="product15"]')
item15counter = browser.find_element_by_xpath('//*[@id="productOwned15"]')
state15 = item15button.get_attribute("class")
content15 = item15counter.get_attribute("innerHTML")
content15 = 0 if content15 == "" else int(item15counter.get_attribute("innerHTML"))
item16button = browser.find_element_by_xpath('//*[@id="product16"]')
item16counter = browser.find_element_by_xpath('//*[@id="productOwned16"]')
state16 = item16button.get_attribute("class")
content16 = item16counter.get_attribute("innerHTML")
content16 = 0 if content16 == "" else int(item16counter.get_attribute("innerHTML"))
# -----------------------------#
# click on cookie 50 times then check items accessibility in shop
cookie = browser.find_element_by_xpath('//*[@id="bigCookie"]')
time.sleep(1)
i = 0
while True:
    try:
        cookie.click()
        y = random.random() / 10.0 + 0.05
        time.sleep(y)
        i += 1
        # if "p" is pressed, wait for 10 seconds
        if keyboard.is_pressed("p"):
            time.sleep(10)
        if i == 50:
            if content0 < 7 and "enabled" in state0:
                item0button.click()
                item0counter = browser.find_element_by_xpath('//*[@id="productOwned0"]')
                content0 = int(item0counter.get_attribute("innerHTML"))
                print("clicked")
            if content1 < 7 and "enabled" in state1:
                item1button.click()
                item1counter = browser.find_element_by_xpath('//*[@id="productOwned1"]')
                content1 = int(item1counter.get_attribute("innerHTML"))
            if content2 < 7 and "enabled" in state2:
                item2button.click()
                item2counter = browser.find_element_by_xpath('//*[@id="productOwned2"]')
                content2 = int(item2counter.get_attribute("innerHTML"))
            if content3 < 7 and "enabled" in state3:
                item3button.click()
                item3counter = browser.find_element_by_xpath('//*[@id="productOwned3"]')
                content3 = int(item3counter.get_attribute("innerHTML"))
            if content4 < 7 and "enabled" in state4:
                item4button.click()
                item4counter = browser.find_element_by_xpath('//*[@id="productOwned4"]')
                content4 = int(item4counter.get_attribute("innerHTML"))
            if content5 < 7 and "enabled" in state5:
                item5button.click()
                item5counter = browser.find_element_by_xpath('//*[@id="productOwned5"]')
                content5 = int(item5counter.get_attribute("innerHTML"))
            if content6 < 7 and "enabled" in state6:
                item6button.click()
                item6counter = browser.find_element_by_xpath('//*[@id="productOwned6"]')
                content6 = int(item6counter.get_attribute("innerHTML"))
            if content7 < 7 and "enabled" in state7:
                item7button.click()
                item7counter = browser.find_element_by_xpath('//*[@id="productOwned7"]')
                content7 = int(item7counter.get_attribute("innerHTML"))
            if content8 < 7 and "enabled" in state8:
                item8button.click()
                item8counter = browser.find_element_by_xpath('//*[@id="productOwned8"]')
                content8 = int(item8counter.get_attribute("innerHTML"))
            if content9 < 7 and "enabled" in state9:
                item9button.click()
                item9counter = browser.find_element_by_xpath('//*[@id="productOwned9"]')
                content9 = int(item9counter.get_attribute("innerHTML"))
            if content10 < 7 and "enabled" in state10:
                item10button.click()
                item10counter = browser.find_element_by_xpath(
                    '//*[@id="productOwned10"]'
                )
                content10 = int(item10counter.get_attribute("innerHTML"))
            if content11 < 7 and "enabled" in state11:
                item11button.click()
                item11counter = browser.find_element_by_xpath(
                    '//*[@id="productOwned11"]'
                )
                content11 = int(item11counter.get_attribute("innerHTML"))
            if content12 < 7 and "enabled" in state12:
                item12button.click()
                item12counter = browser.find_element_by_xpath(
                    '//*[@id="productOwned12"]'
                )
                content12 = int(item12counter.get_attribute("innerHTML"))
            if content13 < 7 and "enabled" in state13:
                item13button.click()
                item13counter = browser.find_element_by_xpath(
                    '//*[@id="productOwned13"]'
                )
                content13 = int(item13counter.get_attribute("innerHTML"))
            if content14 < 7 and "enabled" in state14:
                item14button.click()
                item14counter = browser.find_element_by_xpath(
                    '//*[@id="productOwned14"]'
                )
                content14 = int(item14counter.get_attribute("innerHTML"))
            if content15 < 7 and "enabled" in state15:
                item15button.click()
                item15counter = browser.find_element_by_xpath(
                    '//*[@id="productOwned15"]'
                )
                content15 = int(item15counter.get_attribute("innerHTML"))
            if content16 < 7 and "enabled" in state16:
                item16button.click()
                item16counter = browser.find_element_by_xpath(
                    '//*[@id="productOwned16"]'
                )
                content16 = int(item16counter.get_attribute("innerHTML"))
            i = 0
    except:
        break

print("finished without error")
