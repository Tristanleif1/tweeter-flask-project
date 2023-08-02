# !!START
from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from datetime import datetime
from app.form.form import TweetForm
import random


app = Flask(__name__)

app.config.from_object(Config)
# !!END

@app.route('/')
def index():
    # return '<h1> HELLO </h1>'
    return render_template('index.html', tweet=tweets[random.randint(0, len(tweets)-1)])


@app.route('/feed')
def all_tweets():
    return render_template('feed.html', tweets = tweets)

@app.route('/new', methods=['GET', 'POST'])
def form():

    form = TweetForm()
    if form.validate_on_submit():
        author = form.author.data
        tweet = form.tweet.data
        date = datetime.now().strftime("%Y/%m/%d")
        likes = random.randint(0,1000)
        new_tweet = {
            "id": len(tweets) + 1,
            "author": author,
            "tweet": tweet,
            "date": date,
            "likes": likes
        }
        tweets.append(new_tweet)
        return redirect('/feed')

    return render_template('new_tweet.html', form=form)
