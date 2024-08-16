# Overview 
This directory contains test genotype data in the [AIRR Repertoire genotype](https://docs.airr-community.org/en/stable/datarep/germline.html) format.

# Examples

The example data consists of an iReceptor UTF-8 encoded CSV metadata file from the study
["Immunoglobulin class-switched B cells provide an active immune axis between CNS and periphery in multiple sclerosis"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4176763/) by Palanichamy et. al. . This is the same study used in the
[IMGT test data set](../imgt). In addition, there is a file in the AIRR Repertoire genotype format that contains 
an inferred genotype (using the VDJBase genotype inference tool) from the Repertoire for subject 43113. 

The original iReceptor metadata CSV file can be loaded using the iReceptor Turnkey `load_metadata.sh` command, 
while the genotype can be added to the metadata for subject 43113 by using the iReceptor Turnkey `update_metadata.sh` command.

If you are using an [iReceptor Turnkey Repository](https://github.com/sfu-ireceptor/turnkey-service-php) please refer to the loading data section of the iReceptor Turnkey documentation in order to load this data into an iReceptor Turnkey repository.
