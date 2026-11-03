#!/bin/bash
#SBATCH --partition=dev_gpu_h100
#SBATCH --ntasks=1
#SBATCH --time=00:30:00
#SBATCH --job-name=YOUR_JOB_NAME
#SBATCH --gres=gpu:1
#SBATCH --output=/PATH/TO/YOUR/SLURM/LOG/DIRECTORY/%x_%j.out
#SBATCH --error=/PATH/TO/YOUR/SLURM/LOG/DIRECTORY/%x_%j.err
##SBATCH --mail-type=ALL
##SBATCH --mail-user=YOUR_UNI_MAIL_ADDRESS

source /PATH/TO/YOUR/VIRTUAL/ENVIRONMENT/bin/activate

python - <<'PY'
import torch, subprocess, os
print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("CUDA runtime from PyTorch:", torch.version.cuda)
    print("GPU via nvidia-smi:")
    subprocess.run(["nvidia-smi", "-L"])
    
PY

python THE_PYTHON_FILE_YOU_WANT_TO_RUN.py