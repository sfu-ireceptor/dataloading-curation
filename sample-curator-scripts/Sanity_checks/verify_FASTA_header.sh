#!/bin/bash
#SBATCH --time=05:00:00
#SBATCH --mem=96000M
#SBATCH --account=rpp-breden-ab
#SBATCH --array=1-10%10
#SBATCH --output=/home/lgutierr/projects/rpp-breden-ab/lgutierr/OUTPUT/FASTA_content_verified/Mun/Job_Output/Fasta_cont_verified_%J.out

##Script Author: Laura Gutierrez Funderburk
##Supervised by: Dr. Felix Breden, Dr. Jamie Scott, Dr. Brian Corrie
##Created on: September 27 2018
##Last modified on: September 28 2018

echo "Begin Script"

#######################
##### Directories #####
#######################

# Call array data file
array_data=/home/lgutierr/projects/rpp-breden-ab/lgutierr/SCRIPTS/Array_JOBS/Zvy/

# Scripts directory
script=/home/lgutierr/projects/rpp-breden-ab/lgutierr/SCRIPTS/

# Metadata Directory
metadata_ZVY=/home/lgutierr/projects/rpp-breden-ab/ireceptor/curation/cancer_data_and_papers/zvyagin_mamedov_2017/fasta_files
metadata_MUN=/home/lgutierr/projects/rpp-breden-ab/ireceptor/curation/cancer_data_and_papers/chen_zhang_2016/fasta_files

#######################
# Array File Entries ##
#######################

cd ${array_data}

run_ID=`awk -F_ '{print $1}' runID_in_fastaHeader | head -$SLURM_ARRAY_TASK_ID | tail -1` 
FASTA_file=`awk -F_ '{print $2}' runID_in_fastaHeader | head -$SLURM_ARRAY_TASK_ID | tail -1` 

echo ${run_ID}
echo ${FASTA_file}

#######################
# VerifyFasta Headers #
#######################

cd ${script}

echo "Begin Python: Check Run ID in FASTA"

source ~/ENV/bin/activate

python verify_fasta_headers.py ${metadata_MUN}/${FASTA_file} ${run_ID}

deactivate

echo "End Python: Check Run ID in FASTA"

