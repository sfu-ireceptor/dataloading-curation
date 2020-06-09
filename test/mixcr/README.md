# Overview 
This directory contains test rearrangement data annotated by the MiXCR annotation tool. This directory consists of an example MiXCR annotation file, an accompanying repertoire metadata file, and a simple shell script that loads the files into a local iReceptor repository.

A detailed description of using MiXCR is beyond the scope of this document, for more details please visit the MiXCR documentation page (https://mixcr.readthedocs.io/en/latest/)

# Example Data

The example data in this directory is a small subset of the data from the paper "The Different T-cell Receptor Repertoires in Breast Cancer Tumors, Draining Lymph Nodes, and Adjacent Tissues" by Wang et. al. (https://www.ncbi.nlm.nih.gov/pubmed/28039161). The test data set consists of the first 1000 rearrangments from a single repertoire from this study. As such, it should only be considered in the context of a test data set and is should not be considered a representative sample of the data from this repertoire or from this study. The data set was curated using the iReceptor Data Curation process listed here: http://www.ireceptor.org/curation. The data set, in its entirety, is available through the iReceptor Scientific Gateway (http://gateway.ireceptor.org).

The example data set consists of two data files. The first file is a repertoire metadata file, as a UTF-8 encoded CSV file. The file consists of a header line, which contains the field names that will be written to the repository, followed by a single metadata line for a single repertoire from the above study. In a typical repertoire metadata file, there would be a single line for each repertoire in the study. The second file is a rearrangement file for this repertoire, as annotated using the MiXCR annotation tool. The file is a typical annotation output file from MiXCR. The original repertoire from this study contained over 1,000,000 rearrangments. To make the test data easily manageable for testing purposes, the first 1,000 rearrangements were extracted from this original file. 

If you are using an iReceptor Turnkey Repository (https://github.com/sfu-ireceptor/turnkey-service-php) please refer to the loading data section of the iReceptor Turnkey documentation. This documentation does not apply to you. 
 
If you choose to use these github repositories directly, there is a simple shell script that uses the iReceptor Data Loading module to load the data into an iReceptor Mongo repository. This shell script assumes that the github dataloading_curation (https://github.com/sfu-ireceptor/dataloading-curation), the dataloading_mongo (https://github.com/sfu-ireceptor/dataloading-mongo), and the config (https://github.com/sfu-ireceptor/config) modules are checked out in the same directory and that a local Mongo repository is running.

Assuming that you run this shell script as described above, the following command will load both the repertoire and rearrangement data into the local Mongo repository.

./test_mixcr.sh: This will load the data set (both the repertoire and rearrangement data) into the repository.
