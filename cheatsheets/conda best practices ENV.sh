conda ENV snippets.txt
=========================

conda create

conda create --name myclone --clone myenv


conda clean --all

-------------------------------
conda remove -n myenv --all


-------------------------------
#add conda env to jupyterlab
python -m ipykernel install --user --name=data

#remove conda env from jupyterlab
jupyter kernelspec remove <kernel_name>

c#!/usr/bin/env bashonda install -c conda-forge jupyterlab --force-reinstall

-----
#build packages not hosted on conda-forge
conda build
conda skeleton

------
#using pip in conda env

pip install [package] --upgrade-strategy only-if-needed


##BEST PRACTICES FOR USING PIP & CONDA TOGETHER##
----------
Use pip only after conda
Install as many requirements as possible with conda then use pip.

Pip should be run with --upgrade-strategy only-if-needed (the default).

Do not use pip with the --user argument, avoid all users installs.

Use conda environments for isolation
Create a conda environment to isolate any changes pip makes.

Environments take up little space thanks to hard links.

Care should be taken to avoid running pip in the root environment.

Recreate the environment if changes are needed
Once pip has been used, conda will be unaware of the changes.

To install additional conda packages, it is best to recreate the environment.