#!/bin/bash
#SBATCH -t 0-05:00
#SBATCH --mem=1250
#SBATCH --account=rpp-breden-ab
#SBATCH --job-name=ERR1278160-adaptors
#SBATCH --output ERR1278160-adaptors.out
#SBATCH --error ERR1278160-adaptors.err

source /home/ebarr/projects/rpp-breden-ab/ireceptor/bin/CURATOR/bin/activate
cutadapt -g file:P5_adaptors_forward.txt -g file:P7_adaptors_reverse.txt -g ACACTCTTTCCCTACACGACGCTCTTCCGATCT -g file:C_primers.txt -a file:P5_adaptors_rev_comp.txt -a file:P7_adaptors_rev_comp.txt -a file:C_primers_rev_comp.txt -a AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -G file:P5_adaptors_forward.txt -G file:P7_adaptors_reverse.txt -G ACACTCTTTCCCTACACGACGCTCTTCCGATCT -G file:C_primers.txt -A file:P5_adaptors_rev_comp.txt -A file:P7_adaptors_rev_comp.txt -A file:C_primers_rev_comp.txt -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT --info-file ERR1278160_info.txt --match-read-wildcards --overlap 10 -n 2 --length-tag="length=" --discard-untrimmed -o adrem_ERR1278160_1.fastq -p adrem_ERR1278160_2.fastq /home/ebarr/projects/rpp-breden-ab/ireceptor/curation/other_data_and_papers/chang_kuan_2016/SRA_files/ERR1278160_1.fastq /home/ebarr/projects/rpp-breden-ab/ireceptor/curation/other_data_and_papers/chang_kuan_2016/SRA_files/ERR1278160_2.fastq 
