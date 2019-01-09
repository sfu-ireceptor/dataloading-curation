#!/bin/bash
echo $PWD
if [ -z "$PYTHONPATH" ];
then
    export PYTHONPATH=../../../scripts
fi
if [ -z "$CONFIGPATH" ];
then
    export CONFIGPATH=../../../config
fi


python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -s -l $PWD/imgt -f imgt_sample.csv
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -l $PWD/imgt -f SRR1298731.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -l $PWD/imgt -f SRR1298732.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -l $PWD/imgt -f SRR1298733.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -l $PWD/imgt -f SRR1298734.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -l $PWD/imgt -f SRR1298736.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -l $PWD/imgt -f SRR1298738.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -l $PWD/imgt -f SRR1298740.txz
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -l $PWD/imgt -f SRR1298742.txz


