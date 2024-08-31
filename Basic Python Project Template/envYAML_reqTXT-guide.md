ENVIRONMENT.yml
##make env from yml
conda env create -f environment.yml

##export current env yml
conda env export > environment.yml


REQUIREMENTS.txt
# Lock Packages
pip freeze > requirements.txt

# export requirements.txt
conda list --export > requirements.txt 


##install packages from requirements.txt
# using pip
pip install -r requirements.txt

# using Conda
conda create --name <env_name> --file requirements.txt

summary @ https://stackoverflow.com/questions/48787250/set-up-virtualenv-using-a-requirements-txt-generated-by-conda