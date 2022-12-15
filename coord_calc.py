from cmath import inf
import pandas as pd
import re
from datetime import datetime
from dateutil.parser import parse
import math
import sympy

def get_time(df, i, row):
    time_delta = []
    d_df = pd.DataFrame()
    ID = row['ID']
    d_df = df.drop([i], inplace = False)
    time_delta = []
    indexlist = []
    for j, k in d_df.iterrows():
        time_delta.append(k['Time'] - row['Time'])
        indexlist.append(j)
    delta_df = pd.DataFrame({'Delta Time' : time_delta}, index = indexlist)
    d_df.merge(delta_df, left_index=True, right_index = True)
    d_df.sort_values(by=['Delta Time'])
    print("this is delta df" , d_df)
    return(d_df)

def get_distance(d_df, k, df, row, i, j):
    wentthru = 0
    #time = d_df.at[j, 'Delta Time']
    distance = 0
    if k['ID'] == row['ID']:
        if time.total_seconds() > 0 & wentthru == 0:
            print("This is your time and idk how you lost it" , time)
            distance = 0
            k_long = float(k['DD Long Converted'])
            long_conv = float(row['DD Long Converted'])
            lat_conv = float(row['DD Lat Converted'])
            long_side = abs(long_conv - k_long)
            k_lat = float(k['DD Lat Converted'])
            lat_side = abs(lat_conv - k_lat)
            distance = float(math.sqrt(long_side**2 + lat_side**2))
            print("This is the distance for ", row['ID'], " from", row['Coordinates'], "to ", k['Coordinates'] , "with time of" , time,  ' : ' , distance)
            #df.at[i, 'Distance (DD)'] = distance
            wentthru = 1  
            #df.at[i, 'Time elapsed'] = time
            #df.at[i, 'Distance (DD)'] = distance
            return(df, distance)




def distance_formula(df):

    dista = []
    tim = []
    velo = []
    dis_df = pd.DataFrame({'Distance (DD)' : dista, 'Time elapsed' : tim, "Avg Velocity" : velo})
    df = pd.concat([df, dis_df])

    for i, row in df.iterrows():
        d_df = get_time(df, i, row)
        print(d_df)
        for j, k in d_df.iterrows():
            print(d_df)
            df, distance = get_distance(d_df, k, df, row, i, j)
            
            print("This my distance" , distance)
            '''time_delta = df.at[i, 'Time elapsed']
            time_delta = pd.Timedelta(time_delta)
            time_delta = time_delta.total_seconds()
            print(type(time_delta), time_delta)
            print(type(row['Distance (DD)']), row['Distance (DD)'])
            row["Avg Velocity"] = row['Distance (DD)'] / time_delta
            print(row["Avg Velocity"])'''
    print(df)
    return(df)