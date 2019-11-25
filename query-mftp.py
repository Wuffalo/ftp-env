# -*- coding: utf-8 -*-
"""
2019
@author: wuffalo
"""

import pandas as pd

path_to_excel = "/mnt/c/Users/WMINSKEY/Output/Master_FTP.csv"

df = pd.read_csv(path_to_excel, parse_dates=[7,8], infer_datetime_format=True)

#drop extra columns
df.drop(df.iloc[:,16:], inplace=True, axis=1)

#creates SO-SS column by combining sales order and ship set
df['SO-SS'] = df['Sales_Order'].astype(str) + '-' + df['Ship_Set'].astype(str)

#delete where multiple headers
df.drop(df[df.Carton_ID == "Carton_ID"].index, inplace=True)

x = 1

while x == 1:
    query = input("Enter your query input for the Master FTP file\n"
                "1 - PalletID\n"
                "2 - Carton ID\n"
                "3 - SO-SS\n"
                "4 - SQL Query\n"
                "5 - exit program"
                "> ")
    print("You have selected: ", query)

    if query == "1":
        PalletID = input("Enter in your Pallet ID: ")
        print("You entered the pallet ID of: ", PalletID)
        PLout = df['Pallet_ID'] == PalletID
        print(df[PLout])
    elif query == "2":
        CartonID = int(input("Enter in your carton ID (CID): "))
        print("You entered CID: ", CartonID)
        CIDout = df['Carton_ID'] == CartonID
        print(df[CIDout])
    elif query =="3":
        SOSS = input("Enter in your SO-SS: ")
        print("You entered in the SO-SS: ", SOSS)
        SOSSout = df['SO-SS'] == SOSS
        print(df[SOSSout])
    elif query =="5":
        break