#!/bin/bash

# Takes a 10X barcodes.tsv files from the count pipeline and generates a AIRR Cell JSON file.
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 barcodes.tsv"
    exit
fi

# Steps in the pipeline:
# - Its TSV so we want the first field of the tab separated file.
# - We want unique barcodes only (sort -u)
# - We generate the output JSON, which is an array of cell objects, with awk.
#     - We want a line per cell, with cell_id = barcode
#     - We have extra stuff per line (e.g. virtual_pairing) that is constant
#     - We need to separate with commas except on the last line (the NR stuff)

cat $1 | awk -F'\t' '{print $1}' | sort -u | awk -F'\t' 'BEGIN {therest=",\"virtual_pairing\":false, \"expression_study_method\":\"single-cell transcriptome\""; print "["} {if (NR>1) { printf("{\"cell_id\":\"%s\"%s},\n",$1,therest); } str=$1; } END {printf("{\"cell_id\":\"%s\"%s}\n",str,therest); print "]"}'
