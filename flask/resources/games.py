import models
import requests

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

game = Blueprint('games', 'game')

@game.route("/<page>", methods=["GET"])
def get_games(page):
    get_all_games = requests.get(f"https://rawg-video-games-database.p.rapidapi.com/games?page={page}", headers={"content-type": "application/json", "x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com", "x-rapidapi-key": "f0d3b6eff0mshe2f0073ca021f92p1efce7jsn41df200f1529"})
    return jsonify(get_all_games.json())

@game.route("/<page>/<id>", methods=["GET"])
def get_one_game(page, id):
    get_one_game = requests.get(f"https://rawg-video-games-database.p.rapidapi.com/games/{id}", headers={"content-type": "application/json", "x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com", "x-rapidapi-key": "f0d3b6eff0mshe2f0073ca021f92p1efce7jsn41df200f1529"})
    return jsonify(get_one_game.json())

# @game.route("/", methods=["GET"])
# def get_games():
#     get_all_games = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=08D497C10BC95B83E82D304CD1293794&format=json", data="fields *; limit 10;", headers={"content-type": "application/json", "user-key": "08D497C10BC95B83E82D304CD1293794"})
#     return jsonify(get_all_games.json())



