# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-08-16T19:42:14.609747Z","iopub.execute_input":"2022-08-16T19:42:14.610942Z","iopub.status.idle":"2022-08-16T19:42:14.646181Z","shell.execute_reply.started":"2022-08-16T19:42:14.610890Z","shell.execute_reply":"2022-08-16T19:42:14.644796Z"}}
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:26:53 2022

@author: thaer
"""

import pandas as pd   
import math

# Read Network transactions 
def readNetworkTransactionsFromCSECICIDS2018():
    
    df_1 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
    df_2 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
    df_3 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Friday-23-02-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
    df_4 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Thuesday-20-02-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
    df_5 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Thursday-01-03-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
    df_6 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Thursday-15-02-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
    df_7 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Thursday-22-02-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
    df_8 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Wednesday-14-02-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
    df_9 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Wednesday-21-02-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
    df_10 = pd.read_csv('../Dataset/CSE-CIC-IDS2018/CIC/Wednesday-28-02-2018_TrafficForML_CICFlowMeter.csv', low_memory=False)
 
    df_col = {'df1':df_1,'df_2':df_2,'df_3':df_3,'df_4':df_4,'df5':df_5,'df_6':df_6,'df_7':df_7,'df_8':df_8,'df_9':df_9,'df_10':df_10}

    frames = [df_1.reset_index(drop=True),df_2.reset_index(drop=True), 
              df_3.reset_index(drop=True),df_4.reset_index(drop=True),df_5.reset_index(drop=True),df_6.reset_index(drop=True), 
              df_7.reset_index(drop=True),df_8.reset_index(drop=True),df_9.reset_index(drop=True),df_10.reset_index(drop=True)]

    df_all = pd.concat(frames,
                       ignore_index=True)
    
    
    for i in df_col:
        
        print('----------',i,'----------------')
        print('Rows',f"{len(df_col[i].index):,}")
        print('Shape',df_col[i].shape)    
        print('--------------------------')
        print()
        print()
        
    print('Full Dataframe of Network Transactions in CSE-CIC-IDS2018')
    print('Rows',f"{len(df_all.index):,}")
    print('Shape',df_all.shape)

    print()
    
    del [df_1,df_2,df_3,df_4,df_5,df_6,df_7,df_8,df_9,df_10]
    
    print(df_all[:10])
    
    #return the full network Trx list
    return df_all
#----------------------------------------------------------------------
#Read features(columns) list
def prepareDataFrames():
    
    df_columns = pd.read_csv('../Dataset/UNSW_NB15/NUSW-NB15_features.csv',
                             sep=",", encoding='cp1252')
    #print(list(df_columns.columns))
    #print(df_columns)
    
    return  df_columns   
#-----------------------------------------------------------------------

# Read Network transactions 
def readNetworkTransactions():

    #read Network Features 
    df_columns = prepareDataFrames()
    
    df_1 = pd.read_csv('../Dataset/UNSW_NB15/UNSW-NB15_1.csv', low_memory=False)
    #print(df_1[:10])
    df_1.columns = list(df_columns.iloc[:, 1])
    #print(list(df_1.columns))


    df_2 = pd.read_csv('../Dataset/UNSW_NB15/UNSW-NB15_2.csv', low_memory=False)
    #print(df_2[:10])
    df_2.columns = list(df_columns.iloc[:, 1])

    df_3 = pd.read_csv('../Dataset/UNSW_NB15/UNSW-NB15_3.csv', low_memory=False)
    #print(df_3[:10])
    df_3.columns = list(df_columns.iloc[:, 1])

    df_4 = pd.read_csv('../Dataset/UNSW_NB15/UNSW-NB15_4.csv', low_memory=False)
    #print(df_4[:10])
    df_4.columns = list(df_columns.iloc[:, 1])

    
    df_col = {'df1':df_1,'df_2':df_2,'df_3':df_3,'df_4':df_4}
    
    frames = [df_1.reset_index(drop=True),df_2.reset_index(drop=True), 
              df_3.reset_index(drop=True),df_4.reset_index(drop=True)]
    
    df_all = pd.concat(frames,
                       ignore_index=True)
    for i in df_col:
        
        print('----------',i,'----------------')
        print('Rows',f"{len(df_col[i].index):,}")
        print('Shape',df_col[i].shape)    
        print('--------------------------')
        print()
    print()
    print('Full Dataframe of Network Transactions')
    print('Rows',f"{len(df_all.index):,}")
    print('Shape',df_all.shape)

    print()
    
    del [df_1,df_2,df_3,df_4]

    print(df_all[:10])
    #return the full network Trx list
    return df_all
#--------------------------------------------------------------------- 
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever
#--------------------------------------------------------------------- 
def hexToAminoAcidCode(argument):
    switcher = {
        "0":"K",
        "1":"T",
        "2":"Y",
        "3":"I",
        "4":"Q",
        "5":"H",
        "6":"D",
        "7":"E",
        "8":"R",
        "9":"F",
        "a":"S",
        "b":"V",
        "c":"Y",
        "d":"W",
        "e":"P",
        "f":"F"        
    }
    return switcher.get(argument, "")
#----------------------------------------------------------
def mapHexToAminoAcidCode(iFloatHex):#0xab
    sFullHex = remove_prefix(str(iFloatHex),'0x')
    sResult = ""
    for cChar in sFullHex:
        sResult +=hexToAminoAcidCode(cChar)
        
    return sResult
#----------------------------------------------------------
def digitToAminoAcidCode(argument):
    switcher = {
        '0': "K",#"AAA", Lys
        '1':"T",#"ACA", Thr
        '2':"Y",#"UAU", Tyr
        '3':"I",#"AUA", Ile
        '4':"Q",#"CAA", Gln
        '5':"H",#"CAC", His
        '6':"D",#"GAU", Asp
        '7':"E",#"GAG", Glu
        '8':"R",#"AGA", Arg
        '9':"F",#"UUC", Phe
        '.':"S",#"UCA" Ser
    }
    return switcher.get(argument, "")
#-----------------------------------------------------------
def digitToAminoAcidCodeForMinus(argument):
    switcher = {
        '0':"V",#"GUA", Val
        '1':"Y",#"UAC", Tyr        
        '2':"W",#"UGG", Trp        
        '3':"P",#"CCC", Pro
        '4':"F",#"UUU", Phe
        '5':"L",#"CUA", Leu
        '6':"G",#"GGA", Gly
        '7':"C",#"UGU", Cys
        '8':"N",#"AAU", Asn
        '9':"A",#"GCG", Ala
        '.':"S",#"UCA" Ser  ----> I keep it same as in positive number representation
        '-':"M"#"AUG" Met
    }
    return switcher.get(argument, "")
#----------------------------------------------------------
def mapDigitToAminoAcidCode(iDigitsSeries):#Series of Scaled numbers (ex. -1.447934)
    for index , iDigits in iDigitsSeries.items():
        if iDigits is not None:
            iDigits = str(iDigits).strip()
            fnMappingFunction = mapHexToAminoAcidCode
            sResult = ""
            for cChar in str(iDigits):
                iHexAsciiCode = hex(ord(cChar))
                sResult += fnMappingFunction(cChar) #build AminoAcid DNA code ex AAAAACGACAGA...
        else:
            sResult = ""
        iDigitsSeries[index] = sResult
    return iDigitsSeries
#-----------------------------------------------------------
def checkSimilarity(X,Y,threshold=0.7, rel_tolerance=0.1):
    c = [math.isclose(x1,y1,rel_tol=rel_tolerance) for x1, y1 in zip(X, Y)]
    cItems = len(c)
    fRatio = math.floor(threshold * cItems)
    count_True = c.count(True)
    bResult = False
    if count_True >= fRatio:
        bResult = True
    return bResult
    
#----------------------------------------------------------
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False