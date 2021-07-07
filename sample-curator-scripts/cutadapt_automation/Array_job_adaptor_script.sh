#!/bin/bash
#SBATCH --time=8:00:00
#SBATCH --mem=1024M
#SBATCH --account=rpp-breden-ab
#SBATCH --array=1-99%99
#SBATCH --output=/home/ebarr/projects/rpp-breden-ab/ireceptor/TOY/OUTPUT/Toy-%J.out

#######################
##### Array Items #####
#######################

cd /home/ebarr/projects/rpp-breden-ab/ireceptor/TOY/

exp_ID=`awk -F_ '{print $1}' array_job_data | head -$SLURM_ARRAY_TASK_ID | tail -1` 
run_ID=`awk -F_ '{print $2}' array_job_data | head -$SLURM_ARRAY_TASK_ID | tail -1` 
adapter_f=`awk -F_ '{print $3}' array_job_data | head -$SLURM_ARRAY_TASK_ID | tail -1`
adapter_r=`awk -F_ '{print $4}' array_job_data | head -$SLURM_ARRAY_TASK_ID | tail -1`
adapter_f_rc=`awk -F_ '{print $5}' array_job_data | head -$SLURM_ARRAY_TASK_ID | tail -1`
adapter_r_rc=`awk -F_ '{print $6}' array_job_data | head -$SLURM_ARRAY_TASK_ID | tail -1`

#######################
#### Sanity Check #####
#######################

echo ${exp_ID}
echo ${run_ID}
echo ${adapter_f}
echo ${adapter_r}
echo ${adapter_f_rc}
echo ${adapter_r_rc}

#######################
####### Command #######
#######################

echo "Experiment ID"
echo ${exp_ID}
echo " "
echo "Run ID"
echo ${run_ID}
echo " "
echo "Begin cutadapt"

source /home/ebarr/projects/rpp-breden-ab/ireceptor/bin/CURATOR/bin/activate
cutadapt -g ^${adapter_f} -g ^${adapter_r} -g ^${adapter_f_rc} -g ^${adapter_r_rc} -G ^${adapter_f} -G ^${adapter_r}  -G ^${adapter_f_rc} -G ^${adapter_r_rc} --info-file ${run_ID}_info.txt --match-read-wildcards --overlap 10 -n 2 --length-tag="length=" -o primers_${run_ID}_1.fastq -p primers_${run_ID}_2.fastq ${run_ID}_1.fastq ${run_ID}_2.fastq

echo "End cutadapt"
