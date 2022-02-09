import sys
import argparse
import json
import pandas as pd
import numpy as np


# Generate AIRR Clone data from the 10X files provided.
# rearrangement_file: a typical airr_rearrangements.tsv file (tab separated)
# clonotypes: a typical 10X clonotypes.csv (comma separated)
def processVDJClone(rearrangement_file, clonotype_file, verbose):
    # Open the rearrangement file.
    try:
        with open(rearrangement_file) as f:
            rearrangement_df = pd.read_csv(f, sep='\t', header=None)
    except Exception as e:
        print('ERROR: Unable to read Rearrangement file %s'%(rearrangement_file))
        print('ERROR: Reason =' + str(e))
        return False
    if verbose:
        print(rearrangement_df)

    # Open the clonotype file.
    try:
        with open(clonotype_file) as f:
            clonotype_df = pd.read_csv(f, sep=',')
    except Exception as e:
        print('ERROR: Unable to read Clonotype file %s'%(clonotype_file))
        print('ERROR: Reason =' + str(e))
        return False
    if verbose:
        print(clonotype_df)

    # Iterate over the clonotypes in the clonotype file.
    # Fields: clonotype_id,frequency,proportion,cdr3s_aa,cdr3s_nt,inkt_evidence,mait_evidence
    clone_array = []
    for index, clonotype in clonotype_df.iterrows():
        print('clonotype = %s'%(clonotype['clonotype_id']))
        clone_count = clonotype['frequency']
        junction_aa = 


    return False


    # Iterate over the file a chunk at a time. Each chunk is a data frame.
    #total_records = 0
    #for df_chunk in matrix_df_reader:
        #total_records += chunk_size
        #print("Read %d records"%(total_records))
    print("[")
    num_rows = len(matrix_df.index)
    cell_count = 0
    for ind in matrix_df.index:
        # Get the cell bar code we are processing
        cell_index = matrix_df[1][ind]
        cell = cell_df[0][cell_index-1]

        # Check to see if the barcode is in the B/T cell list, if so process it,
        # if not skip it.
        if cell in cell_dict:
            cell_count += 1
            gene_index = matrix_df[0][ind]
            level = matrix_df[2][ind]

            gene_id = feature_df[0][gene_index-1]
            gene_label = feature_df[1][gene_index-1]


            if cell_count > 1:
                print(',')
            print('{"cell_id":"%s", "property":"%s", "ir_property_label_expression":"%s", "value":%d}'%
                    (cell, gene_id, gene_label, level),end='')

    print("\n]")

    if verbose:
        print("Number of cells = %d"%(cell_count))

    return True

def getArguments():
    # Set up the command line parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=""
    )
    parser = argparse.ArgumentParser()

    # The t-cell/b-cell barcode file name
    parser.add_argument("airr_rearrangements")
    # The cell/barcode file name
    parser.add_argument("clonotypes")
    # Verbosity flag
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Run the program in verbose mode.")

    # Parse the command line arguements.
    options = parser.parse_args()
    return options


if __name__ == "__main__":
    # Get the command line arguments.
    options = getArguments()

    # Process and produce a AIRR Clone file from the 10X VDJ pipeline. This uses the
    # standard 10X airr_rearrangements.tsv and clonotypes.csv files to determine the
    # clones for a data processing of either VDJ B or T cells.
    success = processVDJClone(options.airr_rearrangements, options.clonotypes,
                              options.verbose)

    # Return success if successful
    if not success:
        print('ERROR: Unable to process 10X files (rearrangements=%s, clonotypes=%s)'%
              (options.airr_rearrangements, options.clonotypes))
        sys.exit(1)
