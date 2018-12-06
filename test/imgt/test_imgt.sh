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


python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -s -l $PWD -f imgt_toy_sample.csv
python $PYTHONPATH/dataloader.py --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -i -l $PWD -f imgt_toy.zip
