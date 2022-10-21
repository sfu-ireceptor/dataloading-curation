# Overview 
This directory contains test iReceptor repertoire data files in the [AIRR Repertoire JSON](https://docs.airr-community.org/en/stable/datarep/metadata.html#) format.

# Example Data

The example data in this directory is the metadata that describes the study "[Individual heritable differences result in unique cell lymphocyte receptor repertoires of naïve and antigen-experienced cells](https://doi.org/10.1038/ncomms11112) from Rubelt et al.  There is a single
metadata file that can be used to test AIRR Repertoire metadata loading as well as a file for testing updating metadata.

Each file consists of a header line, which contains the field names that will be written to the repository, followed by a metadata line for each repertoire. The format of the files is the same, with the update files having a set of fields that have changed for each repertoire. The update script changes the field `study_id` from "PRJNA300878" => "PRJNA300878-testupdate"

If you are using an [iReceptor Turnkey Repository](https://github.com/sfu-ireceptor/turnkey-service-php) please refer to the loading data section of the iReceptor Turnkey documentation for more information on loading this data. 
