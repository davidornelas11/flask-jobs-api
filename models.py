from peewee import *
import datetime

DATABASE = PostgresqlDatabase('states')

class State(Model):
  state = CharField()
  programming_language = CharField()
  number_of_jobs = CharField()
  created_at = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([State], safe=True)
  print("TABLES Created")
  DATABASE.close()