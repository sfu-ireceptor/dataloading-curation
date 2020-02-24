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

python $PYTHONPATH/dataloader.py -v --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST --repertoire -f florian.airr.1.json
if [ $? -eq 0 ]
then
    python $PYTHONPATH/dataloader.py -v --database_chunk=1000 --airr --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -f TW04B_B_memory.igblast.airr.small.tsv
fi

