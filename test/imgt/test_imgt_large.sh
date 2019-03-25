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



python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -s -f imgt/PRJNA248411_Palanichamy_2018-12-18.csv
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -i -f imgt/SRR1298731.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -i -f imgt/SRR1298732.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -i -f imgt/SRR1298733.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -i -f imgt/SRR1298734.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -i -f imgt/SRR1298736.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -i -f imgt/SRR1298738.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -i -f imgt/SRR1298740.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt --host=$DB_HOST -i -f imgt/SRR1298742.txz


