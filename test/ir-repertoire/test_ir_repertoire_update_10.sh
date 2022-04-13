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

python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -v --ireceptor --update -f master_metadata_update_10.csv
#python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST --ireceptor -f master_metadata_10.csv
#python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST --ireceptor -f master_metadata_UTF-8-2020-04-04.csv

