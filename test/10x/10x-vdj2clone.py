import sys
import argparse
import json
import pandas as pd
import numpy as np


# Generate AIRR Clone data from the 10X files provided.
# rearrangement_file: a typical airr_rearrangements.tsv file (tab separated)
# clonotypes: a typical 10X clonotypes.csv (comma separated)
def processVDJClone(rearrangement_file, clonotype_file, output_filename, locus, verbose):
    # Open the rearrangement file.
    try:
        with open(rearrangement_file) as f:
            rearrangement_df = pd.read_csv(f, sep='\t')
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
        # Get the clone_id
        clone_id = clonotype['clonotype_id']
        # Select the rearrangements for this clonotype
        if verbose:
            print('clonotype = %s'%(clone_id))
        clone_dict = {}
        clone_rearrangements = rearrangement_df[rearrangement_df.clone_id == clone_id]
        if verbose:
            print('rearrangements for clone_id %s = %d'%(clone_id,len(clone_rearrangements.index)))

        # Get all of the rows that have a rearrangement with the correct locus
        # If there are none, then we don't want to create a clone object for this clone_id
        clone_vcalls = clone_rearrangements[clone_rearrangements['v_call'].str.contains(locus)]
        if len(clone_vcalls.index) <= 0:
            print('Warning: No rearrangements with locus %s in file %s for clone %s'%(locus, rearrangement_file, clone_id))
            continue

        # Select the unique cell_ids from the rearrangements for this clone
        clone_cells = clone_rearrangements.cell_id.unique()
        if verbose:
            print('cells for clone_id %s = %d'%(clone_id,len(clone_cells)))

        # Capture the clone_id
        clone_dict['clone_id'] = clone_id

        # Get the clone count. AIRR defines this as the number of unique cells with
        # the clone_id.
        clone_count = clonotype['frequency']
        if len(clone_cells) != clone_count:
            if verbose:
                print('Warning: Clone count (%d) does not match calculated clone count (%d)'%(clone_count,len(clone_cells)))
        clone_count = len(clone_cells)
        clone_dict['clone_count'] = clone_count

        # Get the UMI count. AIRR defines this as the sum of the duplicate_count field
        # for the rearrangements that have this clone_id
        umi_count = clone_rearrangements['duplicate_count'].sum()
        if verbose:
            print('umi_count for clone_id %s = %d'%(clone_id,umi_count))
        clone_dict['umi_count'] = int(umi_count)

        junction_aa_list = clonotype['cdr3s_aa'].split(';')
        for locus_junction in junction_aa_list:
            junction_info = locus_junction.split(':')
            if junction_info[0] == locus:
                junction_aa = junction_info[1]
                if verbose:
                    print('locus junction_aa = %s %s'%(locus, junction_aa))
                
        junction_list = clonotype['cdr3s_nt'].split(';')
        for locus_junction in junction_list:
            junction_info = locus_junction.split(':')
            if junction_info[0] == locus:
                junction = junction_info[1]
                if verbose:
                    print('locus junction = %s %s'%(locus, junction))

        
        clone_dict['locus'] = locus
        clone_dict['junction_aa'] = junction_aa
        clone_dict['junction'] = junction
        clone_dict['junction_aa_length'] = len(junction_aa)
        clone_dict['junction_length'] = len(junction)

        # Get the germline alignments from the arrangements from the locus of interest
        clone_germline_list = clone_vcalls.germline_alignment.unique()
        # There should only be one, as the germline_alignment from all rearrangements from
        # the same locus should be the same
        if len(clone_germline_list) > 1:
            print('Warning: more than one (%d) germline_alignment found for clone %s (%s)'%(len(clone_germline_list), clone_id, locus))
            #print(clone_germline_list)
        if len(clone_germline_list) == 0:
            print('Warning: No germline_alignment found for clone %s (%s)'%(clone_id, locus))
        else:
            clone_dict['germline_alignment'] = clone_germline_list[0]


        # Add the dictionary to the clone array
        clone_array.append(clone_dict)

    # Write the JSON to a file
    try:
        with open(output_filename, "w") as file:
            json.dump(clone_array, file, indent=4)
    except Exception as e:
        print('ERROR: Unable to write output file %s'%(output_filename))
        print('ERROR: Reason =' + str(e))
        return False

    return True

def getArguments():
    # Set up the command line parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=""
    )
    parser = argparse.ArgumentParser()

    # The rearrangement file name
    parser.add_argument("airr_rearrangements")
    # The clonotype file name
    parser.add_argument("clonotypes")
    # The output file name
    parser.add_argument("output_filename")
    # The locus to extract from the clonotype file.
    parser.add_argument(
        "--locus",
        dest="locus",
        default="IGH",
        help="The locus to extract from the clonotype file [IGH|IGL|IGK|TRA|TRB|TRD|TRG]. If not set then clonotypes will be created for all loci."
    )

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

    # Check for IGH and TRB loci. We only support these for now because the AIRR clone
    # format doesn't support multiple chains in a single clone.
    if not options.locus == "IGH" and not options.locus == "TRB":
        print("ERROR: Only IGH and TRB loci are supported at this time")
        sys.exit(1)

    # Process and produce a AIRR Clone file from the 10X VDJ pipeline. This uses the
    # standard 10X airr_rearrangements.tsv and clonotypes.csv files to determine the
    # clones for a data processing of either VDJ B or T cells.
    success = processVDJClone(options.airr_rearrangements, options.clonotypes,
                              options.output_filename, options.locus, options.verbose)

    # Return success if successful
    if not success:
        print('ERROR: Unable to process 10X files (rearrangements=%s, clonotypes=%s)'%
              (options.airr_rearrangements, options.clonotypes))
        sys.exit(1)
