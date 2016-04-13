#!/usr/bin/python
import re, nltk, random, tweepy, time
from words import wordpos

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

trumpismsbegin = ['Frankly, ', 'To be honest, ', 'You know what? ', 'Listen, ', "I'm the best. ", "I have a great brain and ", "Let's be honest, ", "This is huge, ", 'China ', "I'm smart, '"]
trumpismsend = [' We need a wall.', ' Sad!', ' THAT much I know!', ' THAT much I can tell you!', ' Make America Great Again', ' We will win.', ' It is HUGE!', ' Amazing!', ' Fantastic!', " We're gonna win!'", ' #makeamericagreatagain']

class TwitterWrapper:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def update_status(self, message):
        self.api.update_status(status=message)

shouldbp = random.randint(1, 10)
shouldep = random.randint(1, 10)

def tweetit():
    d = random.randint(0,(len(wordpos['DT'])-1))
    n = random.randint(0,(len(wordpos['NN'])-1))
    v = random.randint(0,(len(wordpos['VBZ'])-1))
    j = random.randint(0,(len(wordpos['JJ'])-1))

    it = wordpos['DT'][d] + ' ' + wordpos['NN'][n] + ' ' + wordpos['VBZ'][v] + ' ' + wordpos['JJ'][j]
    
    bp = random.randint(0, (len(trumpismsbegin)-1))
    bp = trumpismsbegin[bp]
    ep = random.randint(0, (len(trumpismsend)-1))
    ep = trumpismsend[ep]
    
    pick = random.randint(1, 3)
    if pick == 1:
        ep = ''
    elif pick == 3:
        bp = ''
        
    it = re.sub('[!.?,:()"]', '', it)
        
    it = bp + it.lower() + '.' + ep
    
    
    twitter = TwitterWrapper(consumer_key, consumer_secret, access_token, access_token_secret)
    twitter.update_status(it)
    
    print(it)
    
    time.sleep(14400)
    tweetit()
    
tweetit()
