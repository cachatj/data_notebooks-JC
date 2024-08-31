conda ENV snippets.txt
=========================


conda clean --all


-------------------------------
conda remove -n myenv --all


-------------------------------
#add conda env to jupyterlab
python -m ipykernel install --user --name=data

#remove conda env from jupyterlab
jupyter kernelspec remove <kernel_name>

-----
#build packages not hosted on conda-forge
conda build
conda skeleton