import tweepy
import time

consumer_key='QmOf558VfksCcP4B6MNLnwo7M'
consumer_secret='XN66XTlHy0Wu1TMIgsSHqYY1k6QzzjUofRNZdm4BX8ZVc5XAN7'

key='1298302138104389633-8ymoCkpELeice4iCNApQ7Pjm1fGB4l'
secret='9n3jCkl0WNNd29EsoZRuE8lVEFyrNQ5LnmyhWsf7lDXCt'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

tweets=api.mentions_timeline()

file_name="last_seen.txt"

def read_last_seen(file_name):
    file_read=open(file_name,'r')
    last_seen_id=int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(file_name,last_seen_id):
    file_write=open(file_name,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


tweets=api.mentions_timeline(read_last_seen(file_name),tweet_mode='extended')

def reply():
    for tweet in tweets:
        if '#randomthoughts' in tweet.full_text.lower():
            print("New tweet found")
            print("Replied to that particular id"+"..."+ tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " hii deep.. I am happy to see your comment ion my twitter account" ,tweet.id )
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(file_name,tweet.id)

while True:
    reply()
    time.sleep(3)
