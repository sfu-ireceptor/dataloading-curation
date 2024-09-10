# Overview 
This directory contains test MHC genotype data in the [AIRR Repertoire MHC genotype](https://docs.airr-community.org/en/stable/datarep/germline.html) format.

# Examples

The example data consists of an iReceptor UTF-8 encoded CSV metadata file from the study
["Immunoglobulin class-switched B cells provide an active immune axis between CNS and periphery in multiple sclerosis"](https://pubmed.ncbi.nlm.nih.gov/29429978/) by Culina et. al. for subject CerosalettiLab0145.
In addition, there is a file in the AIRR Repertoire MHC genotype format that contains 
the MHC genotype for subject CerosalettiLab0145. 

The iReceptor metadata CSV file can be loaded using the iReceptor Turnkey `load_metadata.sh` command, 
while the genotype can be added to the metadata for subject CerosalettiLab0145  by using the iReceptor Turnkey `update_metadata.sh` command.

If you are using an [iReceptor Turnkey Repository](https://github.com/sfu-ireceptor/turnkey-service-php) please refer to the loading data section of the iReceptor Turnkey documentation in order to load this data into an iReceptor Turnkey repository.
