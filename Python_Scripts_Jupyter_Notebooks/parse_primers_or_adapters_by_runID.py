## Script Author: Laura Gutierrez Funderburk
## Supervised by: Dr. Felix Breden, Dr. Jamie Scott, Dr. Brian Corrie
## Created on October 9
## Last modified on October 14


# Import libraries
import sys
import pandas as pd
from Bio import SeqIO
import Bio

# This function takes as input an Excel file name containing a metadata
# spreadsheet, for example, "./Metadata_spreadsheets/Mun/Munson_2016.xlsx"

# It returns the appropriate sheet containing metadata information

def get_metadata_sheet(file_name):

    # Tabulate Excel file
    table = pd.ExcelFile(file_name)
    # Identify sheet names in the file and store in array
    sheets = table.sheet_names
    # How many sheets does it have
    number_sheets = len(sheets)

    ### Select metadata spreadsheet
    metadata_sheet = ""
    for i in range(number_sheets):
        # Check which one contains the word metadata in the title and hold on to it
        if "Metadata"== sheets[i] or "metadata"==sheets[i]:
            metadata_sheet = metadata_sheet + sheets[i]
            break 
        # Need to design test that catches when there is no metadata spreadsheet ; what if there are multiple metadata sheets?        
        
    # This is the sheet we want
    metadata = table.parse(metadata_sheet)
    
    return metadata

# This function takes as input an Excel spreadsheet and a column name containing either primers or adapters, for example 
# "./Metadata_spreadsheets/Mun/Munson_2016.xlsx","forward_primers" corresponds to the spreadsheet name and the column of interest

# It returns an array whose elements are the entries found under the column of interest
def handle_primers(file_name,primer_type):
    
    # Use function above to get the sheet we want
    metadata = get_metadata_sheet(file_name)
    # List comprehension to get all entries under the column of interest
    primer = [item for item in metadata[primer_type]]
    
    return primer

# This function takes as input an Excel spreadsheet and a column name containing either primers or adapters, for example 
# "./Metadata_spreadsheets/Mun/Munson_2016.xlsx","forward_primers" corresponds to the spreadsheet name and the column of interest

# The output is an array with "clean" primers - some primers have spaces or other characters in between that should not be there
def clean_up_primers(file_name,primer_type):
    
    # NEED TO DESIGN TEST THAT DEALS WITH NON UNIFORM ENTRIES, for example, when 
    # there are NaN values in every other entry
    
    # Get primers
    primer = handle_primers(file_name,primer_type)
    
    number_primers = len(primer)
    
    primer_split = []
    
    for i in range(number_primers):
        if type(primer[i])==float:
            primer_split.append(" ")
        else:
            primer_split.append(primer[i].split(" "))
            
    # Clean them up
    clean_primer_split = [[item[i] for i in range(len(item)) if item[i].isalpha() ] for item in primer_split]
    
    return clean_primer_split

# This function takes as input an Excel spreadsheet and a column name containing either primers or adapters, for example 
# "./Metadata_spreadsheets/Mun/Munson_2016.xlsx","forward_primers" corresponds to the spreadsheet name and the column of interest

# The output is an array whose entries are the reverse complement of the entries found in the corresponding column
def reverse_complement(file_name,primer_type):
    
    #get clean primers
    clean_primer = clean_up_primers(file_name,primer_type)
    # count length of array once
    size = len(clean_primer)
    # get reverse complement of each entry, for each array 
    rc_clean_primer = [[Bio.Seq.reverse_complement(clean_primer[j][i])\
                            for i in range(len(clean_primer[j]))] for j in range(size)]

    return rc_clean_primer

# This function takes as input an Excel spreadsheet, a column name containing either primers or adapters and True or False
# depending on whether we want reverse complement or not , for example 
# "./Metadata_spreadsheets/Mun/Munson_2016.xlsx","forward_primers",False corresponds to the spreadsheet name and the column of interest
# and it indicates we want the original primers (not reverse complement)

