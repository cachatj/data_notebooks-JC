# download and install
curl -sSL https://install.python-poetry.org | python3 -

# path for python poetry, add to ~/.profile
export PATH="/Users/JCachat/.local/bin:$PATH"


# test install 
poetry --version

# update install
poetry self update

# configure venv folder to be within project dir (rather than .cache folder; improves portability). start by listing settings
$ poetry config --list

# change venv settings 
poetry config virtualenvs.in-project true