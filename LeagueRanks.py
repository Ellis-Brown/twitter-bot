from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re


def findStats(summoners):
    output = open('Name-Ranks.txt', 'w')
    bot = webdriver.Firefox()
    totalPoints = 0
    totalPlayers = 0
    for ign in summoners:
        totalPlayers += 1
        bot.get('https://na.op.gg/summoner/userName=' + ign)
        # time sleep
        try:
            rank = bot.find_element_by_class_name(
                "TierRank").get_attribute('innerHTML')
            lp = bot.find_element_by_class_name(
                "LeaguePoints").get_attribute('innerHTML').strip()
            score = getScore(rank, lp)
            user = ign + ": " + rank + " " + lp + "  score: " + str(score)
            totalPoints += score
            print(user)
            output.write('%s\n' % user)
        except:
            print("Error occured trying to find summoner: " + ign)

        return totalPoints / totalPlayers


# Reads from an input file, and creates a file


def readFile():
    # returns an array of fileName, summonerNameArray]
    file1 = open('people.txt', 'r')
    lines = file1.readlines()
    totalArray = []
    summonerNameArray = []
    currTeam = False
    for line in lines:
        if "Coach:" in line:
            continue
        result = re.search(':(.*),', line)
        teamName = re.search('-(.*)-', line)
        if teamName and currTeam:
            totalArray.append([oldTeamName, summonerNameArray])
            oldTeamName = teamName[1].strip()
            summonerNameArray = []
        elif teamName:
            currTeam = True
            oldTeamName = teamName[1].strip()
        if result:
            summonerNameArray.append(result[1].strip())
    outputFile = open('SummonerNames.txt', 'w')
    for listitem in summonerNameArray:
        outputFile.write('%s\n' % listitem)
    print(totalArray)
    return totalArray


def getScore(rank, lp):
    array = ['Iron', 'Bronze', 'Silver', 'Gold', 'Platinum',
             'Diamond', 'Master', 'Grandmaster', 'Challenger']
    # if theres a space, then add this value to their score... (5-X)
    division = rank
    score = 0
    if " " in rank:
        division = rank[:-2]
        score += 4 - int(rank[-1])
    score += array.index(division) * 4
    score += int(lp[:lp.index(" ")]) * 0.01
    return score


file = open('Team-scores.txt', 'w')

for entry in readFile()[1]:
    average = findStats(entry[1])
    file.write(str(entry[1]) + " " + str(average))
