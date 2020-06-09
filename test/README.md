# Test Data Sets

This directory contains a set of subdirectories consisting of a small number of data files that can be uses to test an iReceptor Turnkey node's data loading process. The tests use the iReceptor Data Loading module's python scripts to load a set of test data into an iReceptor Turnkey Mongo repository. 

There are three rearrangement subdirectories, one for each of the annotation tools that the iReceptor Data Loading module supports. There are subdirectories for each of the igblast, MiXCR, and IMGT HighV-QUEST annotation tools. Each of the subdirectories has a small, but realistic and representative data set for each tool.

There are two repertoire subdirectoires, one for each of the repertoire metadata formats that the iReceptore Data Loading module supports. The are subdirectories for both the iReceptor repertoire metadata format and the AIRR Repertoire data loading format. 

This data should not be used in production deployments of the iReceptor Turnkey repository, and should be used only for local testing of the installation and interface. Once the system is tested, you should re-initialize the database to a new empty database, then load your own data.


