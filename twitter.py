import tweepy
from textblob import TextBlob
consumer_key ="VuNYJuHQ61TFA6al1s0YMFIkl"
consumer_secret ="ywxYmRo6tdi7RPsuadLrRd48EjYcuygdIsqPSoyivhyxkJoRmq"

access_token ="154904428-Y8xoFlGU8QgqvuBIzeD2jYezcEMFfJOS2uIGbJgm"
access_token_secret ="n66aPA3AqqgOH1GNBzoGUV5bB13nLa88SbpWvH1KuamEh"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets=api.search("Trump")

for tweet in public_tweets:
 print(tweet.text)
 analysis = TextBlob(tweet.text)
 print(analysis.sentiment)


