from requests_oauthlib import OAuth1Session
import json

class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.oauth_session = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)
    
    def search_tweets(self, query):
        params = {"q": query}
        endpoint = "https://api.twitter.com/1.1/search/tweets.json"
        req = self.oauth_session.get(endpoint, params = params)
        tweetslist = []
        if req.status_code == 200:
            timeline = json.loads(req.text)
            for tweet in timeline["statuses"]:
                tweetslist.append(tweet["text"])
        
        return tweetslist
    
    def get_user_tweets(self, screen_name):
        params = {
            "screen_name": screen_name,
            "count"      : 200
            }
        endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        req = self.oauth_session.get(endpoint, params = params)
        tweetslist = []
        if req.status_code == 200:
            timeline = json.loads(req.text)
            tweetslist = [tweet["text"] for tweet in timeline]
        
        return tweetslist
