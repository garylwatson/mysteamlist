# Matthew Loehr
# Python script for splitting up the relevantgamedata csv into useable csv's for our database according to Gary's specification
import csv

with open("./relevantgamedata.csv") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=',')
    
    # Reformats the game title, appid, and metacritic scores
    with open("reformattedgames.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name","appid", "score"])

        for i in range(1):
            next(csv_reader)
        for row in csv_reader:
            score = row[4]
            if score == "'metacritic'":
                score = -1
            else:
                score = int(score[10:12])
            writer.writerow([row[0],row[1],score])
        f.close()

    # reformats the categories each game
    csvfile.seek(0)
    for i in range(1):
        next(csv_reader)
    with open("reformattedcategories.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["appid","categories"])

        for row in csv_reader:
            appid = row[1]
            categories = row[2].split("', '")
            categories[0]=categories[0][2:]
            categories[len(categories)-1]=categories[len(categories)-1][0:len(categories[len(categories)-1])-2]
            for i in range(len(categories)):
                writer.writerow([appid,categories[i]])
        f.close()

    # reformats the generes of each game
    csvfile.seek(0)
    for i in range(1):
        next(csv_reader)
    with open("reformattedgenres.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["appid","genres"])

        for row in csv_reader:
            appid = row[1]
            genres = row[3].split("', '")
            genres[0]=genres[0][2:]
            genres[len(genres)-1]=genres[len(genres)-1][0:len(genres[len(genres)-1])-2]
            for i in range(len(genres)):
                writer.writerow([appid,genres[i]])