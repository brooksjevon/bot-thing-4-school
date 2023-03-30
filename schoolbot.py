from selenium import webdriver
from time import sleep

from in_fo import searcher

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://retoolyourschool.com/vote/")

sleep(4)

# search bar
search_bar = driver.find_element('xpath', '/html/body/div[1]/div/div/main/div[2]/div/input')

# input info into search bar
search_bar.send_keys(searcher)

# orange button vote now
sleep(4)
orangebutton = driver.find_element('xpath', '/html/body/div[1]/div/div/main/div[2]/div/ol/li/a')
orangebutton.click()

# jibba jabba uh captha information


# refresh

sleep(10)