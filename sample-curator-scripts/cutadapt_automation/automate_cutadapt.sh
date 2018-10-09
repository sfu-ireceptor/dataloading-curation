#!/bin/bash
#SBATCH --time=05:00:00
#SBATCH --mem=96000M
#SBATCH --account=rpp-breden-ab
#SBATCH --array=1-99%99
#SBATCH --output=/home/lgutierr/projects/rpp-breden-ab/lgutierr/OUTPUT/AUTOMATE/cutadapt/cutadapt_input__%J.out

##Script Author: Laura Gutierrez Funderburk
##Supervised by: Dr. Felix Breden, Dr. Jamie Scott, Dr. Brian Corrie
##Created on: October 9 2018
##Last modified on: October 9 2018

echo "Begin Script"

#######################
##### Directories #####
#######################

# Call array data file
array_data=/home/lgutierr/projects/rpp-breden-ab/lgutierr/SCRIPTS/Array_JOBS/Zvy/

# Scripts directory
script=/home/lgutierr/projects/rpp-breden-ab/lgutierr/SCRIPTS/

# Metadata Directory
metadata_ZVY=/home/lgutierr/projects/rpp-breden-ab/ireceptor/curation/cancer_data_and_papers/zvyagin_mamedov_2017
output_directory=/home/lgutierr/projects/rpp-breden-ab/ireceptor/curation/cancer_data_and_papers/zvyagin_mamedov_2017/automating_cutadapt/

#######################
# Array File Entries ##
#######################

cd ${array_data}

run_ID=`awk -F_ '{print $1}' runID_in_fastaHeader | head -$SLURM_ARRAY_TASK_ID | tail -1` 
FASTA_file=`awk -F_ '{print $2}' runID_in_fastaHeader | head -$SLURM_ARRAY_TASK_ID | tail -1` 

echo ${run_ID}
echo ${FASTA_file}

#######################
# Generate cutadapt   #
#######################

cd ${script}

echo "Begin Python: Generate cutadapt input"

source ~/ENV/bin/activate

python parse_primers_or_adapters_by_runID.py ${metadata_ZVY}/papers/"Zvyagin_Mamedov_2017.xlsx" ${output_directory} ${run_ID} "-g" "forward.txt"

deactivate

echo "End Python: Generate cutadapt input"

