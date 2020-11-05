#!/bin/bash

# This shell script assumes that the iReceptor dataloading-mongo and
# dataloading-curation git repositories are installed next to each other
# in the same parent directory. This can be overridden by setting the 
# the PYTHONPATH and CONFIGPATH environment variables as required.

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

# Load the metadata
python $PYTHONPATH/dataloader.py -v --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST --ireceptor -f IR-Binder-000001_metadata_2020-07-21.csv

# Load the clone data
if [ $? -eq 0 ]
then
    python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -v --mixcr-clone -f TRB-Pt-1-8_S150.clones.txt
fi

# Load the rearrangement data
if [ $? -eq 0 ]
then
    python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -v --mixcr -f TRB-Pt-1-8_S150.mixcr_annotation.txt
fi
