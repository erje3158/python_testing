# Python Testing

This git repository is where I'm storing all my code testing the capabilities of Python. 

## Conda Installation
For simplicity, I've been using the Conda environmental management system. It is considered "best practice" to use an environmental management system with mutliple versions of the Python interpreter installed when working with Python as to not mess up the base installation that ships with your OS. Python is highly package and interpreter dependent, so the last thing you want to do is overwrite your system's environmental variables and embedded installation of Python. 

+ Install [Miniconda](https://conda.io/miniconda.html)
+ `$ conda update conda`
+ `$ conda config --add channels intel`
+ `$ conda create -n idp intellpython3_full python=3` - `-n` specifies `idp` as the name of this configuration

## Using Conda
Typing `$ source activate idp` will open up a termainal session with your environmental variables pointing correctly to the version of Python associated with `idp`. Run a code with `$ python <code_name>`, or run an interactive session by typing `$ python`. Exit the terminal session by `$ source deactivate idp`.
