from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import re



def findStats(summoners):
    output = open('Name-Ranks', 'w')
    bot = webdriver.Firefox()
    for ign in summoners:
        bot.get('https://na.op.gg/summoner/userName=' + ign)
        #time sleep 
        rank = bot.find_element_by_class_name("TierRank").get_attribute('innerHTML')
        lp = bot.find_element_by_class_name("LeaguePoints").get_attribute('innerHTML').strip()
        user = ign + ": " + rank + " " + lp
        output.write('%s\n' % user)
          
#Reads from an input file, and creates a file  
def readFile():
    file1 = open ('people.txt', 'r')
    lines = file1.readlines()
    summonerNameArray = []
   
    for line in lines:
        result = re.search(':(.*),', line)
        if result:
            summonerNameArray.append(result[1].strip())
    outputFile = open('SummonerNames.txt', 'w')
    for listitem in summonerNameArray:
        outputFile.write('%s\n' % listitem)
    return summonerNameArray


findStats(readFile())


