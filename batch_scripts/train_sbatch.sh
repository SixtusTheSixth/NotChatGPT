#!/bin/bash

#SBATCH -n 8
#SBATCH --mem=64G
#SBATCH -t 48:00:00


echo "going to call python ../model.py --save_weights --num_epochs 1 --max_num_tokens 1024"
python ../model.py --save_weights --num_epochs 1 --max_num_tokens 1024