#!/bin/bash
#SBATCH -t 0-05:00
#SBATCH --mem=1250
#SBATCH --account=rpp-breden-ab
#SBATCH --job-name=ERR1278160-filter
#SBATCH --output ERR1278160-filter.out
#SBATCH --error ERR1278160-filter.err

source /home/ebarr/projects/rpp-breden-ab/ireceptor/bin/CURATOR/bin/activate
cutadapt -q 25 --pair-filter=any --minimum-length 60 --length-tag "length=" -o ERR1278160_filtered_1.fastq -p ERR1278160_filtered_2.fastq adrem_ERR1278160_1.fastq adrem_ERR1278160_2.fastq 
