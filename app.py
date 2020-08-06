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
        time.sleep(7) # lets the twitter page load up
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN) #logs us in
        time.sleep(5) #Lets us load in.
    
    #Purpose: Like the tweets by hastag
    def like_tweet_hastag(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
        time.sleep(5)
        for i in range(1, 5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            print(tweets)
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            print(links)

            tweetLinks = [i.get_attribute('href')
                for i in bot.find_elements_by_xpath("//a[@dir='auto']")] # Looking for all the element where they have an attribute dir=auto - not the best way but I was in a hurry, lol

            
          

ellis = TwitterBot('angelwithashotgun4348@gmail.com', 'passwordBOT')
ellis.login()
ellis.like_tweet_hastag('League of Legends')