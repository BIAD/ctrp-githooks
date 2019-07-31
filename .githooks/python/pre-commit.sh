#!/bin/bash
#
# A pre-commit hook to run Pylint on all files. Use the "pylintrc" config file.
# It exclude these folder: venv, virtualenv, lib
#


echo "pre-commit: Running lint check"
find . -type d \( -path ./venv -o -path ./virtualenv -o -path ./lib \) -prune -o -iname '*.py' | xargs pylint --ignore=venv --ignore=virtualenv --ignore=lib --rcfile=pylintrc

