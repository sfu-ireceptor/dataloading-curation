# Overview 
This directory contains test rearrangement data annotated by the MiXCR annotation tool. This directory consists of an example MiXCR annotation file and an accompanying repertoire metadata file. A detailed description of using MiXCR is beyond the scope of this document, for more details please visit the MiXCR documentation page (https://mixcr.readthedocs.io/en/latest/)

The iReceptor data loader maps a set of MiXCR exportAlignment fields to the AIRR standard fields when loaded. These fields will then appear in the repository as AIRR fields. Recommended export parameters for MiXCR include:

For v2.x: mixcr exportAlignments -c CHAIN -vHit -dHit -jHit -vGene -dGene -jGene -vFamily -dFamily -jFamily -vHitScore -dHitScore -jHitScore -nFeature CDR3 -aaFeature CDR3 -lengthOf CDR3 -readId -sequence -descrR1 -f path/to/annotatedfile.vdjca SRRfile_mixcr_annotation.txt

For v3.x: mixcr exportAlignments -c CHAIN -vHit -dHit -jHit -vGene -dGene -jGene -vFamily -dFamily -jFamily -vHitScore -dHitScore -jHitScore -nFeature CDR3 -aaFeature CDR3 -lengthOf CDR3 -readIds -targetSequences -descrsR1 path/to/annotatedfile.vdjca SRRfile_mixcr_annotation.txt

# Example Data

The example data in this directory is a small subset of the data from the paper "The Different T-cell Receptor Repertoires in Breast Cancer Tumors, Draining Lymph Nodes, and Adjacent Tissues" by Wang et. al. (https://www.ncbi.nlm.nih.gov/pubmed/28039161). The test data set consists of the first 1000 rearrangments from a single repertoire from this study. As such, it should only be considered in the context of a test data set and is should not be considered a representative sample of the data from this repertoire or from this study. The data set was curated using the iReceptor Data Curation process listed here: http://www.ireceptor.org/curation. The data set, in its entirety, is available through the iReceptor Scientific Gateway (http://gateway.ireceptor.org).

The example data set consists of two data files. The first file is a repertoire metadata file, as a UTF-8 encoded CSV file. The file consists of a header line, which contains the field names that will be written to the repository, followed by a single metadata line for a single repertoire from the above study. In a typical repertoire metadata file, there would be a single line for each repertoire in the study. The second file is a rearrangement file for this repertoire, as annotated using the MiXCR annotation tool. The file is a typical annotation output file from MiXCR. The original repertoire from this study contained over 1,000,000 rearrangments. To make the test data easily manageable for testing purposes, the first 1,000 rearrangements were extracted from this original file. 

If you are using an iReceptor Turnkey Repository (https://github.com/sfu-ireceptor/turnkey-service-php) please refer to the loading data section of the iReceptor Turnkey documentation.
