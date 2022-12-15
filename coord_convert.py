#def convert_dm(dm_df):
import pandas as pd
import re

def convert_dms(dms_df):
    deglist = []
    deglist2 = []
    for i, row in dms_df.iterrows():
        lat = row['Lat'].replace('"','')
        long = row['Long'].replace('"','')
        bLat = re.split(r'\N{DEGREE SIGN}|\'', lat)
        bLong = re.split(r'\N{DEGREE SIGN}|\'', long)
        min = float(bLat[1])
        min2 = float(bLong[1])
        deg_m = min/60
        deg_m2 = min2/60
        sec = float(bLat[2])
        sec2 = float(bLong[2])
        deg_s = sec/3600
        deg_s2 = sec2/3600
        dLat = float(bLat[0])
        dLong = float(bLong[0])
        deg = float(dLat + deg_m + deg_s)
        deg2 = float(dLong + deg_m2 + deg_s2)
        #id = dms_df['ID'][i]
        deglist.append(deg)
        deglist2.append(deg2)
    degdf = pd.DataFrame({'DD Lat Converted': deglist, 'DD Long Converted': deglist2})
    dms_df = dms_df.join(degdf)
    return(dms_df)

def convert_dd(dd_df):
    deglist1 = []
    deglist2 = []
    for i, row in dd_df.iterrows():
        lat = row['Lat'].replace('\N{DEGREE SIGN}','')
        long = row['Long'].replace('\N{DEGREE SIGN}','')
        deglist1.append(lat)
        deglist2.append(long)
    degdf = pd.DataFrame({'DD Lat Converted': deglist1, 'DD Long Converted': deglist2})
    dd_df = dd_df.join(degdf)
    return(dd_df)

def convert_ddm(ddm_df):
    deglist = []
    deglist2 = []
    for i, row in ddm_df.iterrows():
        lat = row['Lat'].replace('"','')
        long = row['Long'].replace('"','')
        bLat = re.split(r'\N{DEGREE SIGN}|\'', lat)
        bLong = re.split(r'\N{DEGREE SIGN}|\'', long)
        min = float(bLat[1])
        min2 = float(bLong[1])
        deg_m = min/60
        deg_m2 = min2/60
        dLat = float(bLat[0])
        dLong = float(bLong[0])
        deg = float(dLat + deg_m)
        deg2 = float(dLong + deg_m2)
        deglist.append(deg)
        deglist2.append(deg2)
    degdf = pd.DataFrame({'DD Lat Converted': deglist, 'DD Long Converted': deglist2})
    ddm_df = ddm_df.join(degdf)
    return(ddm_df)

def combine_df(dd, ddm, dms):
    dd = pd.concat([dd, ddm])
    combined_df = pd.concat([dms, dd])
    combined_df = combined_df.reset_index(drop = True)
    return(combined_df)