from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import base64
from dotenv import load_dotenv, find_dotenv
from vapecloud.config import Config

load_dotenv(find_dotenv())

application = Flask(__name__)
application.config.from_object(Config)

