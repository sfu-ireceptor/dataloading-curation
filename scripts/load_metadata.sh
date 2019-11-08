#!/bin/bash

# This shell script loads the study repertoire metadata
#     1) The first parameter is the type of repertoire file
#     2) The second parameter is the directory where the log output files will be stored.
#     3) The third parameter is the repertoire metadata file

if [ $# -ne 3 ];
then
    echo "Usage: $0 [repertoire|sample] out_dir metadata.json"
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


# Keep track of the type of reperotire file we are proecessing
repertoire_type=$1
# Process the next command line parameter
shift
# Keep track of the output directory for the log files.
outdir=$1
# Process the next command line parameter
shift
# Keep track of the metadata file for the study.
metadata=$1
# Process the next command line parameter
shift

# Get the base file name for the metadata
metadata_file=$(basename $metadata)
# Get a string for the date we can use to timestamp files.
current_time=$(date "+%Y.%m.%d-%H.%M.%S")
# Generate the output file for the metadata file.
out_file=$outdir/$metadata_file.$current_time.out

# Run the python data loading script on the metadata file, exit if there is an error
echo "Starting load process at $current_time"
echo "Loading metadata file $metadata (log file = $out_file)"
python $PYTHONPATH/dataloader.py  --host=$DB_HOST -v --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --$repertoire_type -f $metadata > $out_file
if [ $? -ne 0 ];
then
    echo "Error: Could not load metadate file $metadata, see $out_file"
    exit 1 
fi
end_time=$(date "+%Y.%m.%d-%H.%M.%S")
echo "Done loading file $metadata ($end_time)"
