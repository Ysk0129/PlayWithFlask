from sampleapp import app
from flask import render_template
from flask import request
from sampleapp.twconfig import twkeys
from sampleapp.models.count import Counter
from sampleapp.models.twitterapi import TwitterAPI
from sampleapp.models.wordprocessing import WordProcessing
from sampleapp.models.datacache import DataCache

@app.route('/')
def index():
    message = {}
    counter = Counter()
    counter.incrCount()
    message["count"] = counter.getCount()

    return render_template('index.html', message=message)

@app.route('/tweet',  methods=['POST'])
def tweet():
    message = {}

    message["name"] = request.form["name"]
    twitter = TwitterAPI(twkeys["ConsumerKey"], twkeys["ConsumerSecret"], twkeys["AccessToken"], twkeys["AccessTokenSecret"])
    message["tweets"] = twitter.get_user_tweets(message["name"])
    
    words = []
    wp = WordProcessing()
    for tweet in message["tweets"]:
        words.extend(wp.separate_words(tweet))
    message["words"] = wp.count_words(words)

    cache = DataCache()
    cache.save_list(message["name"], message["tweets"])

    return render_template('tweet.html', message=message)
