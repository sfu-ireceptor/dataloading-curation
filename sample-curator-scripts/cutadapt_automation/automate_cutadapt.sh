#!/bin/bash
#SBATCH --time=05:00:00
#SBATCH --mem=96000M
#SBATCH --account=rpp-breden-ab
###################################################----------------------------------------------------------->NUMBER OF JOBS IN ARRAY DEPENDS ON NUMBER OF ROWS IN METADATA SPREADHSEET
#SBATCH --array=1-10%10
###################################################----------------------------------------------------------->CHANGE THIS DIRECTORY
#SBATCH --output=/home/lgutierr/projects/rpp-breden-ab/lgutierr/OUTPUT/AUTOMATE/cutadapt/cutadapt_input__%J.out

##Script Author: Laura Gutierrez Funderburk
##Supervised by: Dr. Felix Breden, Dr. Jamie Scott, Dr. Brian Corrie
##Created on: October 9 2018
##Last modified on: October 25 2018

echo "Begin Script"

#######################
##### Directories #####
#######################
###################################################----------------------------------------------------------->CHANGE THESE DIRECTORIES
# Call array data file
array_data=/home/lgutierr/projects/rpp-breden-ab/lgutierr/SCRIPTS/Array_JOBS/Zvy/

# Scripts directory
script=/home/lgutierr/projects/rpp-breden-ab/lgutierr/SCRIPTS/

# Metadata Directory
metadata_ZVY=/home/lgutierr/projects/rpp-breden-ab/ireceptor/curation/cancer_data_and_papers/zvyagin_mamedov_2017
output_directory=/home/lgutierr/projects/rpp-breden-ab/lgutierr/OUTPUT/AUTOMATE/METADATA/Zvy/

#######################
# Array File Entries ##
#######################

cd ${array_data}

run_ID=`awk -F_ '{print $1}' runID_in_fastaHeader | head -$SLURM_ARRAY_TASK_ID | tail -1` 
FASTA_file=`awk -F_ '{print $2}' runID_in_fastaHeader | head -$SLURM_ARRAY_TASK_ID | tail -1` 

echo ${run_ID}
echo ${FASTA_file}

###########################
# Generate cutadapt input #
###########################

cd ${script}

echo "Begin Python: Generate cutadapt input"

source ~/ENV/bin/activate

python parse_primers_or_adapters_by_runID.py ${metadata_ZVY}/papers/"Zvyagin_Mamedov_2017.xlsx" ", "  ${output_directory} ${run_ID} 1 "-g" "_primer_forward.txt"

deactivate

echo "End Python: Generate cutadapt input"

###########################
## Fetch Cutadapt Input ##
###########################

forward_primers=`awk '{print}' ${output_directory}${run_ID}_primer_forward.txt`

 

########################### 
## Feed cutadapt command ##  
########################### 

echo "Begin cutadapt"

source /home/lgutierr/projects/rpp-breden-ab/ireceptor/bin/CURATOR/bin/activate

echo ${forward_primers}

cutadapt ${forward_primers} --info-file ${run_ID}_info.txt --match-read-wildcards --overlap 10 -n 2 --length-tag="length=" -o primers_${run_ID}_1.fastq -p primers_${run_ID}_2.fastq ${run_ID}_1.fastq ${run_ID}_2.fastq

echo "End cutadapt"
