#!/bin/bash

# This shell script loads a set of rearrangement data into the iReceptor repository.
# It makes the following assumptions: 
#     1) The study metadata is already loaded. The metadata can be loaded by using the
#        load_metadata script.
#     2) The first parameter is the directory where the log output files will be stored.
#     3) The second parameter is the type of rearrangment data to process. It assumes that
#        all rearrangement files are of the same type.
#     4) The rest of the parameters are the rearrangement files to process.
#
# Given the above, the script will iterated over all of the rearrangement files given and
# try to load them using the metadata specified in the meta data file.
# 
# Note: an example simple usage, assuming that the metadata has been loaded and all
# of the rearrangement files (as imgt compressed .tsv files) are in the same directory would be:
#
# load_rearrangements . imgt *.tsv

if [ $# -lt 3 ];
then
    echo "Usage: $0 out_dir [airr|imgt|mixcr] rearrangement1 rearrangement2 ... rearrangementN"
    exit 1
fi

if [ -z "$PYTHONPATH" ];
then
    export PYTHONPATH=../../../dataloading-mongo/dataload
fi
if [ -z "$CONFIGPATH" ];
then
    export CONFIGPATH=../../../config
fi
if [ -z "$DB_HOST" ];
then
    export DB_HOST=localhost
fi


# Keep track of the output directory for the log files.
outdir=$1
# Process the next command line parameter
shift
# Keep track of the type of rearrangement file we are proecessing
rearrangement_type=$1
# Process the next command line parameter
shift

# Get a string for the date we can use to timestamp files.
current_time=$(date "+%Y.%m.%d-%H.%M.%S")

# Run the python data loading script on the metadata file, exit if there is an error
echo "Starting load process at $current_time"

# Each of the remaining command line parameters is expected to be a rearrangement file
# of the type specified by the rearrangement file type parameter. Loop over the rest
# of the command line arguements and process each as a rearrangement file.
while [ "$1" != "" ]; do
    filename=$1
    annotation_file=$(basename $filename)
    # Generate the log file name.
    out_file=$outdir/$annotation_file.$current_time.out
    # Load the rearrangement file, exit if failed.
    echo "Loading annotation file $filename (log file = $out_file)"
    python $PYTHONPATH/dataloader.py  --host=$DB_HOST -v --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --$rearrangement_type -f $filename > $out_file

    if [ $? -ne 0 ];
    then
        echo "Error: Could not load annotation file $filename, see $out_file"
        exit 1 
    fi
    end_time=$(date "+%Y.%m.%d-%H.%M.%S")
    echo "Done loading file $filename ($end_time)"
    # Shift the command line parameters so we can parse the next file.
    shift
done
end_time=$(date "+%Y.%m.%d-%H.%M.%S")
echo "Finished load process at $end_time"
