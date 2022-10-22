# Overview 
This directory contains test rearrangement data annotated by the HighV-QUEST
annotation resource provided by the ImMunoGeneTics (IMGT) information system.
IMGT HighV-Quest can process files of up to 500,000 sequences and provides the
resulting annotation files as a
set of CSV files in a tarred and compressed file bundle (a .txz file).
This directory consists of a set of example IMGT HighV-QUEST annotated files and
accompanying repertoire metadata files.

A detailed description of using HighV-QUEST is beyond the scope of this
document, for more details please visit the HighV-QUEST page
(https://www.imgt.org/HighV-QUEST/home.action)

# Examples

There is a single data set in this directory
that consists of eight repertoires and is a subset of the data from the paper "Immunoglobulin class-switched B cells provide an active immune axis between CNS and periphery in multiple sclerosis" by Palanichamy et. al.
(https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4176763/). The data set was curated using the iReceptor Data Curation process listed here: http://www.ireceptor.org/curation. The full data set from this study is available through the iReceptor Scientific Gateway (http://gateway.ireceptor.org).

The directory consists of 
a iReceptor Repertoire metadata file (a UTF-8 encoded CSV file) and a set of rearrangement files.
Each repertiore has been annotated with the HighV-QUEST annotation
tool and the directory contains a single rearrangement file (a single .txz file) for each
repertoire. 
If you are using an iReceptor Turnkey Repository (https://github.com/sfu-ireceptor/turnkey-service-php) please refer to the loading data section of the iReceptor Turnkey documentation for more detailed instructions on loading Repertoire metadata and Rearrangement files.



