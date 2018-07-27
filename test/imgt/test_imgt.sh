#!/bin/bash
echo $PWD
export PYTHONPATH=../../../scripts
python $PYTHONPATH/dataloader.py -s -l $PWD -f imgt_toy_sample.csv
python $PYTHONPATH/dataloader.py -i -l $PWD -f imgt_toy.zip
