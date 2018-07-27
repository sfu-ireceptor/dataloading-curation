#!/bin/bash
echo $PWD
export PYTHONPATH=../../../scripts
python $PYTHONPATH/dataloader.py -s -l $PWD -f SRR1033679_mixcr_sample.csv
python $PYTHONPATH/dataloader.py -m -l $PWD -f SRR1033679_mixcr_annotation_test.1000lines.txt
