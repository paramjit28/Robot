from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import sys, time

import time


class new:
            
    def sprint(str):
        for c in str + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.1)

    def browser():
        browser = webdriver.Chrome() 
        browser.get('https://www.google.com/')
        time.sleep(10)

    def youtube():
        site = 'https://www.youtube.com/results?search_query='
        name = input("What would you like to search for: ")
        browser = webdriver.Chrome()
        browser.get(site + name)
        print('Please click on the link: ' + browser.current_url)
        time.sleep(50)
       
        
        

    def amazon():
        browser = webdriver.Chrome() 
        browser.get('https://www.amazon.com/')


    def weather():
        browser = webdriver.Chrome()
        browser.get('https://www.google.com/search?q=houston+weather&oq=houston+weather&aqs=chrome..69i57j69i60l3.1896j0j4&sourceid=chrome&ie=UTF-8')
            
        

