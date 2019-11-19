import models
import requests

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

game = Blueprint('games', 'game')

@game.route("/", methods=["GET"])
def get_games():
    get_all_games = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=08D497C10BC95B83E82D304CD1293794&format=json", data="fields *; limit 10;", headers={"content-type": "application/json", "user-key": "08D497C10BC95B83E82D304CD1293794"})
    return jsonify(get_all_games.json())

@game.route("/<id>", methods=["GET"])
def get_one_game(id):
    get_one_game = requests.get(f"https://store.steampowered.com/api/appdetails?appids={id}", headers={"content-type": "application/json", "user-key": "08D497C10BC95B83E82D304CD1293794"})
    return jsonify(get_one_game.json())


