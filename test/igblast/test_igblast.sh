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


python $PYTHONPATH/dataloader.py -s --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -l $PWD -f analy13_sample.csv
python $PYTHONPATH/dataloader.py -a --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -l $PWD -f analy13.igblast_airr_annots.txt
