# By Matthew Loehr
# Script for making csv file with all relevant information that we need from steam games
import steamfront
import csv
import time
import simplejson.errors

# opens the game list csv file we have
with open("./steamgamelist.csv") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=',')

    #creates new csv that will store all relevant game data to us
    with open("relevantgamedata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name","appid", "categories","genres","metacritic"])

        client = steamfront.Client()
        for i in range(102004):
            next(csv_reader)
        for row in csv_reader:
            try:
                if(str(client.getApp(appid=row[0]).type) == "game"):
                    writer.writerow([row[1],row[0],str(client.getApp(appid=row[0]).categories),str(client.getApp(appid=row[0]).genres),str(client.getApp(appid=row[0]).metacritic)])
                    time.sleep(1)
                else:
                    pass
            except (steamfront.errors.AppNotFound, TypeError, simplejson.errors.JSONDecodeError):
                pass

