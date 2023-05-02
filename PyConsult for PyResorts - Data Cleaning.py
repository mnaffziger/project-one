#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import os
import scipy.stats as st
import datetime

from scipy.stats import linregress
from pprint import pprint

from config import weather_api_key
from config import geoapify_key

from citipy import citipy


# In[2]:


#import csv file
resort_city_data_df = pd.read_csv("Resources/resort_city_crime_weather_df.csv", index_col="City_ID")

resort_city_data_df


# In[3]:


#cleaning up column names
resort_city_data_df.rename(columns={"Country_x" : "Country"}, inplace=True)
resort_city_data_df.drop(columns="Country_y", inplace=True)
resort_city_data_df


# In[4]:


#setting climate parameters for ideal locations
resort_city_ideal_df = resort_city_data_df.loc[(resort_city_data_df["Max Temp"] < 29)
                                 & (resort_city_data_df["Max Temp"] > 28)
                                & (resort_city_data_df["Humidity"] < 70) 
                                & (resort_city_data_df["Humidity"] > 20)
                                & (resort_city_data_df["Wind Speed"] < 8)
                                & (resort_city_data_df["Cloudiness"] == 0)]

resort_city_ideal_df


# In[5]:


#see how many cities are in the dataframe
resort_city_ideal_df.count()


# In[17]:


resort_city_ideal_hotel_df = resort_city_ideal_df.copy()

resort_city_ideal_hotel_df["Number of Hotels"] = ""
resort_city_ideal_hotel_df["Number of Resturants"] = ""
resort_city_ideal_hotel_df["Bodies of Water"] = ""
resort_city_ideal_hotel_df["Tourist Attractions"] = ""
resort_city_ideal_hotel_df["Natural Places"] = ""
resort_city_ideal_hotel_df["Hospital"] = ""
resort_city_ideal_hotel_df["Entertainment"] = ""
resort_city_ideal_hotel_df["Rental Car"] = ""
resort_city_ideal_hotel_df["Airport"] = ""

resort_city_ideal_hotel_df.head()


# In[18]:


def city_categories(categories, column, df):
    
    for index, row in df.iterrows():
        # get latitude, longitude from the DataFrame
        latitude = row["Lat"]
        longitude = row["Lng"]

        # Add filter and bias parameters with the current city's latitude and longitude to the params dictionary

        # Set base URL
       
        radius = 8000

        # Set the parameters for the type of search
        filters = f"circle:{longitude},{latitude},{radius}"
        bias = f"proximity:{longitude},{latitude}"
        limit = 200

        # set up a parameters dictionary
        params = {
            "categories":categories,
            "limit":limit,
            "filter":filters,
            "bias":bias,
            "apiKey":geoapify_key    
        }

        # Set base URL
        base_url = "https://api.geoapify.com/v2/places"

        # run a request using our params dictionary
        response = requests.get(base_url, params=params)
        response_json = response.json()

        #pprint(response_json)


        # Grab the first hotel from the results and store the name in the hotel_df DataFrame
        try:
            df.loc[index, column] = len(response_json["features"])
        except (KeyError, IndexError):
            df.loc[index, column] = 0   
        
    return df 


# In[ ]:


categories = "airport.international"
column = "Airport"
resort_city_ideal_hotel_df = city_categories(categories, column, resort_city_ideal_hotel_df)


# In[34]:


cities_airports = resort_city_ideal_hotel_df[(resort_city_ideal_hotel_df[["Airport"]] != 0).all(axis=1)]


# In[35]:


cities_airports


# In[39]:


categories = "accommodation, beach.beach_resort"
column = "Number of Hotels"
ideal_cities_all_df = city_categories(categories, column, cities_airports)



# In[40]:


categories = "natural.water.sea,natural.water.reef,natural.water"
column = "Bodies of Water"
ideal_cities_all_df = city_categories(categories, column, cities_airports)


# In[41]:


categories = "tourism"
column = "Tourist Attractions"
ideal_cities_all_df = city_categories(categories, column, cities_airports)


# In[42]:


categories = "catering.restaurant"
column = "Number of Resturants"
ideal_cities_all_df = city_categories(categories, column, cities_airports)


# In[43]:


categories = "natural"
column = "Natural Places"
ideal_cities_all_df = city_categories(categories, column, cities_airports)


# In[44]:


categories = "healthcare.hospital"
column = "Hospital"
ideal_cities_all_df = city_categories(categories, column, cities_airports)


# In[45]:


categories = "rental.car"
column = "Rental Car"
ideal_cities_all_df = city_categories(categories, column, cities_airports)


# In[46]:


categories = "entertainment"
column = "Entertainment"
ideal_cities_all_df = city_categories(categories, column, cities_airports)


# In[47]:


ideal_cities_all_df


# In[101]:


#sorting for  lowest hotels
cities_sorted_by_hotels = ideal_cities_all_df.sort_values("Number of Hotels", ascending=True)

cities_sorted_by_hotels


# In[103]:


cities_sorted_by_hotels.to_csv("Resources/ideal_cities_all_info.csv", index_label="City_ID")


# In[ ]:





# In[ ]:




