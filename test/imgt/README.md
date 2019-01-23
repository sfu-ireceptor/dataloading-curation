# Overview 
This directory contains test rearrangement data annotated by the HighV-QUEST
annotation resource provided by the ImMunoGeneTics (IMGT) information system.
IMGT HighV-Quest can process files of up to 500,000 sequences and provides the
resulting annotation files as a
set of CSV files in a tarred and compressed file bundle (a .txz file).
This directory consists of a set of example IMGT HighV-QUEST annotated files,
accompanying repertoire metadata files, and a simple shell script that loads
the files into a local iReceptor repository.

A detailed description of using HighV-QUEST is beyond the scope of this
document, for more details please visit the HighV-QUEST page
(https://www.imgt.org/HighV-QUEST/home.action)

# Examples

There are two example rearrangement data sets in this directory, a data set that
consists of a single repertoire (subdirectory imgt_toy) and a data set that
consists of eight repertoires (subdirectory imgt). Each directory consists of 
a repertoire metadata file (a UTF encoded CSV file) and a set of 
rearrangement files.
Each repertiore has been annotated with the HighV-QUEST annotation
tool and contains a single rearrangement file (a single .txz file) for each
repertoire.

Both of these data sets are a subset of the data from the paper 
"Immunoglobulin class-switched B cells provide an active immune axis between CNS and periphery in multiple sclerosis" by Palanichamy et. al.
(https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4176763/). The data sets were curated using the iReceptor Data Curation process listed here: http://www.ireceptor.org/curation. The full data set from this study is available through the iReceptor Scientific Gateway (http://gateway.ireceptor.org).

Both examples have a simple shell script that uses the iReceptor Data Loading module to load the data into an iReceptor Mongo repository. These shell scripts assume that the data and the data loading modules are components of the iReceptor Turnkey Repository platform (https://github.com/sfu-ireceptor).

Assuming that you are running these shell scripts from within an iReceptor Turnkey system, the following commands will load both the repertoire and rearrangement data into the repository.

./test_imgt_toy.sh: This will load the data set in the imgt_toy subdirectory into the repository.

./test_imgt_large.sh: This will load the larger data set in the imgt subdirectory into the repository.

It should be noted that it will not be possible to load both of these data sets at the same time. The iReceptor Data Loading module checks for duplicate data and will not allow a set of rearrangements to be loaded if it is ambigous as to which repertoire it should assign the rearrangements. Because the two example data sets share a rearrangement file, if you load both repertoire CSV files the rearrangement loader will not know which repertoire to assign the rearrangements. The loader will happily load the repertoire files, but it will fail when you try to load the rearrangments. If you load one of the examples, it will be necessary to delete the data from the repository for that example before you can load the other data set.
