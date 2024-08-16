# Instructions

Using the iReceptor Turnkey data loading commands to load this data:
```
$TURNKEY/scripts/load_metadata.sh ireceptor $DATA/dataloading-curation/test/airr-reactivity/PRJNA744851-Minervina/R23-cell-reactivity-metadata.csv
$TURNKEY/scripts/load_cells.sh airr-cell $DATA/dataloading-curation/test/airr-reactivity/PRJNA744851-Minervina/R23_inf_vax2-t-cells.json
$TURNKEY/scripts/load_reactivity.sh airr-reactivity $DATA/dataloading-curation/test/airr-reactivity/PRJNA744851-Minervina/R23_reactivity.json
$TURNKEY/scripts/link_reactivity2cell.sh $DATA/dataloading-curation/test/airr-reactivity/PRJNA744851-Minervina/R23-reactivity-to-cell.tsv
```
Where the iReceptor Turnkey repository is installed in $TURNKEY and this github repositrory is cloned into $DATA.

