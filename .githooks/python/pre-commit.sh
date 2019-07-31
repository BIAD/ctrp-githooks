#!/bin/bash
#
# A pre-commit hook to run Pylint on all files. Use the "pylintrc" config file.
# It exclude these folder: venv, env, lib
#


echo "pre-commit: Running lint check"
find . -type d \( -path ./venv -o -path ./env -o -path ./lib \) -prune -o -iname '*.py' | xargs pylint --ignore=venv --ignore=env --ignore=lib --rcfile=pylintrc

