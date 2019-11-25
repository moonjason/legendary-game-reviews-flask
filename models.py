import os

from playhouse.db_url import connect
from peewee import *
from flask_login import UserMixin

# DATABASE = connect(os.environ.get('DATABAUSE_URL'))
DATABASE = SqliteDatabase('game.sqlite')

class User(UserMixin, Model):
  username = CharField()
  email = CharField()
  password = CharField()

  # def __init__(self, username, email, password):
  #   self.username = username
  #   self.email = email
  #   self.password = password

  # def is_authenticated(self):
  #   return True

  # def is_active(self):
  #   return True
  
  # def is_anonymous(self):
  #   return False

  # def get_id(self):
  #   return unicode(self.id)

  # def __repr__(self):
  #   return "<User %r>" % (self.username)

  class Meta: 
    database = DATABASE

class Review(Model):
    game_id = CharField()
    user_id = ForeignKeyField(User)
    title = CharField() 
    up_votes = CharField() 
    down_votes = CharField() 
    body = CharField()
    is_positive = BooleanField()
    class Meta: database = DATABASE


def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User, Review], safe=True)
  print("Tables Created")
  DATABASE.close()