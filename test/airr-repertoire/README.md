# Overview 
This directory contains test repertoire data files in the [AIRR Repertoire JSON](https://docs.airr-community.org/en/stable/datarep/metadata.html#) format for loading into an [iReceptor Turnkey Repository](https://github.com/sfu-ireceptor/turnkey-service-php). Please refer to the loading data section of the iReceptor Turnkey documentation for more information on how to load this data. 

# Example Data

The example data in this directory contains the Repertoire metadata from the study "[Individual heritable differences result in unique cell lymphocyte receptor repertoires of naïve and antigen-experienced cells](https://doi.org/10.1038/ncomms11112) from Rubelt et al.  There is a single
metadata AIRR JSON file for all of the Repertoires and this file can be used to test AIRR Repertoire metadata loading into an iReceptor Repository using the `load_metadata.sh` script.

In addition, there is a second Repertoire JSON file that can be used to test the iReceptor Turnkey's Repertoire metadata update capability. 
The second file contains a single repertoire that is identical to one of the repertoires loaded in the step above,
with the `study_id` field changed from "PRJNA300878" => "PRJNA300878-testupdate". This file can be used with the `update_metadata.sh` script to
update a Repertoire field that is already loaded in an iReceptor Turnkey repository.
