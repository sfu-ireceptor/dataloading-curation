#!/bin/bash
echo $PWD
if [ -z "$PYTHONPATH" ];
then
    export PYTHONPATH=../../../dataloading-mongo/scripts
fi
if [ -z "$CONFIGPATH" ];
then
    export CONFIGPATH=../../../dataloading-mongo/config
fi
if [ -z "$DB_HOST" ];
then
    export DB_HOST=localhost
fi


python $PYTHONPATH/dataloader.py --host=$DB_HOST --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -s -l $PWD -f toy_data_sample.csv
python $PYTHONPATH/dataloader.py --host=$DB_HOST --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -v -a -l $PWD -f toy_data.tsv
