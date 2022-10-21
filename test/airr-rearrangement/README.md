# Overview 
This directory contains test rearrangement data in the AIRR format. This data was produced from Cell Ranger's VDJ pipeline, and uses the airr_rearrangements.tsv file produced from this pipeline. 

A detailed description of using cellranger is beyond the scope of this document, for more details please visit the [cellranger documentation page](https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/what-is-cell-ranger)

# Example Data

The example data in this directory is a small subset of the data from the paper "[Immune cell profiling of COVID-19 patients in the recovery stage by single-cell sequencing](https://doi.org/10.1038/s41421-020-0168-9) from Wen et al. The data set consists of the Rearrangement data from a single subject in this study (subject HC1). As such, it should only be considered in the context of a test data set and it should not be considered a representative sample of the data from this study. The data set was curated using the [iReceptor Data Curation process](http://www.ireceptor.org/curation). The data set, in its entirety, is available through the [iReceptor Scientific Gateway](http://gateway.ireceptor.org).

The example data set contains a repertoire metadata file, as a UTF-8 encoded CSV file. The file consists of a header line, which contains the field names that will be written to the repository, followed by a metadata line for three repertoires from the above study, one for the b-cell IGH and IGL and IGK rearrangements. In a typical repertoire metadata file, there would be a single line for each repertoire in the study. The remaining files are the Rearrangement data for the HC1 subject, split into different files by locus (IGH, IGL, IGK).

If you are using an [iReceptor Turnkey Repository](https://github.com/sfu-ireceptor/turnkey-service-php) please refer to the loading data section of the iReceptor Turnkey documentation for more information on loading this data. 
