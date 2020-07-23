from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)
app.secret_key = 'um-nome'
app.config.from_object('config')

picFolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = picFolder

db  = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0', port = 8085))

from app.models import tables
from app.controllers import default
