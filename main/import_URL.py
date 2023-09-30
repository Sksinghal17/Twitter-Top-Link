import math
import sys,tweepy
import datetime
import time
import re
from urlextract import URLExtract


consumer_key = 'wR7VdqCDY2M8KCrdqCz5a7jgR'
consumer_secret = 'Rd6zeupsULrqsYvxdxgcPqd5dm0myEbIkUt7TA86J2vjyOIFzS'
access_token = '3858872419-1qxuPAez5G6iRbQXN3omekpI1l4T3oGctc7dtEV'
access_secret = '41TqCsAxDB203wyp7ETbSu5jpugzhzfT1bjz5D7Tk9iRz'


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    

#input of twitter user id
    
pp = input()

user = api.get_user(pp)






ans=[]

def get_tweets(api, username):
    page = 1
    deadend = False
    while True:
        tweets = api.user_timeline(username, page = page)

        for tweet in tweets:
            
            if (datetime.datetime.now() - tweet.created_at).days < 7:

                for url in tweet.entities['urls']:
                    expanded_url=url['expanded_url']
                    ans.append(expanded_url)
        
            else:
                deadend = True
                return
            
        if not deadend:
            page=page + 1

get_tweets(api, pp)

for x in ans:
    print(x)









