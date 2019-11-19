from flask import Flask
from flask_login import LoginManager
app = Flask(__name__)

############import resources here!
#################

login_manager = LoginManager() #sets up the ability to set up the session

app.secret_key = "somethibgasjdhfs" #need this to encode session
login_manager.init_app(app) #setting up session


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
# CORS()
##################################

if __name__ == "__main__":
    #use this when models are ready
    # print("tables connected")
    # models.initialize()
    app.run()