import sys
import argparse
import json
import pandas as pd
import numpy as np


# process GEX data from the 10X files provided.
def processVDJGEX(b_t_cell_file, cell_file, feature_file, matrix_file, verbose):
    # Open the b_cell or t_cell JSON file.
    try:
        with open(b_t_cell_file) as f:
            cell_dict = json.load(f)
    except Exception as e:
        print('ERROR: Unable to read B/T Cell JOSN file %s'%(b_t_cell_file))
        print('ERROR: Reason =' + str(e))
        return False
    if verbose:
        print(cell_dict)

    # Open the cell file.
    try:
        with open(cell_file) as f:
            cell_df = pd.read_csv(f, sep='\t', header=None)
    except Exception as e:
        print('ERROR: Unable to read Cell file %s'%(cell_file))
        print('ERROR: Reason =' + str(e))
        return False
    if verbose:
        print(cell_df)

    # Open the feature file.
    try:
        with open(feature_file) as f:
            feature_df = pd.read_csv(f, sep='\t', header=None)
    except Exception as e:
        print('ERROR: Unable to read Feature file %s'%(feature_file))
        print('ERROR: Reason =' + str(e))
        return False
    if verbose:
        print(feature_df)

    # Open the matrix file for reading in chunks.
    chunk_size = 1000
    try:
        with open(matrix_file) as f:
            #matrix_df_reader = pd.read_csv(f, sep=' ', chunksize=chunk_size)
            #matrix_df = pd.read_csv(f, sep=' ', header=[0,1,2])
            matrix_df = pd.read_csv(f, sep=' ', header=None)
    except Exception as e:
        print('ERROR: Unable to read matrix file %s'%(matrix_file))
        print('ERROR: Reason =' + str(e))
        return False
    if verbose:
        print(matrix_df)

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
    parser.add_argument("b_t_cell_file")
    # The cell/barcode file name
    parser.add_argument("cell_file")
    # The repertoire_id to summarize
    parser.add_argument("feature_file")
    # The repertoire_id to summarize
    parser.add_argument("matrix_file")
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

    # Process and produce a AIRR GEX file from the 10X VDJ pipeline. This uses the
    # standard 10X cell_barcodes.json to determine which cells are b or t-cells but still
    # uses the count pipeline barcodes.tsv file for the cell indexes and features.tsv for
    # the gene features. It uses the 10X matrix.mtx file (stripped of headers) to get the
    # count for each cell/gene pair. It has three columns, the first column is an index
    # into the features.tsv, the second column is the index into the barcodes.tsv file,
    # and the third column is the count of the number of times that feature was found
    # for that cell.
    success = processVDJGEX(options.b_t_cell_file, options.cell_file, options.feature_file,
                         options.matrix_file, options.verbose)

    # Return success if successful
    if not success:
        print('ERROR: Unable to process 10X files (cells=%s, features=%s, matrix=%s)'%
              (options.cell_file, options.feature_file,options.matrix_file))
        sys.exit(1)
