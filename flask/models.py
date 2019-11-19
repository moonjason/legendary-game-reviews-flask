from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('game.sqlite')

class User(UserMixin, Model):
  username = CharField()
  email = CharField()
  password = CharField()

  class Meta:
    database = DATABASE

########## Need model for Game review or game 
########## not sure yet

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User], safe=True)
  print("Tables Created")
  DATABASE.close()