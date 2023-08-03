# !!START
from flask import Flask, render_template
from .config import Config
from .tweets import tweets
import random


app = Flask(__name__)

app.config.from_object(Config)
# !!END

@app.route('/')
def index():
    # return '<h1> HELLO </h1>'
    return render_template('index.html', tweet=tweets[random.randint(0, len(tweets)-1)])
