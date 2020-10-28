import steamfront
import csv

f = open("../steamapikey.txt")
apikey = f.readline()
f.close()

#done by Matthew Loehr
def getUserProfile(id):
    client = steamfront.Client(apikey)
    return client.getUser(id64 = id)

def getGameList(profile):
    return profile.apps

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

def getSteamName(profile):
    return profile.name  

def buildProfile(user, id):
    with open("UserProfiles.csv", "a", newline="") as f:
        csvwriter = csv.writer(f)
        profile = getUserProfile(id)
        list = getGameList(profile)
        games = getGameInfo(list)
        csvwriter.writerow([user ,getSteamName(profile),games,len(games)])

#done by Adam Johnson modified by Matthew Loehr
def loginFcn():
    client = steamfront.Client(apikey)
    name = input("Enter mySteamList username: ")
    userid = input("Enter Steam id: ")
    client = steamfront.Client(apikey)
    buildProfile(name, int(userid))

loginFcn()