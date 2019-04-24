import calendar
import datetime
import json
import numpy as np
import pandas as pd
import requests
import sys

def getbikecountinformation(startdate, enddate):
    """
    This module downloads the Mountain to Sound Trail Bikes Count dataset
    from seattle.data.gov at a specific station in the trail between a 
    given start and end date  
    """
    # define the API endpoints for acquiring the datasets
    mountaintosoundtrailendpoint = 'https://data.seattle.gov/resource/ekqi-b8f3.json'

    #define the headers used for the API calls. 
    headers = {'User-Agent' : 'https://github.com/sumanbhagavathula'
               ,'From' : 'sumanbh@uw.edu'
               ,'Host': 'data.seattle.gov'
               ,'Accept':'application/json'
               ,'X-App-Token': 'gBpsY5UwY6V9flay65beFbf9o' 
              }

    mtstrailwestofi90bikecountinformation = pd.DataFrame()

    try:
        params = {}
        myquery='SELECT date, bike_north, bike_south WHERE date BETWEEN "' \
            + startdate + 'T00:00:00.000" AND "' +  enddate + 'T23:59:59.000"'
        endpoint = mountaintosoundtrailendpoint+'?$query='+myquery
        api_call = requests.get(endpoint.format(**params))
        results=api_call.json()
        mtstrailwestofi90bikecountinformation = \
            mtstrailwestofi90bikecountinformation.append(pd.DataFrame(results))
    except:
        print("Unexpected error while processing")

    return pd.DataFrame(mtstrailwestofi90bikecountinformation)


def test_create_dataframe(input_dataframe):
    """
    This module accepts an input dataframe and checks for below:
    1. The columns date, bike_north and bike_south
    2. The data type for the columns as Object
    3. the dataset has atleast 10 rows 
    """
    if not('date' in input_dataframe.columns \
       and 'bike_north' in input_dataframe.columns \
       and 'bike_south' in input_dataframe.columns):
        print("Expected Columns not present");
        return False

    df_datatypes = input_dataframe.dtypes

    if not('O' == df_datatypes['date'] \
            and 'O' == df_datatypes['bike_north'] \
            and 'O' == df_datatypes['bike_south']): 
        print("Data type requirement of columns not met");
        return False

    if(10 >= len(input_dataframe.index)):
        print(len(input_dataframe.index))
        print("Does not have adequate number of rows");
        return False
    return True
