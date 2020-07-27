# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a twitter scraping program.
"""

import GetOldTweets3 as got
import pandas as pd
import numpy as np

text_query = ['lockdown','coronavirus', 'covid19'] #
count = 1000

cities=['list of city names']
#cities=['Bhopal','Indore']
def text_query_to_csv(text_query, count, place):
    leng = 0
    i=0      
    for query in text_query:
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setLang('en').setMaxTweets(count).setNear(place).setSince("start date").setUntil("end date")
        
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
            
        text_tweets = [[place, query, tweet.date, tweet.text,tweet.id,tweet.username,tweet.geo,tweet.retweets,tweet.favorites,tweet.hashtags] for tweet in tweets]

        if i == 0:
            tweets_df = pd.DataFrame(text_tweets, columns = ['Place', 'Query', 'Datetime', 'Text','TweetID','username','geo','retweets','favourites','hashtags'])
        else:
            temp = pd.DataFrame(text_tweets, columns = ['Place', 'Query', 'Datetime', 'Text','TweetID','username','geo','retweets','favourites','hashtags'])
            tweets_df = tweets_df.append(temp)  
        i+=1
        tweets_df = tweets_df.sample(frac=1).reset_index(drop=True)
 
        if len(tweets_df) > count:
            tweets_df = tweets_df.head(count)
    return tweets_df   
 
df=pd.DataFrame()
temp=pd.DataFrame()
i=0
for place in cities: 
    temp=text_query_to_csv(text_query, count, place)
    if i==0:
        df = temp
    else:
        df = df.append(temp)
    i+=1
df.to_csv('statename.csv')