#!/bin/bash
#SBATCH --time=8:00:00
#SBATCH --mem=1024M
#SBATCH --account=rpp-breden-ab
#SBATCH --array=1-99%99
#SBATCH --output=/home/lgutierr/projects/rpp-breden-ab/lgutierr/OUTPUT/FASTA_verified/Fasta_verified_%J.out

echo "Begin Script"

#######################
##### Directories #####
#######################

metadata_spr=/project/6008066/ireceptor/curation/


#######################
# Generate Array File #
#######################

echo "Begin Python: Check Run ID in FASTA"

source ~/ENV/bin/activate

python verify_fasta.py ${metadata_spr}cancer_data_and_papers/zvyagin_mamedov_2017/papers/Zvyagin_Mamedov_2017.xlsx

deactivate

echo "End Python: Check Run ID in FASTA"

