## Script Author: Laura Gutierrez Funderburk
## Supervised by: Dr. Felix Breden, Dr. Jamie Scott, Dr. Brian Corrie
## Created on: October 21
## Last modified on: October 21

import requests
import json
import csv
import pandas as pd

# READ FROM URL
# EXAMPLE JSON_Content = "https://ipa.ireceptor.org/v2/samples" or JSON_Content = "https://ipa.ireceptor.org/v2/sequences_summary"

JSON_Content = str(sys.argv[1])

#AIRR Standardards
min_AIRR_std = "/home/lgutierrezfunderburk/Documents/Notebooks/iReceptor/airr-standards/AIRR_Minimal_Standard_Data_Elements.xlsx"

df_min_AIRR_std = pd.read_excel(min_AIRR_std)

min_std = [item for item in df_min_AIRR_std["AIRR Formats WG field name"]]

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

"""BEGIN SCRIPT"""

[df_items,df_sum] = get_dataframes(JSON_Content)


check_min_std_df_items = [[item in df_items.columns,item] for item in min_std]
check_min_std_df_summary = [[item in df_summary.columns,item] for item in min_std]
count_items = 0
for i in range(len(check_min_std_df_items)):
    if True in check_min_std_df_items[i]:
        count_items +=1

count_sum = 0
for i in range(len(check_min_std_df_summary)):
    if True in check_min_std_df_summary[i]:
        count_sum +=1

message_arr = []
message_arr.append("Begin Sanity Check on API\n")
message_arr.append("Check performed on search " + str(JSON_Content) + "\n")
message_arr.append("Sanity Check: AIRR minimum standards\n")
message_arr.append("Summary\n")
message_arr.append("Items category: " + str(count_items) + " out of " + str(len(min_std)) + " standards were met\n")
message_arr.append("Summary category: " + str(count_sum) + " out of " + str(len(min_std)) + " standards were met\n")

