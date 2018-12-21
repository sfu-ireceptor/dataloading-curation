#!/bin/bash

# This shell script loads a set of IMGT vQuest data into the iReceptor repository. It makes
# the following assumptions: 
#     1) The first parameter is the directory where all of the data resides
#     2) The second parameter is the metadata file to use
#     3) It assumes that each rearrangement is a tarred, zipped folder.
#
# Given the above, the script will iterated over all of the tarred/zipped folders in the
# data directory, and try to load them using the metadata specified in the meta data file.

if [ $# -ne 3 ];
then
    echo "Usage: $0 metadata.csv data_dir out_dir"
    exit 1
fi

if [ -z "$PYTHONPATH" ];
then
    export PYTHONPATH=../../../scripts
fi
if [ -z "$CONFIGPATH" ];
then
    export CONFIGPATH=../../../config
fi

metadata=$1
datadir=$2
outdir=$3
# Get the base file name for the metadata
metadata_file=$(basename $metadata)
# Get a string for the date we can use to timestamp files.
current_time=$(date "+%Y.%m.%d-%H.%M.%S")

echo "Starting load process at $current_time"
out_file=$outdir/$metadata_file.$current_time.out
echo "Loading metadata file $metadata (log file = $out_file)"
python $PYTHONPATH/dataloader.py -v --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -s -f $metadata > $out_file
if [ $? -ne 0 ];
then
    echo "Error: Could not load metadate file $metadata, see $out_file"
    exit 1 
fi

for filename in $datadir/*.txz; do
    annotation_file=$(basename $filename)
    out_file=$outdir/$annotation_file.$current_time.out
    echo "Loading annotation file $filename (log file = $out_file)"
    python $PYTHONPATH/dataloader.py -v --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -f $filename > $out_file
    end_time=$(date "+%Y.%m.%d-%H.%M.%S")
    echo "Done loading file $filename ($end_time)"

    if [ $? -ne 0 ];
    then
        echo "Error: Could not load annotation file $filename, see $out_file"
        exit 1 
    fi
done
end_time=$(date "+%Y.%m.%d-%H.%M.%S")
echo "Finished load process at $end_time"
