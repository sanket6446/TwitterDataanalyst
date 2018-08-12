import tweepy
from tweepy import OAuthHandler
import json
import nltk

consumer_key = '4LqzP4v2Wh11NhwDAyGIUqGwh'
consumer_secret = 'z5dScxufdinu8Gk3Tja38iZgGHmQM3JNgMHOyh28UumC7FTGUw'
access_token = '2939164626-gWrdSOlhn1eoYUt66KrNTWmhLuKgYdMU8MzPF20'
access_secret = '1Ug34QU2P0dtafbEHfly3u7HevXSOTznvVpwdGnSU2CmC'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener

import csv
class MyListener(StreamListener):
    def on_data(self, data):
        try:
            j = json.loads(data)
            with open('F:\TwitterData/coalnew.csv','a') as csvfile:
                fieldnames = {'created_at', 'id', 'text'}
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                #writer.writeheader()
                writer.writerow({'created_at': j['created_at'], 'id': j['id'], 'text': j['text']})
        except BaseException as e:
            print('Error on_data: %s'%str(e))
            return True

        def on_error(self, status):
            print(status)
            return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['coal'])
