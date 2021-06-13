import pandas as pd
import numpy as np
import json
import requests

df = pd.read_csv('playas_translated_columns_new_1') #load our data

ratings = [] #two empty lists that will make up our new columns
google_place_id = []

for index, row in df.iterrows(): #for every row of the column
    name = row['Name'].replace(" ", "%20") #replace spaces with %20 to fit url
    lat = row['lat']
    lng = row['lon']
    
    #replace ENTERAPIKEYHERE in the below URL with the API key:
    nearby = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=ENTERAPIKEYHERE&location={lat},{lng}&radius=1000&name={name}&type=natural_feature"
    response=requests.get(nearby) #access url
    response.raise_for_status() #check for errors
    
    r=json.loads(response.text) #r is the response from the api as a python variable
    try: # try to fill ratings, google_place_id with values, except if URl returned no valid response
        ratings.append(r['results'][0]['rating'])
    except IndexError:
        ratings.append(np.nan)
    try:
        google_place_id.append(r['results'][0]['place_id'])
    except IndexError:
        google_place_id.append(np.nan)
        
df['rating'] = ratings #add column to dataframe
df['google_place_id'] = google_place_id #add column to dataframe
