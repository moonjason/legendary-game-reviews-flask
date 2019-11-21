import models
import requests

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

game = Blueprint('games', 'game')

@game.route("/<page>", methods=["GET"])
def get_games(page):
    all_games = requests.get(f"https://api.rawg.io/api/games?dates=2019-01-01,2019-12-31&ordering=-added&page={page}", headers={"content-type": "application/json", "x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com", "x-rapidapi-key": "f0d3b6eff0mshe2f0073ca021f92p1efce7jsn41df200f1529"})
    return jsonify(all_games.json())

@game.route("/<page>/<id>", methods=["GET"])
def get_one_game(page, id):
    one_game = requests.get(f"https://api.rawg.io/api/games/{id}", headers={"content-type": "application/json", "x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com", "x-rapidapi-key": "f0d3b6eff0mshe2f0073ca021f92p1efce7jsn41df200f1529"})
    return jsonify(one_game.json())

@game.route("/<page>/<id>/<search>", methods=["GET"])
def get_matched_games(page, id, search):
     matched_games = requests.get(f"https://api.rawg.io/api/games?search={search}", headers={"content-type": "application/json", "x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com", "x-rapidapi-key": "f0d3b6eff0mshe2f0073ca021f92p1efce7jsn41df200f1529"})
     return jsonify(matched_games.json())




