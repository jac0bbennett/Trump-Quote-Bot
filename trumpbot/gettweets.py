
    
# This is an adapted version of https://gist.github.com/yanofsky/5436496

import urllib, json
import sys
import tweepy
from tweepy import OAuthHandler

def twitter_fetch(screen_name,maxnumtweets=200):

    consumer_token = ""
    consumer_secret = ""
    access_token = ""
    access_secret = ""

    
    auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    
    api  = tweepy.API(auth)
    
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print("...%s tweets downloaded so far" % (len(alltweets)))

    for status in alltweets: 
        it = (status.text).encode('utf-8')
        with open('tweets.txt', 'a', encoding='utf-8') as f:
            f.write(bytes(it).decode('utf-8') + ' ')

   

if __name__ == '__main__':
    twitter_fetch('realDonaldTrump')
    
    
