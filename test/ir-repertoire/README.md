# Overview 
This directory contains test iReceptor repertoire data files in the iReceptor UTF-8 encoded CSV format (as exported from Excel).
More information on this format can be found in the [metadata directory](../../metadata) in this github repository.

# Example Data

The example data in this directory is a small subset of data from a number of example studies. There is a single
metadata file that can be used to test iReceptor metadata loading as well as two files for testing updating metadata,
including a file that updates a set of fields in one repertoire and one that updates a set of fields in all repertoires. 

Each file consists of a header line, which contains the field names that will be written to the repository, followed by a metadata line for each repertoire. The format of the files is the same, with the update files having a set of fields that have changed for each repertoire.

- metadata_update_1.csv: `study_id`: "PRJNA188191" => "PRJNA00005", `my_field`: None => "MY VALUE"

- meradata_update_10.csh: `study_id`: "PRJNA188191" => "PRJNA188191-XXX" where XXX is the number of the repertoire 1-10.


If you are using an [iReceptor Turnkey Repository](https://github.com/sfu-ireceptor/turnkey-service-php) please refer to the loading data section of the iReceptor Turnkey documentation for more information on loading this data. 
