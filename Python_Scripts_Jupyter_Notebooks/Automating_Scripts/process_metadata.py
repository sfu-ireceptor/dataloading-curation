import pandas as pd
import os
import sys
from Bio import SeqIO
import Bio

## Begin script

# Read file, input is a .xlsx file
file = str(sys.argv[1])

# Tabulate file using Pandas DataFrames
table = pd.read_excel(file)

## Extract Desired Information
experiment_id = table['experiment_id']
adapter_f = table['adapter_sequence_forward ']
adapter_r = table['adapter_sequence_reverse']
run_id = table['run_id']

## Clean Up Entries: experiment_id
exp_id = [experiment_id[i] for i in range(1,len(experiment_id))]
# Clean Up Entries: run_id
r_id = [run_id[i] for i in range(1,len(run_id))]
# Get adapter_forward
adapter_forward =[adapter_f[i].split(",")[0] for i in range(1,len(adapter_f))]
# Get reverse complement of adapter_forward
adapter_forward_rc = [Bio.Seq.reverse_complement(adapter_forward[i]) for i in range(len(adapter_forward))]
# Get adapter_reverse
adapter_reverse =[adapter_r[i].split(",")[0] for i in range(1,len(adapter_r))]
# Get reverse complement of adapter_reverse
adapter_reverse_rc = [Bio.Seq.reverse_complement(adapter_reverse[i]) for i in range(len(adapter_reverse))]


# Write new file

with open("array_job_data","w") as f:
    for i in range(len(r_id)):
        f.write(exp_id[i] + "_" + r_id[i] + "_" + adapter_forward[i] + "_" \
          + adapter_reverse[i] + "_" + adapter_forward_rc[i]+ "_" + adapter_reverse_rc[i]  + "\n")
f.close()