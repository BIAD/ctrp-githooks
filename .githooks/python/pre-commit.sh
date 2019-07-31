#!/bin/bash
#
# An hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
# Pylint will exit if it is not 100% covered, we could set the threshold.
# However, it would be better to change pylincrc config to allow certain rules.
# Since we can have more control which rules can be broken.

# Run pylint and check the score
echo "pre-commit: Running lint check"
pylint --rcfile=./pylintrc


