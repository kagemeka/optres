#!/bin/bash

apt update
pip install -U pip
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH=$HOME/.local/bin:$PATH' >>~/.bashrc
export PATH=$HOME/.local/bin:$PATH
poetry --version
echo 'please run "source ~/.bashrc"'
