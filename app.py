from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class TwitterBot:
    def __init__(self,username,password): #using __init__ is like a constructor
        #You can get access to the datafields by calling self.(data)
        self.username = username # Don't push these to git
        self.password = password
        self.bot = webdriver.Firefox() #Make sure you have firefox installed

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3) # lets the twitter page load up

ellis = TwitterBot('angelwithashotgun4348@gmail.com', 'passwordBOT')
ellis.login()