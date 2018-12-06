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

python $PYTHONPATH/dataloader.py -s --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -l $PWD -f analy13_sample.csv
python $PYTHONPATH/dataloader.py -a --mapfile=$CONFIGPATH/AIRR-iReceptorMapping.txt -l $PWD -f analy13.igblast_airr_annots.txt
