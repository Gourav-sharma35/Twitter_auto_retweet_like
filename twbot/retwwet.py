import tweepy
import time
consumer_key='QmOf558VfksCcP4B6MNLnwo7M'
consumer_secret='XN66XTlHy0Wu1TMIgsSHqYY1k6QzzjUofRNZdm4BX8ZVc5XAN7'

key='1298302138104389633-8ymoCkpELeice4iCNApQ7Pjm1fGB4l'
secret='9n3jCkl0WNNd29EsoZRuE8lVEFyrNQ5LnmyhWsf7lDXCt'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag="java"
tweet_numbers=4
tweets=tweepy.Cursor(api.search,hashtag).items(tweet_numbers)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()
