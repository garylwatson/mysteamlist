import steamfront
import csv
import sys

f = open("../steamapikey.txt")
apikey = f.readline()
f.close()

#Returns a user object from the steamfront package
def getUserProfile(id):
    client = steamfront.Client(apikey)
    return client.getUser(id64 = id)

#returns the applications that are tied with a profile
def getGameList(profile):
    return profile.apps

#returns a dictionary with all the relevant game information we are storing 
def getGameInfo(list):
    gameDict = {}
    for i in range(len(list)):
        try:
            game = list[i]
            game.unlazify()
            gameDict[game.appid] = [game.name, game.play_time]
        except steamfront.errors.AppNotFound:
            pass
    return gameDict

#returns the steam profile name
def getSteamName(profile):
    return profile.name  

#creates a new entry in the profile csv when logging in with a username and steam ID
def buildProfile(user, id):
    with open("UserProfiles.csv", "a", newline="") as f:
        csvwriter = csv.writer(f)
        profile = getUserProfile(id)
        list = getGameList(profile)
        games = getGameInfo(list)
        csvwriter.writerow([user ,id, getSteamName(profile),games,len(games)])

#done by Adam Johnson modified by Matthew Loehr
#logs into mysteamlist when given the username and steam id
def loginFcn():
    client = steamfront.Client(apikey)
    name = input("Enter mySteamList username: ")
    userid = input("Enter Steam id: ")
    client = steamfront.Client(apikey)
    newprofile = True
    with open("UserProfiles.csv", "r", newline="") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if userid == row[1]:
                print("Welcome back!")
                newprofile = False
    if newprofile:
        buildProfile(name, int(userid))

loginFcn()