from flask import Flask 

app = Flask(__name__)
app.secret_key = 'KKurataisthebest'

from app import views