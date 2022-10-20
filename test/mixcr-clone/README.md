# Overview 
This directory contains test clone data annotated by the MiXCR annotation tool. This directory consists of an example MiXCR clone file and an accompanying repertoire metadata file. A detailed description of using MiXCR is beyond the scope of this document, for more details please visit the MiXCR documentation page (https://mixcr.readthedocs.io/en/latest/)

# Example Data

The example data in this directory is a small subset of the data from the paper "[Next-Generation Sequencing of T and B Cell Receptor Repertoires from COVID-19 Patients Showed Signatures Associated with Severity of Disease](https://doi.org/10.1016/j.immuni.2020.06.024) from Schultheiß et al. The data set consists of a set of sequence annotations and clones from a single repertoire from this study. As such, it should only be considered in the context of a test data set and it should not be considered a representative sample of the data from this study. The data set was curated using the iReceptor Data Curation process listed here: http://www.ireceptor.org/curation. The data set, in its entirety, is available through the iReceptor Scientific Gateway (http://gateway.ireceptor.org).

The example data set consists of two data files. The first file is a repertoire metadata file, as a UTF-8 encoded CSV file. The file consists of a header line, which contains the field names that will be written to the repository, followed by a single metadata line for a single repertoire from the above study. In a typical repertoire metadata file, there would be a single line for each repertoire in the study. The second file is a clone file for this repertoire, as annotated using the MiXCR annotation tool. The file is a typical annotation output file from MiXCR.

Please refer to the loading data section of the iReceptor Turnkey documentation (https://github.com/sfu-ireceptor/turnkey-service-php) on how to load this data into and iReceptor Turnkey repository.

