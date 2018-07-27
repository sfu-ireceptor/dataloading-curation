#!/bin/bash
echo $PWD
export PYTHONPATH=../../../scripts
python $PYTHONPATH/dataloader.py -s -l $PWD -f analy13_sample.csv
python $PYTHONPATH/dataloader.py -a -l $PWD -f analy13.igblast_airr_annots.txt
