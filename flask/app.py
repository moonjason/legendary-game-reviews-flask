from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
import models 

DEBUG = True

from resources.users import user
from resources.games import game
from resources.reviews import review

login_manager = LoginManager() #sets up the ability to set up the session

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.secret_key = "somethibgasjdhfs" #need this to encode session
login_manager.init_app(app) #setting up session

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    g.db.close()
    return response


############################need cors here!
# CORS() for user
# CORS(user, origins=["http://localhost:3000"], supports_credentials=True)
app.register_blueprint(user, url_prefix="/user")

##################################

# CORS(game, origins=["http://localhost:3000"], supports_credentials=True)
app.register_blueprint(game, url_prefix="/api/v1/games")
app.register_blueprint(review, url_prefix="/api/v1/reviews")

if __name__ == "__main__":
    #use this when models are ready
    print("tables connected")
    models.initialize()
    app.run(debug=DEBUG)