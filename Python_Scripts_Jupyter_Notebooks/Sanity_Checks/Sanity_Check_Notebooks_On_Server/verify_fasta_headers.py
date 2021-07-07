import pandas as pd
import os
import sys
from Bio import SeqIO
import Bio

from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio import SeqIO

## Begin script
# Read file, input is a .xlsx file
file_name = str(sys.argv[1])
fasta_files = str(sys.argv[2])
run_IDs = str(sys.argv[3])
output_path = str(sys.argv[4])

write_test_result(file_name,fasta_files,runIDS,output_path)
        

def split_fasta_name(fasta_file_name):
    chars = []
    for char in fasta_file_name:
        if not char.isalnum() and not char.isalpha():
            chars.append(char)
            
    return chars

def parse_file(file_name):
    # Use pandas to parse file, identify sheets
    table = pd.ExcelFile(file_name)
    sheets = table.sheet_names
    number_sheets = len(sheets)

    ### Select metadata spreadsheet
    metadata_sheet = ""
    for i in range(number_sheets):
        if "Metadata"== sheets[i] or "metadata"==sheets[i]:
            metadata_sheet = metadata_sheet + sheets[i]
            break 
        # Need to design test that catches when there is no metadata spreadsheet ; what if there are multiple metadata sheets?        
    
    return metadata_sheet

def get_runID_FASTA_name(file_name):
    metadata_sheet = parse_file(file_name)
    
        
    metadata = table.parse(metadata_sheet)

    # Isolate file columns
    iR_fasta = metadata["fasta_file_name"]
    iR_runID = metadata["run_id"]

    return [iR_fasta,iR_runID]   
    

def perform_split_header_test(fasta_files):
    
    records = list(SeqIO.parse(fasta_files, "fasta"))
    
    number_id = len(records)
    
    first_char = split_fasta_name(records[0].id)[0]
    
    check_first_char = [[False,i] for i in range(number_id) if split_fasta_name(records[i].id)[0]!=first_char]
    
    return check_first_char

def perform_runID_in_FASTA_header(fasta_files,run_IDs):
    
    records = list(SeqIO.parse(fasta_files, "fasta"))
    
    number_id = len(records)
    
    first_char = split_fasta_name(records[0].id)[0]
    
    all_the_records = [records[i].id.split(first_char)[0] for i in range(number_id)]
    
    test = [[False,i] for i in range(number_id) if run_IDs != all_the_records[i]]
    
    return test

def write_test_result(file_name,fasta_files,runIDs,output_path):
    
    check_first_char = perform_split_header_test(fasta_files)
    
    number_wonky_format = len(check_first_char)
    
    check_content_header_test = perform_runID_in_FASTA_header(fasta_files,run_IDs)
    
    number_mis_header = len(check_content_header_first)
    
    file_content = [file_name,number_wonky_format,number_mis_header]
    
    with open(output_path + "RUN_ID_IN_HEADER" + run_IDS) as f:
        for item in file_content:
            f.write(item)
    f.close()
    

        