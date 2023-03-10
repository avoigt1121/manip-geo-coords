
import pandas as pd
import re
from datetime import datetime
from dateutil.parser import parse


def read_file():
    string = open('RANDOMtextdocumentwithcoords.txt', 'r')
    string_sp = string.read()
    string_sp = string_sp.replace(',', "")
    return(string_sp)


def find_dms(string_sp):
    dms_df = pd.DataFrame
    dms_list = []
    count = 0
    counter = 0
    for dms in re.finditer('[-0-9\d{1,4}]+\N{DEGREE SIGN}+[0-9\d{2}]+\'+[0-9.\d{2,7}]+\"+\s+[-0-9\d{1,4}]+\N{DEGREE SIGN}+[0-9\d{2}]+\'+[0-9.\d{2,7}]+\"', string_sp):
        dms_date = string_sp[dms.end():dms.end()+26]
        dms_date = parse(dms_date)
        dmsID = string_sp[dms.end()+27:dms.end()+40]
        dmsID = dmsID.split()[0]
        coords = dms.group()
        counter += 1
        lat = coords.split()[0]
        long = coords.split()[1]
        dms_true = True
        dd_true = False
        dm_true = False
        dms_i = [dms.group(), lat, long, dms_date, dmsID, dms_true, dd_true, dm_true]
        dms_list.append([])
        for j in range(8):
            dms_list[count].append(dms_i[j])
        count += 1
    dms_df = pd.DataFrame(dms_list, columns = ['Coordinates', 'Lat', 'Long','Time', 'ID', 'Original DMS?', 'Original DD?', 'Original DDM?'])
    dms_df = dms_df.sort_values(by = ['ID'], ascending = True)
    return(dms_df)

def find_dd(string_sp):
    dd_df = pd.DataFrame
    dd_list = []
    count = 0
    counter = 0
    for dd in re.finditer('[-0-9\d{1,4}]+.+[0-9.\d{2,7}]+\N{DEGREE SIGN}+\s+[-0-9\d{1,4}]+.+[0-9.\d{2,7}]+\N{DEGREE SIGN}', string_sp):
        dd_date = string_sp[dd.end():dd.end()+26]
        dd_date = parse(dd_date)
        ddID = string_sp[dd.end()+27:dd.end()+40]
        ddID = ddID.split()[0]
        coords = dd.group()
        counter += 1
        lat = coords.split()[0]
        long = coords.split()[1]
        dms_true = False
        dd_true = True
        ddm_true = False
        dd_i = [dd.group(), lat, long, dd_date, ddID, dms_true, dd_true, ddm_true]
        dd_list.append([])
        for j in range(8):
            dd_list[count].append(dd_i[j])
        count += 1
    dd_df = pd.DataFrame(dd_list, columns = ['Coordinates', 'Lat', 'Long','Time', 'ID','Original DMS?', 'Original DD?', 'Original DDM?'])
    dd_df = dd_df.sort_values(by = ['ID'], ascending = True)
    return(dd_df)


def find_ddm(string_sp):
    ddm_df = pd.DataFrame
    ddm_list = []
    count = 0
    counter = 0
    for ddm in re.finditer('[-0-9\d{1,4}]+\N{DEGREE SIGN}+[0-9\d{2}]+.+[0-9\d{2,7}]+\'+\s+[-0-9\d{1,4}]+\N{DEGREE SIGN}+[0-9\d{2}]+.+[0-9\d{2,7}]+\'', string_sp):
        ddm_date = string_sp[ddm.end():ddm.end()+26]
        ddm_date = parse(ddm_date)
        ddmID = string_sp[ddm.end()+27:ddm.end()+40]
        ddmID = ddmID.split()[0]
        coords = ddm.group()
        counter += 1
        lat = coords.split()[0]
        long = coords.split()[1]
        dms_true = False
        dd_true = False
        ddm_true = True
        ddm_i = [ddm.group(), lat, long, ddm_date, ddmID, dms_true, dd_true, ddm_true]
        ddm_list.append([])
        for j in range(8):
            ddm_list[count].append(ddm_i[j])
        count += 1
    ddm_df = pd.DataFrame(ddm_list, columns = ['Coordinates', 'Lat', 'Long', 'Time', 'ID', 'Original DMS?', 'Original DD?', 'Original DDM?'])
    ddm_df = ddm_df.sort_values(by = ['ID'], ascending = True)
    return(ddm_df)
