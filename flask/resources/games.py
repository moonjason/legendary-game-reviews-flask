import models
import requests

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

game = Blueprint('games', 'game')

@game.route("/", methods=["GET"])
def get_ten_games():
    r = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=STEAMKEY&format=json", data="fields name; limit 100; sort popularity desc; where themes !=(42);", headers={"content-type": "application/json", "user-key": "a3151b1ce686df4983737ccc7f8798e8"})
    print(jsonify(r.json()), "THIS IS TYPE")
    return jsonify(games=r.json())

# WE ARE USING THE API JASON FOUND
# DATA="" is basically the query selector, and headers is where we specify the key and the type of content the api is providing.
# r.json() turns the response into python, and jsonify turns the response into readable json format.
