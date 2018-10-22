## Script Author: Laura Gutierrez Funderburk
## Supervised by: Dr. Felix Breden, Dr. Jamie Scott, Dr. Brian Corrie
## Created on: October 21
## Last modified on: October 21

import requests
import json
import csv
import pandas as pd


JSON_Content = str(sys.argv[1])

#AIRR Standardards
min_AIRR_std = "/home/lgutierrezfunderburk/Documents/Notebooks/iReceptor/airr-standards/AIRR_Minimal_Standard_Data_Elements.xlsx"

df_min_AIRR_std = pd.read_excel(min_AIRR_std)

min_std = [item for item in df_min_AIRR_std["AIRR Formats WG field name"]]

study = min_std[0:10]
subject = min_std[10:22]
diag_int = min_std[22:30]
sample = min_std[30:38]
process = min_std[38:66]
data_raw_reads = min_std[66:67]
process = min_std[67:73]
data_proc_seq = min_std[73:82]
data_proc_seq

# Need stronger testing for user input
def type_of_entry(JSON_Content):

    test_type_search = []
    if "sequences_summary" in JSON_Content.split("/v2/")[1]:
        test_type_search.insert(0,False)
        test_type_search.insert(1,True)
        test_type_search.insert(2,False)
    elif "samples" in JSON_Content.split("/v2/")[1]:
        test_type_search.insert(0,True)
        test_type_search.insert(1,False)
        test_type_search.insert(2,False)
    else:
        test_type_search.insert(0,False)
        test_type_search.insert(1,False)
        test_type_search.insert(2,True)
    
    return test_type_search

def get_dataframes(JSON_Content):
    
    test_type_search = type_of_entry(JSON_Content)
    
    dataframes = []
    
    column_e = [0 for i in range(5)]
    df = pd.DataFrame(columns=column_e)
    
    if test_type_search[2]!=True:
        DATA = json.loads(requests.get(JSON_Content).text)
        if test_type_search[1] == True:
            df_items = pd.DataFrame.from_dict(DATA["items"])
            df_summary = pd.DataFrame.from_dict(DATA["summary"])

            dataframes.insert(0,df_items)
            dataframes.insert(1,df_summary)
        else:
            df_summary = pd.DataFrame.from_dict(DATA)
            
            dataframes.insert(0,df)
            dataframes.insert(1,df_summary)
    else:
        
        
        
        dataframes.insert(0,df)
        dataframes.insert(1,df)
    return dataframes