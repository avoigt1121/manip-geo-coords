from cmath import inf
import pandas as pd
import re
from datetime import datetime
from dateutil.parser import parse
import math
import sympy


def distance_formula(df):
    dista = []
    tim = []
    dis_df = pd.DataFrame({'Distance (DD)' : dista, 'Time elapsed' : tim})
    df = pd.concat([df, dis_df])

    for i, row in df.iterrows():
        d_df = pd.DataFrame()
        ID = row['ID']
        long_conv = float(row['DD Long Converted'])
        lat_conv = float(row['DD Lat Converted'])
        d_df = df.drop([i], inplace = False)
        time_delta = []
        indexlist = []
        for j, k in d_df.iterrows():
            time_delta.append(k['Time'] - row['Time'])
            indexlist.append(j)
        delta_df = pd.DataFrame({'Delta Time' : time_delta}, index = indexlist)
        d_df = d_df.merge(delta_df, left_index=True, right_index = True)
        for j, k in d_df.iterrows():
            wentthru = 0
            time = k['Delta Time']
            if time.total_seconds() > 0 & wentthru == 0:
                distance = 0
                if k['ID'] == row['ID']:
                    k_long = float(k['DD Long Converted'])
                    long_side = abs(long_conv - k_long)
                    k_lat = float(k['DD Lat Converted'])
                    lat_side = abs(lat_conv - k_lat)
                    distance = float(math.sqrt(long_side**2 + lat_side**2))
                    print("This is the distance for ", row['ID'], " from", row['Coordinates'], "to ", k['Coordinates'] , "with time of" , time,  ' : ' , distance)
                    df.at[i, 'Distance (DD)'] = distance
                    wentthru = 1  
            elif k['ID'] == row['ID']:
                print(df.at[i, 'Distance (DD)'])
                if math.isnan(df.at[i, 'Distance (DD)']):
                    if math.isnan(distance):
                        df.at[i, 'Distance (DD)'] = 0
                    else:
                       df.at[i, 'Distance (DD)'] = distance
        df.at[i, 'Time elapsed']= time
        #df['Distance'][row] = distance
    print("this be df :" , df)
