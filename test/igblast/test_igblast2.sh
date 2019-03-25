#!/bin/bash
echo $PWD
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


python $PYTHONPATH/dataloader.py --host=$DB_HOST --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -s -f toy_data_sample.csv
python $PYTHONPATH/dataloader.py --host=$DB_HOST --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -v -a -f toy_data.tsv
