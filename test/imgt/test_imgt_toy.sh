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

python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -s -f imgt_toy/PRJNA248411_Palanichamy_SRR1298740.csv
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -v -i -f imgt_toy/SRR1298740.txz
