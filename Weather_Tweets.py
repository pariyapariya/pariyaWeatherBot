#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dependencies
import tweepy
import time
import json
import os
import random
import requests as req
import datetime


# Import your config file(s) and variable(s)

# Heroku check
is_heroku = False
if 'IS_HEROKU' in os.environ:
    is_heroku = True

if is_heroku == False:
    from config import consumer_key, consumer_secret, access_token, access_token_secret, weather_api_key
else:
    consumer_key = os.environ.get('remote_dbendpoint')
    consumer_secret = os.environ.get('remote_dbport')
    access_token = os.environ.get('remote_dbname')
    access_token_secret = os.environ.get('remote_dbuser')
    weather_api_key = os.environ.get('remote_dbpwd')


# In[3]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[4]:


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    city = 'Washington, D.C.'
    units = 'imperial'
    query_url = (f'{url}appid={weather_api_key}&q={city}&units={units}')

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(
        "[pariyabot] - Weather in DC " +\
        (datetime.datetime.now().strftime("%I:%M %p") + " " +\
         str(weather_json["main"]["temp"])+"F"))

    # Print success message
    print("Tweeted successfully!")


# In[5]:


# Test out the function
# WeatherTweet()


# In[ ]:


# Tweet out the weather every one minute
while(True):
    WeatherTweet()
    time.sleep(60)


# In[ ]:




