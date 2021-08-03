#!/usr/bin/env python
# coding: utf-8

# In[79]:


# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a twitter scraping program.
"""
import GetOldTweets3 as got
import pandas as pd
import numpy as np



text_query = ['coronavirus', 'covid19'] # THIS 'Lockdown', 
start_date = "2020-03-01"
end_date = "2020-03-31"
count = 5000
states = ["Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil_Nadu", "Telangana", "Tripura", "Uttarakhand", "Uttar Pradesh", "West_Bengal"]

cities =    [["Bhubaneswar", "Cuttack", "Rourkela", "Brahmapur", "Sambalpur"],
             ["Chandigarh", "Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
             ["Jaipur", "Jodhpur", "Kota", "Bikaner", "Ajmer"],
             ["Gangtok", "Dzongu", "Geyzing", "Mangan", "Namchi"],
             ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Tiruppur"],
             ["Hyderabad", "Warangal", "Nizamabad", "Khammam", "Karimnagar"],
             ["Agartala", "Kailashahar", "Kamalpur", "Khowai", "Kumarghat"],
             ["Dehradun", "Nainital", "Haridwar", "Roorkee", "Rudrapur"],
             ["Lucknow", "Kanpur", "Ghaziabad", "Agra", "Meerut"],
             ["Kolkata", "Asansol", "Siliguri", "Durgapur", "Bardhaman"]] # THIS

# Function that pulls tweets based on a general search query and turns to csv file

# Parameters: (text query you want to search), (max number of most recent tweets to pull from)

def text_query_to_csv(text_query, count, place, start_date, end_date):
    # Creation of query object
    # Creation of query object
    leng = 0
    i=0
    for query in text_query:
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setLang('en').setMaxTweets(count).setNear(place).setSince(start_date).setUntil(end_date)
        # THIS (setSince("2020-05-01").setUntil("2020-05-31")) 
            # Creation of list that contains all tweets
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
            # Creating list of chosen tweet data
        text_tweets = [[place, query, tweet.date, tweet.text,tweet.id,tweet.username,tweet.geo,tweet.retweets,tweet.favorites,tweet.hashtags] for tweet in tweets]

            # Creation of dataframe from tweets
        if i == 0:
            tweets_df = pd.DataFrame(text_tweets, columns = ['Place', 'Query', 'Datetime', 'Text','TweetID','username','geo','retweets','favourites','hashtags'])
        else:
            temp = pd.DataFrame(text_tweets, columns = ['Place', 'Query', 'Datetime', 'Text','TweetID','username','geo','retweets','favourites','hashtags'])
            tweets_df = tweets_df.append(temp)  
        i+=1
        #tweets_df = pd.DataFrame(tweets_df, columns = ['Place', 'Query', 'Datetime', 'Text','TweetID','username','geo','retweets','favourites','hashtags'])
        #tweets_df = tweets_df.iloc[np.random.permutation(len(tweets_df))]
        tweets_df = tweets_df.sample(frac=1).reset_index(drop=True)
        if len(tweets_df) > count:
            tweets_df = tweets_df.head(count)
    return tweets_df   
 
    
df=pd.DataFrame()
temp=pd.DataFrame()
i=0
for city in cities:   
    for place in city: 
        temp=text_query_to_csv(text_query, count, place, start_date, end_date)
        if i==0:
            df = temp
        else:
            df = df.append(temp)
        i+=1

df.to_csv('march_data.csv')
