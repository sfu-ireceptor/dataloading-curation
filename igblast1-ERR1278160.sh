#!/bin/bash
#SBATCH -t 0-10:00
#SBATCH --mem=1250
#SBATCH --account=rpp-breden-ab
#SBATCH --job-name=ERR1278160-blast
#SBATCH --output ERR1278160-blast
#SBATCH --error ERR1278160-blast

module load nixpkgs/16.09
module load gcc/5.4.0
module load igblast/1.8.0
echo -n "Starting at "
date

# Avoid having to type long folder names
export IRECEPTOR=~/projects/rpp-breden-ab/ireceptor
# Where the databases are
export IRECEPTOR_IGBLAST=$IRECEPTOR/bin/igblast
# Where the data is
export DATA=$IRECEPTOR/curation/other_data_and_papers/chang_kuan_2016
export SAMPLE=ERR1278160

echo "Data folder = $DATA"
echo "Sample = $SAMPLE"
echo ""

igblastn -germline_db_V $IRECEPTOR_IGBLAST/ig_heavy/igh_v \
	 -germline_db_J $IRECEPTOR_IGBLAST/ig_heavy/igh_j \
	 -germline_db_D $IRECEPTOR_IGBLAST/ig_heavy/igh_d \
	 -organism human -domain_system imgt -query \
	 $DATA/fasta_files/paired_$SAMPLE.fasta \
	 -auxiliary_data $EBROOTIGBLAST/optional_file/human_gl.aux \
	 -show_translation -out \
	 $SAMPLE.fmt7 

echo ""
echo -n "Finished at "
date
