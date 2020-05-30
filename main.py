import requests
import json

CC = 'br'

def findID(name, list):
    #print("Searching for: " + name)
    for game in list:
        if (game["name"] == name):
            #print ('ID: ' + str(game["appid"]))
            return game["appid"]
    return 0

with open('index.html') as json_file:
    raw = json.load(json_file)
namesAndIds = raw["applist"]["apps"]["app"]

games = []

with open('jogos') as gamesFile:
    for line in gamesFile:
        games.append(line.rstrip())

print("SteamID,Name,Price")

for gameName in games:
    ID = findID(gameName, namesAndIds)

    if (ID):
        r = requests.get('https://store.steampowered.com/api/appdetails?appids='+ str(ID) +'cc='+ CC + '&filters=price_overview')
        price = int (r.json()[str(ID)]['data']['price_overview']['final']) / 100
    else:
        price = 0

    print (str(ID) + ',' + gameName + ',' + str(price))