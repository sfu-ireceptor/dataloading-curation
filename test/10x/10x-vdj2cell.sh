#!/bin/bash

# Takes 10X VDJ cell_barcodes.json files from the VDJ pipeline and generates a
# AIRR Cell JSON file. The file is a JSON array of strings.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 cell_barcodes.json"
    exit
fi
# Steps in the pipeline:
# - Its JSON so we only want the lines with a " in it (grep "\"")
# - We want the string without quotes, use awk with " as seperator (awk -F'"' '{print $2}')
# - We want unique barcodes only (sort -u)
# - We generate the output JSON, which is an array of cell objects, with awk. 
#     - We want a line per cell, with cell_id = barcode
#     - We have extra stuff per line (e.g. virtual_pairing) that is constant
#         - BEGIN we set up "therest" of the stuff to print out.
#     - We need to separate with commas except on the last line (the NR stuff)
#         - When NR == 0, we simply cache the line to print next time
#         - NR > 0 we print out the previous line, and cache this line.
#         - At the END we print out the last cached line and close the array.
#        
cat $1 | grep "\"" | awk -F'"' '{print $2}' | sort -u | awk -F'\t' 'BEGIN {therest=",\"virtual_pairing\":false, \"expression_study_method\":\"single-cell transcriptome\""; print "["} {if (NR>0) { printf("{\"cell_id\":\"%s\"%s},\n",$1,therest); } str=$1; } END {printf("{\"cell_id\":\"%s\"%s}\n",str,therest); print "]"}'
