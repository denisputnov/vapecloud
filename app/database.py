from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.config import application

db = SQLAlchemy(application)

