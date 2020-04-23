# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys

browser = webdriver.Firefox()
browser.get('https://twitter.com/login')
delay = 3 #seconds

try:
    usern_box = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'session[username_or_email]')))
    usern_box.send_keys(sys.argv[1])
except TimeoutException:
    print('Taking too long to load')

try:
    password_box = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'session[password]')))
    password_box.send_keys(sys.argv[2])
except TimeoutException:
    print('Taking too long to load')
    
try:
    login_btn = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')))
    login_btn.click()
except TimeoutException:
    print('Taking too long to load')

try:
    tweet_box = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'DraftEditor-root')))
    tweet_box.click()
    actions = ActionChains(browser)
    actions.send_keys(sys.argv[3])
    actions.perform()
except TimeoutException:
    print('Taking too long to load')

time.sleep(3)
try:
    tfv_code = browser.find_element_by_id('challenge_response')
    code = input("Enter the code sent to you...")
    tfv_code.send_keys(code)
    browser.find_element_by_id('email_challenge_submit').click()   
except:
    print('No 2-step Verification!')
try:
    tweet_btn = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')))
    #WebDriverWait(browser, delay).until(lambda browser: browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/span/span').text == sys.argv[3])
    tweet_btn.click()
except TimeoutException:
    print('Taking too long to load')
