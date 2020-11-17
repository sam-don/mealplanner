
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from database import init_db
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = init_db(app)

ma = Marshmallow(app)

from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)
