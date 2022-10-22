# Overview 
This directory contains iReceptor repertoire data files in the iReceptor UTF-8 encoded CSV format (as exported from Excel) for testing Repertoire data loading into an [iReceptor Turnkey Repository](https://github.com/sfu-ireceptor/turnkey-service-php). Please refer to the loading data section of the iReceptor Turnkey documentation for more information on how to load this data. More information on the iReceptor CSV Repertoire metadata format can be found in the [metadata directory](../../metadata) in this github repository.

# Example Data

The example data in this directory is a small subset of data from a number of example studies. There is a iReceptor Repertoire
metadata file that can be used to test iReceptor metadata loading using the `load_metadata.sh` script. Since it is relatively common
to need to update Repertoire metadata once it is loaded into an iReceptor Turnkey repository, there are also two files for testing updating
metadata using the `update_metadata.sh` script. One file contains updates for a set of fields in one repertoire and one file contains updates for a set of fields in all repertoires. 

Each file consists of a header line, which contains the field names that will be written to the repository, followed by a metadata line for each repertoire. The format of the files for the main and the update files is the same, with the update files having a set of fields that have changed for each repertoire. The metadata files with updates in them contain the following changes:

- metadata_update_1.csv: `study_id`: "PRJNA188191" => "PRJNA00005", `my_field`: None => "MY VALUE"
- meradata_update_10.csh: `study_id`: "PRJNA188191" => "PRJNA188191-XXX" where XXX is the number of the repertoire 1-10.
