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
        
metadata = table.parse(metadata_sheet)

# Isolate file columns
iR_fasta = metadata["fasta_file_name"]
iR_igblast = metadata["igblast_file_name"]
iR_imgt = metadata["imgt_file_name"]
iR_mixcr = metadata["mixcr_file_name"]
iR_runID = metadata["run_id"]

size_fasta = iR_fasta.count()
size_runID = iR_runID.count()
print(size_fasta,size_runID)

# Generate list comprehension 
fasta_files = [iR_fasta[i] for i in range(1,size_fasta)] 
run_IDs = [iR_runID[i] for i in range(1,size_fasta)] 


#size_test = len(fasta_files)

#print(size_test)

test_runID_fastaName_match = [[run_IDs[i],fasta_files[i]] for i in range(len(fasta_files))]

#print(test_runID_fastaName_match)

test_arr = []
for i in range(len(fasta_files)):
    if test_runID_fastaName_match[i][0] in test_runID_fastaName_match[i][1]:
        test_arr.append(True)
    else:
        test_arr.append([False,test_runID_fastaName_match[i][0], test_runID_fastaName_match[i][1]])

print(test_arr)

# Write new file
with open("./Array_JOBS/" + str(sys.argv[2]) +  "runID_in_fastaHeader","w") as f:
    for i in range(len(fasta_files)):
        f.write(run_IDs[i] + "_" + fasta_files[i] + "\n")
f.close()