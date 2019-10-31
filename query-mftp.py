# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:59:28 2019

@author: c05wmi1
"""

import pandas as pd

path_to_FTP = 'C:/Users/WMINSKEY/Output/Master_FTP.csv'
MFTP = pd.read_csv(path_to_FTP)

# MFTP.loc[:, ~MFTP.columns.str.contains('^Unnamed')] delete all empty columns, column name start with Unnamed


# =============================================================================
# def OpenMasterFTP():
#     MFTP = pd.read_csv(path_to_FTP)
#     return MFTP
# =============================================================================

# =============================================================================
# def QueryPalletID(PalletID):
#     qPallet =   """
#                 SELECT Pallet_ID, Carton_ID, Weight
#                 FROM MFTP
#                 WHERE MFTP.Pallet_ID = PalletID
#                 """
#     return pdsql.pysqldf(qPallet)
# =============================================================================

## Ask user which input they want to provide and record it

query = input("Enter your query input for the Master FTP file\n"
              "1 - PalletID\n"
              "2 - Carton ID\n"
              "3 - SO-SS\n"
              "> ")
print("You have selected: ", query)

if query == "1":
    PalletID = input("Enter in your Pallet ID: ")
    print("You entered the pallet ID of: ", PalletID)
    print(MFTP.query('Pallet_ID == PalletID', inplace = True))
elif query == "2":
    CartonID = input("Enter in your carton ID (CID): ")
    print("You entered CID: ", CartonID)
elif query =="3":
    SOSS = input("Enter in your SO-SS: ")
    print("You entered in the SO-SS: ", SOSS)

foo = MFTP.loc[df['Pallet_ID']==PalletID]
foo = df.ix[(df['column1']==value) | (df['columns2'] == 'b') | (df['column3'] == 'c')]
