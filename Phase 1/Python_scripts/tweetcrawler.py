import tweepy
import csv
import json
import pandas as pd
####input your credentials here
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('tweetsdata.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)

track=['yoga','gym','fitness','Mindfulness','spirituality','yogaspirit','meditation','fitness','healthylife','nutrition','strength']
for t in track:
    print "Tracking "+t
    for tweet in tweepy.Cursor(api.search,q=t,count=100000000,lang="en",since="2000-01-01",include_entities=True).items():
	print "Tracking ..."+t
	csvWriter.writerow([tweet.created_at,tweet.entities, tweet.text.encode('utf-8')])
	print tweet.created_at
    print "Finished "+t+"\n"
csvFile.close()
