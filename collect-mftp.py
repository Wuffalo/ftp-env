# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:30:25 2018

@author: c05wmi1
"""

import pandas as pd
import os

path_to_FTP = "/mnt/shared-drive/05 - Office/FTP/FTP Files/"

def GetHumanReadable(size,precision=2):
    suffixes=['B','KB','MB','GB','TB']
    suffixIndex = 0
    while size > 1024 and suffixIndex < 4:
        suffixIndex += 1 #increment the index of the suffix
        size = size/1024.0 #apply the division
    return "%.*f%s"%(precision,size,suffixes[suffixIndex])

file_list = []

# walk file directory and create list of files
for subdir, dirs, files in os.walk(path_to_FTP):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".csv"):
            if filepath not in file_list:
                file_list.append(filepath)

df_list = []

# for each file name, grab file, format and append to list of dataframes
for f in file_list:
    sheet = pd.read_csv(f, error_bad_lines=False)
    f_source = os.path.basename(f).strip('.csv')
    sheet["FTPday"] = f_source
    b_size = os.stat(f).st_size
    sheet["FTPsize"] = b_size
    df_list.append(sheet)

Master_FTP = pd.concat(df_list, ignore_index=True, sort=False)

Master_FTP.to_csv('C:/Users/WMINSKEY/Output/Master_FTP.csv',index=False)