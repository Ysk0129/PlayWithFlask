from sampleapp import app
from flask import render_template
from sampleapp.twconfig import twkeys
from sampleapp.models.count import Counter
from sampleapp.models.twitterapi import TwitterAPI

@app.route('/')
def index():
    counter = Counter()
    counter.incrCount()
    count = counter.getCount()
    twitter = TwitterAPI(twkeys["ConsumerKey"], twkeys["ConsumerSecret"], twkeys["AccessToken"], twkeys["AccessTokenSecret"])
    tweets = twitter.get_user_tweets("@pref_saitama")
    return render_template('index.html', message=count, tweets=tweets)
