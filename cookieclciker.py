# -----------------------------#
# CookieClicker_bot
# Autor: Michal Findra
# Mail: xfindr00@fit.vutbr.cz
# version: 0.4
# -----------------------------#
# to do:
# upgrade clicker
# move cursor randomly on cookie
# change loop for clicking
# add options to launch program with:
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
# definiton of class shopitem
class shopitem:
    def __init__(self, num):
        self.num = num
        self.buttonn = browser.find_element_by_xpath('//*[@id="product{}"]'.format(num))
        self.counterr = browser.find_element_by_xpath(
            '//*[@id="productOwned{}"]'.format(num)
        )
        self.content = self.counterr.get_attribute("innerHTML")
        # if amount is 0 set 0, default was ""
        self.content = (
            0 if self.content == "" else int(self.counterr.get_attribute("innerHTML"))
        )
        self.state = self.buttonn.get_attribute("class")

    def reinit(self):
        self.content = self.counterr.get_attribute("innerHTML")
        self.content = (
            0 if self.content == "" else int(self.counterr.get_attribute("innerHTML"))
        )


# -----------------------------#
# load Chrome webdriver
def extrct_hash():
    pass


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
items = list()
for i in range(17):
    items.append(shopitem(i))

# click on cookie 50 times then check items accessibility in shop
cookie = browser.find_element_by_xpath('//*[@id="bigCookie"]')
time.sleep(1)
o = 0
while True:
    try:
        cookie.click()
        y = random.random() / 10.0 + 0.05
        time.sleep(y)
        # if "p" is pressed, wait for 10 seconds
        if keyboard.is_pressed("p"):
            time.sleep(10)
        if keyboard.is_pressed("q"):
            break
        length = len(items)
        if o == 50:
            for j in range(length):
                # print("item {} amount is: ".format(j), items[j].content)
                if (items[j].content < 7) and ("enabled" in items[j].state):
                    try:
                        items[j].buttonn.click()
                    except:
                        print("cannont click")
                # check if any element was sold and update number of items - useless
                if items[j].content > 0:
                    items[j].reinit()
                o = 0
        o += 1
    except:
        print("finished by breaking of the loop")
        break
print("finished without error")
