# Overview 
This directory contains test MHC genotype data in the [AIRR Repertoire MHC genotype](https://docs.airr-community.org/en/stable/datarep/germline.html#mhc-genotypes) format.

# Examples

The example data consists of an iReceptor UTF-8 encoded CSV metadata file from the study
["Immunoglobulin class-switched B cells provide an active immune axis between CNS and periphery in multiple sclerosis"](https://pubmed.ncbi.nlm.nih.gov/29429978/) by Culina et. al. for subject CerosalettiLab0145.
In addition, there is a file in the AIRR Repertoire MHC genotype format that contains 
the MHC genotype for subject CerosalettiLab0145. 

The iReceptor metadata CSV file can be loaded using the iReceptor Turnkey ([iReceptor Turnkey Repository](https://github.com/sfu-ireceptor/turnkey-service-php)) `load_metadata.sh` command.
```
load_metadata.sh ireceptor dataloading-curation/test/mhc-genotype/Culina-CerosalettiLab0145-metadata.csv
```
The genotype can be added to the metadata for subject CerosalettiLab0145 by using the iReceptor Turnkey `update_metadata.sh` command.
```
update_metadata.sh repertoire dataloading-curation/test/mhc-genotype/Culina-CerosalettiLab0145-metadata-mhc.json
```
NOTE: In the MHC file provided, the repertoire_id, data_processing_id, and sample_processing_id need to have
values added from the repository that the data was loaded into using the load_metadata.sh script above. These
values can be retrieved from the repository using the following command:
```
curl -s -d '{"filters":{"op":"=","content":{"field":"subject.subject_id","value":"CerosalettiLab0145"}},"fields":["subject.subject_id","repertoire_id","sample.sample_processing_id","data_processing.data_processing_id","data_processing.data_processing_files"]}' https://your_repository.org/airr/v1/repertoire
```
The values for these fields in the file Culina-CerosalettiLab0145-metadata-mhc.json need to be replaced with the values returned by the query above.
