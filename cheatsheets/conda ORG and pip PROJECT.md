last night I got super caught up in python environments, version control & working on multiple projects within organizations across two computers.

--consider two computers (hardware): MacMini & MacBookPro
--consider two ORGANIZATIONS: torchlightai & ccvresearch
--each ORG has multiple PROJECTS: torchlightai/footprints & torchlightai/spruce | ccvresearch/dataprep & ccvresearch/cannabis-data
--would like to use git verison control to host & sync btw computers, and mostly rely on pip packages within ORGs and btw PROJECTs, rather than mixing conda & pip

need a sanity check on the idea of creating a ORG conda environment (that contains core items: conda install python, jupyter-lab, sqlite), and then within the ORG conda env establishing venv for each project (that contains pip dependencies: pip install pandas, numpy).

aka, Import Multiple Projects into a Single Git Repository.
aka, A single git repository for multiple projects (in same ORG).

So ORGs get conda enviroment and core, universal items installed via conda. Then, PROJECTs within each ORG are established within a venv. in the terminal it looks like this:

$ (PROJECT venv) (ORG conda env) user/ORG/PROJECT %:

--------------------

Open terminal, create ORG folder in user root. cd to ORG folder.
$ (base) jcachat %:
$ (base) jcachat %: mk dir torchlightai
$ (base) jcachat %: cd torchlightai

Create ORG conda env with python==3.9.12 postgresql cairo. activate conda env (essentially, environment.yml)
$ (base) jcachat/torchlightai %: 
$ (base) jcachat/torchlightai %: conda create torchlightai python==3.9.13
$ (base) jcachat/torchlightai %: conda activate torchlightai

create PROJECT subfolders, cd to project subfolder & create PROJECT venv and activate.
$ (torchlightai) jcachat/torchlightai %: mkdir footprints
$ (torchlightai) jcachat/torchlightai %: cd footprints
$ (torchlightai) jcachat/torchlightai/footprints %:
$ (torchlightai) jcachat/torchlightai/footprints %: python3 -m venv footprints ./
$ (torchlightai) jcachat/torchlightai/footprints %: source ./bin/activate
$ (footprints) (torchlightai) jcachat/torchlightai/footprints %: python3 --verison
Python 3.9.13
use pip to install dependencies unique for each project
$ (footprints) (torchlightai) jcachat/torchlightai/footprints %: pip install pandas numpy scipy

the idea is to align dev environments with directory structures, and allow the projects to be individually git vc’d in a way that they can easily be recreated or sync’d btw desktop macmini & macbook pro (or even coworkers machine). It also allows you to completely blow up a project’s code, but always restore from start. its like a way to revert back to day 1 on both org env and project envs

there are other ways to do this:
I could make a base torchlightai conda env, install core packages (environment.yml)....then clone that base ORG env with PROJECT tag, so torchlightai_footpritnts env is made. the use pip to install dependencies and requirements. 

another clever approach would be to create ORG conda env, establish git repo. then for each project create a new branch first, then use pip to install packages. thus branches could just be dropped or restored in case of blow up & the git repo can be sync’d across computers. 

using a docker container for each ORG and then establishing virtual environments for each PROJECT within that container is also an obvious solution. but you guys said you didnt run footprints in docker containers locally for development - so was shying away form that. 

------------------

I guess my goal was to establish portable, modular & reset-able PROJECT dev envs found within with directory structures that could easily be passed from my desktop, to my laptop, to your laptop, to a new hires computer self-contained. that would be version controlled to a single gitlab or gitlab_private or github repo that everyone pulls from.

at any rate, I am just curious if you have ever heard of making venv within conda env’s - stacking, or nesting virtutal environments. Not much in google about this. Prob some crazy PATH, PYTHONPATH potential problems - so wanted to ask you for a sanity check.

how do you manage and switch btw footprints & say spruce dev environments? from a virtual env, directory structure & version control perspective? This is applicable to the briefly discussed task of providing onboarding guides for installing footprints with conda instead of pip.

no rush here, and I am moving on. feel into a time-blackhole last night playing with this and given the effort and result of successfully making nested conda env around a pip managed venv - I dont want to just throw it all away, so curious to what your thoughts are, redflags & how you manage it. Moving on to hire priority tasks. looking at the weekend.

hope you guys are doing well.