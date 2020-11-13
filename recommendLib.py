# Created by Adam Johnson

# Recommend games based on library

def recommendLibrary():
    # Connect to Steam
    import steamfront
    import login
    user = login.loginFcn()
    API_KEY = "1A709663E9448C9129559C952D980649"
    client = steamfront.Client(API_KEY)

    # Input minimum metacritic score and number of recommendations
    try:
        minScore = int(input("Enter minimum metacritic score for recommendations: "))
    except ValueError:
        print("Score is not integer, defaulting to 75")
        minScore = 75

    try:
        number = int(input("Enter maximum number of recommendations you want: "))
    except ValueError:
        print("Max recommendations is not an integer, defaulting to 5")
        number = 5

    # Search through user's games for most played
    apps = user.apps
    game1 = apps[0]
    game2 = apps[1]
    game3 = apps[3]
    time1 = game1.play_time
    time2 = game2.play_time
    time3 = game3.play_time

    for app in apps:
        tempTime = app.play_time

        # new most played
        if tempTime > time1:
            time3 = time2
            game3 = game2
            time2 = time1
            game2 = game1
            time1 = tempTime
            game1 = app

        # new second most played
        elif tempTime <= time1 and tempTime > time2:
            time3 = time2
            game3 = game2
            time2 = tempTime
            game2 = app

        # new third most played
        elif tempTime <= time2 and tempTime > time3:
            time3 = tempTime
            game3 = app

    # Find more details about most played games
    game1.unlazify()
    game2.unlazify()
    game3.unlazify()
    time1 = time1 / 60
    time2 = time2 / 60
    time3 = time3 / 60

    compareGenres = game1.genres

    # Find shared tags
    compareTag1 = set(game1.categories).intersection(game2.categories)
    compareTag2 = set(compareTag1).intersection(game3.categories)

    try:
        compareTag2.remove('Steam Achievements')
        compareTag2.remove('Remote Play on Tablet')
        compareTag2.remove('Steam Cloud')
    except ValueError:
        pass
    except KeyError:
        pass

    # optional output
    # print("Finding up to ", number, "games based on: ", compareTag2, compareGenres, minScore)

    # Find up to <number> other games in library with shared tags (compareTag2),
    # the same genre as the most played game (compareGenres), metacritic score >= minScore
    i = 0
    gameList = []

    # For a database recommender, pull from database here instead of looping through library
    for app in apps:
        try:
           app.unlazify()
        except (steamfront.errors.AppNotFound, TypeError):
            continue

        try:
            score = int(app.metacritic['score'])
            if len(set(compareTag2).intersection(app.categories)) > 0 and len(set(compareGenres).intersection(app.genres)) and (score >= minScore):
                gameList.append(app.name)
                i = i + 1
        except TypeError:
            continue

        if i >= number:
            break

    print(gameList)
