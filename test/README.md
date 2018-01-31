# Test Data Set

This directory contains a small number of data files that can be uses to test an iReceptor turnkey node by loading the MongoDb database using the project Python scripts. 

The imgt_sample.csv data is excerpted from the AIRR B cell data from the public AIRR study by *Palanichamy et al.(2014)*.
The mixcr_sample.csv data is excerpted from the TCR cell data from the public AIRR study by *Putintseva et al. (2013)*

This data should not be used in production deployments of the turnkey but only for local testing of the installation and interface. Once the system is tested, you should re-initialize the database to a new empty database, then load your own data, suitably formatted.

**Sample.csv Metadata File**

This is sample metadata from the above study. You should load this file first into the database.

Note that the data file is a comma delimited file with headers following the standard template (Excel) spreadsheet AIRR compliant data table format of the iReceptor project For further details about this format, see the ([iReceptor Data Curation repository site](https://github.com/sfu-ireceptor/dataloading-curation). 

**IMGT.zip Annotation Archive**

This is a zip archive file of IMGT analysis sequence annotation *txz* archive files. Each *txz* archive - named something like SRR123456.txz, where '123456' would be the sample identifier  - when extracted contains a set of IMGT annotation text output files resulting from processing one sample. The data loader expects to see and currently loads the following subset of these IMGT analysis files:

```
1_Summary.txt
2_IMGT-gapped-nt-sequences.txt
3_Nt-sequences.txt
4_IMGT-gapped-AA-sequences.txt
5_AA-sequences.txt
7_V-REGION-mutation-and-AA-change-table.txt
11_Parameters.txt
```
See the ([iReceptor Data Curation repository site](https://github.com/sfu-ireceptor/dataloading-curation) for more information about this data format. 
