from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('game.sqlite')

class User(UserMixin, Model):
  username = CharField()
  email = CharField()
  password = CharField()

  class Meta:
    database = DATABASE

class Game(Model):
    title = CharField()
    genres = CharField()
    creator = CharField()
    release_date = CharField()
    description = CharField()

    class Meta: database = DATABASE


def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User, Game], safe=True)
  print("Tables Created")
  DATABASE.close()