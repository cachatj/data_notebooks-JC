Setting up From Nothin.....


1) ## Download & Install Homebrew

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


2) ## Add Homebrew to PATH

echo '# Set PATH, MANPATH, etc., for Homebrew.' >> /Users/jcachat/.zprofile 
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/jcachat/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"


3) ## Install Anaconda / Miniconda

https://docs.anaconda.com/anaconda/install/mac-os/

CMD line ## Include the bash command regardless of whether or not you are using the Bash shell
bash ~/Downloads/Anaconda3-2020.05-MacOSX-x86_64.sh


## Restart Terminal, allow conda env to initate. 


4) ## Install Poetry - packager & dependencey mgmt
curl -sSL https://install.python-poetry.org | python3 -
	
	## Add poetry to PATH
	export PATH="/Users/jcachat/.local/bin:$PATH

	# test install 
	poetry --version

	# update install
	poetry self update

	# configure venv folder to be within project dir (rather than .cache folder; improves portability). start by listing settings
	$ poetry config --list

	# change venv settings 
	poetry config virtualenvs.in-project true

5) ## create torchlightai conda env
conda create --name torchlightai python==3.9.7


