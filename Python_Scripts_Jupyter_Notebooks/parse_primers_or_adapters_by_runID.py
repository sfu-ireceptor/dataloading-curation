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
    
    # Get primers
    primer = handle_primers(file_name,primer_type)
    
    # Split them into an array
    primer_split = [item.split(" ") for item in primer]
    
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
    # Do we want reverse complement?
    if rc_option=="False": 
        # No
        clean_primer = clean_up_primers(file_name,primer_type)
       
    elif rc_option=="True":
        # Yes
        clean_primer = reverse_complement(file_name,primer_type)
        
    
    #check sizes match:
    size_runID, size_cleanprimer = len(run_ID),len(clean_primer)
    
    if size_runID==size_cleanprimer:
        
        run_ID_primer_dictionary = {run_ID[i]:clean_primer[i] for i in range(size_runID)}
        
    # Need to develop test for when this fails. 
    return run_ID_primer_dictionary


## Begin script
# Read file, input is a .xlsx file
file_name = str(sys.argv[1])
primer_option = str(sys.argv[2])
reverse_complement_option = str(sys.argv[3])



test_dic = build_dictionary(file_name,primer_option,reverse_complement_option)

print(test_dic)
        
# # Create dictionary, where run_id is key, and primers are values
# size = len(clean_forward_primers)
# run_ID_forward_dic = {run_ID[i]:clean_forward_primers[i] for i in range(size)}
# run_ID_reverse_dic = {run_ID[i]:clean_reverse_primers[i] for i in range(size)}
# run_ID_rc_forward_dic =  {run_ID[i]:clean_rc_forward_primers[i] for i in range(size)}
# run_ID_rc_reverse_dic = {run_ID[i]:clean_rc_reverse_primers[i] for i in range(size)}

