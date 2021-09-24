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

#creates SO-SS column by combining sales order and ship set. Strips float decimel
df['SO-SS'] = df['Sales_Order'].astype(str).str.strip('.0') + '-' + df['Ship_Set'].astype(str).str.strip('.0')

#delete where multiple headers
df.drop(df[df.Carton_ID == "Carton_ID"].index, inplace=True)

x = 1

while x == 1:
    query = input("Enter your query input for the Master FTP file\n"
                "1 - PalletID\n"
                "2 - Carton ID\n"
                "3 - SO-SS\n"
                "4 - SQL Query\n"
                "5 - exit program\n"
                "0 - save previous output"
                "> ")
    print("You have selected: ", query)

    if query == "1":
        PalletID = input("Enter in your Pallet ID: ")
        print("You entered the pallet ID of: ", PalletID)
        PLout = df['Pallet_ID'] == PalletID #creates mask
        print(df[PLout])
        temp = df[PLout]
    elif query == "2":
        CartonID = int(input("Enter in your carton ID (CID): "))
        print("You entered CID: ", CartonID)
        CIDout = df['Carton_ID'] == CartonID #creates mask
        print(df[CIDout])
        temp = df[CIDout]
    elif query =="3":
        SOSS = input("Enter in your SO-SS: ")
        print("You entered in the SO-SS: ", SOSS)
        SOSSout = df['SO-SS'] == SOSS #creates mask
        print(df[SOSSout])
        temp = df[SOSSout]
    elif query =="4":
        customer_choice = input("Enter 1 to query End Customer or 2 to query Ship To customer. ")
        if customer_choice == "1":
            text = input("Enter in your customer string: ")
            # search by multiple equal terms
            # df[df['Behavior'].str.contains('nt|nv', na=False)]
            temp_df = df[df['END_CUSTOMER_NAME'].str.contains(text, na=False, case=False)] #creates df
            print(temp_df)
            temp = temp_df
        elif customer_choice == "2":
            text = input("Enter in your customer string: ")
            temp_df = df[df['SHIP_TO_CUSTOMER_NAME'].str.contains(text, na=False, case=False)] #creates df
            print(temp_df)
            temp = temp_df
        else:
            print("Input invalid.")
    elif query =="5":
        print("Goodbye")
        break
    elif query =="0":
        temp.to_csv('/mnt/c/Users/WMINSKEY/Output/query_output.csv',index=False)

