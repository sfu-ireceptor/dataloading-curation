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

python $PYTHONPATH/dataloader.py -v --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST --ireceptor -f BWNW-ImmuneCODE-Repertoire-Tags-002-ir-metadata-2020-08-26.csv
if [ $? -eq 0 ]
then
    python $PYTHONPATH/dataloader.py -v --adaptive --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -f 7972BW_TCRB.tsv
fi

