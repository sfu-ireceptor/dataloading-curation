#!/bin/bash

# Takes a 10X barcodes.tsv files from the count pipeline and generates a AIRR Cell JSON file.

echo $@
cat $@ | awk -F'\t' '{print $1}' | tail -n +2 | sort -u | awk -F'\t' 'BEGIN {therest=",\"virtual_pairing\":false"; print "["} {if (NR>1) { printf("{\"cell_id\":\"%s\"%s},\n",$1,therest); } str=$1; } END {printf("{\"cell_id\":\"%s\"%s}\n",str,therest); print "]"}'
