# Test Data Sets

This directory contains a set of subdirectories consisting of a small number of data files that can be uses to test an iReceptor Turnkey node's data loading process. The tests use the iReceptor Data Loading module's python scripts to load a set of test data into an iReceptor Turnkey Mongo repository. 

There are three subdirectories, one for each of the annotation tools that the iReceptor Data Loading module supports. There are subdirectories for each of the igblast, MiXCR, and IMGT HighV-QUEST annotation tools. Each of the subdirectories has a small, but realistic and representative data set for each tool.

This data should not be used in production deployments of the iReceptor Turnkey repository, and should be used only for local testing of the installation and interface. Once the system is tested, you should re-initialize the database to a new empty database, then load your own data.

**A note about repertoire metadata files**

Repertoire metadata files are UTF-8 encoded comma delimited text files (CSV files), consisting of a single header line followed by a single line for each repertoire. The header line should consist of the names of the keys that will be stored in the Mongo repository. If the intent is to create an AIRR compatible repository, then the header lines should consist of keys that map to AIRR fields as specified in the MiAIRR standard as defined in the "AIRR Formats WG field name" as described here: https://github.com/airr-community/airr-standards/blob/master/AIRR_Minimal_Standard_Data_Elements.tsv

Repertoire metadata files are loaded into a repository using the iReceptor Data Curation loading scripts (https://github.com/sfu-ireceptor/dataloading-mongo). The data loading scripts will store all columns contained in the repertoire metadata CSV file, and will provide warnings to the user if the file is missing MiAIRR compatible field names. Please refer to the documentaion on the data loading python scripts on how to use these scripts to load repertoire data into a repository. Examples of using the scripts are provided in the shell scripts in each of the annotation tool data folders.

The iReceptor Project maintains a Repertoire Metadata standard file format that it uses in its internal data curation process (http://www.ireceptor.org/curation). Files in this format can be found in each of the example data sets within the MiXCR, IMGT, and igblast folders in this directory.
