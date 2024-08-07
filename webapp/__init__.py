import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData 
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, '..', 'database.db')
# db = SQLAlchemy(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:postgres@localhost:5432/postgres'
db = SQLAlchemy(app=app, metadata=MetaData(schema="konfidantea"))


from webapp import encrypted_secret
from webapp import routes