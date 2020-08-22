from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import base64
from admin.admin import admin
from dotenv import load_dotenv, find_dotenv
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

load_dotenv(find_dotenv())

application = Flask(__name__)
application.debug = True
application.config.from_object(Config)

application.register_blueprint(admin, url_prefix='/admin')

db = SQLAlchemy(application)

migrate = Migrate(application, db)
manager = Manager(application)

manager.add_command('db', MigrateCommand)

