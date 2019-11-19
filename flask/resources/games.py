import models
import requests

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

game = Blueprint('games', 'game')

@game.route("/", methods=["GET", "POST"])
def get_games():
    get_all_games = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=08D497C10BC95B83E82D304CD1293794&format=json", data="fields *; limit 10;", headers={"content-type": "application/json", "user-key": "08D497C10BC95B83E82D304CD1293794"})

    allGames = get_all_games.json()["applist"]["apps"]
    allIds = [game["appid"] for game in allGames]

    for i, id in enumerate(allIds):
        if i < 1:
            get_one_game = requests.get(f"https://store.steampowered.com/api/appdetails?appids={id}", data="fields *; limit 10;", headers={"content-type": "application/json", "user-key": "08D497C10BC95B83E82D304CD1293794"})            
            retrieved_game = get_one_game.json()[str(id)]["data"]
            body = {"title": retrieved_game["name"], "genres": retrieved_game["genres"], "creator": retrieved_game["developers"], "release_date": retrieved_game["release_date"], "description": retrieved_game["about_the_game"]}
            Game = models.Game.create(**body)
            print(body)

    get_one_game = requests.get("https://store.steampowered.com/api/appdetails?appids=1088487", data="fields *; limit 10;", headers={"content-type": "application/json", "user-key": "08D497C10BC95B83E82D304CD1293794"})
    return jsonify(get_one_game.json())
    # return jsonify(r.json()["applist"]["apps"][0:10])
    # return jsonify(r.json()["1073920"]["data"]["release_date"])

# WE ARE USING THE API JASON FOUND
# DATA="" is basically the query selector, and headers is where we specify the key and the type of content the api is providing.
# r.json() turns the response into python, and jsonify turns the response into readable json format.
