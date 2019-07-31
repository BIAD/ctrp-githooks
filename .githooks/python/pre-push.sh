#!/bin/bash
#
# An hook script to verify what is about to pushed to remote repository.
# Called by "git push" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the push.
# Coverage threshold rate is set to 95%


# format the code. - This will be always successful
echo "pre-push: Run unittest"
coverage run -m unittest discover tests

if [ $? -ne 0 ]; then
	echo 'Aborting push'
	exit 1
fi


# Run coverage
echo "pre-push: coverage, fail if it is under 95%"
coverage report --fail-under=95

