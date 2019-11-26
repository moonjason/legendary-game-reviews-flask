import os

from playhouse.db_url import connect
from peewee import *
from flask_login import UserMixin

DATABASE = connect(os.environ.get('DATABASE_URL'))

class User(UserMixin, Model):
  username = CharField()
  email = CharField()
  password = CharField()
  class Meta: 
    database = DATABASE

class Review(Model):
    game_id = CharField()
    user_id = ForeignKeyField(User)
    title = CharField() 
    up_votes = CharField() 
    down_votes = CharField() 
    body = TextField()
    is_positive = BooleanField()
    class Meta: database = DATABASE


def initialize():
  DATABASE.connect()
  DATABASE.create_tables([User, Review], safe=True)
  print("Tables Created")
  DATABASE.close()