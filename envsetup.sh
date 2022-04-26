#!/bin/bash -i

mamba env create -f environment.yml -p ~/envs/ligo-hw6
conda activate ligo-hw6
python -m ipykernel install --user --name ligo-hw6 --display-name "IPython - ligo-hw6"