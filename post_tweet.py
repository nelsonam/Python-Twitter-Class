import os
import tweepy

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_key = os.environ['access_token']
access_secret = os.environ['access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

api.update_status(status="Come see my workshop at SF Python tonight! http://www.meetup.com/sfpython/events/225128409/")
