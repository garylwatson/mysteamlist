import steamfront
import csv
import sys

apikey = "F093A1F972CA49F96184569787D7108E"

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
            gameDict[game.appid] = game.play_time
        except steamfront.errors.AppNotFound:
            pass
    return gameDict

#returns the steam profile name
def getSteamName(profile):
    return profile.name  

#creates a new entry in the profile csv when logging in with a username and steam ID
def buildProfile(user, id, pas):
    prof = getUserProfile(id)
    games = getGameList(prof)
    titles = getGameInfo(games)
    with open("userprofile/UserProfiles.csv", "a", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow([id ,user, pas])
        f.close()
    with open("userprofile/steamNames.csv", "a", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow([id, getSteamName(prof)])
        f.close()
    with open("userprofile/steamGames.csv", "a", newline="") as f:
        csvwriter = csv.writer(f)
        for appid in titles:
            csvwriter.writerow([id, appid, titles[appid]])
        f.close()
    with open("userprofile/numGames.csv", "a", newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow([id ,len(titles)])
        f.close()
    return 'built'




#done by Adam Johnson modified by Matthew Loehr
#logs into mysteamlist when given the username and steam id
def loginFcn(n, uid):
    client = steamfront.Client(apikey)
    name = n
    userid = uid
    client = steamfront.Client(apikey)
    newprofile = True
    with open("userprofile/UserProfiles.csv", "r", newline="") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if userid == row[2] and name == row[1]:
                return "welcome back"
    if newprofile:
        return "not found"

#loginFcn("matt",76561198035639224)