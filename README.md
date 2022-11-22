### Hexlet tests and linter status:
[![Actions Status](https://github.com/GregTMJ/python-project-51/workflows/hexlet-check/badge.svg)](https://github.com/GregTMJ/python-project-51/actions)
[![Python CI](https://github.com/GregTMJ/python-project-51/actions/workflows/app-check.yml/badge.svg?branch=main)](https://github.com/Gregtmj/python-project-51/actions/workflows/app-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/0b0f477643eaf5a77637/maintainability)](https://codeclimate.com/github/GregTMJ/python-project-51/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0b0f477643eaf5a77637/test_coverage)](https://codeclimate.com/github/GregTMJ/python-project-51/test_coverage)


## Getting Started

#### Clone the current repository via command:
```git clone https://github.com/GregTMJ/python-project-51.git```

## Requirements
* python >= 3.7
* Poetry >= 1.14
* make >= 4

#### Check your pip version with the following command:
```python -m pip --version```

#### Make sure that pip is always up to date. If not, use the following:
```python -m pip install --upgrade pip```

#### Next install poetry on your OS. (the link is below)
[Poetry installation](https://python-poetry.org/docs/)
##### don't forget to init poetry packages with command ```poetry init```


## Makefile

#### Using the Makefile you can generate all the needed packages for you virtual environment
```make install``` to install poetry packages. \
```make build``` to build your packages inside your project. \
```make package-install``` installs the built package from our OS, so we can start using simple shell commands.

#### test your application with the following command```page-loader -h```
##### also don't forget to check the tests inside the folder tests, check if everything works with the command: 
```poetry run pytest```

### Some examples for the app
#### To start the app 
[![asciicast](https://asciinema.org/a/533726.svg)](https://asciinema.org/a/533726)

#### how the app works
[![asciicast](https://asciinema.org/a/533727.svg)](https://asciinema.org/a/533727)