# The output is a dictionary whose keys are run_id's and whose values are the corresponding primers, 

def build_dictionary(file_name,primer_type,rc_option):
    # get right sheet
    metadata = get_metadata_sheet(file_name)
    
    # identify run_ID
    run_ID = [item for item in metadata['run_id']]
    
    if type(run_ID[0])==float:
        
        size_runID = len(run_ID)
        new_runID = [run_ID[i] for i in range(1,size_runID)]  
    else:
        size_runID = len(run_ID)
        new_runID = [run_ID[i] for i in range(0,size_runID)]
       
    # Do we want reverse complement?
    if rc_option==False: 
        # No
        clean_primer = clean_up_primers(file_name,primer_type)
        #print(clean_primer)
    elif rc_option==True:
        # Yes
        clean_primer = reverse_complement(file_name,primer_type)
            
    #check sizes match:
    size_runID, size_cleanprimer = len(new_runID),len(clean_primer)
    #print(size_runID,size_cleanprimer)
    
    if size_runID==size_cleanprimer:
        
        run_ID_primer_dictionary = {new_runID[i]:clean_primer[i] for i in range(size_runID)}
        
    else:
        print(size_runID,size_cleanprimer)
    # Need to develop test for when this fails. 
    return run_ID_primer_dictionary

# This function takes as input a dictionary whose keys are runIDs and whose values are either
# forward/reverse primers or forward/reverse adapters, a directory to output the content, a key (a run ID), 
# the adapter type (-g,-a,-G,-A) appropriate for cutadapt, and extra information "output_filename"

# This function writes a string of adapters or primers separated by the adapter_type character

## For example, if the forward adapters associated with run ID SRR3500416 are 

# AGGAGCTCCAGATGAAAGACTC GCTCATCCTCCAGGTGCGGGAG, then this function will write on a file the string

#  -g AGGAGCTCCAGATGAAAGACTC -g GCTCATCCTCCAGGTGCGGGAG
def write_formatted_entries(dictionary,file_directory,key,adapter_type,output_filename):
    
    # Open file to write content on
    with open(file_directory + key + output_filename,"w") as f:
        # For each entry in the array stored under dictionary[key]
        for item in dictionary[key]:
            # Write string for cutadapt command 
            f.write(" " + str(adapter_type) + " " + str(item))
        f.close()

    
# This function will take as input an integer between 1 and 8, and it will output either
# An array with column names and a boolean value or a string indicating wrong option

# The column names correspond to forward/reverse primers or adapters, the boolean value indicates whether
# we want the reverse complement of the primers/adapters
def switch_menu(argument):
    switcher = {
        1: ["forward_primers",False],
        2: ["forward_primers",True],
        3: ["reverse_primers",False],
        4: ["reverse_primers",True],
        5: ["adapter_sequence_reverse",False],
        6: ["adapter_sequence_reverse",True],
        7: ["adapter_sequence_forward ",False],
        8: ["adapter_sequence_forward ",True]
    }
    
    return switcher.get(argument, "Invalid option was chosen, please select a number between 1 and 8")
    
## Begin script
# Read file, input is a .xlsx file
file_name = str(sys.argv[1])
directory = str(sys.argv[2])
key = str(sys.argv[3])
option = int(sys.argv[4])
adapter_type = str(sys.argv[5])
output_extra_info = str(sys.argv[6])

chosen_option = switch_menu(option)

if chosen_option=='Invalid option was chosen, please select a number between 1 and 8':
    print("Invalid option was chosen, please select a number between 1 and 8 \nPlease enter your command again")

else:

    dictionary = build_dictionary(file_name,chosen_option[0],chosen_option[1])
    
    write_formatted_entries(dictionary,directory,key,adapter_type,output_extra_info)


# Sample use
# python parse_primers_or_adapters_by_runID.py "./Metadata_spreadsheets/Mun/Munson_2016.xlsx" "./Metadata_spreadsheets/Mun/" "SRR3500416" 1 "-g" "_primer_forward.txt"
