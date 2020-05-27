# iReceptor Data Curation

This GIT repository contains example files and documentation for loading data into iReceptor repositories. Examples for metadata as well as rearrangement files for a number of widely used annotation tools are provided. The README files in each of the subfolders contain more documentation.

For more information on metadata curation, please refer to: 
* [The iReceptor Metadata documentation](metadata)
* [The iReceptor metadata example](test/ir_repertoire)
* [The AIRR repertoire metadata example](test/airr_repertoire)

For more details on rearrangement curation, please refer to:
* [The test data set documentation](test)
* [The AIRR rearrangement format (including igblast) example](test/igblast)
* [The MiXCR rearrangement format example](test/mixcr)
* [The IMGT V-QUEST rearrangement example](test/imgt)

# The iReceptor Data Curation process

The iReceptor team follows a relatively strict data curation process. This process is documented on the [iReceptor Curation page](http://www.ireceptor.org/curation). We do not discuss this process in detail here, but instead suggest simple processes that can make data curation easier to manage.

The iReceptor curation process is focused around the curation of data for a single study. As such, we recommend that all data that is being curated for a specific study be stored in a single directory. As an example, we will use one of the [IMGT example data sets](test/imgt/imgt).

As mentioned, we recommended that all files relevant to the curation of data from a single study be located in a single directory. This would include the Repertoire Metadata file for the study as well as all of the Rearrangement files for each Repertoire. In the case of the IMGT example, this includes a single metadata file (PRJNA248411_Palanichamy_2018-12-18.csv). We tend to structure the metadata file name using the studies Study ID from NCBI, the principal (or contact) author, and the date the file was last modified. In addition, for each of the 8 sample repertoires in the study, in this case there is a single IMGT annotation file. Again, we use the NCBI accession number for the file in the filename to help manage the data. Note that it is possible to have more than one file for a single repertoire. Both the Repertoire Metadata file and the iReceptor Data Loader support having multiple files per repertoire sample.

Given the above structure, it is quite simple to use both the iReceptor Data Loading code as well as the helper Data Loading scripts to load AIRR-seq data in such a form. Please refer to the [shell scripts](test/imgt/test_imgt_large.sh) in the individual annotation tool folders for example uses of the iReceptor Data Loader scripts to load a complete study.
