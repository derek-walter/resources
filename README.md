# resources
Just simple resources to avoid google

## Python
### Python Locally

After screwing around as always on a new computer, the following worked:

pip -V
> pip 22.2.2 from /Users/walt/.pyenv/versions/3.8.5/lib/python3.8/site-packages/pip (python 3.8)  
> notice pip is part of pyenv, not local install

which pip
> /Users/walt/.pyenv/shims/pip

which pip3
> /Users/walt/.pyenv/shims/pip3

which pip3.10
> /usr/local/bin/pip3.10   
> Had local install of python 3.10, deleted from applications

pyenv global
> 3.8.5

pyenv versions
> \* 3.8.5 (set by /Users/walt/.pyenv/version)

pyenv global 3.10.6
> pyenv: version `3.10.6' not installed

pyenv install --list
> long list stopping at 3.8. Realize its been months, seeing pyenv out of date and 3.10 not installed

brew list
> Bunch of packages, notice pyenv in brew, must have been managed that way

brew update  
brew upgrade  
pyenv install --list  
pyenv install 3.10.6  
pyenv version  
> 3.8.5 (set by /Users/walt/.pyenv/version)

pyenv global 3.10.6  
pip -V  
> pip 22.2.1 from /Users/walt/.pyenv/versions/3.10.6/lib/python3.10/site-packages/pip (python 3.10)  
> It works!

cd repository
pipenv --python 3.10.6  
> ✔ Successfully created virtual environment! (3.10.6)