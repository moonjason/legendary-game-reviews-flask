from flask import Flask, jsonify, g
from flask_login import LoginManager
app = Flask(__name__)
import models 

DEBUG = True

############import resources here!
from resources.users import user
from resources.games import game
#################

login_manager = LoginManager() #sets up the ability to set up the session

app.secret_key = "somethibgasjdhfs" #need this to encode session
login_manager.init_app(app) #setting up session

# @login_manager.user_loader
# def load_user(userid):
#     try:
#         return models.User.get(models.User.id == userid)
#     except models.DoesNotExist:
#         return None

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

###############move this to controller when ready
@app.route("/")
def hello():
    return "Hello World!"
#####################################


############################need cors here!
# CORS() for user
##################################
app.register_blueprint(game, url_prefix="/api/v1/games")


if __name__ == "__main__":
    #use this when models are ready
    # print("tables connected")
    # models.initialize()
    app.run(debug=DEBUG)