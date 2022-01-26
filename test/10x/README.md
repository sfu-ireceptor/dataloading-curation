# Using the 10X test data sets

## Creating an AIRR cell file

Create an AIRR cell file from either the cell_barcodes.json file from the VDJ pipeline or the barcodes.tsv file from the count pipeline:

```
10x-vdj2cell.sh cell_barcodes.json > cells.json
10x-count2cell.sh barcodes.tsv > cells.json
```
If using the VDJ pipeline, you typically want to run 10x-vdj2cell.sh on the cell_barcodes.json file in both the vdj_b and vdj_t directories
This will give you two cells.json files with the t-cell and b-cell cell definitions in the two respective files.

If you are using the count pipeline, you want to run 10x-count2cell.sh on the barcodes.tsv file in the count/sample_feature_bc_matrix directory.

## Creating an AIRR GEX file

Create an AIRR GEX file is slightly more complex. It makes use of the files in the count/sample_feature_bc_matrix directory. If
you are using the VDJ pipeline to create just b-cell and t-cell related GEX data, you also need the cell_barcodes.json file from 
either (or both tpyically) from the vdj_b and vdj_t directories. In a typical 10X output directory, to generate t-cell and b-cell 
GEX data, do the following:

```
# First trim the matrix.mtx file so it does not have the three header lines
tail -n +4 count/sample_feature_bc_matrix/matrix.mtx > count/sample_feature_bc_matrix/matrix-trimmed.mtx

# Then generate two GEX AIRR JSON files, one for the b-cells and one for the t-cells
python3 10x-vdj2GEX.py vdj_b/cell_barcodes.json count/sample_feature_bc_matrix/barcodes.tsv count/sample_feature_bc_matrix/features.tsv count/sample_feature_bc_matrix/matrix-trimmed.mtx > vdj_b_gex.json
python3 10x-vdj2GEX.py vdj_t/cell_barcodes.json count/sample_feature_bc_matrix/barcodes.tsv count/sample_feature_bc_matrix/features.tsv count/sample_feature_bc_matrix/matrix-trimmed.mtx > vdj_t_gex.json
```
