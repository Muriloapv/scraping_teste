from flask import Flask
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.secret_key = 're'
app.config.from_object('')

db = SQLALchemy(app)
from app import routes, models