from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from  app.config import DEVconfig
from  sqlalchemy import or_,and_
app=Flask(__name__,template_folder='templates',static_folder='static')
app.config.from_pyfile('config.py')
db=SQLAlchemy(app)

class role(db.Model):
    __tablename__='test'
    id=db.column(db.Integer,par)