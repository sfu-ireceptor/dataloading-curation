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


python $PYTHONPATH/dataloader.py -s --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -f analy13_sample.csv
python $PYTHONPATH/dataloader.py -v -a --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -f analy13.igblast_airr_annots.txt.gz
