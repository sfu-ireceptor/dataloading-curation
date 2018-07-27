#!/bin/bash
echo $PWD
export PYTHONPATH=../../../scripts
python $PYTHONPATH/dataloader.py -s -l $PWD -f toy_data_sample.csv
python $PYTHONPATH/dataloader.py -a -l $PWD -f toy_data.tsv
